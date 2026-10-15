from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vendor import Vendor
from app.schemas.vendor_schema import VendorCreate, VendorRead


router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post(
    "/",
    response_model=VendorRead,
    status_code=status.HTTP_201_CREATED,
)
def register_vendor(
    vendor_data: VendorCreate,
    db: Session = Depends(get_db),
):
    email = str(vendor_data.email).lower()

    existing_vendor = db.scalar(
        select(Vendor).where(Vendor.email == email)
    )

    if existing_vendor:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A vendor with this email already exists",
        )

    vendor = Vendor(
        business_name=vendor_data.business_name.strip(),
        email=email,
        phone=vendor_data.phone.strip(),
        business_category=vendor_data.business_category.strip(),
        commission_rate=vendor_data.commission_rate,
        status="pending",
    )

    try:
        db.add(vendor)
        db.commit()
        db.refresh(vendor)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Vendor registration conflicts with an existing record",
        )

    return vendor


@router.get("/", response_model=list[VendorRead])
def list_vendors(
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Vendor).order_by(Vendor.id)
    ).all()


@router.get("/{vendor_id}", response_model=VendorRead)
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db),
):
    vendor = db.get(Vendor, vendor_id)

    if vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )

    return vendor
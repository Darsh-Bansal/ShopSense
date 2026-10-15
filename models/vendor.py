from datetime import datetime
from decimal import Decimal
from sqlalchemy import(CheckConstraint,DateTime,Numeric,String,func)
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Vendor(Base):
    tablename = "vendors"

    __table_args__ = (
        CheckConstraint(
            "commission rate >=0 and commission rate <=100",
            name = 
        )
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    business_name: Mapped[str] = mapped_column(
    String(150), nullable=False, index=True
    )

    email: Mapped[str] = mapped_column(
    String(255), nullable=False, unique=True, index=True
    )

    phone: Mapped[str] = mapped_column(
    String(30), nullable=False
    )

    business_category: Mapped[str] = mapped_column(
    String(100), nullable=False
    )

    commission_rate: Mapped[Decimal] = mapped_column(
    Numeric(5, 2), nullable=False, default=Decimal("10.00")
    )

    status: Mapped[str] = mapped_column(
    String(20), nullable=False, default="pending", index=True
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False,
    )
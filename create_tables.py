from app.database import Base, engine
from app.models.vendor import Vendor

# Import other models here as they are implemented.

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")
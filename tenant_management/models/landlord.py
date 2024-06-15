from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from tenant_management.database import Base

class Landlord(Base):
    __tablename__ = 'landlords'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    apartments = relationship("Apartment", back_populates="landlord")

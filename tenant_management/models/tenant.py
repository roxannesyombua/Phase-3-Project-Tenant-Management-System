from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tenant_management.database import Base

class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))

    apartment = relationship("Apartment", back_populates="tenants")

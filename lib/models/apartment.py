from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tenant_management.database import Base

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    landlord_id = Column(Integer, ForeignKey('landlords.id'))

    landlord = relationship("Landlord", back_populates="apartments")
    tenants = relationship("Tenant", back_populates="apartment")

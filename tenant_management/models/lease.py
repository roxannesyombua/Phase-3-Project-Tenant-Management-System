from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tenant_management.database import Base

class Lease(Base):
    __tablename__ = 'leases'
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'))
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)

    tenant = relationship("Tenant")

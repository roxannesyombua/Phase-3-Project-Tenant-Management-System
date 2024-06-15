# lib/helpers.py

from tenant_management.models import Tenant, Landlord, Apartment, Lease
from tenant_management.database import session

def validate_landlord_exists(landlord_id):
    landlord = session.query(Landlord).get(landlord_id)
    return landlord is not None

def validate_apartment_exists(apartment_id):
    apartment = session.query(Apartment).get(apartment_id)
    return apartment is not None

def validate_tenant_exists(tenant_id):
    tenant = session.query(Tenant).get(tenant_id)
    return tenant is not None




from tenant_management.models import Tenant, Landlord, Apartment, Lease
from tenant_management.database import session
from tenant_management.helpers import validate_landlord_exists, validate_apartment_exists, validate_tenant_exists

def add_tenant(name, contact, apartment_id):
    if validate_apartment_exists(apartment_id):
        tenant = Tenant(name=name, contact=contact, apartment_id=apartment_id)
        session.add(tenant)
        session.commit()
    else:
        raise ValueError(f'Apartment ID {apartment_id} does not exist.')

def list_tenants():
    return session.query(Tenant).all()

def remove_tenant(tenant_id):
    if validate_tenant_exists(tenant_id):
        tenant = session.query(Tenant).get(tenant_id)
        session.delete(tenant)
        session.commit()
        return True
    return False

def add_landlord(name, contact):
    landlord = Landlord(name=name, contact=contact)
    session.add(landlord)
    session.commit()

def list_landlords():
    return session.query(Landlord).all()

def remove_landlord(landlord_id):
    if validate_landlord_exists(landlord_id):
        landlord = session.query(Landlord).get(landlord_id)
        session.delete(landlord)
        session.commit()
        return True
    return False

def add_apartment(address, landlord_id):
    if validate_landlord_exists(landlord_id):
        apartment = Apartment(address=address, landlord_id=landlord_id)
        session.add(apartment)
        session.commit()
    else:
        raise ValueError(f'Landlord ID {landlord_id} does not exist.')

def list_apartments():
    return session.query(Apartment).all()

def remove_apartment(apartment_id):
    if validate_apartment_exists(apartment_id):
        apartment = session.query(Apartment).get(apartment_id)
        session.delete(apartment)
        session.commit()
        return True
    return False

def add_lease(tenant_id, start_date, end_date):
    if validate_tenant_exists(tenant_id):
        lease = Lease(tenant_id=tenant_id, start_date=start_date, end_date=end_date)
        session.add(lease)
        session.commit()
    else:
        raise ValueError(f'Tenant ID {tenant_id} does not exist.')

def list_leases():
    return session.query(Lease).all()

def remove_lease(lease_id):
    lease = session.query(Lease).get(lease_id)
    if lease:
        session.delete(lease)
        session.commit()
        return True
    return False

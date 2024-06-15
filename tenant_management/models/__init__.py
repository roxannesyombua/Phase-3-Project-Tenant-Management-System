import sqlite3

from tenant_management.models.apartment import Apartment
from tenant_management.models.landlord import Landlord
from tenant_management.models.tenant import Tenant
from tenant_management.models.lease import Lease

__all__ = ["Apartment", "Landlord", "Tenant", "Lease"]


CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

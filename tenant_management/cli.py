# lib/cli.py
import click
from tenant_management.utility import (
    add_tenant, list_tenants, remove_tenant,
    add_landlord, list_landlords, remove_landlord,
    add_apartment, list_apartments, remove_apartment,
    add_lease, list_leases, remove_lease
)
from tenant_management.database import session
from tenant_management.models import Base, engine

@click.group()
def main():
    """Tenant Management System"""
    pass

@click.command()
def addtenant():
    """Add a new tenant"""
    name = click.prompt("Enter tenant's name")
    contact = click.prompt("Enter tenant's contact")
    apartment_id = click.prompt("Enter apartment ID", type=int)
    add_tenant(name, contact, apartment_id)
    click.echo(f'Tenant {name} added.')

@click.command()
def listtenants():
    """List all tenants"""
    tenants = list_tenants()
    for tenant in tenants:
        click.echo(tenant)

@click.command()
def removetenant():
    """Remove a tenant by ID"""
    tenant_id = click.prompt("Enter tenant ID", type=int)
    if remove_tenant(tenant_id):
        click.echo(f'Tenant {tenant_id} removed.')
    else:
        click.echo(f'Tenant {tenant_id} not found.')

@click.command()
def addlandlord():
    """Add a new landlord"""
    name = click.prompt("Enter landlord's name")
    contact = click.prompt("Enter landlord's contact")
    add_landlord(name, contact)
    click.echo(f'Landlord {name} added.')

@click.command()
def listlandlords():
    """List all landlords"""
    landlords = list_landlords()
    for landlord in landlords:
        click.echo(landlord)

@click.command()
def removelandlord():
    """Remove a landlord by ID"""
    landlord_id = click.prompt("Enter landlord ID", type=int)
    if remove_landlord(landlord_id):
        click.echo(f'Landlord {landlord_id} removed.')
    else:
        click.echo(f'Landlord {landlord_id} not found.')

@click.command()
def addapartment():
    """Add a new apartment"""
    address = click.prompt("Enter apartment address")
    landlord_id = click.prompt("Enter landlord ID", type=int)
    add_apartment(address, landlord_id)
    click.echo(f'Apartment at {address} added.')

@click.command()
def listapartments():
    """List all apartments"""
    apartments = list_apartments()
    for apartment in apartments:
        click.echo(apartment)

@click.command()
def removeapartment():
    """Remove an apartment by ID"""
    apartment_id = click.prompt("Enter apartment ID", type=int)
    if remove_apartment(apartment_id):
        click.echo(f'Apartment {apartment_id} removed.')
    else:
        click.echo(f'Apartment {apartment_id} not found.')

@click.command()
def addlease():
    """Add a new lease"""
    tenant_id = click.prompt("Enter tenant ID", type=int)
    start_date = click.prompt("Enter lease start date")
    end_date = click.prompt("Enter lease end date")
    add_lease(tenant_id, start_date, end_date)
    click.echo(f'Lease for tenant {tenant_id} added.')

@click.command()
def listleases():
    """List all leases"""
    leases = list_leases()
    for lease in leases:
        click.echo(lease)

@click.command()
def removelease():
    """Remove a lease by ID"""
    lease_id = click.prompt("Enter lease ID", type=int)
    if remove_lease(lease_id):
        click.echo(f'Lease {lease_id} removed.')
    else:
        click.echo(f'Lease {lease_id} not found.')





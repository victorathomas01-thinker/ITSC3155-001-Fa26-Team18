"""Import all models before metadata.create_all so FKs resolve together.

Part 2: create_all creates missing tables in an EMPTY database. It does not
alter existing MySQL tables; use migrations for pre-existing deployments.
"""
from ..dependencies.database import Base, engine
from . import customers, promotions, orders, sandwiches, resources, recipes, order_details, payments, reviews

def index():
    Base.metadata.create_all(bind=engine)

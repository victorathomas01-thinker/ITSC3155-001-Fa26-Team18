# Part 2 — Database design decisions

Source handout: *Database Design Considerations for Online Restaurant Ordering System*. The handout explicitly describes **concepts, not mandatory table names**.

## Proposed SQLAlchemy tables

| Table | Primary key | Foreign keys | Purpose |
|---|---|---|---|
| customers | id | — | Guest customer contact and address |
| sandwiches | id | — | Menu dishes, price, calories, food category |
| resources | id | — | Ingredients, current stock and unit |
| recipes | id | sandwich_id, resource_id | Required quantity per menu dish |
| promotions | id | — | Discount codes and expiration |
| orders | id | customer_id, promotion_id | Dated orders, tracking, fulfillment, status and totals |
| order_details | id | order_id, sandwich_id | Order line items, quantity and purchase price |
| payments | id | order_id | Payment type, amount, status, reference and optional last four digits |
| reviews | id | customer_id, order_id, sandwich_id | Ratings and feedback tied to orders and dishes |

The existing starter table names `sandwiches`, `resources`, and `recipes` are retained for route compatibility even though they serve as generic menu items, ingredients, and menu ingredient requirements.

## Relationships and data integrity

- One customer → many orders and reviews.
- One promotion → many orders.
- One order → many details, payments, and reviews.
- One sandwich → many order details, recipe ingredients, and reviews.
- One resource → many recipe rows.
- Reviews reference both the order and the reviewed dish. Application logic must verify that the order belongs to the customer and contains that dish before accepting a review.
- Unique `tracking_number` (when set), promotion `code`, menu `sandwich_name`, resource `item`, payment transaction reference, and recipe (sandwich, resource).
- Nonnegative prices, inventory, and amounts; positive quantity for line items and recipes; ratings between 1 and 5.

## Security and implementation notes

- **Do not store raw card numbers, expiration or CVV.** Use only method, provider transaction reference, payment status and optional last four digits; actual card processing should be delegated to a compliant payment service.
- Guest checkout is supported without a login or account password. `customer_id` is nullable on orders for backwards compatibility with the existing sample API route, but new OROS order creation should attach or create a customer.
- Existing routes only cover the starter API; this **Part 2 deliverable is database structure**, not a claim that all final product endpoints are implemented.
- `Base.metadata.create_all()` is set to create all tables in a fresh database at startup. It **will not add new columns to existing tables**. If your MySQL schema already has the starter tables, create a separate fresh development database or use a reviewed migration. Do not drop teammates' production data.
- Test with a fresh MySQL database and `SHOW TABLES;` / `SHOW CREATE TABLE orders;`, and check Swagger startup after imports. The connector edit does not itself establish that a MySQL instance was started and inspected.

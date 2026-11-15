# Team 18 — User Stories and Acceptance Criteria

Project: **Online Restaurant Ordering System (OROS)**. This is a readable companion to the completed **User Stories.xlsx** professor template. All stories are planned, not implemented. See [Product Backlog](PRODUCT_BACKLOG.md).

### US-01 — Configure MySQL persistence (PB-01)

As a developer, I want to configure a MySQL database and data models so that the system can save restaurant data reliably.

**Acceptance:** MySQL tables can be created; API reads and writes persist; connection settings can be configured.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Foundation / rubric

### US-02 — Manage menu items (PB-02)

As a restaurant staff member, I want to add, update, view, and remove menu items so that customers always see our current menu.

**Acceptance:** Menu CRUD persists; dishes include price, calories, categories, and ingredients; invalid prices are rejected.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Staff 1.1

### US-03 — Track ingredient quantities (PB-03)

As a restaurant staff member, I want to manage ingredient quantities and the ingredients used by each dish so that the kitchen has accurate stock information.

**Acceptance:** Ingredient quantities and dish-ingredient requirements can be saved and updated.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Staff 1.2

### US-04 — Warn about unavailable ingredients (PB-04)

As a restaurant staff member, I want to receive a warning when an order requires ingredients we do not have so that we can avoid accepting orders the kitchen cannot prepare.

**Acceptance:** Insufficient stock produces a clear shortage response; stock cannot become negative.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Staff 1.2

### US-05 — Browse menu details (PB-05)

As a customer, I want to see each dish's ingredients, price, calories, and food category so that I can decide what to order.

**Acceptance:** Menu responses list the required dish attributes.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 1 · **Reference:** Customer needs / Customer 2.5

### US-06 — Search and filter menu (PB-06)

As a customer, I want to search and filter dishes by name and food category so that I can quickly find food that fits my preferences.

**Acceptance:** Search handles category examples such as vegetarian, spicy, kids, and low fat; no matches return an empty list.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 1 · **Reference:** Customer 2.5

### US-07 — Place orders without an account (PB-07)

As a customer, I want to place an order as a guest using my name, phone number, and delivery address when needed so that I do not have to create an account.

**Acceptance:** No registration is required; guest contact details are saved; delivery address is required when appropriate.

**Priority:** High · **Points:** 8 · **Proposed sprint:** 1 · **Reference:** Customer 2.1

### US-08 — Choose delivery or takeout (PB-08)

As a customer, I want to select takeout or delivery when ordering so that the restaurant knows how I want to receive my food.

**Acceptance:** The fulfillment method is saved; delivery requests validate the address.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 1 · **Reference:** Customer 2.3

### US-09 — Order multiple menu items (PB-09)

As a customer, I want to order multiple dishes with selected quantities so that I can purchase everything I want in one order.

**Acceptance:** Order line items, quantities, prices, and totals are saved accurately; a tracking identifier is issued.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Customer 2.1

### US-10 — Pay for an order (PB-10)

As a customer, I want to pay for my order using one of several supported payment methods so that I can finish checkout using an available option.

**Acceptance:** Multiple payment methods are supported; amount, method, and payment status are recorded; do not store raw card details.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Customer 2.2

### US-11 — Create and manage promo codes (PB-11)

As a restaurant staff member, I want to create, edit, disable, and delete promotional codes with expiration dates so that the restaurant can offer controlled discounts.

**Acceptance:** Promo codes support creation, updates, deletion, expiry and validity constraints.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Staff 1.6

### US-12 — Apply promotional codes (PB-12)

As a customer, I want to enter a promotional code during checkout so that I can receive a valid discount.

**Acceptance:** Valid codes adjust the order total; invalid or expired codes show a clear error.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Customer 2.7

### US-13 — Track orders using a tracking number (PB-13)

As a customer, I want to look up my order status using a tracking number so that I can see the latest status without an account.

**Acceptance:** A tracking number retrieves the latest persisted status; unknown identifiers return not-found.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Customer 2.4

### US-14 — View all orders and individual orders (PB-14)

As a restaurant staff member, I want to see all orders and open a specific order's details so that I can manage customer purchases accurately.

**Acceptance:** Staff can list orders and inspect item quantities, customer details, totals, and fulfillment method.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Staff 1.3

### US-15 — Update order progress (PB-15)

As a restaurant staff member, I want to update an order's status as it is prepared and fulfilled so that customers and kitchen workers have current information.

**Acceptance:** Valid status transitions persist and are reflected in staff and customer tracking responses.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Staff 1.3 / Customer 2.4

### US-16 — Show a chef preparation queue (PB-16)

As a kitchen worker, I want to see a preparation-focused list of active orders and their items so that I can prepare dishes efficiently.

**Acceptance:** Kitchen view includes active order items and quantities, without unnecessary customer personal data.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Customer needs / operations

### US-17 — Rate and review ordered dishes (PB-17)

As a customer, I want to rate and review dishes I have ordered so that I can share feedback about my experience.

**Acceptance:** A 1-5 rating and optional written review is associated with a purchased dish.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Customer 2.6

### US-18 — Read dish ratings and reviews (PB-18)

As a customer, I want to read other customers' ratings and written reviews for a dish so that I can make a more informed choice.

**Acceptance:** Customers can list reviews by dish with rating, comment, and date.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Customer 2.6

### US-19 — Inspect complaints and dissatisfaction (PB-19)

As a restaurant staff member, I want to review low ratings and customer complaints so that I can understand the reasons for dissatisfaction.

**Acceptance:** Staff can identify and read low-rated reviews, including complaint text.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Staff 1.4 / 1.5

### US-20 — Identify unpopular dishes (PB-20)

As a restaurant owner, I want to identify the least frequently purchased dishes so that I can improve the menu using sales data.

**Acceptance:** Report ranks dishes by sales volume for a selected period.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Staff 1.4

### US-21 — Calculate daily food-sales revenue (PB-21)

As a restaurant owner, I want to see total food-sale revenue for any selected day so that I can understand how much the restaurant earned.

**Acceptance:** Report sums eligible paid food sales for a requested date and returns zero when appropriate.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Staff 1.7

### US-22 — Filter orders by date range (PB-22)

As a restaurant staff member, I want to view orders placed during a selected date range so that I can review past transactions.

**Acceptance:** Returned orders fall within the supplied dates; invalid date ranges are rejected.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Staff 1.8

### US-23 — Summarize preferences and order trends (PB-23)

As a restaurant owner, I want to see summaries of order trends, customer preferences, and order statuses so that I can make data-informed business decisions.

**Acceptance:** Persisted records produce meaningful summaries by category, status, and sales date.

**Priority:** Medium · **Points:** 5 · **Proposed sprint:** 2 · **Reference:** Customer needs / analysis

### US-24 — Validate request data and errors (PB-24)

As a developer, I want to receive clear error responses for invalid API requests so that customers and staff do not accidentally save bad data.

**Acceptance:** Malformed inputs, negative quantities, missing fields, and unknown IDs produce appropriate HTTP errors.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 1 · **Reference:** Operational efficiency

### US-25 — Document the endpoints in Swagger (PB-25)

As a developer, I want to read API documentation and examples in Swagger UI so that the team and restaurant staff can learn how to use the system.

**Acceptance:** API docs list meaningful routes, request and response schemas, and examples.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 1 · **Reference:** Documentation

### US-26 — Provide automated API tests (PB-26)

As a developer, I want to run repeatable tests of API behavior so that the team can catch mistakes before a demonstration.

**Acceptance:** pytest covers successful requests and validation failures with reproducible setup.

**Priority:** High · **Points:** 5 · **Proposed sprint:** 1 · **Reference:** Testing rubric

### US-27 — Complete CRUD for all data tables (PB-27)

As a developer, I want to create, retrieve, update, and delete records for every required table so that the API meets the project's database-management requirements.

**Acceptance:** All tables expose complete CRUD behavior as appropriate; missing-record cases are handled.

**Priority:** High · **Points:** 8 · **Proposed sprint:** 2 · **Reference:** CRUD rubric

### US-28 — Populate useful demonstration data (PB-28)

As a developer, I want to load realistic example menu items, orders, reviews, and discounts so that the group can demonstrate all of the required features.

**Acceptance:** Seed data includes varied dishes, ingredient quantities, orders, statuses, ratings, and promo codes.

**Priority:** High · **Points:** 3 · **Proposed sprint:** 2 · **Reference:** Demo rubric


# ITSC 3155 — Final Project guide (Fall 2026)

**Project:** Online Restaurant Ordering System (OROS) — REST API only, no frontend. Show functionality through FastAPI Swagger UI backed by MySQL.

**Official professor's source:** [Final Project — Description and Checklist](https://docs.google.com/document/d/1_fZFBVvWM_vdDVWbpzF3RtFD-VIzjnSU_b-sjqsD4FY/edit). This guide is a condensed navigation aid and does not supersede Canvas instructions.

## Phase 1 — Requirement analysis and user stories (15 points)

- GitHub (5): repo link, members and TA added, code skeleton, conventional commits.
- Product backlog (5): planned features and priorities.
- User stories (5): requirements from staff/customer roles.
- Current submission mirrors: [product backlog](PRODUCT_BACKLOG.md), [user stories](USER_STORIES.md). Their Google Sheets originals live in [Team 18 Drive](https://drive.google.com/drive/folders/1i6folBxKi0tPjLkSZ_BWoZdFpbLO8ydv).

## Phase 2 — Software and database design (20 points)

- GitHub link (1).
- Three casual software block diagrams (12).
- Schema and models package for database tables and relationships (6).
- Re-submit updated product backlog and user stories (0.5 each), even if unchanged.

## Phase 3 — Final product

- Two sprint backlogs and two sprint reviews (12).
- Functional REST API (33): all eight staff requirements and seven customer requirements, CRUD on every table, MySQL, demonstration data, at least one pytest unit test.
- Updated product backlog and user stories (5), even if unchanged.
- Final 4–5 minute presentation recording (20): each member on camera, introductions, requirements-focused live demo, challenges/learning, edited and polished video uploaded to GitHub.
- Documentation (15): user manual, technical architecture, endpoint documentation, examples, development environment.
- Group participation (10).

## Required staff API capabilities (8)

1. Create, edit, delete menu items.
2. Alert when insufficient ingredients prevent an order.
3. View all orders or a specific order.
4. Find unpopular or complained-about dishes.
5. Understand dissatisfaction from reviews.
6. Create and manage promo codes with expiration dates.
7. Calculate daily food-sale revenue.
8. Filter orders by date range.

## Required customer API capabilities (7)

1. Place guest orders without sign-up; save required contact/address details.
2. Pay for an order.
3. Choose takeout or delivery.
4. Track status by tracking number.
5. Search by food type, such as vegetarian.
6. Rate/review purchased dishes and see reviews.
7. Apply promo codes.

## Important distinctions and unresolved planning issues

- The imported instructor skeleton and a few orders/order-details routes **do not mean the completed OROS API exists**. Implement and test features against the rubric.
- The submitted Drive backlog currently contains **13 features**, and Drive user stories **13 rows**, while an earlier expanded GitHub draft mapped **28 planned features**. The main GitHub files now mirror the Drive submission; expanded alternatives are preserved in `planning-drafts/`.
- The existing Drive backlog refers to sprints **1–5**, but the official rubric requires **two** sprints. Agree on a two-sprint plan and update the shared Drive sheet before changing its numbers; do not quietly rewrite classmates' work.
- A separate TA request asks to correct the final-project attendance log's actual class dates. See [TA correction checklist](TA_SUBMISSION_CORRECTIONS.md). Attendance dates and records must be verified, not inferred.

## Practical next steps

1. Agree with teammates which requirements and two-sprint assignments you will implement.
2. Ensure three software diagrams, schema, and models package exist for Part 2.
3. Implement the missing models/routes/services with MySQL; test each of 15 customer/staff requirements and CRUD coverage.
4. Populate sample records, run pytest and Swagger demonstration, write manuals and presentation plan.
5. Submit revised documents on Canvas as the instructor requests; verify the attendance sheet with actual class/meeting dates before confirming completion to Elijah.

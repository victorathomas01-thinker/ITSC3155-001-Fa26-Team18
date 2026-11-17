# Part 2 — Software and Database Design

- [Three design diagrams (PDF)](Team18_Part2_Three_Design_Diagrams.pdf) covering API architecture, database relationships, and guest checkout through fulfillment
- [Database design and table map](PART2_DATABASE_DESIGN.md)
- [SQLAlchemy models](../api/models/), [Pydantic schemas](../api/schemas/), and [model loader](../api/models/model_loader.py)
- [Product backlog](../part-1/PRODUCT_BACKLOG.md) and [user stories](../part-1/USER_STORIES.md) shared with Part 1
- [Run the API and test](../README.md#run-the-api-and-test)

Local verification on a fresh MySQL database confirmed nine tables, nine primary keys, and ten foreign keys. Swagger and OpenAPI returned HTTP 200, the live order smoke checks succeeded, and pytest passed.

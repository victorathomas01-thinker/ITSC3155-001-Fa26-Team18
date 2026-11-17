from os import environ


class conf:
    db_host = environ.get("OROS_DB_HOST", "localhost")
    db_name = environ.get("OROS_DB_NAME", "sandwich_maker_api")
    db_port = int(environ.get("OROS_DB_PORT", "3306"))
    db_user = environ.get("OROS_DB_USER", "root")
    db_password = environ.get("OROS_DB_PASSWORD", "")
    app_host = "localhost"
    app_port = 8000

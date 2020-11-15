"""
DBConnection unit tests
"""
from dbconn.connect import DBConnection
from sqlalchemy.engine import Engine

def test_init_success():
    conn = DBConnection()

    assert hasattr(conn, "_logger")
    assert hasattr(conn, "_engine")
    assert isinstance(conn.engine, Engine)

def test_nondefault_connection():
    conf = {
        "address": "my_db",
        "port": "1234",
        "user": "foo",
        "password": "bar",
        "database": "baz"
    }
    conn = DBConnection(**conf)

    assert conf['address'] == conn.engine.url.host
    assert int(conf['port']) == conn.engine.url.port
    assert conf['user'] == conn.engine.url.username
    assert conf['database'] == conn.engine.url.database
    assert conf['password'] == conn.engine.url.password

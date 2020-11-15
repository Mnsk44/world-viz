"""
Entry point for World data visualization app
"""
from server.app import app
from server.layout import layout
import server.callbacks

app.layout = layout

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)
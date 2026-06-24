import os
from mcp.server.fastmcp import FastMCP
from seed_data import MOCK_MOVIES

# Create a FastMCP server instance
mcp = FastMCP("AnimeMovieBridge")

SCHEMA_PATH = "/Users/mustaphamelemustapha/Code/Anime movie/schema.sql"
API_ROUTES_PATH = "/Users/mustaphamelemustapha/Code/Anime movie/api_routes.py"

@mcp.tool()
def get_database_schema() -> str:
    """Returns the PostgreSQL DDL database schema definitions from schema.sql."""
    if not os.path.exists(SCHEMA_PATH):
        return "Error: schema.sql file not found."
    with open(SCHEMA_PATH, "r") as f:
        return f.read()

@mcp.tool()
def get_api_endpoints() -> str:
    """Returns the FastAPI endpoint declarations and schemas from api_routes.py."""
    if not os.path.exists(API_ROUTES_PATH):
        return "Error: api_routes.py file not found."
    with open(API_ROUTES_PATH, "r") as f:
        return f.read()

@mcp.tool()
def fetch_mock_movies() -> list:
    """Returns mock dataset of anime movies with mirrors, resolutions, and genres for UI development."""
    return MOCK_MOVIES

if __name__ == "__main__":
    mcp.run()


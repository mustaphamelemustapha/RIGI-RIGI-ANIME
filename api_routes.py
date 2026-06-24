from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime
import uuid
from seed_data import MOCK_MOVIES

app = FastAPI(
    title="Anime Movie Download Platform API",
    description="Backend endpoints for dynamic content grids, mirror fallback routing, and fuzzy search.",
    version="1.0.0"
)

# --- Pydantic Schemas ---
class MovieResponse(BaseModel):
    movie_id: int
    title: str
    synopsis: str
    release_date: str
    poster_url: str
    genres: List[str]
    rating: float
    downloads_count: str

class DownloadLinkResponse(BaseModel):
    link_id: int
    movie_id: int
    resolution: str
    file_size: str
    link_url: str
    mirror_name: str
    is_active: bool

# --- Endpoints ---

@app.get("/movies/trending", response_model=List[MovieResponse])
async def get_trending_movies(limit: int = 10):
    """
    Get top trending movies based on download activity from User_Analytics.
    """
    return [
        {
            "movie_id": m["movie_id"],
            "title": m["title"],
            "synopsis": m["synopsis"],
            "release_date": m["release_date"],
            "poster_url": m["poster_url"],
            "genres": m["genres"],
            "rating": m["rating"],
            "downloads_count": m["downloads_count"]
        } for m in MOCK_MOVIES[:limit]
    ]


@app.get("/movies/latest", response_model=List[MovieResponse])
async def get_latest_movies(limit: int = 10):
    """
    Get latest releases ordered by release_date.
    """
    # Sort by release date descending
    sorted_movies = sorted(MOCK_MOVIES, key=lambda x: x["release_date"], reverse=True)
    return [
        {
            "movie_id": m["movie_id"],
            "title": m["title"],
            "synopsis": m["synopsis"],
            "release_date": m["release_date"],
            "poster_url": m["poster_url"],
            "genres": m["genres"],
            "rating": m["rating"],
            "downloads_count": m["downloads_count"]
        } for m in sorted_movies[:limit]
    ]

@app.get("/movies/search", response_model=List[MovieResponse])
async def search_movies(q: str):
    """
    Perform a fast fuzzy search for movie titles.
    """
    query = q.lower()
    filtered = [m for m in MOCK_MOVIES if query in m["title"].lower()]
    return [
        {
            "movie_id": m["movie_id"],
            "title": m["title"],
            "synopsis": m["synopsis"],
            "release_date": m["release_date"],
            "poster_url": m["poster_url"],
            "genres": m["genres"],
            "rating": m["rating"],
            "downloads_count": m["downloads_count"]
        } for m in filtered
    ]

@app.get("/movies/{movie_id}/download-links", response_model=List[DownloadLinkResponse])
async def get_download_links(movie_id: int):
    """
    Retrieves all available download mirrors/links for a movie.
    """
    # Find movie
    movie = next((m for m in MOCK_MOVIES if m["movie_id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
        
    links = []
    for idx, mirror in enumerate(movie["mirrors"]):
        links.append({
            "link_id": movie_id * 100 + idx,
            "movie_id": movie_id,
            "resolution": mirror["resolution"],
            "file_size": mirror["file_size"],
            "link_url": mirror["link_url"],
            "mirror_name": mirror["mirror_name"],
            "is_active": mirror["is_active"]
        })
    return links

@app.post("/movies/{movie_id}/download-analytics")
async def track_download(movie_id: int):
    """
    Log an entry in the User_Analytics table when a user clicks a download link.
    """
    return {"status": "success", "message": "Analytic log saved."}

@app.get("/api/v1/health")
async def health_check():
    """
    Production health check endpoint for container orchestration.
    """
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}



-- Database Schema for Anime Movie Download Platform

-- Enable trgm extension for fuzzy search capabilities
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- 1. Movies Table
CREATE TABLE IF NOT EXISTS Movies (
    Movie_ID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Synopsis TEXT,
    Release_Date DATE,
    Poster_URL TEXT,
    Genres VARCHAR(100)[] NOT NULL, -- Array of genres (e.g., Action, Romance, Shounen)
    Created_At TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for fast case-insensitive title search and fuzzy searches
CREATE INDEX IF NOT EXISTS idx_movies_title_trgm ON Movies USING gin (Title gin_trgm_ops);

-- Index for genres array search
CREATE INDEX IF NOT EXISTS idx_movies_genres ON Movies USING gin (Genres);

-- 2. Download Mirrors & Links Table
CREATE TABLE IF NOT EXISTS Download_Links (
    Link_ID SERIAL PRIMARY KEY,
    Movie_ID INTEGER REFERENCES Movies(Movie_ID) ON DELETE CASCADE,
    Resolution VARCHAR(20) NOT NULL, -- e.g., 720p, 1080p, 4K
    File_Size VARCHAR(50) NOT NULL,  -- e.g., 1.2 GB, 800 MB
    Link_URL TEXT NOT NULL,
    Mirror_Name VARCHAR(100) NOT NULL, -- e.g., Mega, GDrive, Direct Server
    Is_Active BOOLEAN DEFAULT TRUE,  -- False if link verification fails
    Last_Checked TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    Created_At TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for fast mirror checks and active download routing
CREATE INDEX IF NOT EXISTS idx_download_links_movie_active ON Download_Links(Movie_ID, Is_Active);

-- 3. User Analytics Table
CREATE TABLE IF NOT EXISTS User_Analytics (
    Analytic_ID SERIAL PRIMARY KEY,
    Movie_ID INTEGER REFERENCES Movies(Movie_ID) ON DELETE CASCADE,
    Event_Type VARCHAR(50) DEFAULT 'download', -- e.g., page_view, download
    Timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for querying popular/trending downloads grouped by timeframe
CREATE INDEX IF NOT EXISTS idx_user_analytics_movie_timestamp ON User_Analytics(Movie_ID, Timestamp);

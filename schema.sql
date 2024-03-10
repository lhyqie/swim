DROP TABLE IF EXISTS swimmers;

CREATE TABLE swimmers (
    id TEXT PRIMARY KEY,
    fastest_time TEXT NOT NULL,
    crawl_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
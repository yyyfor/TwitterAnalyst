use zw627;

CREATE TABLE IF NOT EXISTS Topics(
    topic VARCHAR(255) NOT NULL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_update TIMESTAMP);

CREATE TABLE IF NOT EXISTS Locations(
    place VARCHAR(255) NOT NULL PRIMARY KEY,
    latitude DOUBLE,
    longitude DOUBLE);

CREATE TABLE IF NOT EXISTS Tweets(
    TWTID BIGINT NOT NULL PRIMARY KEY,
    topic VARCHAR(255) NOT NULL, 
    user_id BIGINT,
    created_at DATETIME,
    favorite_count INT,
    text VARCHAR(255),
    place VARCHAR(255),
    sentiment INT,
    FOREIGN KEY(topic) REFERENCES Topics (topic)
    );

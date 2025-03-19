--This script will delete all the inserted data while keeping the structure of the db intact. Also resets the default id counters for the tables with serial columns.
-- Truncate all tables and reset ID counters
TRUNCATE TABLE crawldb.link RESTART IDENTITY CASCADE;
TRUNCATE TABLE crawldb.image RESTART IDENTITY CASCADE;
TRUNCATE TABLE crawldb.page_data RESTART IDENTITY CASCADE;
TRUNCATE TABLE crawldb.page RESTART IDENTITY CASCADE;
TRUNCATE TABLE crawldb.site RESTART IDENTITY CASCADE;

-- Truncate tables without serial columns (no need to reset ID counters)
TRUNCATE TABLE crawldb.data_type CASCADE;
TRUNCATE TABLE crawldb.page_type CASCADE;
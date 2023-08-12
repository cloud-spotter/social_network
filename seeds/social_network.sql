-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS accounts CASCADE;
DROP SEQUENCE IF EXISTS accounts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email text,
    user_name text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO accounts (email, user_name) VALUES ('George@hello.com', 'George Orwell');
INSERT INTO accounts (email, user_name) VALUES ('Ben@hiya.com', 'Ben Almond');


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
-- The foreign key name is always {other_table_singular}_id
    account_id int,
    constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, views, account_id) VALUES ('Tomatoes', 'Growing tomatoes test', 3, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Post 2', 'Post 2 content', 24, 2);

-- Student Innovation Idea Portal: database schema
-- Tables are ordered so every referenced table is created first.

CREATE TABLE IF NOT EXISTS categories (
                                          category_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                                          category_name VARCHAR(50) NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS users (
                                     user_id       INTEGER PRIMARY KEY AUTOINCREMENT,
                                     full_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role          VARCHAR(10)  NOT NULL CHECK (role IN ('STUDENT', 'ADMIN', 'HELPER')),
    created_at    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS ideas (
                                     idea_id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                     title                VARCHAR(200) NOT NULL,
    description          TEXT         NOT NULL,
    category_id          INTEGER      NOT NULL REFERENCES categories(category_id),
    submitted_by_user_id INTEGER      NOT NULL REFERENCES users(user_id),
    helper_id            INTEGER      REFERENCES users(user_id),
    reviewed_by_admin_id INTEGER      REFERENCES users(user_id),
    status               VARCHAR(20)  NOT NULL DEFAULT 'SUBMITTED'
    CHECK (status IN ('SUBMITTED', 'UNDER_REVIEW', 'APPROVED', 'REJECTED')),
    created_at           TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at           TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS idea_members (
                                            idea_id   INTEGER     NOT NULL REFERENCES ideas(idea_id),
    user_id   INTEGER     NOT NULL REFERENCES users(user_id),
    team_role VARCHAR(50),
    joined_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (idea_id, user_id)
    );

CREATE TABLE IF NOT EXISTS comments (
                                        comment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                                        idea_id      INTEGER   NOT NULL REFERENCES ideas(idea_id),
    admin_id     INTEGER   NOT NULL REFERENCES users(user_id),
    comment_text TEXT      NOT NULL,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS status_history (
                                              history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                              idea_id    INTEGER     NOT NULL REFERENCES ideas(idea_id),
    old_status VARCHAR(20) CHECK (old_status IN ('SUBMITTED', 'UNDER_REVIEW', 'APPROVED', 'REJECTED')),
    new_status VARCHAR(20) NOT NULL CHECK (new_status IN ('SUBMITTED', 'UNDER_REVIEW', 'APPROVED', 'REJECTED')),
    admin_id   INTEGER     REFERENCES users(user_id),
    changed_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
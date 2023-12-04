CREATE DATABASE storybook;

-- User Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50),
    Email VARCHAR(100),
    PasswordHash VARCHAR(255),
    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Child Table
CREATE TABLE CHILD (
    ChildID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    ChildName VARCHAR(50),
    Age INT,
    Pronouns VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Story Table
CREATE TABLE Stories (
    StoryID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(100),
    Content TEXT,
    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
    ChildID INT,
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID)
);
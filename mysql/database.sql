use db;

CREATE TABLE users(
    UserId int not null AUTO_INCREMENT, 
    FirstName varchar(100) not null,
    Info varchar(100) not null, 
    PRIMARY KEY (UserID)
);

INSERT INTO users(FirstName, Info)
VALUES ("Evgeny", "350"), ("Nikita", "400"), ("IVAN", "500");
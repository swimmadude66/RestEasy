Create Table IF NOT EXISTS Users(
ID INTEGER PRIMARY KEY AUTOINCREMENT, 
username varchar(20) UNIQUE, 
pass_hash char(64),
isAdmin INTEGER,
isActive INTEGER);




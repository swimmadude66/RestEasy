Create Table IF NOT EXISTS Users(
ID INTEGER PRIMARY KEY, 
username varchar(20), 
pass_hash char(64),
isAdmin INTEGER,
isActive INTEGER);




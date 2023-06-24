DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS groups_mtuci CASCADE;
DROP TABLE IF EXISTS cafedra CASCADE;

CREATE TABLE cafedra
(
	caf_id int NOT NULL PRIMARY KEY,
	title TEXT NOT NULL,
	decanat varchar(5)
);

CREATE TABLE groups_mtuci
(
	gr_id int NOT NULL PRIMARY KEY,
	title varchar(7) NOT NULL,
	caf int NOT NULL,
	FOREIGN KEY (caf) REFERENCES cafedra(caf_id)
);

CREATE TABLE students
(
	st_id int NOT NULL PRIMARY KEY,
	st_name text NOT NULL,
	passport varchar(11) NOT NULL,
	st_group int NOT NULL,
	FOREIGN KEY (st_group) REFERENCES groups_mtuci(gr_id)
);

INSERT INTO cafedra VALUES (1, 'informaticks', 'it');
INSERT INTO cafedra VALUES (2, 'network information techonology and sirveces', 'ssis');

INSERT INTO groups_mtuci VALUES(1, 'BVT2203', 1);
INSERT INTO groups_mtuci VALUES(2, 'BPI2107', 1);
INSERT INTO groups_mtuci VALUES(3, 'BST2007', 2);
INSERT INTO groups_mtuci Values(4, 'BEI2201', 2);

INSERT INTO students VALUES (1, 'Nastya', '1122333444', 1);
INSERT INTO students VALUES (2, 'Ilvina', '5566777888', 1);
INSERT INTO students VALUES (3, 'Darya', '9900111222', 1);
INSERT INTO students VALUES (4, 'Sabina', ' 3344555666', 1);
INSERT INTO students VALUES (5, 'Ilya', '7788999000', 1);
INSERT INTO students VALUES (6, 'Anton', '1212345345', 2);
INSERT INTO students VALUES (7, 'Artem', '6767890890', 2);
INSERT INTO students VALUES (8, 'Petya', '1212234234', 2);
INSERT INTO students VALUES (9, 'Mira', '3434456456', 2);
INSERT INTO students VALUES (10, 'Vlad', '5656678678',2);
INSERT INTO students VALUES (11, 'Pecyatskiy', '7878890890', 3);
INSERT INTO students VALUES (12, 'Genadiy Gorin', '9090012012', 3);
INSERT INTO students VALUES (13, 'Andrei', '0099888777', 3);
INSERT INTO students VALUES (14, 'Boris', '6655444333', 3);
INSERT INTO students VALUES (15, 'Marya', '2211000999', 3);
INSERT INTO students VALUES (16, 'Natasha', '8877666555', 4);
INSERT INTO students VALUES (17, 'Tamarochka', '4433222111', 4);
INSERT INTO students VALUES (18, 'Petron', '0000999999', 4);
INSERT INTO students VALUES (19, 'Lena', '8888777777', 4);
INSERT INTO students VALUES (20, 'Katya', '1337666228', 4)

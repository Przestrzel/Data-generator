-- CREATE

CREATE DATABASE Moj_Index_UT
GO

USE Moj_Index_UT
GO

--Nauczyciele

CREATE TABLE Nauczyciele (
ID int NOT NULL PRIMARY KEY,
Imie varchar(20),
Nazwisko varchar(30),
);

--Kursy

CREATE TABLE Kursy (
ID_kursu int NOT NULL PRIMARY KEY,
Nazwa_kursu varchar(50),
Max_liczba_uczestnikow int,
Opis_kursu varchar(100)
);

--Studenci

CREATE TABLE Studenci (
ID int NOT NULL PRIMARY KEY,
Imie varchar(20),
Nazwisko varchar(30),
Miejscowosc varchar(30)
);

--Zajecia

CREATE TABLE Zajecia (
ID_zajec int NOT NULL PRIMARY KEY,
ID_kursu int FOREIGN KEY REFERENCES Kursy(ID_kursu) NOT NULL,
ID_nauczyciele int FOREIGN KEY REFERENCES Nauczyciele(ID) NOT NULL,
Dzien int,
Godzina_rozpoczecia time(0),
Godzina_zakonczenia time(0),
Rok int,
Semestr varchar(10),
Typ_zajec varchar(30),
Wydzial varchar(50)
);

--Zajecia studentow

CREATE TABLE Zajecia_studentow (
ID_student int FOREIGN KEY REFERENCES Studenci(ID) NOT NULL,
ID_zajec int FOREIGN KEY REFERENCES Zajecia(ID_zajec) NOT NULL,
PRIMARY KEY (ID_student, ID_zajec),
Ocena float
);
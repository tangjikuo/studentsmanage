drop database if exists STUDENTSMANAGE;
create database STUDENTSMANAGE;
use STUDENTSMANAGE;
DROP TABLE IF EXISTS STUDENTSMANAGE.TEACHER;
CREATE TABLE TEACHER(
         NAME  VARCHAR(255) COLLATE UTF8_BIN NULL,
         SEX VARCHAR(255) COLLATE UTF8_BIN NULL ,
         TEA_NO VARCHAR(255) COLLATE UTF8_BIN NOT NULL UNIQUE,
         PASSWD VARCHAR(255) COLLATE UTF8_BIN NOT NULL ,
         PRIMARY KEY (PASSWD)
     )ENGINE=INNODB DEFAULT CHARSET=UTF8;
drop table if exists STUDENTSMANAGE.STUDENT;
CREATE TABLE STUDENT(
     	NAME VARCHAR(255) COLLATE UTF8_BIN  NULL,
     	SEX VARCHAR(255) COLLATE UTF8_BIN,
     	STU_NO VARCHAR(255) COLLATE UTF8_BIN NOT NULL UNIQUE ,
     	TEA_NO VARCHAR(255) COLLATE UTF8_BIN NOT NULL ,
     	SCORE VARCHAR(255) COLLATE UTF8_BIN NULL,
     	PRIMARY KEY (STU_NO),
     	FOREIGN KEY (TEA_NO) REFERENCES TEACHER(TEA_NO)
     )ENGINE=INNODB DEFAULT CHARSET=UTF8;
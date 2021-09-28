CREATE DATABASE bank_statements;

CREATE TABLE bank_statements.`Bank` (
  `id` tinyint AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE bank_statements.`Statement` (
  `id` smallint AUTO_INCREMENT,
  `bank_id` tinyint,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`bank_id`) REFERENCES Bank(id)
);

CREATE TABLE bank_statements.`StatementLine` (
  `id` int AUTO_INCREMENT,
  `statement_id` smallint,
  `transaction_date` date NOT NULL,
  `ag_movm` varchar (10),
  `concept` varchar (50),
  `debit` float,
  `credit` float,
  `balance` float,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`statement_id`) REFERENCES `Statement`(id)
);

DROP TABLE StatementLine;
DROP TABLE `Statement`;
DROP TABLE Bank;
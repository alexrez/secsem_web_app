CREATE TABLE users (
	id				SERIAL PRIMARY KEY,
	login			varchar(20) NOT NULL CHECK (login <> ''),
	money_amount	integer DEFAULT 0,
	card_number		varchar(16),
	status			boolean NOT NULL
);

CREATE TABLE realy_secret_datas (
	id 				integer,
	password			varchar(20) NOT NULL CHECK (password <> ''),
	FOREIGN KEY (id) REFERENCES users (id)
);


INSERT INTO users (login, money_amount, card_number, status)
	VALUES
	('admin', 99, '4916708165394191', true),
	('Alex', 8, '4331496598218578', true),
	('Bob', 72, '4331496598218578', true),
	('Pane', 9, '4331496598218578', false),
	('Kovi', 17, '4331496598218578', false),
	('Kuch', 86, '4331496598218578', false);

INSERT INTO realy_secret_datas
	VALUES
	(1, 'admin123'),
	(2, 'qwerty'),
	(3, 'columbus'),
	(4, 'val11'),
	(5, 'devils'),
	(6, 'number_one');

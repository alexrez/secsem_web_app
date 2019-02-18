from sqlalchemy import (
	MetaData, Table, Column, ForeignKey,
	Integer, Text, VARCHAR, Boolean
)

meta = MetaData()

users = Table(
	'users', meta,
	Column('id', Integer, primary_key = True),
	Column('login', VARCHAR, nullable = False),
	Column('money_amount', Integer, server_default = "0"), 
	Column('card_number', VARCHAR),
	Column('status', Boolean, nullable = False)
)

realy_secret_datas = Table(
	'realy_secret_datas', meta,
	Column('id', Integer, ForeignKey('users.id')),
	Column('password', VARCHAR, nullable = False),
)
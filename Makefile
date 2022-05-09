#from cProfile import run


serve:
    flask run

migrations: 
	flask db init

migrate:
	flask db migrate #-m "migration"

.PHONY: run_redis
run_redis:
	redis-server

.PHONY: run_server
run_server:
	python manage.py runserver
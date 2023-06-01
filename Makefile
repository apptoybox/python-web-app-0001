.PHONY: all build start stop

all: build

build:
	docker build -t loadbalancer -f Dockerfile.loadbalancer .
	docker build -t appserver -f Dockerfile.appserver .
	docker build -t database -f Dockerfile.database .

start:
	docker-compose up -d

stop:
	docker-compose down

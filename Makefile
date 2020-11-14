.PHONY: build
build:
	docker build --tag world-viz .

#--- Running the program ---#
.PHONY: run
run:
	docker-compose up

.PHONY: run-detached
run-detached:
	docker-compose up --detach

.PHONY: shutdown
shutdown:
	docker-compose down

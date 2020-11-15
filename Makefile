#--- Testing ---#
.PHONY: build
build:
	docker build --tag world-viz --target production .

.PHONY: build-db-pop
build-db-pop:
	docker build --tag world-viz_db_pop --target db_population .

.PHONY: build-test
build-test: build
	docker build --tag world-viz_test -f $(CURDIR)/util/Test.Dockerfile .

.PHONY: unit-test
unit-test: build-test
	docker run --rm world-viz_test \
		pytest test

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

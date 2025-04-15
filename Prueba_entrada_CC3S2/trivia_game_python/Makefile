DOCKER_COMPOSE = docker compose

.PHONY: up down build clear check

check:
    @command -v $(DOCKER_COMPOSE) >/dev/null 2>&1 || { \
        echo >&2 "Error: docker is not installed"; \
        exit 1; \
    }

up: check
	$(DOCKER_COMPOSE) up --build

down: check
	$(DOCKER_COMPOSE) down

go: check
	$(DOCKER_COMPOSE) up

clear: check
	docker image prune -f
.DEFAULT_GOAL := help

# Load environment variables from .env file
include .env
export

# Targets
.PHONY: help clean all-local all-docker

help:
	@echo "Available targets:"
	@echo "  make all-local      - Run the application locally (without Docker)"
	@echo "  make all-docker     - Build Docker image, run container, and clean up"
	@echo "  make all-jupyter    - Set up Jupyter notebooks locally within the virtual environment"
	@echo "  make build          - Build the Docker image"
	@echo "  make run            - Run the Docker container"
	@echo "  make clean          - Remove the Docker container and image"
	@echo "  make venv-setup     - Set up and activate a virtual environment"
	@echo "  make venv-install   - Install dependencies in the virtual environment"
	@echo "  make train-model    - Train the sentiment analysis model"
	@echo "  make local-run      - Run the application locally within the virtual environment"

all-local: venv-setup venv-install local-run

all-docker: build run clean

all-jupyter: venv-setup venv-install local-jupyter

venv-setup:
	@echo "Setting up and activating virtual environment..."
	@python -m venv $(VENV_NAME)
ifeq ($(OS),Windows_NT)
	@.\\$(VENV_NAME)\\Scripts\\activate
else
	@. $(VENV_NAME)/bin/activate
endif

venv-install:
	@echo "Installing dependencies in virtual environment..."
	pip install -r src/requirements.txt

local-jupyter:
	@echo "Running the jupyter notebooks locally within the virtual environment..."
	jupyter notebook

local-run:
	@echo "Running the application locally within the virtual environment..."
	python src/main.py

build: venv-setup venv-install
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE_NAME):$(GIT_HASH) --build-arg TRAIN_MODEL=$(TRAIN_MODEL) .
	@echo "Docker image built with tag: $(DOCKER_IMAGE_NAME):$(GIT_HASH)"

run:
	@echo "Running Docker container..."
	@-docker rm -f $(DOCKER_CONTAINER_NAME)
	@docker run -it --name $(DOCKER_CONTAINER_NAME) -v $(DATA_PATH):/app/data $(DOCKER_IMAGE_NAME):$(GIT_HASH)

clean:
	@echo "Cleaning up Docker container and image..."
	@docker rm -f $(DOCKER_CONTAINER_NAME) || true
	@docker rmi -f $(DOCKER_IMAGE_NAME):$(GIT_HASH) || true
	@echo "Cleanup complete."

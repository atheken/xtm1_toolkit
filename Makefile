TAG ?= latest

build:
	docker buildx create --use
	docker buildx build --platform=linux/amd64,linux/arm64 . --push --tag atheken/xtm1-toolkit:$(TAG)

requirements.txt: Pipfile.lock
	@pipenv lock --requirements > requirements.txt

build-docker: requirements.txt
	@docker pull python:3
	@docker build . --no-cache -t hivdb/hivdb-cms-builder:latest

push-docker: build-docker
	@docker push hivdb/hivdb-cms-builder:latest

pull-docker:
	@docker pull hivdb/hivdb-cms-builder:latest

debug:
	@docker run \
		--mount type=bind,source=$(PWD),target=/app \
		--workdir /app --rm -it \
		hivdb/hivdb-cms-builder:latest \
		bash

_docker-build:
	@rm -rf build/
	@docker run \
		--mount type=bind,source=$(PWD),target=/app \
		--workdir /app --rm -it \
		hivdb/chiro-cms-builder:latest \
		python build.py

_fast-build:
	@rm -rf build/
	@pipenv run python build.py

sync-hivfacts:
	@rsync -av --delete --delete-excluded --exclude={'*.yml','*.yaml'} ../hivfacts/data/* resources/hivfacts-data


build: $(shell find . -type f -not -path "./.git*" -a -not -path "*.swp" -a -not -path "*.swo" -a -not -path "*/.DS_Store" -a -not -path "*/.gradle/*" -a -not -path "*/build/*" -a -not -path "*.log" -a -not -path "*/local/*" | sed 's#\([| ]\)#\\\1#g') build.py
	@test -e $(shell which pipenv) && make _fast-build || make _docker-build

deploy-localhost: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/localhost --delete

deploy-staging: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/staging --delete

deploy-staging2: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/staging2 --delete

deploy-prod: build
	@docker run \
		--mount type=bind,source=$(HOME)/.aws,target=/root/.aws,readonly \
		--mount type=bind,source=$(PWD),target=/app,readonly \
		--rm -it hivdb/hivdb-cms-builder:latest \
		aws s3 sync /app/build s3://cms.hivdb.org/prod \
		--delete --cache-control max-age=600

deploy-all: deploy-localhost deploy-staging deploy-staging2 deploy-prod


.PHONY: build-docker push-docker deploy-* sync-hivfacts

create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md docs/SPECIFICATION.md
	touch src/.gitkeep tests/.gitkeep

install:
	pip3 install -r requirements.txt

install-dep:
	pip3 install -e .

test-pytest:
	python3 -m pytest

activate-env:
	source ./.venv/bin/activate
setup:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
install:
	venv/bin/pip install ${PKG}
	venv/bin/pip freeze > requirements.txt
run:
	venv/bin/python analysis.py
install: venv
	pip3 install -Ur requirements.txt
venv :
	test -d venv || python3 -m venv venv
activate:
	. venv/bin/activate
run:
	python3 server.py
clean:
	rm -rf venv
	find -iname "*.pyc" -delete

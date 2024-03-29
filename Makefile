init-venv:
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi

install: init-venv
	source .venv/bin/activate; python3 -m pip install .[dev]

test:
	source .venv/bin/activate; python3 -m pytest --junitxml=build/test_results/report.xml

check: test

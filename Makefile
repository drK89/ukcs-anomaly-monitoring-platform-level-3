.PHONY: install run test api dashboard docker
install:
	python -m pip install -r requirements.txt
run:
	python run_pipeline.py
test:
	python -m unittest discover -s tests -v
api:
	python run_api.py
dashboard:
	streamlit run dashboard.py
docker:
	docker compose up --build


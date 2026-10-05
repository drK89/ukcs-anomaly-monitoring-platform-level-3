FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python run_pipeline.py
EXPOSE 8000
CMD ["python", "run_api.py"]


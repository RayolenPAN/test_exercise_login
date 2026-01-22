FROM python:3.10-slim
WORKDIR /python_app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install playwright && playwright install chromium
COPY . .
CMD ["pytest", "tests/", "-v", "--alluredir=allure-results"]
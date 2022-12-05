# Resume Parser Ranker Web

<img src="https://img.shields.io/static/v1?label=Docker&message=Compose&color=PURPLE"/> <img src="https://img.shields.io/static/v1?label=Slim.ai&message=Reports&color=YELLOW"/> <img src="https://img.shields.io/static/v1?label=Docker&message=Slim&color=YELLOW"/>



This is a web application for ranking the resume parser results. It is built using Django and React.

Main implementation of resume parser is in [this repository](https://github.com/gamingflexer/resume-parser-ranker)

Some Features:
- API Documentation
- Dockerization with best practices 
- Docker Compose for easy deployment
- Docker-slim for smaller docker images
- Docker multi-stage builds for smaller docker images
- Slim.ai for image optimization
- Reports for docker images

## Installation

#### Prerequisites for docker

- Docker
- Docker Compose

#### Steps

1. Clone the repository
2. Run `docker-compose up` in the root directory
3. Go to `http://localhost:8000` in your browser

#### Prerequisites for local development

- Python 3.6

#### Steps

1. Clone the repository
2. Create a virtual environment using `virtualenv venv`
3. Activate the virtual environment using `source venv/bin/activate`
4. Install the requirements using `pip install -r requirements.txt`
5. Run the migrations using `python manage.py make migrations` and `python manage.py migrate`
6. Run the server using `python manage.py runserver`
7. Go to `http://localhost:8000` in your browser

## Django Apps & API Documentation

## Dockerization Reports

#### Docker Image Size

#### Docker Image Layers

#### Docker Image Vulnerabilities

#### Docker Image Security

#### Docker Image Build Time

#### Slim.ai Reports
# TinyURL using Django and PostgresQL

The TinyURL project is a URL shortening service built using Django, designed to transform long URLs into shorter, more manageable links. This service provides users with the ability to generate unique short URLs that redirect to the original longer URLs. Additionally, it incorporates a feature to set expiration dates for the shortened URLs, ensuring they are automatically deleted once expired. This is facilitated using Celery and Redis, where Celery handles the background task of deleting expired URLs at scheduled intervals.

Key features of the project include:

* URL Shortening: Generate a unique short URL for any provided long URL.
* Expiration Date: Assign an expiration date to each shortened URL, after which the URL becomes invalid and is automatically deleted.
* Background Task Handling: Utilize Celery and Redis to manage the deletion of expired URLs without affecting the performance of the main application.
* User Interface: A simple web interface for users to input their long URLs and receive short URLs in return.
* Database Management: Store URLs and their metadata, such as creation and expiration dates, in a database.
The project structure is organized with separate modules for URL handling, background tasks, and Celery configuration, ensuring a clean and maintainable codebase. The integration of Celery and Redis allows for efficient management of background tasks, making the service reliable and scalable.

## Features

* URL shortening
* URL expiration
* Efficient database management

## Requirements

* Python 3.12
* Django 3.x
* PostgresQL 12.x
* Celery 5.x
* Redis 6.x

## Installation

1. Clone the repository: `git clone https://github.com/aDiTyA-2712/TinyURL-using-Django-and-PostgresQL.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Run the application: `python manage.py runserver`

## Usage

1. Create a new URL: `http://localhost:8000/create`
2. Get a shortened URL: `http://localhost:8000/<short_code>`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
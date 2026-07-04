# OrainAuth - Django

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## Features

- **Custom User Model:** Fully customizable user profiles using Django's `AbstractUser`
- **Secure Authentication:** Password hashing, CSRF protection, and session-based security

## Tech Stack

- **Backend:** [Python](https://www.python.org/) & [Django](https://www.djangoproject.com/)
- **Frontend:** HTML5, CSS3, [Bootstrap 4/5](https://getbootstrap.com/)
- **Database:** MySQL
- **Security:** Django Middleware, CSRF Tokens, Password Hashing

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git

## Installation

Follow these steps to get a local copy up and running:

1. **Clone the repository:**

```bash
   git clone https://github.com/2yt-code/OrainAuth.git
   cd OrainAuth
```

2. **Create a Virtual Environment:**

```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
```

3. **Install dependencies:**

```bash
   pip install -r requirements.txt
```

4. **Run Migrations:**

```python
   python manage.py migrate
```

5. **Start the Server:**

```python
   python manage.py runserver
```

Now open http://127.0.0.1:8000/ in your browser

## Usage

To access the authentication flow:

    - Login: accounts/login
    - Register:  accounts/register
    - Dashboard: dashboard/
    - Home : /

## Screenshots

![Login Page](https://github.com/2yt-code/OrainAuth/blob/main/core/Screenshots/screenshot-1.png)
![Dashboard Page](https://github.com/2yt-code/OrainAuth/blob/main/core/Screenshots/screenshot-2.png)
![Home Page](https://github.com/2yt-code/OrainAuth/blob/main/core/Screenshots/screenshot-3.png)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

I would appreciate it if you could add a star to support my project 🙏
Made with ❤️ by [2yt](https://github.com/2yt-code)

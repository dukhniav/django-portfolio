![](https://img.shields.io/github/actions/workflow/status/dukhniav/django-portfolio/codacy.yml)
![](https://img.shields.io/github/actions/workflow/status/dukhniav/django-portfolio/django.yml)
![](https://img.shields.io/github/actions/workflow/status/dukhniav/django-portfolio/semgrep.yml)

1 - run makemigrations
2 - run migrate
3 - run manage.py loaddata bill_types.json (to load default bill types)


2. Adding a new subapp
2.1. python manage.py startapp payments ./personal_finance/payments
2.2. update the new subapp name in `app.py` file (reference bills or payments apps)

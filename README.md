# Django Starter

A template to start a Django project. I aim to make this:
- easy to use: by simplify the features as much as possible and clear code comments
- comprehensive: by supporting various features and use-cases

This is made possible by very helpful knowledge from the book
 [Django 2 by Example](https://learning.oreilly.com/library/view/django-2-by/9781788472487/).
 
CSS are taken from the source code of the book at:
> https://github.com/PacktPublishing/Django-2-by-Example

## Requirements

- Python: 3.7+
- Django: 3
- Postgres: 12

## Configurations

### Databases

| app | env | db name | user | password |
|---|---|---|---|---|
| blog | local | django_starter_blog_db | django_starter | 123 |

### Admin users

| app | env | user | password |
|---|---|---|---|
| blog | local | mt | 123 |

For other information, including design decisions, please take a look at [wiki][wiki].

[wiki]: https://github.com/mt40/django_starter/wiki
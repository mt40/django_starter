# Django Starter

A template to start a Django project. I aim to make this:
- easy to use: by simplify the features as much as possible and clear code comments
- comprehensive: by supporting various features and use-cases

This is made possible by very helpful knowledge from the book
 [Django 2 by Example](https://learning.oreilly.com/library/view/django-2-by/9781788472487/).

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

## Design

### Search engine

For simplicity, this project uses Postgres Full Text Search. We are already using Postgres
as DB anyway. If you want to integrate another search engine like Elastic Search, consider 
looking at [HayStack][haystack].


[haystack]: http://haystacksearch.org
# Model Bakery and Faker Bug

This project is to replicate a strange bug that happens when you're using Faker with a Model Bakery Recipe and trying to
seed the faker data to have consistent results in your assertions.

Tests in `tests/test_recipes.py` illustrate the bug. Versions less than 1.3.2 work and version greater than 1.3.3 don't
work. All the tests fail randomly, so you have to run them multiple times to see if they work or don't work
(e.g. `for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_from_global; done`).

Facts:
1. Model Bakery versions 1.1.1 to 1.3.2 work with Django versions 3.2, 4.0, and 4.1.
2. Model Bakery version 1.3.3 and greater don't work with Django versions 3.2 and 4.0
3. Model Bakery version 1.3.3 and Django 4.1 work
4. When you run individual tests multiple times they randomly pass and fail
   (e.g. `for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_from_global; done`)
5. When using just Faker with seeding, but without using a Model Baker Recipe it passes 100% of the time.

Things tried:
1. Upgrading to the newest version of Faker
2. Upgrading to Django 4.1.1 fixed it
3. Tried upgrading to model-bakery 1.7.0 and that didn't fix it
4. When using `@pytest.mark.parametrize("num", list(range(1, 11)))` on each test method, they either all pass or all fail
5. Tried downgrading to pytest 6.2.5 from 7.1.3, and it didn't fix it

Strangely enough trying to reproduce the same bug in a fork of model_bakery didn't produce any results. Probably because
test is using Django 4.1.
See: https://github.com/epicserve/model_bakery/compare/main...epicserve:model_bakery:bug/faker_seeding_bug?expand=1

## Setup

1. Create a virtual environment.
    ```
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install required python dependencies.
    ```
    pip install -r requirements.txt
    ```

## Run tests

```
pytest
```

or use tox to run the tests with multiple versions of Model Bakery and Django

```
tox
```

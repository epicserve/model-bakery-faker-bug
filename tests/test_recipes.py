import pytest as pytest
from faker import Faker
from model_bakery.recipe import Recipe

global_faker = Faker()

"""
Tests to try and isolate why the export tests with snapshots don't work after upgrading model_baker. In my testing
versions less than 1.3.2 work and version greater than 1.3.3 don't work. All the tests fail randomly, so you have to run
them multiple times to see if they work or don't work.

Facts:
1. Versions 1.1.1 to 1.3.2 works. Starting with version 1.3.3 it breaks.

Things tried:
1. Upgrading to the newest version of Faker
2. Upgrading to Django 4.1.1 fixed it, however upgrading from 3.2.9 to 3.2.15 didn't fix it
3. Tried upgrading to model-bakery 1.7.0 and that didn't fix it
4. When using `@pytest.mark.parametrize("num", list(range(1, 11)))` on each test method, they either all pass or all fail
5. Tried downgrading to pytest 6.2.5 from 7.1.3 and it didn't fix it

Strangely enough try to reproduce the same bug in a fork of model_bakery didn't produce any results.
See: https://github.com/epicserve/model_bakery/compare/main...epicserve:model_bakery:bug/faker_seeding_bug?expand=1
"""


@pytest.mark.django_db
class TestFakerSeeding:
    def test_faker_directly(self):
        """
        WORKS 100% of the time!!!!
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_directly; done
        """
        global_faker.seed_instance(10)
        username1 = global_faker.user_name()
        username2 = global_faker.user_name()
        assert username1 == "pattersonbelinda"
        assert username2 == "stevenhenry"

    def test_faker_seeding_from_global(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_from_global; done
        """
        global_faker.seed_instance(10)

        user_recipe = Recipe(
            "auth.User",
            username=global_faker.user_name,
            email=global_faker.email,
        )

        user = user_recipe.make()
        assert user.username == "pattersonbelinda"

    def test_faker_seeding_form_local(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_form_local; done
        """
        faker = Faker()
        faker.seed_instance(10)

        user_recipe = Recipe(
            "auth.User",
            username=faker.user_name,
            email=faker.email,
        )

        user = user_recipe.make()
        assert user.username == "pattersonbelinda"
        assert user.email == "stevenhenry@example.com"

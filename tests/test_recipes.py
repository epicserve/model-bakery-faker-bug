import pytest as pytest
from faker import Faker
from model_bakery.recipe import Recipe

global_faker = Faker()


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return 10


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

    def test_faker_instance_seeding_from_global(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_instance_seeding_from_global; done
        """
        global_faker.seed_instance(10)

        user_recipe = Recipe(
            "auth.User",
            username=global_faker.user_name,
            email=global_faker.email,
        )

        user = user_recipe.make()
        assert user.username == "pattersonbelinda"

    def test_faker_instance_seeding_form_local(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_instance_seeding_form_local; done
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

    def test_faker_seeding_from_global(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_from_global; done
        """
        Faker.seed(10)

        user_recipe = Recipe(
            "auth.User",
            username=global_faker.user_name,
            email=global_faker.email,
        )

        user = user_recipe.make()
        assert user.username == "austinhenry"

    def test_faker_seeding_form_local(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_seeding_form_local; done
        """
        Faker.seed(10)
        faker = Faker()

        user_recipe = Recipe(
            "auth.User",
            username=faker.user_name,
            email=faker.email,
        )

        user = user_recipe.make()
        assert user.username == "pattersonbelinda"
        assert user.email == "stevenhenry@example.com"

    def test_fake_wrapper_func(self):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_fake_wrapper_func; done
        """
        _faker = Faker()
        _faker.seed_instance(10)

        def get_fake(func_name):
            return getattr(_faker, func_name)()

        user_recipe = Recipe(
            "auth.User",
            username=get_fake('user_name'),
            email=get_fake('email'),
        )
        user = user_recipe.make()
        assert user.username == "pattersonbelinda"
        assert user.email == "stevenhenry@example.com"

    def test_faker_with_fixture(self, faker, faker_seed):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_with_fixture; done
        """
        username1 = faker.user_name()
        username2 = faker.user_name()
        assert username1 == "pattersonbelinda"
        assert username2 == "stevenhenry"

    def test_faker_with_fixture_recipe(self, faker, faker_seed):
        """
        for i in {1..20}; do pytest tests/test_recipes.py::TestFakerSeeding::test_faker_with_fixture_recipe; done
        """

        user_recipe = Recipe(
            "auth.User",
            username=faker.user_name,
            email=faker.email,
        )

        user = user_recipe.make()
        assert user.username == "pattersonbelinda"
        assert user.email == "stevenhenry@example.com"

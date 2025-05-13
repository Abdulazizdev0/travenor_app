import pytest
from django.contrib.auth import get_user_model
from user.models import *
from datetime import datetime
from travel.models import Travels




@pytest.mark.django_db
def test_user():
    user = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    assert user.phone == "0987654321"
    assert user.firstname == "first_name"
    assert user.lastname == "last_name"
    assert user.image == "image"
    assert user.location == "location"
    assert user.birth_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert user.joined_at is not None
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False



@pytest.mark.django_db
def test_user_manager():
    User = get_user_model()
    user = User.objects.create_user(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    assert user.phone == "0987654321"
    assert user.firstname == "first_name"
    assert user.lastname == "last_name"
    assert user.image == "image"
    assert user.location == "location"
    assert user.birth_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert user.joined_at is not None
    assert user.is_active is True
    assert user.is_staff is False


@pytest.mark.django_db
def test_user_manager_create_superuser():
    User = get_user_model()
    user = User.objects.create_superuser(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    assert user.phone == "0987654321"
    assert user.firstname == "first_name"
    assert user.lastname == "last_name"
    assert user.image == "image"
    assert user.location == "location"
    assert user.birth_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert user.joined_at is not None
    assert user.is_active is True
    assert user.is_staff is True


@pytest.mark.django_db
def test_saved():
    user = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    travel = Travels.objects.create(
        name="title",
        description="description",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,
    )

    saved = Saved.objects.create(
        user=user,
        travel=travel,


    )
    assert saved.user == user
    assert saved.travel == travel
    assert saved.saved_at is not None



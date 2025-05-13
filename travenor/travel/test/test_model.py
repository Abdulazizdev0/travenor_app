import pytest
from travel.models import Travels,TravelImage,TravelCategory,Review,TravelGuide
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Category
from user.models import User
from staff.models import Employee,Role




@pytest.mark.django_db
def test_travel_model():
    travel = Travels.objects.create(
        name="title",
        description="description",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,

    )
    assert travel.name == "title"
    assert travel.description == "description"
    assert travel.level == "orta"
    assert travel.start_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert travel.end_date == datetime.strptime("2023-01-02", "%Y-%m-%d").date()
    assert travel.price == 1000
    assert travel.created_at is not None


@pytest.mark.django_db
def test_travel_image():
    image1 = SimpleUploadedFile( name='test_image.jpg',content=b'some_image_data_here',content_type='image/jpeg')
    travel = Travels.objects.create(
        name="title",
        description="description",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,
    )

    image = TravelImage.objects.create(
        travel=travel,
        image=image1,
    )

    assert image.travel == travel
    assert image.image.name.startswith('images/travel_images/test_image')



@pytest.mark.django_db
def test_travel_category():
    travel = Travels.objects.create(
        name="title",
        description="description",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,
    )

    category = Category.objects.create(name="category")


    travelctg = TravelCategory.objects.create(
        travel=travel,
        category=category,
    )

    assert travelctg.travel == travel
    assert travelctg.category == category



@pytest.mark.django_db
def test_review_model():
    travel = Travels.objects.create(
        name="title",
        description="description",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,
    )
    user = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    review = Review.objects.create(
        travel=travel,
        user=user,
        rating=5,
        comment="comment",
    )


    assert review.travel == travel
    assert review.user == user
    assert review.rating == 5
    assert review.comment == "comment"
    assert review.created_at is not None


@pytest.mark.django_db
def test_travel_guide():
    travel = Travels.objects.create(
        name="title",
        description="description",
        price=1000,
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
    )
    user = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    )
    employee = Employee.objects.create(
        user=user,
        role=Role.objects.create(name="role"),
        email="email@gmail.com",
        salary=1000,
        hire_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),

    )

    travelguide = TravelGuide.objects.create(
        employee=employee,
        travel=travel,
    )
    assert travelguide.employee == employee
    assert travelguide.travel == travel




import pytest
from booking.models import Booking,Payment
from travel.models import Travels
from user.models import User
from datetime import datetime




@pytest.mark.django_db
def test_booking_model():
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
    booking = Booking.objects.create(
        travel=travel,
        user=user,
        status="pending",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
        price=1000,
        guests_count=1,
    )

    assert booking.travel == travel
    assert booking.user == user
    assert booking.status == "pending"
    assert booking.start_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert booking.end_date == datetime.strptime("2023-01-02", "%Y-%m-%d").date()
    assert booking.price == 1000
    assert booking.created_at is not None
    assert booking.guests_count == 1



@pytest.mark.django_db
def test_payment_model():
        travel=Travels.objects.create(
            name="title",
            description="description",
            start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
            price=1000,
        )
        user=User.objects.create(
            phone="0987654321",
            firstname="first_name",
            lastname="last_name",
            image="image",
            location="location",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        )
        booking=Booking.objects.create(
            travel=travel,
            user=user,
            status="pending",
            start_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            end_date=datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
            price=1000,
            guests_count=1,
        )
        payment = Payment.objects.create(
            booking=booking,
            type="card",
            amount=1000,
        )
        assert payment.booking == booking
        assert payment.type == "card"
        assert payment.amount == 1000
        assert payment.date is not None

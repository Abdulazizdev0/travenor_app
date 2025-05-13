import pytest
from notification.models import Notification
from user.models import User



@pytest.mark.django_db
def test_notification_model():
    user = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date="2023-01-01",
    )
    notification = Notification.objects.create(
        user=user,
        title="title",
        content="content",
    )
    assert notification.user == user
    assert notification.title == "title"
    assert notification.content == "content"
    assert notification.sent_at is not None
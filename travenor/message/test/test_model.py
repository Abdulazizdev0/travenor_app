import pytest
from message.models import Message
from user.models import User


@pytest.mark.django_db
def test_message_model():
    user1 = User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date="2023-01-01",
    )
    user2 = User.objects.create(
        phone="1234567890",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date="2023-01-01",

    )
    message = Message.objects.create(
        sender=user1,
        receiver=user2,
        content="content",
    )
    assert message.sender == user1
    assert message.receiver == user2
    assert message.content == "content"
    assert message.sent_at is not None
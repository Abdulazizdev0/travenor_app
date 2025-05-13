import pytest
from core.models import Category,Region


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(name="category")
    assert category.name == "category"

@pytest.mark.django_db
def test_region_model():
    region = Region.objects.create(name="region")
    assert region.name == "region"
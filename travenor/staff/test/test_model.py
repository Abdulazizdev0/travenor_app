import pytest
from staff.models import Employee,Role
from user.models import User


@pytest.mark.django_db
def test_employee_model():
    user=User.objects.create(
        phone="0987654321",
        firstname="first_name",
        lastname="last_name",
        image="image",
        location="location",
        birth_date="2023-01-01",
    )
    role = Role.objects.create(name='role')

    employee = Employee.objects.create(
        user=user,
        role=role,
        email='email@gmail.com',
        salary=1000,
    )

    assert employee.user == user
    assert employee.role == role
    assert employee.email == 'email@gmail.com'
    assert employee.salary == 1000
    assert employee.hire_date is not None


@pytest.mark.django_db
def test_role_model():
    role = Role.objects.create(name='role')
    assert role.name == 'role'




from rest_framework import viewsets
from .serializers import EmployeeSerializer
from ..permissions import IsAdminOrReadOnly
from staff.models import Employee



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]
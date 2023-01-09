# ViewSets define the view behaviour.
from rest_framework import viewsets
from example.models import School
from example.serializers.schools import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

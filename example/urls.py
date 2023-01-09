from rest_framework import routers
from example.views import SchoolViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)  # this created http request routes
# also r'schools' will be the endpoint


urlpatterns = []

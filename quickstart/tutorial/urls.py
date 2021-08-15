from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

# registering viewset with router class for matic generating the URLConf for API
""" we need more control over the API URLs we can simply drop down to using
regular class-based views, and writing the URL conf explicitly """
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
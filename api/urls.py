from django.conf.urls import url, include

# ========== API IMPORTS ============= #

from rest_framework import routers

from users.views import UserViewSet
from log.views import LogViewSet
from . import views

router = routers.DefaultRouter()

router.register(r'logs', LogViewSet)
router.register(r'usersapi', UserViewSet)
router.register(r'users', views.LoginViewset)
router.register(r'subjects', views.SubjectViewset)

urlpatterns = [
	#API REST
    url(r'^', include(router.urls)),
    url(r'^token$', views.getToken),
]
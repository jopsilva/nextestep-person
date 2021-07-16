from django.contrib import admin
from django.urls import path, include
from person.views import TypeViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('types', TypeViewSets, basename = 'Types')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# MVS - Router
from rest_framework import routers
from todo.views import TodoView

router = routers.DefaultRouter()
router.register('todo', TodoView)

# urlpatterns += [
#     path('', router.urls),
# ]

urlpatterns += router.urls
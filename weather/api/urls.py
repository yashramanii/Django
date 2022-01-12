from django.urls import include, path
from rest_framework import routers
from api.views import TodoListApiView

router = routers.DefaultRouter()
router.register('todo', TodoListApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    # path('', TodoListApiView.as_view())
]

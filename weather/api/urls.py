from django.urls import include, path
from rest_framework import routers
from api.views import addition, index, TodoListApiView

router = routers.DefaultRouter()
router.register('todo', TodoListApiView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    # path('', TodoListApiView.as_view())
     path('',index, name='index'),
    path('add',addition, name='add'),
]

from django.urls import include, path
from rest_framework import routers
from api.views import TodoListApiView, divide, index, addition, multiplication, subtraction

router = routers.DefaultRouter()
router.register('todo', TodoListApiView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    # path('', TodoListApiView.as_view())
    path('',index, name='index'),
    path('add',addition, name='add'),
    path('sub',subtraction, name='sub'),
    path('mul',multiplication, name='mul'),
    path('div',divide, name='div'),
]

from django.urls import path
from . import views 

urlpatterns = [
    path('test', views.testView),
    path('list', views.list),
    path('add/<str:add_item>', views.add),
    path('update/<int:id>/<str:value>', views.update),
    path('delete/<str:id>', views.delete),
    path('message/<str:message_str>', views.message, name="message_alert")

]
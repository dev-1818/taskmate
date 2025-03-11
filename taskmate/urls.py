
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_view.index, name='index'),
    path('task/', include('todolist_app.urls')),
    path('account/', include('user_app.urls')),
    path('contact', task_view.contact, name='contact'),
    path('about/', task_view.about, name='about'),
]
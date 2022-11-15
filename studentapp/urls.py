from django.contrib import admin
from django.urls import path
from studentapp import views


urlpatterns = [
    # path('/',views.index),
    path('',views.index),
    path('one/',views.one),
    path('filter/',views.filter),
    # path('admin/', admin.site.urls),
]
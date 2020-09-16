
from django.urls import path
from .views import home, branches, subjects, tutorials

urlpatterns = [
    path('', home, name='home'),
    path('semester/<int:sem>/branches', branches, name='branches'),
    path('semester/<int:sem>/branches/<str:branch>/subjects/',
         subjects, name='subjects'),
    path('semester/<int:sem>/branches/<str:branch>/subjects/<int:sub_id>/tutorials',
         tutorials, name='tutorials'),
]

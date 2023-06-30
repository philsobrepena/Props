from django.urls import path
from myprops.views import list_props, send_props, mark_prop_viewed

urlpatterns = [
    path('mark_prop_viewed/', mark_prop_viewed, name='mark_prop_viewed'),
    path("send/", send_props, name="send_props"),
    path("", list_props, name="list_props"),
]

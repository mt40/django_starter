from django.urls import path
from . import views

# For url namespace
# See: https://docs.djangoproject.com/en/3.1/topics/http/urls/#url-namespaces-and-included-urlconfs
app_name = "blog"  # pylint: disable=invalid-name

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    # path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
]

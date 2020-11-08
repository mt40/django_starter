from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", {"page": page, "posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})


class PostListView(ListView):
    """
    Class-based view, which is in general better than function-based views.

    See:
        https://docs.djangoproject.com/en/3.1/topics/class-based-views/
        https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview
    """

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)

        if form.is_valid():
            # retrieve form fields passed validation
            data = form.cleaned_data

            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"""{data['name']} ({data['email']}) recommends you reading '{post.title}'"""
            message = f'Read "{post.title}" at {post_url}\n\n' \
                      f'{data["name"]}\'s comments: {data["comments"]}'
            send_mail(subject, message, "admin@myblog.com", [data["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )

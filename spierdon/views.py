from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from .models import SpierdonUser, Challenge


@login_required
def index(request):
    """Return main view of spierdon app. Works only if user is logged.
        :param request: HttpRequest object
        :returns: HttpResponse object with a combined template
    """
    # return render(request, 'index.html')

    user_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=False)

    return render_to_response("index.html", {
        'user': request.user,
        'spierdon': request.user.spierdonuser,
        'user_challenges': user_challenges,
    })


@login_required
def rank(request):
    return render_to_response("rank.html", {
        "items": SpierdonUser.objects.order_by("-exp"),
        "has_public": request.user.spierdonuser.public_level,
    })

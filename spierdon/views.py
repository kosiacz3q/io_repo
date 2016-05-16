from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import SpierdonUser, Challenge, UserActiveChallenge
from django.core.urlresolvers import reverse
from django.template import RequestContext


@login_required
def index(request):
    """
    Generate main page.

    :param request: HttpRequest object
    :return: HttpResponse object with user and challenges info included
    """
    # return render(request, 'index.html')


    user_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=False)

    user_completed_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=True)

    return render_to_response("index.html", {
        'user': request.user,
        'spierdon': request.user.spierdonuser,
        'user_challenges': user_challenges,
        'user_completed_challenges': user_completed_challenges,
        },
        RequestContext(request))


@login_required
def complete_challenge(request, challenge_id):
    """
    Mark challenge as completed and redirect to main page.

    :param request: HttpRequest object
    :param challenge_id: challenge's id
    :return: HttpResponseRedirect object
    """

    challenge_to_complete = get_object_or_404(UserActiveChallenge, challenge__pk=challenge_id)

    challenge_to_complete.completed = True
    challenge_to_complete.save()

    return HttpResponseRedirect(reverse('spierdon:index'))


@login_required
def rank(request):
    """
    Create ranking of users. Works only if logged user shares its statistics to the public.

    :param request: HttpRequest object
    :return: HttpResponse object with ranking dict
    """
    return render_to_response("rank.html", {
        "items": SpierdonUser.objects.order_by("-exp"),
        "has_public": request.user.spierdonuser.public_level,
    })

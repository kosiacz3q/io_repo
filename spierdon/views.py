from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import SpierdonUser, Challenge, UserActiveChallenge
from django.core.urlresolvers import reverse
from django.template import RequestContext


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

    user_completed_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=True)

    spierdonUser = SpierdonUser.objects.get(user = request.user)

    return render_to_response("index.html", {
        'user': request.user,
        'spierdon': spierdonUser,
        'user_challenges': user_challenges,
        'user_completed_challenges': user_completed_challenges,
        },
        RequestContext(request))


@login_required
def complete_challenge(request, challenge_id):

    challenge_to_complete = get_object_or_404(UserActiveChallenge, challenge__pk=challenge_id)

    challenge_to_complete.completed = True
    challenge_to_complete.save()

    return HttpResponseRedirect(reverse('spierdon:index'))


@login_required
def rank(request):
    return render_to_response("rank.html", {
        "items": SpierdonUser.objects.order_by("-exp"),
        "has_public": request.user.spierdonuser.public_level,
    })


@login_required
def addChallange:

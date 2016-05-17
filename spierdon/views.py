from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SpierdonUser, Challenge, UserActiveChallenge, ChallengeForm
from django.core.urlresolvers import reverse
from django.template import RequestContext
import random


@login_required
def index(request):
    """
    Generate main page.

    :param request: HttpRequest object
    :return: HttpResponse object with user and challenges info included
    """
    user_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=False)

    user_completed_challenges = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=True)

    spierdon_user = SpierdonUser.objects.get(user=request.user)

    return render_to_response("index.html", {
        'user': request.user,
        'spierdon': spierdon_user,
        'user_challenges': user_challenges,
        'user_completed_challenges': user_completed_challenges,
        'ranking': SpierdonUser.objects.order_by("-exp")[:5],
        'has_public': request.user.spierdonuser.public_level,
    }, RequestContext(request))


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

    challenge_to_complete.user.exp += challenge_to_complete.challenge.exp;
    challenge_to_complete.user.save();

    return HttpResponseRedirect(reverse('spierdon:index'))


@login_required
def ranking(request):
    """
    Create ranking of users. Work only if logged user shares its statistics to the public.

    :param request: HttpRequest object
    :return: HttpResponse object with ranking dict
    """
    return render_to_response("ranking.html", {
        "items": SpierdonUser.objects.order_by("-exp"),
        "has_public": request.user.spierdonuser.public_level,
    })


@login_required
def add_challenge(request):
    """
    Create add challenge form.

    :param request: HttpRequest object
    :return: HttpResponseRedirect object
    """
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # challenge = form.save(commit=False)
                # challenge.picture = form.cleaned_data['picture']
                # challenge.save()
                return HttpResponseRedirect('/')
            except:
                pass
    return render_to_response('addChallange.html', {'form': ChallengeForm()},
                              context_instance=RequestContext(request))


@login_required
def get_challenges(request):
    """
    Get five random challenges available for current user (ie. those which are assigned to current user's level
    and not already completed).

    :param request: HttpRequest object
    :return: HttpResponse object with drawn challenges
    """
    challenges = Challenge.objects.filter(min_level__lte=request.user.spierdonuser.level,
                                          max_level__gte=request.user.spierdonuser.level)
    user_challenges = [i.challenge for i in UserActiveChallenge.objects.filter(user__exact=request.user.spierdonuser)]
    challenges = [e for e in challenges if e not in user_challenges]
    random.shuffle(challenges)
    return render_to_response('newChallenge.html', {
        "items": challenges[:5]
    })


@login_required
def join_challenge(request, challenge_id):
    """
    Join user to challenge with given id.

    :param request: HttpRequest object
    :param challenge_id: id of challenge to which user wants to join
    :return: HttpResponse of index() method
    """
    _, created = UserActiveChallenge.objects.get_or_create(challenge=Challenge.objects.get(pk=challenge_id),
                                                           user=SpierdonUser.objects.get(user=request.user))
    return index(request) if created else HttpResponse("You already joined to this challenge.")

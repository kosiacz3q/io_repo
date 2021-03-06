from django.shortcuts import render_to_response, get_object_or_404, render
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
        useractivechallenge__completed=False,
        useractivechallenge__blocked=False)

    spierdon_user = SpierdonUser.objects.get(user=request.user)

    return render(request, "index.html", {
        'user': request.user,
        'spierdon': spierdon_user,
        'user_challenges': user_challenges,
        'ranking': SpierdonUser.objects.order_by("-exp")[:4],
        'has_public': request.user.spierdonuser.public_level,
    })


@login_required
def get_completed(request):
    items = Challenge.objects.filter(
        useractivechallenge__user__user__username=request.user.username,
        useractivechallenge__completed=True, useractivechallenge__blocked=False)

    return render(request, "completed.html", {
        'items': items,
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
    if request.method == 'POST':
        request.user.spierdonuser.public_level = not request.user.spierdonuser.public_level
        request.user.spierdonuser.save()

    return render(request, "ranking.html", {
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
    return render(request, 'addChallange.html', {'form': ChallengeForm()},
                  context_instance=RequestContext(request))


@login_required
def block_challenge(request, challenge_id):
    """
    Votes for block challenge form.

    :param request: HttpRequest object
    :return: HttpResponseRedirect object
    """
    challenge_to_block = get_object_or_404(UserActiveChallenge, challenge__pk=challenge_id)

    challenge_to_block.blocked = True
    challenge_to_block.save()

    if (UserActiveChallenge.objects.filter(pk=challenge_id, blocked=True).count() > 1):
        challenge_to_block.challenge.blocked = True
        challenge_to_block.challenge.save()

    return HttpResponseRedirect(reverse('spierdon:index'))


@login_required
def get_challenges(request):
    """
    Get five random challenges available for current user (ie. those which are assigned to current user's level
    and not already completed).

    :param request: HttpRequest object
    :return: HttpResponse object with drawn challenges
    """
    challenges = Challenge.objects.filter(min_level__lte=request.user.spierdonuser.level,
                                          max_level__gte=request.user.spierdonuser.level,
                                          blocked=False)
    user_challenges = [i.challenge for i in UserActiveChallenge.objects.filter(user__exact=request.user.spierdonuser)]
    challenges = [e for e in challenges if e not in user_challenges]
    random.shuffle(challenges)
    return render(request, 'newChallenge.html', {
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
    return HttpResponseRedirect(reverse('spierdon:index')) if created else HttpResponse(
        "You already joined to this challenge.")

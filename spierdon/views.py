from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """Return main view of spierdon app. Works only if user is logged.
        :param request: HttpRequest object
        :returns: HttpResponse object with a combined template
    """
    return render(request, 'index.html')

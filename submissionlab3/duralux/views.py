from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


#@login_required(login_url="/login/")
def index(request):
    context = {}

    html_template = loader.get_template('pages/index.html')
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('pages/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('pages/auth-404-cover.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('pages/auth-maintenance-cover.html')
        return HttpResponse(html_template.render(context, request))
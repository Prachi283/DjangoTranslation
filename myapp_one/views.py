from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
    
    def render_to_response(self, context, **response_kwargs):
    
        response = super(HomePageView, self).render_to_response(context, **response_kwargs)
        response.delete_cookie(settings.LANGUAGE_COOKIE_NAME)
        return response
    
    template_name = 'home.html'

def home(request): 
    response = render(request, 'home.html')
    return response
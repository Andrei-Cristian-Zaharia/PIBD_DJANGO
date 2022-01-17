from django.db import transaction
from django.views.generic import TemplateView

from PIBD_PROJECT.models import Actor, Contract, Movie


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
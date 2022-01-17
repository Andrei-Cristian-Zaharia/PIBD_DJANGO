from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from PIBD_PROJECT.models import Contract, Actor, Movie


class ContractPageView(TemplateView):
    template_name = 'contracts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            contracts = Contract.Contract.objects.all()
            actors = Actor.Actor.objects.all()
            movies = Movie.Movie.objects.all()
        context['contracts'] = contracts
        context['actors'] = actors
        context['movies'] = movies

        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('deleteContract') is not None:

            with transaction.atomic():
                contract = Contract.Contract.objects.get(CONTRACT_ID = int(self.request.POST.get('selected_deleteContract')))

            contract.remove()

        if self.request.POST.get('addContract') is not None:

            actors = self.request.POST.getlist('createContractForThisActor')

            for actor in actors:
                contract = Contract.Contract()

                contract.ACTOR = Actor.Actor.objects.get(ACTOR_ID = str(actor))
                contract.MOVIE = Movie.Movie.objects.get(MOVIE_ID=int(self.request.POST.get('createContractForThisMovie')))

                contract.PAYCHECK = self.request.POST.get('paycheck')
                contract.DATE = parse(self.request.POST.get('date'))
                contract.DETAILS = self.request.POST.get('details')

                contract.create()

        if self.request.POST.get('editContract') is not None:

            with transaction.atomic():
                contract = Contract.Contract.objects.get(CONTRACT_ID = int(self.request.POST.get('selected_editContract')))

                actor = Actor.Actor.objects.get(ACTOR_ID = int(self.request.POST.get('editContractForThisActor')))
                actor = actor if actor != None else contract.ACTOR

                movie = Movie.Movie.objects.get(MOVIE_ID = int(self.request.POST.get('editContractForThisMovie')))
                movie = movie if movie != None else contract.MOVIE

                date = self.request.POST.get('dateE')
                date = parse(date) if date != '' else contract.DATE

                paycheck = self.request.POST.get('paycheckE')
                paycheck = paycheck if paycheck != '' else contract.PAYCHECK

                details = self.request.POST.get('detailsE')
                details = details if details != '' else contract.DETAILS

                updateContract = Contract.Contract(CONTRACT_ID=contract.CONTRACT_ID, ACTOR=actor,
                                                   MOVIE=movie, DETAILS=details, DATE=date, PAYCHECK=paycheck)

                updateContract.update()

        return self.render_to_response(self.get_context_data())
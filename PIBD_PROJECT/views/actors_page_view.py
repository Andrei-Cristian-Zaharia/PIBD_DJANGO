from django.db import transaction
from django.views.generic import TemplateView
from dateutil.parser import parse

from PIBD_PROJECT.models import Actor


class ActorPageView(TemplateView):
    template_name = 'actors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            actors = Actor.Actor.objects.all()
        context['actors'] = actors
        print(actors)

        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('deleteActor') is not None:

            with transaction.atomic():
                actor = Actor.Actor.objects.get(ACTOR_ID = int(self.request.POST.get('selected_deleteActor')))

            actor.remove()

        if self.request.POST.get('addActor') is not None:
            actor = Actor.Actor()
            actor.LASTNAME = self.request.POST.get("lastname")
            actor.FIRSTNAME = self.request.POST.get("firstname")
            actor.EMAIL_ADDRESS = self.request.POST.get("emailaddress")
            actor.PHONE_NUMBER = int(self.request.POST.get("phone"))
            actor.BIRTHDATE = parse(self.request.POST.get("birthdate"))
            actor.NATIONALITY = self.request.POST.get("nationality")

            if self.request.POST.get("prefered_role") is None:
                actor.PREFERED_ROLE = "Doesn't hane any"
            else:
                actor.PREFERED_ROLE = self.request.POST.get("prefered_role")

            if self.request.POST.get("checkbox") == "yes":
                actor.OCCUPIED = True
            else:
                actor.OCCUPIED = False

            actor.create()

        if self.request.POST.get('editActor') is not None:

            with transaction.atomic():
                actor = Actor.Actor.objects.get(ACTOR_ID = int(self.request.POST.get('selected_editActor')))

            lastname = self.request.POST.get("Elastname")
            lastname = lastname if lastname != '' else actor.LASTNAME

            firstname = self.request.POST.get("Efirstname")
            firstname = firstname if firstname != '' else actor.FIRSTNAME

            email_address = self.request.POST.get("Eemailaddress")
            email_address = email_address if email_address != '' else actor.EMAIL_ADDRESS

            phone = self.request.POST.get("Ephone")
            phone = phone if len(str(phone)) == 10 else actor.PHONE_NUMBER

            birthdate = self.request.POST.get("Ebirthdate")
            birthdate = parse(birthdate) if birthdate != '' else actor.BIRTHDATE

            nationality = self.request.POST.get("Enationality")
            nationality = nationality if nationality != '' else actor.NATIONALITY

            prefered_role = self.request.POST.get("Eprefered_role")
            prefered_role = prefered_role if prefered_role != '' else actor.PREFERED_ROLE

            checkbox = self.request.POST.get("Echeckbox")
            checkbox = True if checkbox == "yes" else False

            updateActor = Actor.Actor(ACTOR_ID=actor.ACTOR_ID, LASTNAME=lastname,
                                      FIRSTNAME=firstname, EMAIL_ADDRESS=email_address,
                                      PHONE_NUMBER=phone, BIRTHDATE=birthdate,
                                      NATIONALITY=nationality, PREFERED_ROLE=prefered_role, OCCUPIED=checkbox)

            updateActor.update()

        return self.render_to_response(self.get_context_data())

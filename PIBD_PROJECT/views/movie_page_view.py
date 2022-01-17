from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from PIBD_PROJECT.models import Movie


class MoviePageView(TemplateView):
    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            movies = Movie.Movie.objects.all()
        context['movies'] = movies

        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('deleteMovie') is not None:

            with transaction.atomic():
                movie = Movie.Movie.objects.get(MOVIE_ID = int(self.request.POST.get('selected_deleteMovie')))

            movie.remove()

        if self.request.POST.get('addMovie') is not None:
            movie = Movie.Movie()
            movie.MOVIE_NAME = self.request.POST.get('name')
            movie.MOVIE_TYPE = self.request.POST.get('type')
            movie.PRODUCTION_COMPANY = self.request.POST.get('production')
            movie.RELEASE_DATE = parse(self.request.POST.get('release'))
            movie.LANGUAGE = self.request.POST.get('language')
            movie.COUNTRY_ORIGIN = self.request.POST.get('country')
            movie.RAITING = int(self.request.POST.get('raiting'))
            movie.MOVIE_DIRECTOR = self.request.POST.get('director')

            movie.create()

        if self.request.POST.get('editMovie') is not None:

            with transaction.atomic():
                movie = Movie.Movie.objects.get(MOVIE_ID = int(self.request.POST.get('selected_editMovie')))

            name = self.request.POST.get('Ename')
            name = name if name != '' else movie.MOVIE_NAME

            type = self.request.POST.get('Etype')
            type = type if type != '' else movie.MOVIE_TYPE

            production = self.request.POST.get('Eproduction')
            production = production if production != '' else movie.PRODUCTION_COMPANY

            date = self.request.POST.get('Erelease')
            date = parse(date) if date != '' else movie.RELEASE_DATE

            language = self.request.POST.get('Elanguage')
            language = language if language != '' else movie.LANGUAGE

            origin = self.request.POST.get('Ecountry')
            origin = origin if origin != '' else movie.COUNTRY_ORIGIN

            raiting = int(self.request.POST.get('Eraiting'))
            raiting = raiting if raiting <= 10 or raiting >= 0 else movie.RAITING

            director = self.request.POST.get('Edirector')
            director = director if director != '' else movie.MOVIE_DIRECTOR

            updateMovie = Movie.Movie(MOVIE_ID=movie.MOVIE_ID, MOVIE_NAME=name,
                                      MOVIE_TYPE=type, MOVIE_DIRECTOR=director,
                                      PRODUCTION_COMPANY=production, RELEASE_DATE=date,
                                      LANGUAGE=language, COUNTRY_ORIGIN=origin, RAITING=raiting)

            updateMovie.update()

        return self.render_to_response(self.get_context_data())
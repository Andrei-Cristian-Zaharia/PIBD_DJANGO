from django.db import models, transaction


class Movie(models.Model):
    MOVIE_ID = models.BigAutoField(primary_key=True)
    MOVIE_NAME = models.CharField(max_length=45)
    MOVIE_TYPE = models.CharField(max_length=45)
    PRODUCTION_COMPANY = models.CharField(max_length=45)
    RELEASE_DATE = models.DateField(blank=True, null=True)
    LANGUAGE = models.CharField(max_length=45, blank=True, null=True)
    COUNTRY_ORIGIN = models.CharField(max_length=45, blank=True, null=True)
    RAITING = models.FloatField(blank=True, null=True)
    MOVIE_DIRECTOR = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filme'

    def __str__(self):
        return self.MOVIE_NAME

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()
from django.db import models, transaction
from PIBD_PROJECT.models import Actor, Movie

class Contract(models.Model):
    CONTRACT_ID = models.BigAutoField(primary_key=True)
    ACTOR = models.ForeignKey('Actor', on_delete=models.CASCADE)
    MOVIE = models.ForeignKey('Movie', on_delete=models.CASCADE)
    DATE = models.DateField(blank=True, null=True)
    PAYCHECK = models.IntegerField(blank=True, null=True)
    DETAILS = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'
        unique_together = (('CONTRACT_ID', 'MOVIE', 'ACTOR'),)

    def __str__(self):
        return self.CONTRACT_ID

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()

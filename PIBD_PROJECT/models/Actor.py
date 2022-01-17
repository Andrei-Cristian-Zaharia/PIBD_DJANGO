from django.db import models, transaction


class Actor(models.Model):
    ACTOR_ID = models.BigAutoField(primary_key=True)
    LASTNAME = models.CharField(max_length=45)
    FIRSTNAME = models.CharField(max_length=45)
    EMAIL_ADDRESS = models.CharField(max_length=45, blank=True, null=True)
    PHONE_NUMBER = models.IntegerField()
    BIRTHDATE = models.DateField(blank=True, null=True)
    NATIONALITY = models.CharField(max_length=45, blank=True, null=True)
    PREFERED_ROLE = models.CharField(max_length=45, blank=True, null=True)
    OCCUPIED = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actori'

    def __str__(self):
        return self.FIRSTNAME

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()
from django.db import models

# Create your models here.
class ClintsRegister(models.Model):
    number_of_clients = models.IntegerField("Number of Clients", default=0, blank=True, null=True)
    Projects_completed = models.IntegerField("Projects Completed", default=0, blank=True, null=True)
    successful_appeals = models.IntegerField("Successful Appeals", default=0, blank=True, null=True)


    def __str__(self):
        return f"{self.number_of_clients}  |  {self.Projects_completed} | {self.successful_appeals}"
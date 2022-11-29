from django.db import models

# Create your models here.

class State(models.TextChoices):
    EVENT1 = 'r', "Reptile week"
    EVENT2 = 'i', "Feeding the deers"
    EVENT3 = 'd', "Adopt a pet"

#class Event(models.TextChoices):
#    Event_1 = '1', "Lizard week"
#    Event_2 = '2', "Feeding the deers"
#    Event_3 = '3', "Adopting a pet"

class Event(models.Model):
    name = models.CharField(verbose_name="Attendee name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Select event", max_length=1, choices=State.choices)

    def __str__(self):
        return self.name


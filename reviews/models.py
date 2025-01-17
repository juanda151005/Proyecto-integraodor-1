from django.db import models
from django.contrib.auth.models import User
from city.models import City

class range(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGTH = 8
        NINE = 9
        TEN = 10

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=100)
    general_review = models.CharField(max_length=2000)
    touristic_places_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    history_and_culture_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    gastronomy_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    costs_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    safety_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    weather_rate = models.IntegerField(choices=range.choices, default=range.ONE)
    general_rate = models.FloatField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calcular el promedio de los campos de tasa
        total_rate = (
            self.touristic_places_rate +
            self.history_and_culture_rate +
            self.gastronomy_rate +
            self.costs_rate +
            self.safety_rate +
            self.weather_rate
        )
        num_rates = 6
        self.general_rate = total_rate / num_rates
        
        super().save(*args, **kwargs)


    def __str__(self):
        return self.city

class ReplyReview(models.Model):
    text = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self): 
        return self.text
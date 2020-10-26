from django.db import models

class Machine(models.Model):
    machineName = models.CharField(max_length=255)
    body_text = models.TextField()

    def __str__(self):
        return self.machineName

class Probleme(models.Model):
    machineName = models.CharField(max_length=255)
    body_text = models.TextField()

    def __str__(self):
        return self.machineName
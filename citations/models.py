from django.db import models

class Citation(models.Model):
    class AuteurChoices(models.TextChoices):
        NOUREDDINE_OUBIHI = 'Noureddine Oubihi', 'Noureddine Oubihi'
        NOLWENN_MYRAN = 'Nolwenn Myran', 'Nolwenn Myran'
        DAMIEN_PRACA = 'Damien Praca', 'Damien Praca'
        JEROME_DIAZ_REY = 'Jérome Diaz-Rey', 'Jérome Diaz-Rey'
        VALENTIN_MARTIN = 'Valentin Martin', 'Valentin Martin'
        JEREMY_GROSS = 'Jérémy Gross', 'Jérémy Gross'

    auteur = models.CharField(max_length=50, choices=AuteurChoices.choices)
    description = models.CharField(max_length=500, null=True)
    date = models.DateField()

    def __str__(self):
        return f"Citation {self.description} by {self.auteur}"

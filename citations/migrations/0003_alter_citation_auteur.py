# Generated by Django 5.0.1 on 2024-06-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citations', '0002_alter_citation_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='auteur',
            field=models.CharField(choices=[('Noureddine Oubihi', 'Noureddine Oubihi'), ('Nolwenn Myran', 'Nolwenn Myran'), ('Damien Praca', 'Damien Praca'), ('Jérome Diaz-Rey', 'Jérome Diaz-Rey'), ('Valentin Martin', 'Valentin Martin'), ('Jérémy Gross', 'Jérémy Gross')], max_length=50),
        ),
    ]
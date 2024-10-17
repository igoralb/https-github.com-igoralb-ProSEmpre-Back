# Generated by Django 5.1.2 on 2024-10-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_artigos_legendabanner_materiaisapoio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nossasferramentas',
            name='ferramenta',
        ),
        migrations.AddField(
            model_name='nossasferramentas',
            name='destaque',
            field=models.CharField(default='', max_length=10, verbose_name='Texto ferramenta destaque'),
        ),
        migrations.AddField(
            model_name='nossasferramentas',
            name='normal',
            field=models.CharField(default='', max_length=10, verbose_name='Texto ferramenta normal'),
        ),
    ]
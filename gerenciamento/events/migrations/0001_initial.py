# Generated by Django 5.0.3 on 2024-08-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('show', 'Show'), ('teatro', 'Teatro'), ('orquestra', 'Orquestra'), ('musical', 'Musical'), ('humor', 'Humor')], max_length=20)),
                ('dataInicial', models.DateTimeField()),
                ('dataFinal', models.DateTimeField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gratuito', models.BooleanField(default=False)),
                ('local', models.CharField(max_length=200)),
                ('horario', models.TimeField()),
                ('cidade', models.CharField(max_length=100)),
                ('vagas', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIAutentificacion', '0003_usuario_user_lastname_usuario_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='token',
            field=models.TextField(max_length=30),
        ),
    ]

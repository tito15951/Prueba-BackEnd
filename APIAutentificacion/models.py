from asyncio.windows_events import NULL
from django.db import models

class Usuario(models.Model):
    usuario=models.TextField(primary_key=True,max_length=20)
    user_name=models.TextField(null=False,max_length=20)
    user_lastname=models.TextField(null=False,max_length=20)
    contrasenia=models.TextField(null=False,max_length=20)
    token=models.TextField(null=True,max_length=30,default=NULL)

    def __str__(self):
        return self.usuario

    def get_usuario(self):
        return self.usuario

    def get_contrasenia(self):
        return self.contrasenia


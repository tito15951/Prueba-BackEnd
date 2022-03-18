from email import header
from email.mime import application
import mimetypes
import re
from telnetlib import STATUS
from wsgiref import headers
from django.shortcuts import render
from django.views import View
from .models import Usuario
from django.http import JsonResponse
from django.utils.crypto import get_random_string

class AllUsers(View):
    def get(self,request):
        if request.method=='GET':
            if('token' in request.GET and len(request.GET['token'])>1):#Verifica que tenga el token y que no sea vacio
                try:
                    usuario=Usuario.objects.get(token=request.GET['token'])#Si el token no existe, falla y se va
                    usuarios=Usuario.objects.all()
                    return JsonResponse(list(usuarios.values('user_name','user_lastname')),safe=False,status=200)
                except:
                    resp={'error_message':"Token de acceso invalido"}
                    return JsonResponse(resp,safe=False,status=401)
            else:
                resp={'error_menssage':"No se encuentra la pagina"}
                return JsonResponse(resp,safe=False,status=404)
        else:
            resp={'error_menssage':"Peticion invalida"}
            return JsonResponse(resp,safe=False,status=400)
            

class AutenticateUser(View):
    def post(self,request):
        if request.method=='POST':
            if(('user' in request.POST) and ('password' in request.POST)):#Verifica que este bien estructurado
                try:#Si no lo encuentra es porque se equivocó o no existe y falla, se va para el except
                    usuario=Usuario.objects.get(usuario=request.POST['user'], contrasenia=request.POST['password'])
                    token = get_random_string(length=30)#Creo un token aleatorio
                    usuario.token=token
                    usuario.save()
                    resp={'token':token,'user_name':request.POST['user']}
                    return JsonResponse(resp,safe=False,status=200)#Creo la respuesta y la envio
                except:
                    return JsonResponse({'error_message':"Credenciales invalidas o usuario inexistente"},safe=False,status=401)#Si no escribe bien el usuario o contra, devuelve ese mensjae
            else:
                resp={'error_menssage':"Peticion invalida"}
                return JsonResponse(resp,safe=False,status=400)
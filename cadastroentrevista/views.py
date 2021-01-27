from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import json

class UsuarioList(viewsets.ViewSet):
                           
    def list(self, request):
        id_post = self.request.query_params.get('id')
        if id_post:
            queryset = Usuario.objects.filter(id=int(id_post))
            serializer = UsuarioSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Usuario.objects.all()
            serializer = UsuarioSerializer(queryset, many=True)
            di = {}
            lista = []
            print(serializer.data)
            for i in serializer.data:
                di['id'] = i['id']
                di['created'] = i['created']
                di['nome'] = i['nome']
                di['idade'] = i['idade']
                di['telefone'] = i['telefone']


                
                lista.append(di)
                di = {}
            return Response(lista)

    def create(self, request):
        print(">>>",request.data)
        queryset = Usuario.objects.create(
            nome=request.data['nome'],
            idade=request.data['idade'],
            telefone=request.data['telefone'],
        )
        return Response({"status":200})

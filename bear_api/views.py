from django.shortcuts import render
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class Testing(APIView):
    def get(self, request, *args, **kwargs):
        return Response(None, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
@api_view(['GET','POST'])

def index(request):
    if request.method=="POST":
     print(request.user)
     print(request.auth)
     print(request.data)
     return Response(data=request.data,status=status.HTTP_200_OK)
    elif request.method=="GET":
        return Response(data="heheheh",status=status.HTTP_200_OK)
    else:
     return Response(data="Request method may not be right")


class Message(APIView):

    def get(self,request):
        return Response(data="great",status=status.HTTP_200_OK)
    def post(self,request):
        return Response(data="great POST" ,status=status.HTTP_200_OK)
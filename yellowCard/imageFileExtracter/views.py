from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .seriliazer import FileSerializer
import numpy
import json
import cv2 
import pytesseract
from PIL import Image
from pytesseract import pytesseract ,Output
from .models import ImageFile
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)
    def get(self,request):
      queryset=ImageFile.objects.all()
      serilizer=FileSerializer(queryset,many=True)
      return Response(data=serilizer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
      test=ImageFile()
      test.image=request.data['image']
      test.save()
      img=request.data['image']
      image = 'media/'+str(img)
      im = Image.open(image)
      test.text = pytesseract.image_to_data(im, output_type=Output.DICT)
      test.save()
      return Response(FileSerializer(test).data, status=status.HTTP_201_CREATED)
    #   file_serializer = FileSerializer(data=test)
    #   image=request.data['image']


    #   if file_serializer.is_valid():
    #       file_serializer.save()
    #       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #   else:
    #       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
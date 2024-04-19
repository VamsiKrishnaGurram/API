from django.shortcuts import render
from .models import *
from .serialization import *
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests



# Create your views here.
@api_view (['GET','POST'])
def getdetails(request):
	if request.method == 'GET' :
		pooja_objects = poojas.objects.all()
		ser_data = pooja_item_serializer(pooja_objects,many=True)
		return JsonResponse(ser_data.data,safe=False)
	elif request.method =='POST' :
		
		ser = pooja_item_serializer(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("Error While saving data !!!")




@api_view(['GET','POST'])
def getproducts(request):
	if request.method =='GET':
		product_objects = Products.objects.all()
		ser_data = product_serializer(product_objects,many=True)
		print(type(ser_data))
		return JsonResponse(ser_data.data,safe=False)
	elif request.method =='POST':
		ser = product_serializer(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("Error While Saving Data ")


@api_view(['GET','POST'])
def getcats(request):
	if request.method =='GET':
		product_objects = cxategories.objects.all()
		ser_data = cxategories_seri(product_objects,many=True)
		print(type(ser_data))
		return JsonResponse(ser_data.data,safe=False)
	elif request.method =='POST':
		ser = cxategories_seri(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("Error While Saving Data ")





def samplepath(request):
	return render(request,"sample.html")


@api_view(['GET'])
def random_image(request):

    response = requests.get('api url with secret key')

    if request.method == 'GET':
        return HttpResponse(response, content_type="image/jpeg")
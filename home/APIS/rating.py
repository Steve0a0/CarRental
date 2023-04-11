from home.models import car_rating
from rest_framework.decorators import api_view
from home.serializers import RatingSerializer
from django.http import  JsonResponse,HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics





class RatingAPI(APIView):
    def get(self, request): 
        getData = car_rating.objects.all()
        serializer = RatingSerializer(getData,many=True)     
        context={'status':'200','data':serializer.data} 
        return JsonResponse(context)
    
    
    def post(self, request):  
        getData = request.data   
        serializer = RatingSerializer(data=getData)
        if serializer.is_valid():
            serializer.save()
            status="200"
        else:
            status = f'{serializer.errors}'    
        context={'status':status}   
        return JsonResponse(context)    
  
    
    def delete(self, request):
        getData = request.data
        get_id = getData['id']
        getData = car_rating.objects.get(id=get_id)
        getData.delete()
        context={'status':'200'}   
        return JsonResponse(context)
        
      
                                  



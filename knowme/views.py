from django.http import JsonResponse
from .models import myDetails
from .serializers import DetailSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_details(request):
    if request.method == 'GET':
        drinks = myDetails.objects.all()
        serializer = DetailSerializer(drinks,many=True)
        return JsonResponse(serializer.data,safe=False)

def push_details(request):
    details=myDetails.objects.create(name='venkat',email='karnativr2611@gmail.com',phno='6302982489',college='Audisankara college of engineering and technology',skills='Javascript,Python') 
    details.save()   
    return JsonResponse({'message':'successfully inserted'})
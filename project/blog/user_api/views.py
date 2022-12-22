from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({
                'message':'token Deleted'
        })

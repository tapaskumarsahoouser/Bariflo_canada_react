from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contact_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data.get('name')
        email = data.get('email')
        phno = data.get('phno')
        companyname = data.get('companyname')
        message = data.get('message')

        if not all([name, email, phno, companyname, message]):
            return JsonResponse({"error": "All fields are required"}, status=400)
        if not isinstance(email, str) or '@' not in email:
            return JsonResponse({"error": "Invalid email address"}, status=400)

        if not isinstance(phno, str) or len(phno) < 10:
            return JsonResponse({"error": "Invalid phone number"}, status=400)

        try:
            
            contact = Contact(
                name=name,
                email=email,
                phno=phno,
                companyname=companyname,
                message=message
            )
            contact.save()
            return JsonResponse({"message": "Contact created successfully"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@api_view(['GET'])
def contact_list(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response({"contacts": serializer.data})


# @csrf_exempt
# def contact_list(request):
#     if request.method == 'GET':
#         contacts = Contact.objects.all()
#         contact_data = [
#             {
#                 'id': contact.id,
#                 'name': contact.name,
#                 'email': contact.email,
#                 'phno': contact.phno,
#                 'companyname': contact.companyname,
#                 'message': contact.message
#             }
#             for contact in contacts
#         ]
#         return JsonResponse({"contacts": contact_data}, safe=False, status=200)
    
#     return JsonResponse({"error": "Method not allowed"}, status=405)


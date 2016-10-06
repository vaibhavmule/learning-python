# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from contact.models import Contact
# from contact.serializers import ContactSerializer


# @api_view(['GET', 'POST'])
# def contact_list(request):
#     """
#     List all contact, or create a new Contact.
#     {
#         "name": "Foo Bar",
#         "number":9326782334
#     }
#     """
#     if request.method == 'GET':
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def contact_detail(request, pk):
#     """
#     Retrieve, update or delete a contact instance.
#     """
#     try:
#         contact = Contact.objects.get(pk=pk)
#     except Contact.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from contact.models import Contact
# from contact.serializers import ContactSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class ContactList(APIView):
#     """
#     List all snippets, or create a new contact.
#     """
#     def get(self, request):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ContactDetail(APIView):
#     """
#     Retrieve, update or delete a contact instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         contact = self.get_object(pk)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from contact.models import Contact
# from contact.serializers import ContactSerializer
# from rest_framework import generics


# class ContactList(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


# class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


from contact.models import Contact
from contact.serializers import ContactSerializer
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

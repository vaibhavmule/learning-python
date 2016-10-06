from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from contact.models import Contact
from contact.serializers import Contactserializer


@api_view(['GET', 'POST'])
def contact_list(request):
    """
    List all contact, or create a new Contact.
    {
        "name": "Foo Bar",
        "number":9326782334
    }
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = Contactserializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Contactserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    """
    Retrieve, update or delete a contact instance.
    """
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Contactserializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Contactserializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
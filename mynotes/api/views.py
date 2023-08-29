from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
@api_view(['GET'])
def getRoutes(request):
    print("asdf")
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    print("coming here")
    if request.method == "POST":
        data = request.data
        data["user"] = request.user.id
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)
    
    


@api_view(["PUT"])
def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteNote(request,pk):
    print("request1234",request.data)
    data = request.data
    note = Note.objects.get(id=pk)
    if request.method == "DELETE":
        note.delete()
        
    return Response({"message": "Note deleted successfully"})

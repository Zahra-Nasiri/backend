from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from base.models import Event, Registrant
from .serializers import EventSerializer, RegistrantSerializer

# Api for Event


@api_view(['GET'])
def get_routes(request):
    """
    This function has a parameter called request and returns all the api routs.
    """
    routes = [
        {'GET': 'api/events'},
        {'GET': 'api/events/id'},
        {'POST': 'api/create-events'},
        {'PUT': 'api/update-events/id'},
        {'DELETE': 'api/delete-events/id'},
        {'GET': 'api/registrants'},
        {'DELETE': 'api/delete-registrants/id'},
        # Registering for a specific event (id is for event)
        {'POST': '/api/create-registrants/id'}

    ]
    return Response(routes)


@api_view(['GET'])
def get_events(request):
    """
    get_events function has a parameter called request and
    returns the list of events.
    """
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_event(request, pk):
    """
    get_event function has two parameters, request and pk.
    pk is the id of event and returns the events which its id has been passed.
    """
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_event(request):
    """
    create event function has a parameter called request,
     which contains the data you want to create the event with,
     including user and data.
     the data requires type, title, location, description, capacity and date_time.
     Jus admin user has access to this view.
    """
    user = request.user
    data = request.data
    event = Event.objects.create(
        type=data['type'],
        title=data['title'],
        owner=user,
        location=data['location'],
        description=data['description'],
        # image = data['image'],
        capacity=data['capacity'],
        date_time=data['date_time']
    )
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_event(request, pk):
    """
    delete events takes two parameter, request and pk.
    This function delete the event you have passed its id.
    Jus admin user has access to this view.
    """
    event = Event.objects.get(id=pk)
    event.delete()
    return Response('Event Deleted Successfully')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_event(request, pk):
    """
    edit event function has two parameter, request and pk.
    Jus admin user has access to this view.
    Enables editing event data.
    """
    data = request.data
    event = Event.objects.get(id=pk)
    event.title = data['title']
    event.type = data['type']
    event.location = data['location']
    event.description = data['description']
    event.capacity = data['capacity']
    event.date_time = data['date_time']
    event.held = data['held']
    event.save()

    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


# Api for registrant
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_registrans(request):
    """
    get registrants has a parameter called request.
    It returns all the registrants.
    Jus admin user has access to this view.
    """
    registrants = Registrant.objects.all()
    serializer = RegistrantSerializer(registrants, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_registrant(request, pk):
    """
    delete registrant takes two parameter request and pk.
    pk is the id of registrant you want to delete.
    This view needs admin permission
    """
    registrant = Registrant.objects.get(id=pk)
    event = registrant.event
    event.enrolled = event.enrolled - 1
    event.save()
    registrant.delete()
    return Response('Registrant Deleted Successfully')


@api_view(['POST'])
def create_registrant(request, pk):
    """
    create registrant takes two parameter request and pk.
    pk is the id of events that user wants to enroll.
    request includes first_name, last_name, student_id, phone_number, university.
    """
    data = request.data
    event = Event.objects.get(id=pk)
    registrant = Registrant.objects.create(
        event=event,
        first_name=data['first_name'],
        last_name=data['last_name'],
        student_id=data['student_id'],
        phone_number=data['phone_number'],
        university=data['university']
    )
    event.enrolled = event.enrolled + 1
    event.save()
    serializer = RegistrantSerializer(registrant, many=False)
    return Response(serializer.data)

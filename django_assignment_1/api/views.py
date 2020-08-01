from rest_framework import status,filters
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import CountrySerializer,StateSerializer,CitySerializer,TownSerializer,PersonSerializer
from .models import Country,State,City,Town,Person
from rest_framework.pagination import PageNumberPagination
# Create your views here.
# This is for Country Entity
class CountryList(APIView):
# used for read data in the country entity
 def get(self,request):
    country=Country.objects.all()
    serializer=CountrySerializer(country,many=True)
    return Response(serializer.data)

 # used for create data in the country entity
 def post(self,request):
    country_nested_created=CountrySerializer.create(self,request.data)
    if(country_nested_created!=None):
       country_nested_created.save()
       data_serialized=CountrySerializer(instance=country_nested_created)
       return Response(data_serialized.data,status=status.HTTP_201_CREATED)
    else:
       return Response("id or name already exists",status=status.HTTP_409_CONFLICT)

class CountryDetail(APIView):
#used for update data in the country entity
  def put(self,request,pk):
    country=Country.objects.get(id=pk)
    updated_data=CountrySerializer.update(self,instance=country,validated_data=request.data)
    data_serialized=CountrySerializer(instance=updated_data)
    return Response( data_serialized.data,status=status.HTTP_201_CREATED)

 #used to delete data in the country entity
  def delete(self,request,pk):
    try:
       country = Country.objects.get(id=pk)
       country.delete()
       return Response("Item successfully Deleted",status=status.HTTP_202_ACCEPTED)
    except:
       return Response("Item Not Found",status=status.HTTP_204_NO_CONTENT)

# This is for State Entity
class StateList(APIView):
    # used for read data in the State entity
 def get(self,request):
    state=State.objects.all()
    serializer=StateSerializer(state,many=True)
    return Response(serializer.data)

 # used for create data in the State entity
 def post(self,request):
    state_nested_created=StateSerializer.create(self,request.data)
    if (state_nested_created != None):
        state_nested_created.save()
        data_serialized=StateSerializer(instance=state_nested_created)
        return Response(data_serialized.data,status=status.HTTP_201_CREATED)
    else:
         return Response("id or name already exists", status=status.HTTP_409_CONFLICT)


class StateDetail(APIView):
#used for update data in the State entity
  def put(self, request, pk):
    state = State.objects.get(id=pk)
    # serializer = StateSerializer(instance=state, data=request.data)
    updated_data=StateSerializer.update(self,instance=state,validated_data=request.data)
    if updated_data!=None:
       data_serialized=StateSerializer(instance=updated_data)
       return Response(data_serialized.data, status=status.HTTP_201_CREATED)
    else:
       return Response(status=status.HTTP_400_BAD_REQUEST)

 #used to delete data in the state entity
  def delete(self,request,pk):
    try:
       state = State.objects.get(id=pk)
       state.delete()
       return Response("Item deleted successfully",status=status.HTTP_202_ACCEPTED)
    except:
       return Response("Item not found",status=status.HTTP_204_NO_CONTENT)

# This is for City Entity
class CityList(APIView):
    # used for read data in the City entity
 def get(self,request):
    city=City.objects.all()
    serializer=CitySerializer(city,many=True)
    return Response(serializer.data)

 # used for create data in the City entity
 def post(self,request):
    serializer=CitySerializer(data=request.data)
    if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
    return Response("Duplicate id",status=status.HTTP_409_CONFLICT)

class CityDetail(APIView):
#used for update data in the City entity
  def put(self, request, pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(instance=city, data=request.data)
    if serializer.is_valid():
        if  city.id == request.data.get('id'):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("id cannot be edited")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #used to delete data in the city entity
  def delete(self,request,pk):
    try:
       city = City.objects.get(id=pk)
       city.delete()
       return Response("Item deleted successfully",status=status.HTTP_202_ACCEPTED)
    except:
       return Response("Item not found",status=status.HTTP_204_NO_CONTENT)


# This is for Town Entity
class TownList(APIView):
    # used for read data in the Town entity
 def get(self,request):
    town=Town.objects.all()
    serializer=TownSerializer(town,many=True)
    return Response(serializer.data)

 # used for create data in the Town entity
 def post(self,request):
    serializer=TownSerializer(data=request.data)
    if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
    return Response("Duplicate id",status=status.HTTP_409_CONFLICT)

class TownDetail(APIView):
#used for update data in the Town entity
  def put(self, request, pk):
    town = Town.objects.get(id=pk)
    serializer = TownSerializer(instance=town, data=request.data)
    if serializer.is_valid():
        if  town.id == request.data.get('id'):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("id cannot be edited")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #used to delete data in the town entity
  def delete(self,request,pk):
    try:
       town = Town.objects.get(id=pk)
       town.delete()
       return Response("Item deleted successfully",status=status.HTTP_202_ACCEPTED)
    except:
       return Response("Item not found",status=status.HTTP_204_NO_CONTENT)

# This is for Person Entity
class PersonList(APIView):
    # used for read data in the Person entity
 def get(self,request):
    person=Person.objects.all()
    serializer=PersonSerializer(person,many=True)
    return Response(serializer.data)

 # used for create data in the Person entity
 def post(self,request):
    serializer=PersonSerializer(data=request.data)
    if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
    return Response("Duplicate id",status=status.HTTP_409_CONFLICT)

class PersonDetail(APIView):
#used for update data in the Person entity
  def put(self, request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person,  data=request.data)
    if serializer.is_valid():
        if  person.id == request.data.get('id'):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("id cannot be edited")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #used to delete data in the person entity
  def delete(self,request,pk):
    try:
       person = Person.objects.get(id=pk)
       person.delete()
       return Response("Item deleted successfully",status=status.HTTP_202_ACCEPTED)
    except:
       return Response("Item not found",status=status.HTTP_204_NO_CONTENT)

#Paginating person class
class  PersonPagination(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    pagination_class = PageNumberPagination


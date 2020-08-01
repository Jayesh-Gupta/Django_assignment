from rest_framework import serializers
from .models import Country,State,City,Town,Person

class CitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model=City
        fields='__all__'

#Serializer Class for State Entitiy
class StateSerializer(serializers.ModelSerializer):
    cities=CitySerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model=State
        fields=['id','Country' , 'Name' , 'Description' , 'Population' , 'GDP','cities']

    def create(self, validated_data):
         cities_data=validated_data.pop('cities')
         try:
            country=Country.objects.get(id=validated_data["Country"])
            validated_data.pop('Country')
            state=State.objects.create(**validated_data,Country=country)
            for city in cities_data:
               city.pop('State')
               city.pop('Country')
               City.objects.create(**city,State=state,Country=country)
            return state
         except:
               return

    def update(self, instance, validated_data):
        cities_data = validated_data.pop('cities')
        if instance.id!=validated_data.get("id"):
           return
        instance.Description=validated_data.get("Description",instance.Description)
        instance.Population=validated_data.get("Population",instance.Population)
        instance.GDP=validated_data.get("GDP",instance.GDP)
        instance.save()
        data={}
        for city in cities_data:
            if "id" in city.keys():
                if City.objects.filter(id=city["id"]).exists():
                    c=City.objects.get(id=city["id"])
                    c.Description=city.get("Description",c.Description)
                    c.Population=city.get("Population",c.Population)
                    c.GDP=city.get("GDP",c.GDP)
                    c.Pin_Code=city.get("Pin_code",c.Pin_Code)
                    c.save()
                else:
                    data["failed"]="id not found"
            else:
                data["failed"]="Provide id for the state"

        return instance

#Serializer Class for Country Entitiy
class CountrySerializer(serializers.ModelSerializer):
    states=StateSerializer(many=True)
    list_of_states=serializers.SerializerMethodField('get_states',read_only=True)
    list_of_cities = serializers.SerializerMethodField('get_cities', read_only=True)
    class Meta:
        model=Country
        fields=['id','Name','Description','Population','GDP','states','list_of_states',"list_of_cities"]
#creating the nested data provided
    def create(self, validated_data):
          states_data=validated_data.pop('states')
          list_of_states_data =validated_data.pop('list_of_states')
          list_of_cities_data=validated_data.pop('list_of_cities')
          try:
            country=Country.objects.create(**validated_data)
            for state in states_data:
               state.pop('Country')
               cities_data=state.pop('cities')
               state_obj=State.objects.create(**state,Country=country)
               for city in cities_data:
                   city.pop("Country")
                   city.pop("State")
                   City.objects.create(**city,State=state_obj,Country=country)
            return country
          except:
               return
#updating the nested information provided
    def update(self, instance, validated_data):
        states_data = validated_data.pop('states')
        instance.Description=validated_data.get("Description",instance.Description)
        instance.Population=validated_data.get("Population",instance.Population)
        instance.GDP=validated_data.get("GDP",instance.GDP)
        instance.save()
        data={}
        for state in states_data:
            if "id" in state.keys():
                if State.objects.filter(id=state["id"]).exists():
                    cities_data=state.pop('cities')
                    state_obj=State.objects.get(id=state["id"])
                    state_obj.Country=instance
                    state_obj.Description=state.get("Description",state_obj.Description)
                    state_obj.Population=state.get("Population",state_obj.Population)
                    state_obj.GDP=state.get("GDP",state_obj.GDP)
                    state_obj.save()
                    for city in cities_data:
                        if "id" in city.keys():
                            if City.objects.filter(id=city["id"]).exists():
                                city_obj=City.objects.get(id=city["id"])
                                city_obj.Country=instance
                                city_obj.State=state_obj
                                city_obj.Description = city.get("Description", city_obj.Description)
                                city_obj.Population = city.get("Population", city_obj.Population)
                                city_obj.GDP = city.get("GDP", city_obj.GDP)
                                city_obj.Pin_Code = city.get("Pin_code", city_obj.Pin_Code)
                                city_obj.save()

                else:
                    data["failed"]="id not found"
            else:
                data["failed"]="Provide id for the state"
        return instance
#getting names of states in a Country
    def get_states(self,state_obj):
        keep_states=[]
        for state in state_obj.states:
           keep_states.append(state.Name)
        return keep_states
#getting names of cities in a Country
    def get_cities(self,state_obj):
        keep_cities=[]
        for state in state_obj.states:
            for city in state.cities:
                keep_cities.append(city.id)
        return keep_cities

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model=Town
        fields='__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','Name','City','Town']



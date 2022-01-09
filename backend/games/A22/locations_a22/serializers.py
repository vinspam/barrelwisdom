from rest_framework import serializers
from games.A22.locations_a22.models import *
from collections import OrderedDict


# Full Data
class A22LocationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.CharField(source="slugname")
    reg = serializers.CharField(source="region.slugname", allow_null=True)
    class Meta:
        model = Location
        fields = ['slug', 'name', 'reg']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.loc_en.name
        if self.context['language'] == 'ja':
            return obj.loc_ja.name
        if self.context['language'] == 'ko':
            return obj.loc_ko.name
        if self.context['language'] == 'fr':
            return obj.loc_fr.name
        if self.context['language'] == 'sc':
            return obj.loc_sc.name
        if self.context['language'] == 'tc':
            return obj.loc_tc.name
        else:
            return obj.loc_en.name
    def to_representation(self, instance):
        result = super(A22LocationSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
 
from rest_framework import serializers
from games.A16.effects_a16.models import Effect
from games.A16.items_a16.models import EffectLines, EffectData

class A16EffectLineSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.CharField(source='item.slug')
    class Meta:
        model = EffectLines
        fields = ['name', 'slug']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.item.item_en.name
        elif self.context['language'] == 'ja':
            return obj.item.item_ja.name
        else:
            return obj.item.item_en.name


class A16EffectDataSerializer(serializers.ModelSerializer):
    effectlines_set = A16EffectLineSerializer(many=True)
    class Meta:
        model = EffectData
        fields = ['effectlines_set']

class A16EffectSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    effectdata_set = A16EffectDataSerializer(many=True)
    class Meta:
        model = Effect
        fields = ['slug', 'name', 'desc', "effectdata_set"]

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.eff_en.name
        elif self.context['language'] == 'ja':
            return obj.eff_ja.name
        else:
            return obj.eff_en.name
    def get_desc(self,obj):
        if 'language' not in self.context:
            return obj.eff_en.desc
        elif self.context['language'] == 'ja':
            return obj.eff_ja.desc
        else:
            return obj.eff_en.desc

class A16EffectSerializerSimple(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Effect
        fields = ['slug', 'name']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.eff_en.name
        elif self.context['language'] == 'ja':
            return obj.eff_ja.name
        else:
            return obj.eff_en.name
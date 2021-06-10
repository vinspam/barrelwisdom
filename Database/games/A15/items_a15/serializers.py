from rest_framework import serializers
from collections import OrderedDict
from games.A15.items_a15.models import *
from games.A15.regions_a15.serializers import A15RegionNameSerializer, A15FieldEventSerializer
from games.A15.monsters_a15.serializers import A15MonsterNameSerializer
from games.A15.properties_a15.serializers import A15PropertyNameSerializer
from games.A15.categories_a15.serializers import A15CategorySerializerName, A15CategorySerializer, A15CategorySerializerLink
from games.A15.effects_a15.serializers import A15EffectSerializer

class A15ItemNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['slugname', 'name']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.item_en.name
        if self.context['language'] == 'ja':
            return obj.item_ja.name
        else:
            return obj.item_en.name

# for easy filtering by ingredient
class A15IngredientSimpleSerializer(serializers.ModelSerializer):
    ing = serializers.SerializerMethodField()
    class Meta:
        model = Ingredient
        fields = ['ing']

    def to_representation(self, instance):
        result = super(A15IngredientSimpleSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])
    def get_ing(self,obj):
        if obj.category is None:
            if self.context['language'] == 'ja':
                return obj.item.item_ja.name
            else:
              return obj.item.item_en.name
        else:
            if self.context['language'] == 'ja':
                return obj.category.cat_ja.name
            else:
                return obj.category.cat_en.name

class A15IngredientSerializer(serializers.ModelSerializer):
    item = A15ItemNameSerializer()
    category = A15CategorySerializerLink()
    class Meta:
        model = Ingredient
        fields = ['item', 'category', 'num']

    def to_representation(self, instance):
        result = super(A15IngredientSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])

class A15CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']

class A15CharacterEquipSerializer(serializers.ModelSerializer):
    chars = A15CharacterSerializer(many=True)
    class Meta:
        model = CharacterEquip
        fields = ['chars']

class A15EquipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equip
        fields = ['hp', 'mp', 'atk', 'defen', 'spd', 'fire', 'water', 'wind', 'earth']

class A15DissasembleSerializer(serializers.ModelSerializer):
    dis = A15ItemNameSerializer(many=True, read_only=True)
    class Meta:
        model = Disassembly
        fields = ['dis']

class A15DissasembledSerializer(serializers.ModelSerializer):
    parent = A15ItemNameSerializer(many=True, read_only=True)
    class Meta:
        model = Disassembled
        fields = ['parent']

class A15RelicSerializer(serializers.ModelSerializer):
    item = A15ItemNameSerializer()
    region = A15RegionNameSerializer()
    area = A15RegionNameSerializer(many=True)
    class Meta:
        model = Relic
        fields = ['region', 'area', 'item']

class A15RelicAreaSerializer(serializers.ModelSerializer):
    region = A15RegionNameSerializer()
    class Meta:
        model = Relic
        fields = ['region']

class A15EffectLineSerializer(serializers.ModelSerializer):
    effect = A15EffectSerializer()
    class Meta:
        model = EffectLine
        fields = ['effect', 'elem', 'number', 'min_elem', 'max_elem']

class A15AreaDataSerializer(serializers.ModelSerializer):
    monsters = A15MonsterNameSerializer(many=True)
    items = A15ItemNameSerializer(many=True)
    rare = A15ItemNameSerializer(many=True)
    maxitem = A15ItemNameSerializer(many=True)
    fieldevent = A15FieldEventSerializer(many=True)
    class Meta:
        model = AreaData
        fields = ['subarea', 'monsters', 'items', 'rare', 'maxitem', 'fieldevent']
    def to_representation(self, instance):
        result = super(A15AreaDataSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])

class A15ItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    categories = A15CategorySerializerName(many=True)
    ingredient_set = A15IngredientSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['slugname', 'name', 'level', 'evalue', 'fire', 'water', 'wind', 'earth', 'effect', 'itype', 'isDLC', 'isDX', 'categories', 'ingredient_set']

    def to_representation(self, instance):
        result = super(A15ItemSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.item_en.name
        if self.context['language'] == 'ja':
            return obj.item_ja.name
        else:
            return obj.item_en.name

class A15ItemFullSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    locations = A15RegionNameSerializer(many=True)
    monsters = A15MonsterNameSerializer(many=True)
    properties = A15PropertyNameSerializer(many=True)
    categories = A15CategorySerializer(many=True)
    ingredient_set = A15IngredientSerializer(many=True)
    characterequip_set = A15CharacterEquipSerializer(read_only=True, many=True)
    equip_set = A15EquipSerializer(many=True)
    disassembly_set = A15DissasembleSerializer(many=True)
    disassembled_set = A15DissasembledSerializer(many=True)
    relic_set = A15RelicAreaSerializer(many=True)
    effectline_set = A15EffectLineSerializer(many=True)
    class Meta:
        model = Item
        fields = ['slugname', 'name', 'desc', 'level', 'evalue', 'fire', 'water', 'wind', 'earth', 'effect', 'size', 'itype', 'isDLC', 'isDX', 'locations', 'monsters', 'properties', 'categories', 'ingredient_set', 'characterequip_set', 'equip_set', 'disassembly_set', 'disassembled_set', 'relic_set', 'effectline_set']

    def to_representation(self, instance):
        result = super(A15ItemFullSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.item_en.name
        if self.context['language'] == 'ja':
            return obj.item_ja.name
        else:
            return obj.item_en.name
    def get_desc(self,obj):
        if 'language' not in self.context:
            return obj.item_en.desc
        if self.context['language'] == 'ja':
            return obj.item_ja.desc
        else:
            return obj.item_en.desc
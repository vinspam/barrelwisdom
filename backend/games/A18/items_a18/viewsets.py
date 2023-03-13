from rest_framework import viewsets, filters
from games.A18.items_a18.models import Item, Category, Catalyst, RecipeIdea
from games.A18.items_a18.serializers import A18CategoryItemSerializer, A18CategorySerializer, A18CatalystSerializer, A18RecipeItemSerializer, A18ItemListSerializer, A18ItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class A18CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = A18CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'slug'

    @action(detail=False) 
    def en(self, request):
        queryset = (
            Category.objects.all()
        )
        serializer = A18CategorySerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="en")
    def en_full(self, request, slug):
        try:
            queryset = (
                Category.objects
                .prefetch_related(
                    'item_set__text',
                    'add_categories__text',
                    'ingredient_set__synth__text',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18CategoryItemSerializer(queryset, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False) 
    def ja(self, request):
        queryset = (
            Category.objects.all()
        )
        serializer = A18CategorySerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ja")
    def ja_full(self, request, slug):
        try:
            queryset = (
                Category.objects
                .prefetch_related(
                    'item_set__text',
                    'add_categories__text',
                    'ingredient_set__synth__text',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18CategoryItemSerializer(queryset, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=False) 
    def sc(self, request):
        queryset = (
            Category.objects.all()
        )
        serializer = A18CategorySerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="sc")
    def sc_full(self, request, slug):
        try:
            queryset = (
                Category.objects
                .prefetch_related(
                    'item_set__text',
                    'add_categories__text',
                    'ingredient_set__synth__text',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18CategoryItemSerializer(queryset, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=False) 
    def tc(self, request):
        queryset = (
            Category.objects.all()
        )
        serializer = A18CategorySerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="tc")
    def tc_full(self, request, slug):
        try:
            queryset = (
                Category.objects
                .prefetch_related(
                    'item_set__text',
                    'add_categories__text',
                    'ingredient_set__synth__text',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18CategoryItemSerializer(queryset, context={'language': 'tc'})
        return Response(serializer.data)

class A18CatalystViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = A18CatalystSerializer

    @action(detail=False) 
    def en(self, request):
        queryset = (
            Catalyst.objects
            .select_related(
                'action1',
                'action2',
                'action3',
                'action4',
                'action5',
                'action6',
                'item__text',
            )
            .prefetch_related(
                'item__categories'
            )
        )
        serializer = A18CatalystSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False) 
    def ja(self, request):
        queryset = (
            Catalyst.objects
            .select_related(
                'action1',
                'action2',
                'action3',
                'action4',
                'action5',
                'action6',
                'item__text',
            )
            .prefetch_related(
                'item__categories'
            )
        )
        serializer = A18CatalystSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)
    
    @action(detail=False) 
    def sc(self, request):
        queryset = (
            Catalyst.objects
            .select_related(
                'action1',
                'action2',
                'action3',
                'action4',
                'action5',
                'action6',
                'item__text',
            )
            .prefetch_related(
                'item__categories'
            )
        )
        serializer = A18CatalystSerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)
    
    @action(detail=False) 
    def tc(self, request):
        queryset = (
            Catalyst.objects
            .select_related(
                'action1',
                'action2',
                'action3',
                'action4',
                'action5',
                'action6',
                'item__text',
            )
            .prefetch_related(
                'item__categories'
            )
        )
        serializer = A18CatalystSerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)

class A18ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = A18ItemListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'slug'

    @action(detail=False) 
    def en(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'categories',
                'ingredients__cat',
                'ingredients__item__text',
            )
        )
        serializer = A18ItemListSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="en")
    def en_full(self, request, slug):
        try:
            queryset = (
                Item.objects
                .select_related(
                    'text',
                    'char1',
                    'char2',
                    'char3',
                    'char4',
                    'book__text',
                    'traits',
                )
                .prefetch_related(
                    'chars',
                    'locations',
                    'categories',
                    'catalysts',
                    'fixed_components',
                    'random_components',
                    'ingredients__cat',
                    'ingredients__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                    'effectlines_set__effectdata_set__effect',
                    'effectlines_set__effectdata_set__component',
                    'masteryline_set__masteries',
                    'recipes__text',
                    'monsters__text',
                    'catalyst',
                    'equip',
                    'shopslot_set__shop',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18ItemSerializer(queryset, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False) 
    def ja(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'categories',
                'ingredients__cat',
                'ingredients__item__text',
            )
        )
        serializer = A18ItemListSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ja")
    def ja_full(self, request, slug):
        try:
            queryset = (
                Item.objects
                .select_related(
                    'text',
                    'char1',
                    'char2',
                    'char3',
                    'char4',
                    'book__text',
                    'traits',
                )
                .prefetch_related(
                    'chars',
                    'locations',
                    'categories',
                    'catalysts',
                    'fixed_components',
                    'random_components',
                    'ingredients__cat',
                    'ingredients__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                    'effectlines_set__effectdata_set__effect',
                    'effectlines_set__effectdata_set__component',
                    'masteryline_set__masteries',
                    'recipes__text',
                    'monsters__text',
                    'catalyst',
                    'equip',
                    'shopslot_set__shop',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18ItemSerializer(queryset, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=False) 
    def sc(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'categories',
                'ingredients__cat',
                'ingredients__item__text',
            )
        )
        serializer = A18ItemListSerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="sc")
    def sc_full(self, request, slug):
        try:
            queryset = (
                Item.objects
                .select_related(
                    'text',
                    'char1',
                    'char2',
                    'char3',
                    'char4',
                    'book__text',
                    'traits',
                )
                .prefetch_related(
                    'chars',
                    'locations',
                    'categories',
                    'catalysts',
                    'fixed_components',
                    'random_components',
                    'ingredients__cat',
                    'ingredients__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                    'effectlines_set__effectdata_set__effect',
                    'effectlines_set__effectdata_set__component',
                    'masteryline_set__masteries',
                    'recipes__text',
                    'monsters__text',
                    'catalyst',
                    'equip',
                    'shopslot_set__shop',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18ItemSerializer(queryset, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=False) 
    def tc(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'categories',
                'ingredients__cat',
                'ingredients__item__text',
            )
        )
        serializer = A18ItemListSerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="tc")
    def tc_full(self, request, slug):
        try:
            queryset = (
                Item.objects
                .select_related(
                    'text',
                    'char1',
                    'char2',
                    'char3',
                    'char4',
                    'book__text',
                    'traits',
                )
                .prefetch_related(
                    'chars',
                    'locations',
                    'categories',
                    'catalysts',
                    'fixed_components',
                    'random_components',
                    'ingredients__cat',
                    'ingredients__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
                    'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                    'effectlines_set__effectdata_set__effect',
                    'effectlines_set__effectdata_set__component',
                    'masteryline_set__masteries',
                    'recipes__text',
                    'monsters__text',
                    'catalyst',
                    'equip',
                    'shopslot_set__shop',
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A18ItemSerializer(queryset, context={'language': 'tc'})
        return Response(serializer.data)


class A18RecipeIdeaViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = A18RecipeItemSerializer

    @action(detail=False) 
    def en(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
            )
            .filter(recipeidea__isnull=False)
            .distinct()
        )
        serializer = A18RecipeItemSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False) 
    def ja(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
            )
            .filter(recipeidea__isnull=False)
            .distinct()
        )
        serializer = A18RecipeItemSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=False) 
    def sc(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
            )
            .filter(recipeidea__isnull=False)
            .distinct()
        )
        serializer = A18RecipeItemSerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=False) 
    def tc(self, request):
        queryset = (
            Item.objects
            .select_related(
                'text',
            )
            .prefetch_related(
                'recipeidea_set__recipeunlock_set__recipecondition_set__category',
                'recipeidea_set__recipeunlock_set__recipecondition_set__race',
                'recipeidea_set__recipeunlock_set__recipecondition_set__monster__text',
                'recipeidea_set__recipeunlock_set__recipecondition_set__item__text',
            )
            .filter(recipeidea__isnull=False)
            .distinct()
        )
        serializer = A18RecipeItemSerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)

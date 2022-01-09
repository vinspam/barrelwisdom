from rest_framework import viewsets, filters
from games.A22.monsters_a22.models import Monster
from games.A22.monsters_a22.serializers import A22MonsterSerializer, A22MonsterSerializerFull
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class A22MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = A22MonsterSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'slugname'

    # full effect list
    @action(detail=False)
    def en(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_en'
            )
            .prefetch_related(
                'drops',
                'drops__item_en',
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False)
    def ja(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_ja'
            )
            .prefetch_related(
                'drops',
                'drops__item_ja'
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=False)
    def ko(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_ko'
            )
            .prefetch_related(
                'drops',
                'drops__item_ko'
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'ko'})
        return Response(serializer.data)

    @action(detail=False)
    def fr(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_fr'
            )
            .prefetch_related(
                'drops',
                'drops__item_fr'
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'fr'})
        return Response(serializer.data)

    @action(detail=False)
    def sc(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_sc'
            )
            .prefetch_related(
                'drops',
                'drops__item_sc'
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=False)
    def tc(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_tc'
            )
            .prefetch_related(
                'drops',
                'drops__item_tc'
            )

        )
        serializer = A22MonsterSerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)

    # single monster view
    @action(detail=True, methods=['get'], url_path="en")
    def en_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_en'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_en',
                    'location',
                    'location__loc_en',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ja")
    def ja_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_ja'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_ja',
                    'location',
                    'location__loc_ja',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ko")
    def ko_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_ko'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_ko',
                    'location',
                    'location__loc_ko',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'ko'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="fr")
    def fr_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_fr'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_fr',
                    'location',
                    'location__loc_fr',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'fr'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="sc")
    def sc_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_sc'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_sc',
                    'location',
                    'location__loc_sc',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="tc")
    def tc_full(self, request, slugname):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_tc'
                )
                .prefetch_related(
                    'drops',
                    'drops__item_tc',
                    'location',
                    'location__loc_tc',
                )
                .get(slugname=slugname)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A22MonsterSerializerFull(queryset, context={'language': 'tc'})
        return Response(serializer.data)
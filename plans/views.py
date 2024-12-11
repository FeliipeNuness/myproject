from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from .models import Signature, Plan
from .serializers import SignatureSerializer, PlanSerializer
from rest_framework import generics, views, response, status

class SubscribeView(APIView):
    # Método POST para inscrever o usuário no plano
    def post(self, request, plan_id):
        # Verifique se o plano existe, se não, crie-o
        plan, created = Plan.objects.get_or_create(
            id=1,  # ID fixo ou alguma lógica para identificá-lo
            defaults={
                'name': 'Plano R$100',
                'description': 'Acesso total ao sistema SGE',
                'price': 100.00,
                'periodicity': 'mensal',
                'resource': {"acesso": "completo", "suporte": "básico"}
            }
        )

        # Obtém o plano específico
        plan = get_object_or_404(Plan, id=plan_id)

        try:
            # Verifica se o usuário já possui uma assinatura ativa
            signature = Signature.objects.get(user=request.user)
            if signature.status == 'ativa':
                return Response({'detail': 'Você já possui uma assinatura ativa.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Reativar assinatura existente
                signature.status = 'ativa'
                signature.start_date = now().date()
                signature.end_date = now().date() + timedelta(days=30)
                signature.plan = plan
                signature.save()
                serializer = SignatureSerializer(signature)
                return Response({'plan': plan.name, 'signature': serializer.data}, status=status.HTTP_200_OK)
        except Signature.DoesNotExist:
            # Cria uma nova assinatura
            signature = Signature.objects.create(user=request.user, plan=plan, status='ativa')
            serializer = SignatureSerializer(signature)
            return Response({'plan': plan.name, 'signature': serializer.data}, status=status.HTTP_201_CREATED)


class PlanCreateListView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
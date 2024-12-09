from django.views.generic import ListView
from plans.models import Plan

# LISTAR TODOS OS PLANOS
class ListPlansViews(ListView):
    model = Plan
    template_name = 'listar_planos.html'  
    context_object_name = 'planos'
    


# LISTAR PLANOS MENSAIS
class MonthlyPlans(ListView):
    model = Plan
    template_name = 'plans/plan.html'  
    context_object_name = 'planos'
    
    def get_queryset(self):
        return Plan.objects.filter(periodicity='mensal')


# LISTAR PLANOS ANUAIS
class AnnualPlans(ListView):
    model = Plan
    template_name = 'plans/plan.html'  
    context_object_name = 'planos'
    
    def get_queryset(self):
        return Plan.objects.filter(periodicity='anual')

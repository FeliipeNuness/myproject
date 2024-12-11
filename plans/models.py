from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now
from django.conf import settings


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    periodicity = models.CharField(
        max_length=10,
        choices=[('mensal', 'Mensal'), ('anual', 'Anual')]
    )

    
    def __str__(self):
        return self.name
    
    
class Signature(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('ativa', 'Ativa'), ('pendente', 'Pendente'), ('expirada', 'Expirada')],
        default='pendente'
    )
    
    def __str__(self):
        return f" {self.user.username} - {self.plan.name}"
    
    
    # FUNÇÃO QUE CALCULA DATA DE TERMINO AUTOMATICAMENTE, PLANO MENSAL
    def save(self, *args, **kwargs):
        
        if not self.end_date:
            self.end_date = now().date() + timedelta(days=30) # ASSINATURA MENSAL
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Assinatura de {self.user.username} - {self.status}"
    
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    periodicity = models.CharField(
        max_length=10,
        choices=[('mensal', 'Mensal'), ('anual', 'Anual')]
    )
    resource = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name
    
    
class Signature(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[('ativa', 'Ativa'), ('pendente', 'Pendente'), ('expirada', 'Expirada')]
    )
    
    def __str__(self):
        return f" {self.user.username} - {self.plan.name}"
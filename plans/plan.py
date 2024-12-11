from plans.models import Plan

plan = Plan.objects.create(
    name = "Plano R$100",
    description = "Acesso total ao sistema SGE",
    price = 100.00,
    periodicity = "mensal",
    resource = {"acesso": "completo", "suporte": "básico"}
)
print(f"Plano criado: {plan}")
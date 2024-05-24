from djongo import models
from django.utils import timezone

class Domicilio(models.Model):
    _id = models.ObjectIdField()
    domicilio_calle = models.CharField(max_length=255, null=False, default="")
    domicilio_altura = models.CharField(max_length=255, null=False, default="")
    domicilio_apto_lote = models.CharField(max_length=255, null=False, default="")
    domicilio_provincia = models.CharField(max_length=255, null=False, default="")

class Apto(models.Model):
    _id = models.ObjectIdField()
    url = models.CharField(max_length=255, null=False, default="")  # url del aws s3
    status = models.CharField(max_length=255, null=False, default="")
    fecha_vigencia = models.DateTimeField(null=False, default=timezone.now)

class Plan(models.Model):
    PLAN_CHOICES = [
        ("BASICO", "Básico"),
        ("PREMIUM", "Premium"),
        ("DELUXE", "Deluxe")
    ]
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=255, null=False)
    nivel_acceso = models.CharField(max_length=50, null=False, default="", choices=PLAN_CHOICES)
    price = models.IntegerField(null=False)  # mensualidad del socio
    sede = models.CharField(max_length=250, null=False)  # merchant ID || slug
    

class Socio(models.Model):
    GENERO_CHOICES = [
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("Otro", "Otro")
    ]

    DNI_CHOICES = [
        ("dni", "DNI"),
        ("pasaporte", "Pasaporte")
    ]

    STATUS_CHOICES = [
        ("activo", "Activo"),
        ("inactivo", "Inactivo"),
        ("suspendido", "Suspendido")
    ]

    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    celular = models.CharField(max_length=255, null=False, default="")
    genero = models.CharField(max_length=255, null=False, default="", choices=GENERO_CHOICES)
    documento_tipo = models.CharField(max_length=50, null=False, default="", choices=DNI_CHOICES)
    documento = models.CharField(max_length=255, null=False, default="")
    email = models.EmailField(max_length=255, null=False, default="")
    fecha_nacimiento = models.CharField(max_length=255, null=False, default="")
    domicilio = models.EmbeddedField(model_container=Domicilio)  # Cambiado a EmbeddedModelField
    last_subscription_date = models.DateTimeField(null=False, default=timezone.now)
    fecha_vigencia_plan = models.DateTimeField(null=False, default=timezone.now)  # vencimiento del plan
    status = models.CharField(max_length=255, null=False, default="", choices=STATUS_CHOICES)
    archived = models.BooleanField(null=False, default=False)
    createdAt = models.DateTimeField(null=False, auto_now_add=True)
    updatedAt = models.DateTimeField(null=False, auto_now=True)
    apto_medico = models.EmbeddedField(model_container=Apto)
    plan = models.EmbeddedField(model_container=Plan)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        db_table = 'clientes'

from djongo import models

class Instance(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    time = models.DateTimeField()
    manual_access_reason = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True)
    access_granted = models.BooleanField(default=False)
    invalid_access_reason = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100)
    

class Socio(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    costo = models.CharField(max_length=128)
    sede_id = models.CharField(max_length=100)
    socio_apellido = models.CharField(max_length=100)
    socio_documento = models.CharField(max_length=100)
    socio_nombre = models.CharField(max_length=100)
    sede_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    instances = models.ArrayField(model_container=Instance)
    entered = models.BooleanField(default=False)
    categoria_socio = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    sede_socio = models.CharField(max_length=100)
    merchant_id = models.CharField(max_length=100)
    
    class Meta: 
        db_table = "accesos"


    

from django.db import models

class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    sxo_mnemonico = models.TextField()

    class Meta:
        managed = True
        db_table = 'sexo'

    def __str__(self):
        return self.sxo_nombre

class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        managed = True
        db_table = 'estado_civil'

    def __str__(self):
        return self.e_ecv_nombre

class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        managed = True
        db_table = 'nacionalidad'

    def __str__(self):
        return self.ncn_nombre

class Persona(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    rut = models.CharField(max_length=11, unique=True,blank=False, null=False)
    nombre = models.TextField(blank=False, null=False)
    apellido_paterno = models.TextField(blank=False, null=False)
    apellido_materno = models.TextField(blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    email_personal = models.TextField(blank=True, null=True)
    email_institucional = models.TextField(blank=False, null=False)
    prs_celular = models.BigIntegerField(blank=True, null=True)
    prs_telefono = models.BigIntegerField(blank=True, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, models.CASCADE, blank=True, null=True)
    sexo = models.ForeignKey(Sexo, models.CASCADE, blank=True, null=True)
    estado_civil = models.ForeignKey(EstadoCivil, models.CASCADE, blank=True, null=True)
    ind_pasaporte = models.BooleanField(default=False)
    pasaporte = models.TextField(blank=True, null=True,default=None)
    prs_fecha_defuncion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'persona'



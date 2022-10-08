from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

def getUUID():
    import uuid
    return uuid.uuid5(uuid.NAMESPACE_DNS, timezone.now().strftime("%Y-%m-%d"))

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
    id = models.UUIDField(primary_key=True, editable=False,default=getUUID(), unique=True)
    rut = models.CharField(max_length=12, unique=True,blank=False, null=False)
    primer_nombre = models.TextField(blank=False, null=False)
    segundo_nombre = models.TextField(blank=False, null=False)
    apellido_paterno = models.TextField(blank=False, null=False)
    apellido_materno = models.TextField(blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    email_personal = models.TextField(blank=True, null=True)
    email_institucional = models.TextField(blank=False, null=False)
    celular = models.BigIntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, models.CASCADE, blank=True, null=True)
    sexo = models.ForeignKey(Sexo, models.CASCADE, blank=True, null=True)
    estado_civil = models.ForeignKey(EstadoCivil, models.CASCADE, blank=True, null=True)
    ind_pasaporte = models.BooleanField(default=False)
    pasaporte = models.TextField(blank=True, null=True,default=None)
    prs_fecha_defuncion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'persona'

    def save(self, *args, **kwargs):
        self.rut = self.rut.replace('.','').strip()
        self.primer_nombre = self.primer_nombre.strip().upper()
        self.segundo_nombre = self.segundo_nombre.strip().upper()
        self.apellido_paterno = self.apellido_paterno.strip().upper()
        self.apellido_materno = self.apellido_materno.strip().upper()
        super(Persona, self).save(*args, **kwargs)
        if self.email_institucional:
            Usuario(
                username=self.email_institucional,
                persona=self,
            ).save()

class Usuario(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, editable=False,default=getUUID(), unique=True)
    username = models.EmailField(max_length = 254)
    password = models.TextField(default=f'''yo{timezone.now().year}''',blank=False, null=False)
    persona = models.OneToOneField(Persona, models.CASCADE, blank=True, null=True)
    ind_cambio_password = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'usuario'

class Modulo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    modulo_padre = models.ForeignKey('self',on_delete=models.CASCADE, related_name='fk_modulo_padre',blank=True, null=True)
    nivel = models.IntegerField(default=1,blank=False, null=False)
    icono = models.TextField()
    orden = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'modulo'
    
    def __str__(self):
        return self.nombre

class TipoRuta(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'tipo_ruta'

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    id = models.BigAutoField(primary_key=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    tipo_ruta = models.ForeignKey(TipoRuta, on_delete=models.CASCADE)
    url = models.TextField(blank=False, null=False)
    
    class Meta:
        managed = True
        db_table = 'ruta'

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    prioridad = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'rol'

    def __str__(self):
        return self.nombre

class ModuloRol(models.Model):
    id = models.BigAutoField(primary_key=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    ind_get = models.BooleanField(default=False)
    ind_post = models.BooleanField(default=False)
    ind_put = models.BooleanField(default=False)
    ind_delete = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'modulo_rol'

class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    rut = models.CharField(max_length=11, unique=True,blank=False, null=False)
    nombre = models.TextField(blank=False, null=False, editable=False)
    telefono = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'empresa'

    def __str__(self):
        return self.nombre

class EmpresaRol(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
   
    class Meta:
        managed = True
        db_table = 'empresa_rol'

class EmpresaRolPersona(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa_rol = models.ForeignKey(EmpresaRol, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    

    class Meta:
        managed = True
        db_table = 'empresa_rol_persona'

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    mnemonico = models.CharField(max_length=10, blank=False, null=False)
    folio_correlativo = models.IntegerField(blank=False, null=False)
    ruta = models.TextField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'tipo_documento'

class EstadoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'estado_documento'

class Documento(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    version = models.IntegerField(blank=False, null=False)
    folio = models.TextField(blank=False, null=False)
    nombre = models.TextField(blank=False, null=False)
    metadatos=models.JSONField()
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    estado_documento = models.ForeignKey(EstadoDocumento, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'documento'

    def __str__(self):
        return f'''{self.folio}-{self.nombre}-(v{self.version})'''



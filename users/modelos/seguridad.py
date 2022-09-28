from email.policy import default
from django.db import models
from users.modelos.personas import Persona

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    usuario = models.TextField(blank=False, null=False)
    contrasena = models.TextField(blank=False, null=False)
    persona = models.ForeignKey('Persona', models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuario'

class TipoModulo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        managed = True
        db_table = 'tipo_modulo'

    def __str__(self):
        return self.nombre


class Modulo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    modulo_padre = models.ForeignKey('self',on_delete=models.CASCADE, related_name='fk_modulo_padre',blank=True, null=True)
    nivel = models.IntegerField(default=1,blank=False, null=False)
    icono = models.TextField()
    orden = models.IntegerField()
    visible = models.BooleanField(default=True)
    tipo_modulo = models.ForeignKey(TipoModulo, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'modulo'

    
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'rol'


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

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=False, null=False, editable=False)

    class Meta:
        managed = True
        db_table = 'perfil'

    def __str__(self):
        return self.prf_nombre


class PerfilRol(models.Model):
    id = models.AutoField(primary_key=True)
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
   
    class Meta:
        managed = True
        db_table = 'perfil_rol'

class PersonaPerfilRol(models.Model):
    id = models.BigAutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perfil_rol = models.ForeignKey(PerfilRol, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'persona_perfil_rol'
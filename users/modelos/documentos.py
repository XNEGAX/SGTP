from django.db import models
from django.contrib.postgres.fields import JSONField

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
        managed = False
        db_table = 'estado_documento'

class Documento(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    version = models.IntegerField(blank=False, null=False)
    folio = models.TextField(blank=False, null=False)
    nombre = models.TextField(blank=False, null=False)
    metadatos=JSONField()
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    estado_documento = models.ForeignKey(EstadoDocumento, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'documento'

    def __str__(self):
        return f'''{self.folio}-{self.nombre}-(v{self.version})'''



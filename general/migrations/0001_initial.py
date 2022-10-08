# Generated by Django 4.1.1 on 2022-10-06 13:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=11, unique=True)),
                ('nombre', models.TextField(editable=False)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empresa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmpresaRol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.empresa')),
            ],
            options={
                'db_table': 'empresa_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'estado_civil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_documento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('nivel', models.IntegerField(default=1)),
                ('icono', models.TextField()),
                ('orden', models.IntegerField()),
                ('modulo_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_modulo_padre', to='general.modulo')),
            ],
            options={
                'db_table': 'modulo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'nacionalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('03660d38-9640-5160-bf1d-ef9bf4b7f2b4'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('primer_nombre', models.TextField()),
                ('segundo_nombre', models.TextField()),
                ('apellido_paterno', models.TextField()),
                ('apellido_materno', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('email_personal', models.TextField(blank=True, null=True)),
                ('email_institucional', models.TextField()),
                ('celular', models.BigIntegerField(blank=True, null=True)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
                ('ind_pasaporte', models.BooleanField(default=False)),
                ('pasaporte', models.TextField(blank=True, default=None, null=True)),
                ('prs_fecha_defuncion', models.DateTimeField(blank=True, null=True)),
                ('estado_civil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.estadocivil')),
                ('nacionalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.nacionalidad')),
            ],
            options={
                'db_table': 'persona',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('prioridad', models.IntegerField()),
            ],
            options={
                'db_table': 'rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('sxo_mnemonico', models.TextField()),
            ],
            options={
                'db_table': 'sexo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('mnemonico', models.CharField(max_length=10)),
                ('folio_correlativo', models.IntegerField()),
                ('ruta', models.TextField()),
            ],
            options={
                'db_table': 'tipo_documento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoRuta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'tipo_ruta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.UUID('03660d38-9640-5160-bf1d-ef9bf4b7f2b4'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.TextField(default='yo2022')),
                ('ind_cambio_password', models.BooleanField(default=True)),
                ('persona', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.persona')),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.modulo')),
                ('tipo_ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.tiporuta')),
            ],
            options={
                'db_table': 'ruta',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.sexo'),
        ),
        migrations.CreateModel(
            name='ModuloRol',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ind_get', models.BooleanField(default=False)),
                ('ind_post', models.BooleanField(default=False)),
                ('ind_put', models.BooleanField(default=False)),
                ('ind_delete', models.BooleanField(default=False)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.modulo')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.rol')),
            ],
            options={
                'db_table': 'modulo_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmpresaRolPersona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('empresa_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.empresarol')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.persona')),
            ],
            options={
                'db_table': 'empresa_rol_persona',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='empresarol',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.rol'),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('version', models.IntegerField()),
                ('folio', models.TextField()),
                ('nombre', models.TextField()),
                ('metadatos', models.JSONField()),
                ('estado_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.estadodocumento')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.tipodocumento')),
            ],
            options={
                'db_table': 'documento',
                'managed': True,
            },
        ),
    ]
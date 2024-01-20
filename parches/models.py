# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.contrib.auth.models import User


from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models
from django.utils import timezone


import uuid

class Actividad(models.Model):
    Futbol = "FUTBOL"
    Baloncesto = "Baloncesto"
    juegoMesa = "Juego de mesa"
    Voleibol = "Voleibol"
    pasarElRato = "Pasar el rato"
    natacion = "natacion"
    patinaje = 'patinaje'
    tenis= 'tenis'
    cilcismo = 'ciclismo' 
   
    deporte = [
        (Futbol, 'Futbol'),
        (Baloncesto, 'Baloncesto'),
        (juegoMesa, 'Juegos De Mesa'),
        (Voleibol,'Voleibol'),
        (pasarElRato,'Pasar el rato'),
        (natacion, 'Natacion'),
        (patinaje, 'Patinaje'),
        (tenis, 'Tenis'),
        (cilcismo,'Cilcismo')
    ]
 
    idactividad = models.AutoField(db_column='idActividad', primary_key=True)
    nombreactividad = models.CharField(db_column='nombreActividad', max_length=30)
    tipoactividad = models.CharField(db_column='tipoActividad', choices=deporte,max_length=15)
    lugar = models.CharField(max_length=40, null=True, blank=True)
    # ubicacion = models.CharField(max_length=80)
    fechainicio = models.CharField(db_column='fechaInicio', max_length=40)
    fechafin = models.CharField(db_column='fechaFin', max_length=40)
    descripcion = models.TextField(db_column="descripcion", max_length=75, blank=True, null=True)
    hora = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='actividad/', max_length=80)
    contacto = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    puntosdeportivos = models.ForeignKey('Puntosdeportivos', models.DO_NOTHING, null=True, blank=True)
    empresa_idempresa = models.ForeignKey('EmpresaPersona', on_delete=models.CASCADE, db_column='empresa_idEmpresa', null=True)

    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'actividad'
        unique_together = (('idactividad', 'puntosdeportivos', 'empresa_idempresa'),)

    
    def delete(self, using= None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



class Documento(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    documentocol = models.FileField(db_column='Documentocol', upload_to='documentos/', max_length=100)  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey('EmpresaPersona', db_column='empresa_idEmpresa', on_delete=models.CASCADE) # Field name made lowercase.

    class Meta:
        db_table = 'documento'
    
    def delete(self, using: None , keep_parents= False):
        self.documentocol.storage.delete(self.documentocol.name)
        super().delete()
    




class EmpresaPersonaManager(BaseUserManager):
    def create_user(self, usuario, correo, telefono, password):
        usuario = self.model(usuario=usuario, correo=correo, telefono=telefono)
        usuario.usuario_activo = True
        usuario.set_password(password)  
        usuario.save()
        return usuario

    def create_superuser(self, usuario, password):
        usuario = self.create_user(usuario=usuario, correo="", telefono=0, password=password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class EmpresaPersona(AbstractBaseUser, PermissionsMixin):
    TipoUser = [
        ('E', 'E'),
        ('U', 'U')
    ]

    Estado_ENUM = [
        ('A', 'A'),
        ('I', 'I')
    ]

    idregistro = models.AutoField(db_column='idRegistro', primary_key=True)  # Field name made lowercase.
    nit = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.CharField(max_length=40, db_column='usuario', unique=True)
    password = models.CharField(max_length=128)
    nombreempresa = models.CharField(db_column='nombreEmpresa', unique=True, max_length=40, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=40)
    correo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=40)
    tipousuario = models.CharField(db_column='tipoUsuario', choices=TipoUser, max_length=1)  # Field name made lowercase.
    fotoperfil = models.ImageField(upload_to='fotoperfil/', max_length=80, null=True)
    resena = models.CharField(max_length=40)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    estado = models.CharField(choices=Estado_ENUM, default='I', max_length=1)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField('self', blank=True, related_name='likes')
    dislikes = models.ManyToManyField('self', blank=True, related_name='dislikes')
    Descripcion = models.TextField(max_length=180, blank=True, null=True)

    

     
    REQUIRED_FIELDS = ['correo', 'telefono'] 
    USERNAME_FIELD = 'usuario'
    EMAIL_FIELD = 'correo'
    # PASSWORD_FIELD = 'contrasena'  

    objects = EmpresaPersonaManager()

    def __str__(self):
        return self.usuario

    def has_perm(self,perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
     
    class Meta:
         db_table = 'empresa/usuario'

    @property
    def is_staff(self):
        return self.usuario_administrador



    # class Meta:
    #     managed = Fals
    #     db_table = 'empresa/persona'

class comentarioUSer(models.Model):
    comment = models.TextField(db_column='comentario')
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(EmpresaPersona, on_delete=models.CASCADE, related_name='comment_author')
    receptor = models.ForeignKey(EmpresaPersona, on_delete=models.CASCADE, db_column='usuario')
    likes = models.ManyToManyField(EmpresaPersona, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(EmpresaPersona, blank=True, related_name='comment_dislikes')
    
    # parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    # @property
    # def children(self):
    #     return comentarioUSer.objects.filter(parent=self).order_by('created_on').all()
    
    # @property
    # def is_parent(self):
    #     if self.parent is None:
    #         return True
    #     return False
    





class Persona(models.Model ):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)
    documento = models.CharField(max_length=45)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=40)
    empresa_idEmpresa = models.ForeignKey('EmpresaPersona', db_column='empresa_idEmpresa', on_delete=models.CASCADE)
    

    class Meta:
        
        db_table = 'persona'
        


class Puntosdeportivos(models.Model):
    idPuntoDeportivo = models.AutoField(db_column='idPuntoDeportivo', primary_key=True)
    nombre = models.CharField(db_column='nombre',max_length=50)
    direccion = models.CharField(db_column='direccion', max_length=40)

    class Meta:
   
        db_table = 'puntosdeportivos'


class Realizacion(models.Model):
    actividad_idactividad = models.ForeignKey('Actividad',on_delete=models.CASCADE,db_column='actividad_idActividad') 
    usuario_idusuario = models.ForeignKey('EmpresaPersona',on_delete=models.CASCADE, db_column='usuario_idEmpresaPersona')  
    comentarios = models.CharField(max_length=45, null=True)
  

    class Meta:
        
        db_table = 'realizacion'

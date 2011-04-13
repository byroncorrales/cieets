# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Musica'
        db.create_table('multimedia_musica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('artista', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('multimedia', ['Musica'])


    def backwards(self, orm):
        
        # Deleting model 'Musica'
        db.delete_table('multimedia_musica')


    models = {
        'multimedia.fotoportada': {
            'Meta': {'object_name': 'FotoPortada'},
            'archivo': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.musica': {
            'Meta': {'object_name': 'Musica'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'artista': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.programaradial': {
            'Meta': {'object_name': 'ProgramaRadial'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.video': {
            'Meta': {'object_name': 'Video'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['multimedia']

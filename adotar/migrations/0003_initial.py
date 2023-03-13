# Generated by Django 4.1.7 on 2023-03-13 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divulgar', '0003_pet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adotar', '0002_delete_pedidoadocao'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('AG', 'Aguardando aprovação'), ('AP', 'Aprovado'), ('R', 'Reprovado')], default='AG', max_length=2)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.pet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

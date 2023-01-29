# Generated by Django 4.1.5 on 2023-01-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=100, verbose_name='Serviço')),
                ('tecnologia', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'NotebookLaptop'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'MultiPaginas')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

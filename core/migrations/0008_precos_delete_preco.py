# Generated by Django 4.1.5 on 2023-01-30 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_preco_delete_precos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('preco', models.CharField(max_length=10, verbose_name='Preco')),
                ('plano', models.CharField(max_length=100, verbose_name='PLano')),
                ('qts_usuarios', models.CharField(max_length=100, verbose_name='Quantidade de Usuarios')),
                ('capacidade', models.CharField(max_length=100, verbose_name='Capacidade')),
                ('email_suporte', models.CharField(max_length=100, verbose_name='Email Suporte')),
                ('atualizacoes', models.CharField(max_length=100, verbose_name='Atualizações')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Preco',
        ),
    ]
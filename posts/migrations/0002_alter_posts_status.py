# Generated by Django 4.2.3 on 2023-08-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('Ожидание подтверждения', 'Ожидание подтверждения'), ('Запрос принят', 'Запрос принят'), (3, 'Детали обмена согласованы'), (4, 'Обмен завершен'), (5, 'Отклонен'), (6, 'Отменен')], default=1),
        ),
    ]
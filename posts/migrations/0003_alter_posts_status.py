# Generated by Django 4.2.3 on 2023-08-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('Ожидание подтверждения', 'Ожидание подтверждения'), ('Запрос принят', 'Запрос принят'), ('Детали обмена согласованы', 'Детали обмена согласованы'), ('Обмен завершен', 'Обмен завершен'), ('Отклонен', 'Отклонен'), ('Отменен', 'Отменен')], default=1, max_length=500),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-11 10:29

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LenderSystem',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('base_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='API Base URL')),
                ('api_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='API Key')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('jwt_obtain', models.URLField(blank=True, max_length=255, null=True, verbose_name='JWT Obtain URL')),
                ('jwt_refresh', models.URLField(blank=True, max_length=255, null=True, verbose_name='JWT Refresh URL')),
                ('name', models.CharField(help_text='Name of the Lender', max_length=255, verbose_name='Lender')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Lender Code')),
            ],
            options={
                'verbose_name': 'Lender',
                'verbose_name_plural': 'Lenders',
            },
        ),
        migrations.CreateModel(
            name='LenderSystemAPI',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the API', max_length=255, verbose_name='API Name')),
                ('host', models.CharField(max_length=255, verbose_name='API Path')),
                ('query_params', models.JSONField(blank=True, default=dict, null=True)),
                ('body', models.JSONField(blank=True, default=dict, null=True)),
                ('method', models.PositiveSmallIntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PUT'), (4, 'PATCH'), (5, 'DELETE')])),
                ('auth_scheme', models.PositiveSmallIntegerField(choices=[(1, 'API Key'), (2, 'Bearer Token')])),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Lender API',
                'verbose_name_plural': 'Lender APIs',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('loanid', models.CharField(help_text='Lender LoanID', max_length=255, null=True, verbose_name='Loan Reference No.')),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='borrowers.loanapplication', verbose_name='Application')),
                ('lender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lenders.lendersystem')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
                'unique_together': {('lender', 'loanid')},
            },
        ),
        migrations.CreateModel(
            name='LoanData',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('request', models.JSONField(default=dict, null=True)),
                ('response', models.JSONField(default=dict, null=True)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='borrowers.loanapplication')),
                ('lender_api', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lenders.lendersystemapi')),
                ('loan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lenders.loan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lendersystemapi',
            name='data',
            field=models.ManyToManyField(through='lenders.LoanData', to='borrowers.LoanApplication'),
        ),
        migrations.AddField(
            model_name='lendersystemapi',
            name='lender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lenders.lendersystem'),
        ),
    ]

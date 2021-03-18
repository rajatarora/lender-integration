# Generated by Django 3.1.7 on 2021-03-18 15:39

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
            name='ChannelPartners',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the Channel Partner', max_length=255, verbose_name='Channel Partner')),
                ('code', models.CharField(help_text='Will beprefixed with lmsId to generate loanId', max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Channel Partner',
                'verbose_name_plural': 'Channel Partners',
            },
        ),
        migrations.CreateModel(
            name='LoanManagementSystem',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('base_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='API Base URL')),
                ('api_key', models.TextField(blank=True, null=True, verbose_name='API Key')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('params', models.JSONField(blank=True, default=dict, null=True, verbose_name='Query Parameters')),
                ('headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Headers')),
                ('body', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Body')),
                ('oauth_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='OAuth URL')),
                ('oauth_headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='OAuth Request Headers')),
                ('oauth_body', models.JSONField(blank=True, default=dict, null=True, verbose_name='OAuth Request Body')),
                ('name', models.CharField(help_text='Name of the Loan Management System', max_length=255, verbose_name='LMS')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='LMS Code')),
            ],
            options={
                'verbose_name': 'LMS',
                'verbose_name_plural': 'LMS',
            },
        ),
        migrations.CreateModel(
            name='PlatformService',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('base_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='API Base URL')),
                ('api_key', models.TextField(blank=True, null=True, verbose_name='API Key')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('params', models.JSONField(blank=True, default=dict, null=True, verbose_name='Query Parameters')),
                ('headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Headers')),
                ('body', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Body')),
                ('oauth_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='OAuth URL')),
                ('oauth_headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='OAuth Request Headers')),
                ('oauth_body', models.JSONField(blank=True, default=dict, null=True, verbose_name='OAuth Request Body')),
                ('name', models.CharField(help_text='Name of the platform service', max_length=255, verbose_name='Service')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Service Code')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='PlatformServiceAPI',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the API', max_length=255, verbose_name='API Name')),
                ('path', models.CharField(max_length=255, verbose_name='API Path')),
                ('params', models.JSONField(blank=True, default=dict, null=True, verbose_name='Query Parameters')),
                ('headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Headers')),
                ('body', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Body')),
                ('iterable', models.BooleanField(blank=True, default=False, null=True)),
                ('iterable_data', models.TextField(blank=True, null=True, verbose_name='Iterable Data Path')),
                ('iterable_filters', models.JSONField(blank=True, default=dict, null=True, verbose_name='Iterable Data Filters')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('PUT', 'PUT'), ('POST', 'POST'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], max_length=10, verbose_name='HTTP Method')),
                ('auth_scheme', models.CharField(choices=[('Token', 'Token'), ('Bearer', 'Bearer'), ('Basic', 'Basic')], max_length=10, verbose_name='HTTP Auth Scheme')),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Workflow Priority')),
                ('data', models.ManyToManyField(through='borrowers.LoanApplicationData', to='borrowers.LoanApplication')),
                ('svc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='platforms.platformservice', verbose_name='SVC')),
            ],
            options={
                'verbose_name': 'Service API',
                'verbose_name_plural': 'Services API',
            },
        ),
        migrations.CreateModel(
            name='LoanManagementSystemAPI',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the API', max_length=255, verbose_name='API Name')),
                ('path', models.CharField(max_length=255, verbose_name='API Path')),
                ('params', models.JSONField(blank=True, default=dict, null=True, verbose_name='Query Parameters')),
                ('headers', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Headers')),
                ('body', models.JSONField(blank=True, default=dict, null=True, verbose_name='Request Body')),
                ('iterable', models.BooleanField(blank=True, default=False, null=True)),
                ('iterable_data', models.TextField(blank=True, null=True, verbose_name='Iterable Data Path')),
                ('iterable_filters', models.JSONField(blank=True, default=dict, null=True, verbose_name='Iterable Data Filters')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('PUT', 'PUT'), ('POST', 'POST'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], max_length=10, verbose_name='HTTP Method')),
                ('auth_scheme', models.CharField(choices=[('Token', 'Token'), ('Bearer', 'Bearer'), ('Basic', 'Basic')], max_length=10, verbose_name='HTTP Auth Scheme')),
                ('priority', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Workflow Priority')),
                ('data', models.ManyToManyField(through='borrowers.LoanApplicationData', to='borrowers.LoanApplication')),
                ('lms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='platforms.loanmanagementsystem', verbose_name='LMS')),
            ],
            options={
                'verbose_name': 'LMS API',
                'verbose_name_plural': 'LMS API',
            },
        ),
    ]

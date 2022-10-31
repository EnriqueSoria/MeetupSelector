# Generated by Django 3.2.16 on 2022-10-31 00:47

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("talks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("description", models.TextField(verbose_name="description")),
                ("location", models.CharField(max_length=255, verbose_name="location")),
                ("meetup_link", models.CharField(max_length=255, verbose_name="meetup_link")),
                ("done", models.BooleanField(default=False, verbose_name="done")),
            ],
            options={
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
        migrations.CreateModel(
            name="Proposal",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("subject", models.CharField(max_length=255, verbose_name="subjects")),
                ("description", models.TextField(verbose_name="description")),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("E", "easy"), ("M", "medium"), ("H", "hard")],
                        default="E",
                        max_length=1,
                        verbose_name="difficulty",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("EN_GB", "english"),
                            ("FR_FR", "french"),
                            ("ES_ES", "spain"),
                            ("ES_EU", "basque"),
                            ("ES_CA", "catalonian"),
                            ("ES_GL", "galicia"),
                        ],
                        default="ES_ES",
                        max_length=6,
                        verbose_name="language",
                    ),
                ),
                ("done", models.BooleanField(default=False, verbose_name="done")),
                (
                    "liked_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="proposals",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="liked_by",
                    ),
                ),
                (
                    "proposed_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="proposal",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="proposed_by",
                    ),
                ),
                (
                    "topics",
                    models.ManyToManyField(
                        related_name="proposals", to="talks.Topic", verbose_name="topics"
                    ),
                ),
            ],
            options={
                "verbose_name": "proposal",
                "verbose_name_plural": "proposals",
            },
        ),
    ]

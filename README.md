# API RESTful con Django REST Framework (DRF) — `restful-intent13`

- **Asignatura:** Desarrollo de Aplicaciones Web (IS093A) — Unidad II: Desarrollo Web Fullstack
- **Institución:** Universidad Nacional del Centro del Perú — Facultad de Ingeniería de Sistemas
- **Práctica:** Guía Práctica Semana 12 — Diseño de APIs RESTful con Django REST Framework (DRF)
- **Repositorio:** https://github.com/nauparirojas/restful-intent13

---

## 1. Objetivo de la Práctica

Diseñar, implementar y documentar una API RESTful *production-ready* utilizando **Django REST Framework (DRF)**, aplicando los principios arquitectónicos REST (*stateless*, *cacheable*, *layered system*, *uniform interface*, *code on demand*, *client-server*) y el estilo **HATEOAS** básico. La solución integra serialización avanzada, `ModelViewSet` + `DefaultRouter`, paginación estándar, filtrado por *query parameters*, *throttling*, configuración de **CORS**, gestión de **CSRF** y documentación interactiva **OpenAPI / Swagger**, dejando una estructura modular preparada para microservicios y contenedores.

---

## 2. Stack Tecnológico y Dependencias

- **Python:** 3.11+
- **Framework Web:** Django 5.x + Django REST Framework (`djangorestframework`)
- **Filtrado:** `django-filter`
- **CORS:** `django-cors-headers`
- **Documentación OpenAPI / Swagger:** `drf-spectacular`

---

## 3. Estructura del Proyecto (`C:\restful-intent13`)

restful-intent13/
├── .env                       # Variables de entorno locales (no versionado)
├── .gitignore                 # Exclusiones (venv/, __pycache__/, .env, db.sqlite3)
├── README.md                  # Documentación técnica del proyecto
├── requirements.txt           # Dependencias del proyecto
├── schema.yml                 # Esquema OpenAPI 3.0 generado con drf-spectacular
├── manage.py                  # CLI de administración de Django
│
├── config/                    # Configuración global del proyecto
│   ├── __init__.py
│   ├── settings.py            # REST_FRAMEWORK, CORS, SPECTACULAR_SETTINGS
│   ├── urls.py                # Enrutamiento base (/api/, /api/schema/, /api/docs/)
│   ├── wsgi.py
│   └── asgi.py
│
└── catalogo/                  # App de dominio desacoplada
    ├── __init__.py
    ├── apps.py
    ├── models.py              # Modelo Producto con índices DB
    ├── serializers.py         # HyperlinkedModelSerializer, validaciones y HATEOAS (_links)
    ├── views.py               # ModelViewSet + @action personalizada
    ├── urls.py                # DefaultRouter
    ├── admin.py
    ├── tests.py
    └── migrations/
        └── __init__.py

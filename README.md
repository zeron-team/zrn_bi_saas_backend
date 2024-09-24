#

## ESTRUCTURA
``` text
bi-saas-project/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py            # Inicializador de la aplicación
│   │   ├── config.py              # Configuraciones generales (DB, JWT, etc.)
│   │   ├── models.py              # Definición de los modelos (Usuarios, Empresas, Conexiones)
│   │   ├── routes/
│   │   │   ├── __init__.py        # Inicializador de rutas
│   │   │   ├── auth.py            # Rutas de autenticación (login, registro)
│   │   │   ├── users.py           # Rutas de administración de usuarios
│   │   │   ├── companies.py       # Rutas de administración de empresas
│   │   │   ├── connections.py     # Rutas de administración de conexiones de DB
│   │   │   ├── queries.py         # Rutas de gestión de consultas SQL
│   │   │   ├── charts.py          # Rutas de creación y gestión de gráficos
│   │   │   └── cms.py             # Rutas del CMS para páginas y gráficos
│   │   ├── services/
│   │   │   ├── __init__.py        # Inicializador de servicios
│   │   │   ├── auth_service.py    # Lógica de autenticación y JWT
│   │   │   ├── user_service.py    # Lógica de negocio para usuarios
│   │   │   ├── company_service.py # Lógica de negocio para empresas
│   │   │   ├── db_service.py      # Lógica para manejar conexiones a DB externas
│   │   │   ├── query_service.py   # Lógica para ejecutar y gestionar consultas SQL
│   │   │   ├── chart_service.py   # Lógica para la creación y gestión de gráficos
│   │   │   └── cms_service.py     # Lógica para el CMS
│   │   ├── utils/
│   │   │   ├── __init__.py        # Inicializador de utilidades
│   │   │   ├── db_connection.py   # Funciones para conexiones con MongoDB
│   │   │   ├── jwt_handler.py     # Funciones para manejar JWT
│   │   │   ├── error_handlers.py  # Manejo de errores global
│   │   │   └── validation.py      # Validación de datos
│   │   └── main.py                # Punto de entrada de la aplicación
│   └── requirements.txt           # Dependencias de Python
│
├── frontend/
│   ├── public/                    # Archivos públicos (index.html, etc.)
│   ├── src/
│   │   ├── assets/                # Recursos estáticos (imágenes, CSS, etc.)
│   │   ├── components/            # Componentes reutilizables
│   │   │   ├── Auth/              # Componentes de autenticación (Login, Registro)
│   │   │   ├── Admin/             # Componentes de administración (Usuarios, Empresas, Conexiones)
│   │   │   ├── Designer/          # Componentes de diseñador (Creación de gráficos, editor SQL)
│   │   │   ├── Viewer/            # Componentes de visualización (Dashboards)
│   │   ├── contexts/              # Contextos de React (Autenticación, Estado Global)
│   │   ├── hooks/                 # Hooks personalizados
│   │   ├── pages/                 # Páginas principales de la aplicación
│   │   ├── services/              # Servicios para consumir APIs del backend
│   │   ├── styles/                # Estilos globales
│   │   ├── utils/                 # Utilidades comunes
│   │   └── App.js                 # Componente principal de la aplicación
│   └── package.json               # Dependencias de React
│
├── db/
│   ├── seed_data.js               # Script para datos iniciales (usuarios, roles, etc.)
│   └── migrations/                # Archivos de migración para cambios en el esquema
│
└── README.md                      # Documentación del proyecto

```

## GIT
- git remote add origin https://github.com/zeron-team/zrn_bi_saas_backend.git
- git push -u origin master 
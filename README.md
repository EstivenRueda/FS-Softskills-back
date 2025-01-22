# FS-Softskills-back

Este es el repositorio backend para el proyecto de Soft Skills

## Instalación local

Este proyecto necesita los siguientes elementos instalados en tu sistema:

- Python 3.11

### 1. Clonar el repositorio:

```sh
git clone https://github.com/EstivenRueda/FS-Softskills-back.git
cd FS-Softskills-back
```

### 2. Crear el entorno virtual

Para Windows:
```sh
python -m venv venv
```

Para Linux y Mac:
```sh
python3 -m venv venv
```

### 3. Activar el entorno virtual

Para Windows:
```sh
.\venv\Scripts\activate
```

Para Linux y Mac OS:
```sh
source venv/bin/activate
```

### 4. Instalar las dependencias
```sh
pip install -r requirements.txt
```

### 5. Instalar la base de datos PostgreSQL
https://www.postgresql.org/download/

###### Guía para Windows
https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/

### 6. Crea la base de datos `finishing_school`
```
createdb finishing_school
```

### 7. Configura las variables de entorno

Copia el archivo `.env.local` a un nuevo archivo llamado `.env` y actualiza las variables como las necesites.

### 8. Aplica las migraciones
```
python manage.py migrate
```

#### 9. Carga los fixtures
```
python manage.py load_production_fixtures
```

### 10. Recopila los archivos estáticos
```
python manage.py collectstatic
```

#### 11. Corre el servidor local
```
python manage.py runserver
```

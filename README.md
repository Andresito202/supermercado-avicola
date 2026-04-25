# Supermercado Avicola

Sistema web de gestion integral para un supermercado especializado en productos avicolas. El proyecto cubre operaciones comerciales y de inventario de punta a punta: autenticacion, catalogo, proveedores, compras, lotes, inventario, punto de venta, caja, mermas, reportes y auditoria.

## Resumen para portafolio

Aplicacion full stack construida con FastAPI, SQLAlchemy, PostgreSQL y frontend multipagina en Bootstrap 5. Incluye autenticacion con JWT, control por roles, flujo de compras con generacion de lotes, salida de inventario por FIFO, reportes operativos, auditoria de acciones y despliegue local con Docker Compose.

## Alcance funcional

- Autenticacion con JWT y control de acceso por roles.
- CRUD de categorias, productos, proveedores y clientes.
- Registro de compras con generacion de lotes y movimientos de inventario.
- Inventario con stock actual, lotes, movimientos, ajustes y alertas de vencimiento.
- Punto de venta con validacion de stock y salida FIFO.
- Modulo de caja con apertura, cierre y movimientos manuales.
- Registro de mermas y trazabilidad operativa.
- Reportes de ventas diarias, top productos, inventario valorizado y mermas.
- Auditoria de acciones sobre el sistema.

## Arquitectura

- `backend/`: API REST en FastAPI, dominio, seguridad, migraciones y tests.
- `frontend/`: interfaz multipagina en HTML, Bootstrap y JavaScript.
- `database/`: seeds iniciales para usuarios, categorias, productos, proveedores y clientes.
- `infra/`: contenedores de backend y PostgreSQL con Docker Compose.
- `docs/`: avance del proyecto, manual de usuario y explicacion tecnica extendida.

## Stack tecnico

- Python 3.12
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL 16
- Pydantic
- JWT + Passlib/Bcrypt
- HTML5
- Bootstrap 5
- JavaScript vanilla
- Docker Compose
- Pytest

## Modulos principales

- `auth`: login, registro de usuarios y perfil autenticado.
- `categorias`: gestion del catalogo base.
- `productos`: productos, precios, unidad de medida y reglas de negocio.
- `proveedores`: terceros y abastecimiento.
- `compras`: entradas de mercancia y alta de lotes.
- `inventario`: stock, movimientos, alertas y ajustes.
- `clientes`: administracion de clientes del punto de venta.
- `ventas`: ventas y devolucion de stock al anular.
- `caja`: apertura, cierre y arqueo operativo.
- `mermas`: registro de perdida o deterioro.
- `reportes`: vistas de control y resumen comercial.
- `auditoria`: trazabilidad de acciones.

## Ejecucion local

### Opcion 1: Docker Compose

```powershell
cd infra
docker compose up --build
```

Servicios esperados:

- Aplicacion: `http://localhost:8000`
- Documentacion API: `http://localhost:8000/docs`
- Base de datos: `localhost:5432`

### Opcion 2: Ejecucion local sin Docker

```powershell
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

En este modo se requiere configurar `DATABASE_URL` en `.env`.

## Credenciales iniciales

Definidas en `.env.example`:

- Usuario admin: `admin`
- Contrasena inicial: `Admin123!`

El seed adicional crea usuarios para roles de cajero, bodeguero, supervisor y gerente.

## Seed de datos

El proyecto incluye datos base para demostrar el sistema:

- 5 usuarios
- 10 categorias
- 30 productos
- 5 proveedores
- 5 clientes

Ejecucion:

```powershell
python database/seeds/seed_data.py
```

## Estructura principal

```text
supermercado-avicola/
|-- backend/
|-- frontend/
|-- database/
|-- docs/
|-- infra/
|-- .env.example
|-- .gitignore
|-- iniciar.bat
|-- detener.bat
|-- README.md
```

## Calidad tecnica

- API modular separada por dominios de negocio.
- Validacion de datos con Pydantic.
- Migraciones versionadas con Alembic.
- Persistencia desacoplada via SQLAlchemy ORM.
- Trazabilidad operativa mediante auditoria.
- Tests automatizados para autenticacion, catalogo y ventas.

## Documentacion adicional

Ver [docs/README.md](C:\Users\Usuario\OneDrive\Desktop\pryecto%20uniminuto\supermercado-avicola\docs\README.md) para navegar la documentacion interna del proyecto.

## Enfoque de ingenieria

- Proyecto orientado a operacion real, no solo a una demo academica.
- Separacion explicita entre API, frontend, infraestructura y datos iniciales.
- Reglas de negocio visibles en compras, inventario, lotes, FIFO y caja.
- Base suficientemente estructurada para evolucionar a produccion o continuar en nuevos sprints.

"""
Seed de datos iniciales para el Supermercado Avicola.
Ejecutar: python -m database.seeds.seed_data
O desde el directorio raiz: python database/seeds/seed_data.py
"""
import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "backend"))

from app.core.database import SessionLocal, Base, engine
from app.core.security import hash_password
from app.models.usuario import Usuario, RolEnum
from app.models.categoria import Categoria
from app.models.producto import Producto, UnidadMedida
from app.models.proveedor import Proveedor
from app.models.cliente import Cliente


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # --- Usuarios ---
        if not db.query(Usuario).first():
            usuarios = [
                Usuario(username="admin", email="admin@avicola.local", hashed_password=hash_password("Admin123!"),
                        nombre_completo="Administrador del Sistema", rol=RolEnum.admin),
                Usuario(username="cajero1", email="cajero1@avicola.local", hashed_password=hash_password("Cajero123!"),
                        nombre_completo="Maria Lopez", rol=RolEnum.cajero),
                Usuario(username="bodeguero1", email="bodega1@avicola.local", hashed_password=hash_password("Bodega123!"),
                        nombre_completo="Carlos Ramirez", rol=RolEnum.bodeguero),
                Usuario(username="supervisor1", email="super1@avicola.local", hashed_password=hash_password("Super123!"),
                        nombre_completo="Ana Torres", rol=RolEnum.supervisor),
                Usuario(username="gerente1", email="gerente@avicola.local", hashed_password=hash_password("Gerente123!"),
                        nombre_completo="Wilson Camacho", rol=RolEnum.gerente),
            ]
            db.add_all(usuarios)
            db.flush()
            print(f"  + {len(usuarios)} usuarios creados")

        # --- Categorias ---
        if not db.query(Categoria).first():
            categorias_data = [
                ("Pollo entero", "Pollos enteros frescos y congelados"),
                ("Presas de pollo", "Pechuga, muslo, pernil, alas, costillar"),
                ("Visceras y menudencias", "Higado, corazon, molleja, patas"),
                ("Embutidos avicolas", "Salchichas, chorizos, jamon de pollo"),
                ("Huevos", "Huevos de gallina por unidad y cubeta"),
                ("Productos procesados", "Nuggets, apanados, hamburguesas de pollo"),
                ("Salsas y condimentos", "Adobos, salsas, especias para pollo"),
                ("Bebidas", "Gaseosas, jugos, agua"),
                ("Granos y cereales", "Arroz, frijol, lenteja, avena"),
                ("Lacteos", "Leche, queso, yogur, mantequilla"),
            ]
            cats = [Categoria(nombre=n, descripcion=d) for n, d in categorias_data]
            db.add_all(cats)
            db.flush()
            print(f"  + {len(cats)} categorias creadas")

        # --- Productos ---
        if not db.query(Producto).first():
            productos_data = [
                ("P001", "Pollo entero fresco", 1, UnidadMedida.kilogramo, 8500, 11500, 5, True),
                ("P002", "Pollo entero congelado", 1, UnidadMedida.kilogramo, 7800, 10500, 5, True),
                ("P003", "Pechuga de pollo", 2, UnidadMedida.kilogramo, 12000, 16000, 3, True),
                ("P004", "Muslo de pollo", 2, UnidadMedida.kilogramo, 7500, 10000, 3, True),
                ("P005", "Pernil de pollo", 2, UnidadMedida.kilogramo, 7000, 9500, 3, True),
                ("P006", "Alas de pollo", 2, UnidadMedida.kilogramo, 6500, 9000, 3, True),
                ("P007", "Costillar de pollo", 2, UnidadMedida.kilogramo, 5000, 7000, 3, True),
                ("P008", "Higado de pollo", 3, UnidadMedida.kilogramo, 4000, 6500, 2, True),
                ("P009", "Molleja de pollo", 3, UnidadMedida.kilogramo, 5500, 8000, 2, True),
                ("P010", "Corazon de pollo", 3, UnidadMedida.kilogramo, 4500, 7000, 2, True),
                ("P011", "Patas de pollo", 3, UnidadMedida.kilogramo, 2000, 3500, 2, True),
                ("P012", "Salchicha de pollo x500g", 4, UnidadMedida.unidad, 5500, 7800, 5, True),
                ("P013", "Chorizo de pollo x500g", 4, UnidadMedida.unidad, 6000, 8500, 3, True),
                ("P014", "Jamon de pollo x250g", 4, UnidadMedida.unidad, 4500, 6500, 3, True),
                ("P015", "Huevo cubeta x30", 5, UnidadMedida.unidad, 14000, 18000, 10, True),
                ("P016", "Huevo unidad", 5, UnidadMedida.unidad, 500, 700, 30, False),
                ("P017", "Nuggets de pollo x500g", 6, UnidadMedida.unidad, 8000, 11000, 5, True),
                ("P018", "Apanado de pollo x500g", 6, UnidadMedida.unidad, 7500, 10500, 3, True),
                ("P019", "Hamburguesa pollo x4", 6, UnidadMedida.unidad, 6000, 8500, 3, True),
                ("P020", "Adobo para pollo x100g", 7, UnidadMedida.unidad, 2000, 3200, 5, False),
                ("P021", "Salsa BBQ x300ml", 7, UnidadMedida.unidad, 4500, 6500, 3, False),
                ("P022", "Gaseosa 1.5L", 8, UnidadMedida.unidad, 3000, 4500, 10, False),
                ("P023", "Jugo natural 1L", 8, UnidadMedida.unidad, 3500, 5000, 5, True),
                ("P024", "Agua 600ml", 8, UnidadMedida.unidad, 800, 1500, 20, False),
                ("P025", "Arroz x500g", 9, UnidadMedida.unidad, 2200, 3200, 10, False),
                ("P026", "Arroz x1kg", 9, UnidadMedida.unidad, 4000, 5500, 8, False),
                ("P027", "Frijol rojo x500g", 9, UnidadMedida.unidad, 3500, 5000, 5, False),
                ("P028", "Leche entera 1L", 10, UnidadMedida.unidad, 3200, 4500, 10, True),
                ("P029", "Queso campesino x500g", 10, UnidadMedida.unidad, 7000, 9500, 3, True),
                ("P030", "Mantequilla x125g", 10, UnidadMedida.unidad, 3000, 4200, 5, True),
            ]
            prods = []
            for codigo, nombre, cat_id, um, pc, pv, sm, perec in productos_data:
                prods.append(Producto(
                    codigo=codigo, nombre=nombre, categoria_id=cat_id,
                    unidad_medida=um, precio_compra=pc, precio_venta=pv,
                    stock_minimo=sm, es_perecedero=perec,
                ))
            db.add_all(prods)
            db.flush()
            print(f"  + {len(prods)} productos creados")

        # --- Proveedores ---
        if not db.query(Proveedor).first():
            proveedores_data = [
                ("900123456-1", "Avicola El Pollo Feliz", "Pedro Martinez", "3101234567", "ventas@pollofeliz.co"),
                ("800987654-2", "Distribuidora Avicola Nacional", "Laura Gomez", "3209876543", "pedidos@avicnacional.co"),
                ("901555888-3", "Huevos La Granja SAS", "Jorge Diaz", "3155558888", "ventas@lagranja.co"),
                ("800111222-4", "Embutidos Pollo Dorado", "Sandra Ruiz", "3181112222", "comercial@pollodorado.co"),
                ("900444333-5", "Distribuidora La Economia", "Felipe Vargas", "3204443333", "pedidos@laeconomia.co"),
            ]
            provs = [Proveedor(nit=n, nombre=nom, contacto=c, telefono=t, email=e) for n, nom, c, t, e in proveedores_data]
            db.add_all(provs)
            db.flush()
            print(f"  + {len(provs)} proveedores creados")

        # --- Clientes ---
        if not db.query(Cliente).first():
            clientes_data = [
                ("1001001001", "Restaurante El Buen Sabor", "3101001001", "buensabor@mail.com"),
                ("1002002002", "Asadero Don Pollo", "3102002002", "donpollo@mail.com"),
                ("1003003003", "Tienda Doña Carmen", "3103003003", None),
                ("1004004004", "Hotel Plaza Central", "3104004004", "compras@plazacentral.co"),
                ("9999999999", "Consumidor Final", None, None),
            ]
            clientes = [Cliente(documento=d, nombre=n, telefono=t, email=e) for d, n, t, e in clientes_data]
            db.add_all(clientes)
            db.flush()
            print(f"  + {len(clientes)} clientes creados")

        db.commit()
        print("\nSeed completado exitosamente.")

    except Exception as e:
        db.rollback()
        print(f"Error en seed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("Ejecutando seed de datos...")
    seed()

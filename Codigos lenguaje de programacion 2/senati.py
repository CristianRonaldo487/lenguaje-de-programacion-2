from graphviz import Digraph

# Crear un diagrama de flujo
dot = Digraph(comment="Flujo de Proceso - Chuñitos Fritos", format="png")
dot.attr(rankdir="TB", size="8")

# Secciones principales
dot.attr('node', shape='box', style='filled', color='lightblue')
dot.node("A", "COMPRA Y RECEPCIÓN DE INSUMOS")
dot.node("B", "PREPARACIÓN")
dot.node("C", "ATENCIÓN AL CLIENTE")

# Subprocesos - Compra y recepción de insumos
dot.attr('node', shape='ellipse', style='filled', color='white')
dot.node("A1", "Recepción de insumos")
dot.node("A2", "Comprobación de insumos")
dot.node("A3", "Pago al proveedor")
dot.node("A4", "Almacenamiento de insumos")

# Subprocesos - Preparación
dot.node("B1", "Lavado de chuñitos")
dot.node("B2", "Selección y descarte")
dot.node("B3", "Pelado y troceado")
dot.node("B4", "Remojo o pre-cocción")
dot.node("B5", "Secado o escurrido")
dot.node("B6", "Fritura de chuñitos")
dot.node("B7", "Escurrido de aceite")
dot.node("B8", "Preparación de salsas")

# Subprocesos - Atención al cliente
dot.node("C1", "Guardado en bandejas")
dot.node("C2", "Porcionado y empaque")
dot.node("C3", "Armado de combos")
dot.node("C4", "Atención al cliente")
dot.node("C5", "Cobro y registro de venta")

# Relaciones entre secciones principales
dot.edge("A", "A1")
dot.edge("A1", "A2")
dot.edge("A2", "A3")
dot.edge("A3", "A4")
dot.edge("A4", "B")

dot.edge("B", "B1")
dot.edge("B1", "B2")
dot.edge("B2", "B3")
dot.edge("B3", "B4")
dot.edge("B4", "B5")
dot.edge("B5", "B6")
dot.edge("B6", "B7")
dot.edge("B7", "B8")
dot.edge("B8", "C")

dot.edge("C", "C1")
dot.edge("C1", "C2")
dot.edge("C2", "C3")
dot.edge("C3", "C4")
dot.edge("C4", "C5")

# Renderizar
output_path = "/mnt/data/flujo_chunitos"
dot.render(output_path, format="png", cleanup=True)

output_path + ".png"

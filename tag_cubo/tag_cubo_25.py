import cadquery as cq
from ocp_vscode import show, set_port

# Parâmetros
lado = 25    
diametro_circulo = 20.5
profundidade_circulo = 2.2
raio_arredondamento = 4

# Criar cubo com arestas arredondadas
resultado = (cq.Workplane("XY")
    .box(lado, lado, lado)
    .edges()
    .fillet(raio_arredondamento)
)

# Adicionar círculo em cada face
# Face superior (Z+)
resultado = resultado.faces(">Z").workplane().circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Face inferior (Z-)
resultado = resultado.faces("<Z").workplane().circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Face frontal (Y+)
resultado = resultado.faces(">Y").workplane(centerOption="CenterOfBoundBox").circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Face traseira (Y-)
resultado = resultado.faces("<Y").workplane(centerOption="CenterOfBoundBox").circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Face direita (X+)
resultado = resultado.faces(">X").workplane(centerOption="CenterOfBoundBox").circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Face esquerda (X-)
resultado = resultado.faces("<X").workplane(centerOption="CenterOfBoundBox").circle(diametro_circulo/2).cutBlind(-profundidade_circulo)

# Exportar para STL
cq.exporters.export(resultado, f"./stl/tag_cubo_{lado}.stl")


set_port(3939)
show(resultado)
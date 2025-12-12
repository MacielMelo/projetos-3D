import cadquery as cq

# Parâmetros
altura = 20      # z
largura = 20     # x
espessura = 20   # y
diametro_circulo = 15
profundidade_circulo = 2
raio_arredondamento = 4

# Criar cubo com arestas arredondadas
resultado = (cq.Workplane("XY")
    .box(largura, espessura, altura)
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
cq.exporters.export(resultado, "tag_cubo_20.stl")
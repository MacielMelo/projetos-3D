import cadquery as cq
from ocp_vscode import *

def criar_caixa_parametrica(
    largura=50,
    profundidade=30,
    altura=20,
    espessura_parede=2,
    raio_cantos=3
):
    """Cria uma caixa paramétrica com tampa."""
    
    # Corpo da caixa
    caixa = (
        cq.Workplane("XY")
        .box(largura, profundidade, altura)
        .faces(">Z")
        .shell(-espessura_parede)
        .edges("|Z")
        .fillet(raio_cantos)
    )
    
    return caixa

# Criar modelo
minha_caixa = criar_caixa_parametrica(
    largura=60,
    profundidade=40,
    altura=25,
    espessura_parede=2.5,
    raio_cantos=4
)

set_port(3939)
show(minha_caixa)
# Exportar
# cq.exporters.export(minha_caixa, "caixa.stl")
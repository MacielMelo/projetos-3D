import cadquery as cq
from ocp_vscode import *

diameter = 12.0
depth = 50.0
qtd = 8

height = 60.0 #(x-axis)
width = (diameter + 5 ) * qtd #(y-axis)
thickness = 15.0 #(z-axis)



# Base
result = ( 
            cq.Workplane("XY")
            .box(thickness,width,height)
            .faces(">Z")
            .workplane()
            .rarray(yCount=qtd, xCount=1, xSpacing=0, ySpacing=5 + diameter)
            .hole(diameter, depth)
          
          )

set_port(3939)
show(result)

cq.exporters.export(result, f"./stl/formao_xilogravura_{height}_{width}.stl")


import cadquery as cq
from ocp_vscode import *

height = 60.0 #(x-axis)
width = 15.0 #(y-axis)
thickness = 60.0 #(z-axis)

diameter = 12.0


# Base
result = ( 
            cq.Workplane("XY")
            .box(width, height, thickness)
            .faces(">Z")
            .workplane()
            .rect(0, height)
            .hole(diameter, 10)
          
          )

set_port(3939)
show(result)


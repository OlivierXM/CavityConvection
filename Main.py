# Cavity Model #
#
#
#
#
#
#

# Imports #
from fenics import *

# Custom Imports #

# inputs #
nx = ny = 100
length = 1
width = 1

# Mesh and Spaces #
mesh = RectangleMesh(Point(0,0), Point(length,width), nx, ny)
meshDim = mesh.topology().dim()


fe = FiniteElement("CG", mesh.ufl_cell(), degree=1)
ve = VectorElement("CG", mesh.ufl_cell(), degree=1)
me = MixedElement([fe, ve])
V = FunctionSpace(mesh, me)




## END SCRIPT ##

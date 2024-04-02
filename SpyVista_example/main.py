import pyvista as pv
import streamlit as st
from stpyvista import stpyvista

# Initialize a plotter object
plotter = pv.Plotter(window_size=[400, 400])

# Create a mesh with a cube
mesh = pv.Cube(center=(0, 0, 0))

# Add some scalar field associated to the mesh
mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]

# Add mesh to the plotter
plotter.add_mesh(mesh, scalars='myscalar', cmap='bwr')

# Final touches
plotter.view_isometric()
plotter.background_color = 'white'

# Send to streamlit
stpyvista(plotter, key="pv_cube")

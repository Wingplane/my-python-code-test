import vtk
import time

# Read STL
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("wheel5.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("wheel6.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("ballwheel.stl")
reader4 = vtk.vtkSTLReader()
reader4.SetFileName("cframe1.stl")
reader5 = vtk.vtkSTLReader()
reader5.SetFileName("pole.stl")


# Create a mapper and actor
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader3.GetOutputPort())
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputConnection(reader4.GetOutputPort())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputConnection(reader5.GetOutputPort())

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)

# assembly actor5
assembly = vtk.vtkAssembly()
assembly.AddPart(actor5)
assembly.SetOrigin(actor5.GetCenter())

# Setup a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actor to the scene
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(assembly)

renderer.SetBackground(0.2, 0.2, 0.8)  # RGB 0~1

print("actor1 center:", actor1.GetCenter())
print("actor2 center:", actor2.GetCenter())
print("actor3 center:", actor3.GetCenter())

actor1.SetOrigin(-35, 5, 110)
actor2.SetOrigin(-35, 5, -10)
actor3.SetOrigin(-15, 105, 50)

for i in range(36):
    time.sleep(0.1)
    assembly.RotateX(10)
    actor1.RotateZ(10)
    actor2.RotateZ(10)
    actor3.RotateZ(10)
    renderWindow.Render()

renderWindowInteractor.Start()

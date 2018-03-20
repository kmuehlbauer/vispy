import argparse

import numpy as np
import vispy
from vispy import app, scene
from vispy.io import imread, read_mesh
from vispy.scene import SceneCanvas
from vispy.scene.visuals import Mesh
from vispy.visuals.filters import TextureFilter



parser = argparse.ArgumentParser()
parser.add_argument('--mesh', default='./data/spot.obj')
args = parser.parse_args()

vertices, faces, normals, texcoords = read_mesh(args.mesh)
texture = np.flipud(imread(args.mesh.replace(".obj", ".png")))

canvas = scene.SceneCanvas(keys='interactive', bgcolor='white', size=(800, 600))
view = canvas.central_widget.add_view()

view.camera = 'arcball'

shading = None
mesh = Mesh(vertices, faces,
            #texcoords=texcoords,
            shading=shading,
            color='lightgreen')

tex = TextureFilter(texture, texcoords)

view.add(mesh)

canvas.show()


# attaching of isoline filter via timer
def on_timer1(event):
    mesh.attach(tex)
    canvas.update()


timer1 = app.Timer(1., iterations=1, connect=on_timer1, start=True)


if __name__ == "__main__":
    app.run()

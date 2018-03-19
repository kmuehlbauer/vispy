import argparse

import numpy as np
import vispy
from vispy.io import imread, read_mesh
from vispy.scene import SceneCanvas
from vispy.scene.visuals import Mesh
from vispy.visuals.filters import TextureFilter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mesh', default='./data/spot.obj')
    args = parser.parse_args()

    vertices, faces, normals, texcoords = read_mesh(args.mesh)
    texture = np.flipud(imread(args.mesh.replace(".obj", ".png")))

    canvas = SceneCanvas(keys='interactive', bgcolor='white', size=(800, 600))
    view = canvas.central_widget.add_view()

    view.camera = 'arcball'

    shading = None
    mesh = Mesh(vertices, faces, texcoords=texcoords, shading=shading,
                color='white')
    mesh.attach(TextureFilter(texture))
    view.add(mesh)

    canvas.show()
    vispy.app.run()


if __name__ == "__main__":
    main()

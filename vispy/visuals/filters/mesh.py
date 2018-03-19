from vispy.gloo import Texture2D
from vispy.visuals.shaders import Function


class TextureFilter(object):

    def __init__(self, texture):
        self.texture = texture
        self.apply_texture = Function("""
        void apply_texture() {
            gl_FragColor *= texture2D($u_texture, $texcoord);
        }
        """)

    def _attach(self, visual):
        frag_post = visual._get_hook('frag', 'post')
        frag_post.add(self.apply_texture())
        self.apply_texture['texcoord'] = \
            visual.shared_program.vert['v_texcoord']
        self.apply_texture['u_texture'] = Texture2D(self.texture)

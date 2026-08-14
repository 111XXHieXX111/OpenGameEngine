#version 330

in vec2 uv;
in vec4 color;
out vec4 frag_color;

uniform sampler2D tex;
uniform int use_tex;

void main() {
    if (use_tex == 0) {
        frag_color = color;
    } else {
        frag_color = texture(tex, uv) * color;
    }
}
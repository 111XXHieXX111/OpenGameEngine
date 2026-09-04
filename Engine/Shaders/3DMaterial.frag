#version 330

in vec2 uv;
in vec4 color;
in vec3 normal;
in vec3 frag_position;

out vec4 frag_color;

uniform sampler2D tex;
uniform int use_tex;
uniform vec3 ambient_light;
uniform vec3 light_position;
uniform vec3 light_color;

void main() {
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_position - frag_position);
    float diff = max(0.0, dot(norm, light_dir));
    
    vec4 ambient_color = vec4(ambient_light * color.rgb, color.a);
    vec4 diffuse_color = vec4(diff * light_color * color.rgb, color.a);
    vec4 out_color = ambient_color + diffuse_color;

    if (use_tex == 0) {
        frag_color = out_color;
    } else {
        frag_color = texture(tex, uv) * out_color;
    }
}
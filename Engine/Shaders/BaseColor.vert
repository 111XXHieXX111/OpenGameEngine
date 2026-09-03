#version 330

layout(location = 0) in vec3 vertex_position;
layout(location = 1) in vec2 vertex_uv;

out vec4 color;
out vec2 uv;

uniform vec4 vertex_color;
uniform mat4 camera_matrix;
uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;
uniform int camera;

void main() {
	color = vertex_color;
	uv = vertex_uv;

	if (camera == 1) {
		gl_Position = camera_matrix * model * vec4(vertex_position, 1.0);
	} else if (camera == 2) {
		gl_Position = proj * view * model * vec4(vertex_position, 1.0);
	}	
}
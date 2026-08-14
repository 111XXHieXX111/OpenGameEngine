#version 330

layout(location = 0) in vec3 vertex_position;
layout(location = 1) in vec4 vertex_color;
out vec4 color;

uniform mat4 camera_matrix;

void main() {
	color = vertex_color;
	gl_Position = camera_matrix * vec4(vertex_position, 1.0);
}
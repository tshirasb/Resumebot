from typing import Dict
import json

from jinja2 import Template


def read_resume_json(json_file_path: str) -> Dict:
    with open(json_file_path, 'r') as json_file:
        parsed = json.load(json_file)

    return parsed


def template_from_file_path(template_file_path: str) -> Template:
    with open(template_file_path, 'r') as template_file:
        raw_template = template_file.read()

    return Template(raw_template)


def render_resume(json_file_path: str, template_file_path: str, output_tex_file_path: str) -> None:
    resume_json = read_resume_json(json_file_path)
    template = template_from_file_path(template_file_path)

    rendered_tex = template.render(resume_json)

    with open(output_tex_file_path, 'w') as output_tex_file:
        output_tex_file.write(rendered_tex)


if __name__ == '__main__':
    render_resume(
        "resume.json",
        "templates/resume.tex.jinja2",
        "tuna.tex"
    )

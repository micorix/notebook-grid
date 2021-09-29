import inquirer
import re
from grid import default_grid_config, save_svg_to_bitmap_file, generate_grid_svg_code


def validate_number(_, val):
    return val.isnumeric()


questions = [
    inquirer.Text(
        "canvas_width",
        message="Canvas width",
        default=default_grid_config.get("canvas_width"),
        validate=validate_number,
    ),
    inquirer.Text(
        "canvas_height",
        message="Canvas height",
        default=default_grid_config.get("canvas_height"),
        validate=validate_number,
    ),
    inquirer.Text(
        "bg_color",
        message="Background color (HTML color name/hex/rgb(r,g,b)",
        default=default_grid_config.get("bg_color"),
    ),
    inquirer.Text(
        "fg_color",
        message="Line color (HTML color name/hex/rgb(r,g,b)",
        default=default_grid_config.get("fg_color"),
    ),
    inquirer.Text(
        "line_weight",
        message="Line weight",
        default=default_grid_config.get("line_weight"),
        validate=validate_number,
    ),
    inquirer.Text(
        "spacing",
        message="Spacing",
        default=default_grid_config.get("spacing"),
        validate=validate_number,
    ),
    inquirer.Confirm(
        "show_small_grid",
        message="Show inner grid",
        default=default_grid_config.get("show_small_grid"),
    ),
]


def get_grid_config():
    return inquirer.prompt(questions)


if __name__ == "__main__":
    svg_code = generate_grid_svg_code(get_grid_config())
    save_svg_to_bitmap_file(svg_code)
    print("Grid has been generated.")

from cairosvg import svg2png


def generate_grid_svg_code(grid_config):
    derived_from_grid_config = {
        "small_grid_spacing": float(grid_config.get("spacing")) / 10,
        "small_grid_line_weight": float(grid_config.get("line_weight")) / 2,
    }

    context_dict = {**grid_config, **derived_from_grid_config}

    svg_code = """
     <svg width="{canvas_width}" height="{canvas_height}" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <pattern id="smallGrid" width="{small_grid_spacing}" height="{small_grid_spacing}" patternUnits="userSpaceOnUse">
                <path d="M {small_grid_spacing} 0 L 0 0 0 {small_grid_spacing}" fill="none" stroke="{fg_color}" stroke-width="{small_grid_line_weight}"/>
            </pattern>
            <pattern id="grid" width="{spacing}" height="{spacing}" patternUnits="userSpaceOnUse">
     """.format(
        **context_dict
    )

    if grid_config.get("show_small_grid") is True:
        svg_code += (
            '<rect width="{spacing}" height="{spacing}" fill="url(#smallGrid)"/>'
        ).format(**context_dict)

    svg_code += """
          <path d="M {spacing} 0 L 0 0 0 {spacing}" fill="none" stroke="{fg_color}" stroke-width="{line_weight}"/>
         </pattern>
        </defs>
       <rect width="{canvas_width}" height="{canvas_height}" fill="{bg_color}" />
       <rect width="{canvas_width}" height="{canvas_height}" fill="url(#grid)" />
        </svg>
    """.format(
        **context_dict
    )
    return svg_code


def save_svg_to_bitmap_file(svg_code):
    svg2png(bytestring=svg_code, write_to="output.png")


default_grid_config = {
    "show_small_grid": False,
    "canvas_width": 1920,
    "canvas_height": 1080,
    "bg_color": "white",
    "fg_color": "black",
    "line_weight": 1,
    "spacing": 100,
}

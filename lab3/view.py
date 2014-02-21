from quik import FileLoader


def render_template(template_file, **kwargs):
    """ Render a template and display it in stdout

    @param template_file: template filepath
    @param kwargs: key/value pairs of data to be rendered
    """
    loader = FileLoader('')
    template = loader.load_template(template_file)
    print template.render(kwargs, loader=loader)

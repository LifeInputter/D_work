__all__ = (
    "templates",
    "TemplateResponse"
)

import os

from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))
TemplateResponse = templates.TemplateResponse
#!/usr/bin/env python

from decouple import config
from fasthtml.common import *
from pathlib import Path
from textwrap import dedent


PORT = config('PORT', default=8000, cast=int)
RELOAD = config('RELOAD', default=True, cast=bool)

css = Path("static/styles.css").read_text()
# javascript = Path("static/script.js").read_text()

hdrs = (
    Link(rel='stylesheet', href='static/normalize.css', type='text/css'),
    Link(rel='stylesheet', href='static/sakura.css', type='text/css'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css', type='text/css'),
    HighlightJS(langs=['python', 'javascript', 'html', 'css']),
    Style(css),
    # Script(javascript),
)

app, rt = fast_app(
    static_path='static',
    hdrs=hdrs,
    pico=False,
)


@rt("/")
def get():
    main_content = Main(
        Div(
            Nav(
                A("Home", href="/"),
                A("About", href="/about"),
                A("Events", href="/events"),
                A("Contact", href="/contact"),
            ),
            Titled(
                "Pythonistas",
                P("Let's do this!")
            )
        )
    )

    return main_content


if __name__ == "__main__":
    serve(appname='main',
          app='app',
          host='0.0.0.0',
          port=PORT,
          reload=RELOAD
    )

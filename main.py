#!/usr/bin/env python

from fasthtml.common import *
from textwrap import dedent

hdrs = (
    Link(rel='stylesheet', href='static/normalize.css', type='text/css'),
    # Link(rel='stylesheet', href='static/sakura.css', type='text/css'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css', type='text/css'),
    # Style("p {color: red;}"),
    HighlightJS(langs=['python', 'javascript', 'html', 'css']),
)

app, rt = fast_app(
    static_path='static',
    hdrs=hdrs,
    pico=False,
)

@rt("/")
def get():
  return Titled("FastHTML", P("Let's do this!"))

@rt("/hello")
def get():
  return Titled("Hello, world!")

@rt("/markdown")
def get(req):
    code_example = dedent("""
    import datetime
    import time

    for i in range(10):
        print(f"{datetime.datetime.now()}")
        time.sleep(1)
    """)
    return Titled(
       "Markdown rendering example",
        Div(
            Pre(Code(code_example))
        )
    )

serve()

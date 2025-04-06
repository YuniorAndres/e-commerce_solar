"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Bienvenido a Solar Store 🌞", size="9"),
            rx.text("Encuentra los mejores paneles solares al mejor precio."),
            rx.button("Ver productos", on_click=rx.redirect("/productos")),
            spacing="4",
            padding="8",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)

"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config



def navbar():
    return rx.hstack(
        rx.image(src="/logo.png", width="60px", height="60px"),  # Puedes cambiar el logo
        rx.spacer(),
        rx.link("Inicio", href="/"),
        rx.link("Productos", href="/productos"),
        rx.link("Contacto", href="/contacto"),
        rx.link("Mi cuenta", href="/cuenta"),
        rx.link("Carrito", href="/carrito"),
        spacing="6",
        padding="2",
        align="center",
    )


def hero_section():
    return rx.center(
        rx.vstack(
            rx.heading("Energía solar para un futuro sostenible", size="8"),
            rx.button("Ver paneles", size="4", on_click=rx.redirect("/productos")),
            spacing="4",
        ),
        padding_y="8",
        bg="gray.100",
        min_height="50vh"
    )


def search_section():
    return rx.hstack(
        rx.text("Filtro o búsqueda:"),
        rx.input(placeholder="Tipo"),
        rx.input(placeholder="Buscar"),
        rx.button("Buscar"),
        spacing="3",
        padding="4",
    )


def product_card(nombre: str, precio: str):
    return rx.box(
        rx.vstack(
            rx.box("Imagen del panel", bg="gray.200", height="100px", width="100%"),
            rx.text(nombre, weight="bold"),
            rx.text(f"{precio} USD"),
            rx.button("Añadir al carrito"),
            spacing="2",
        ),
        border="1px solid #ccc",
        border_radius="md",
        padding="4",
        width="30%",
    )


def products_section():
    return rx.hstack(
        product_card("Panel Solar Modelo X", "399.00"),
        product_card("Panel Solar Modelo Y", "449.00"),
        product_card("Panel Solar Modelo Z", "349.00"),
        spacing="4",
        padding="4",
        justify="center"
    )


def footer():
    return rx.vstack(
        rx.hstack(
            rx.text("Información de contacto"),
            rx.text("Enlaces rápidos"),
            rx.text("Redes sociales"),
            spacing="6",
            padding_y="2",
        ),
        rx.divider(),
        rx.text("© 2025 Solar Store. Todos los derechos reservados."),
        padding="4",
        align="center",
        font_size="sm"
    )


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        hero_section(),
        search_section(),
        products_section(),
        footer(),
        spacing="6"
    )

app = rx.App()
app.add_page(index)

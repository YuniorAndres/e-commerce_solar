import reflex as rx
from rxconfig import config

# -------- NAVBAR --------
def navbar():
    return rx.hstack(
        rx.image(src="/logo.png", width="60px", height="60px"),
        rx.spacer(),
        rx.link("Inicio", href="/"),
        rx.link("Productos", href="/productos"),
        rx.link("Contacto", href="/contacto"),
        rx.link("Mi cuenta", href="/cuenta"),
        rx.link("Carrito", href="/carrito"),
        spacing="6",
        padding="2",
        align="center",
        bg="blue.600",
        color="white"
    )


# -------- HERO SECTION --------
def hero_section():
    return rx.center(
        rx.vstack(
            rx.heading("Energía solar para un futuro sostenible", size="8", color="blue.700"),
            rx.button("Ver paneles", size="4", on_click=rx.redirect("/productos"), color_scheme="blue"),
            spacing="4",
        ),
        padding_y="8",
        bg="blue.50",
        min_height="50vh"
    )


# -------- SEARCH BAR --------
def search_section():
    return rx.hstack(
        rx.text("Buscar paneles:", color="blue.700"),
        rx.input(placeholder="Tipo", width="25%"),
        rx.input(placeholder="Buscar", width="25%"),
        rx.button("Buscar", color_scheme="blue"),
        spacing="3",
        padding="4",
        justify="center",
    )


# -------- PRODUCT CARD --------
def product_card(nombre: str, precio: str):
    return rx.box(
        rx.vstack(
            rx.box("Imagen del panel", bg="blue.100", height="100px", width="100%"),
            rx.text(nombre, weight="bold", color="blue.800"),
            rx.text(f"${precio} USD", color="blue.600"),
            rx.button("Añadir al carrito", color_scheme="blue"),
            spacing="2",
        ),
        border="1px solid #cbd5e0",
        border_radius="md",
        padding="4",
        width="300px",
        box_shadow="md",
        bg="white"
    )


# -------- PRODUCTS SECTION --------
def products_section():
    return rx.flex(
        product_card("Panel Solar Modelo X", "399.00"),
        product_card("Panel Solar Modelo Y", "449.00"),
        product_card("Panel Solar Modelo Z", "349.00"),
        spacing="4",
        padding="4",
        wrap="wrap",
        justify="center"
    )


# -------- FOOTER --------
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
        font_size="sm",
        bg="blue.600",
        color="white"
    )


# -------- INDEX PAGE --------
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        hero_section(),
        search_section(),
        products_section(),
        footer(),
        spacing="6",
        bg="gray.50"  # Claro, fijo

    )


# -------- APP --------
app = rx.App()
app.add_page(index)

# frontend/state.py
import reflex as rx
import httpx

class ProductState(rx.State):
    products: list[dict] = []

    async def fetch_products(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8000/api/products/")
                if response.status_code == 200:
                    self.products = response.json()
        except Exception as e:
            print("Error fetching products:", e)

    async def on_load(self):
        await self.fetch_products()

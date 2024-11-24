from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Setup for templates
templates = Jinja2Templates(directory="templates")

# Static files for images
app.mount("/static", StaticFiles(directory="static"), name="static")

# List of 50 plants with images and details
plants = [
    {"name": "Aloe Vera", "description": "A succulent plant famous for its medicinal properties.", "price": "22.82", "image": "Aloe Vera.webp"},
    {"name": "Basil", "description": "A culinary herb cherished for its aromatic leaves.", "price": "14.98", "image": "Basil.webp"},
    {"name": "Cactus", "description": "A desert-dwelling plant that stores water in its spiny stems.", "price": "9.95", "image": "Cactus.webp"},
    {"name": "Lavender", "description": "A fragrant flowering plant with calming properties.", "price": "16.86", "image": "Lavender.webp"},
    {"name": "Snake Plant", "description": "An air-purifying indoor plant with striking upright leaves.", "price": "21.77", "image": "Snake Plant.webp"},
    {"name": "Spider Plant", "description": "A fast-growing houseplant with cascading green and white leaves.", "price": "15.15", "image": "Spider Plant.webp"},
    {"name": "Peace Lily", "description": "A tropical beauty known for its elegant white flowers.", "price": "20.23", "image": "Peace Lily.webp"},
    {"name": "Fiddle Leaf Fig", "description": "A trendy houseplant with large, violin-shaped leaves.", "price": "7.59", "image": "Fiddle Leaf Fig.webp"},
    {"name": "Money Tree", "description": "An indoor plant symbolizing prosperity, with braided trunks.", "price": "22.03", "image": "Money Tree.webp"},
    {"name": "Orchid", "description": "An exotic plant with delicate and colorful blooms.", "price": "23.46", "image": "Orchid.webp"},
    {"name": "Rosemary", "description": "A hardy herb with needle-like leaves, offering culinary benefits.", "price": "21.12", "image": "Rosemary.webp"},
    {"name": "Thyme", "description": "A versatile herb with small, fragrant leaves, essential for cooking.", "price": "26.87", "image": "Thyme.webp"},
    {"name": "Mint", "description": "A refreshing and fast-growing herb, great for teas and cocktails.", "price": "23.76", "image": "Mint.webp"},
    {"name": "Fern", "description": "A lush green plant with soft, feathery fronds.", "price": "25.45", "image": "Fern.webp"},
    {"name": "Succulent", "description": "A resilient plant with thick, fleshy leaves, perfect for minimalistic decor.", "price": "26.12", "image": "Succulent.webp"},
    {"name": "Bamboo", "description": "A fast-growing plant with tall, elegant stems.", "price": "23.2", "image": "Bamboo.webp"},
    {"name": "Palm", "description": "A tropical plant with broad, fan-like leaves.", "price": "20.4", "image": "Palm.webp"},
    {"name": "Ivy", "description": "A trailing plant that climbs walls or hangs beautifully in pots.", "price": "5.64", "image": "Ivy.webp"},
    {"name": "Jasmine", "description": "A flowering plant with sweet-smelling blossoms, used in perfumes.", "price": "15.8", "image": "Jasmine.webp"},
    {"name": "Gardenia", "description": "A classic plant with fragrant white flowers.", "price": "18.12", "image": "Gardenia.webp"},
    {"name": "Daffodil", "description": "A cheerful spring-flowering bulb with bright yellow petals.", "price": "12.22", "image": "Daffodil.webp"},
    {"name": "Tulip", "description": "A timeless flower with vibrant colors, perfect for gardens.", "price": "12.53", "image": "Tulip.webp"},
    {"name": "Sunflower", "description": "A tall and striking flower that follows the sun.", "price": "26.73", "image": "Sunflower.webp"},
    {"name": "Daisy", "description": "A simple yet charming flower with white petals.", "price": "25.2", "image": "Daisy.webp"},
    {"name": "Hydrangea", "description": "A bushy plant with large, colorful flower clusters.", "price": "24.26", "image": "Hydrangea.webp"},
    {"name": "Lilac", "description": "A fragrant flowering shrub with pastel blooms.", "price": "14.48", "image": "Lilac.webp"},
    {"name": "Marigold", "description": "A vibrant flower with bright orange or yellow petals.", "price": "5.81", "image": "Marigold.webp"},
    {"name": "Petunia", "description": "A colorful annual flower perfect for hanging baskets.", "price": "7.28", "image": "Petunia.webp"},
    {"name": "Begonia", "description": "A versatile plant with vibrant blooms and glossy leaves.", "price": "12.4", "image": "Begonia.webp"},
    {"name": "Poinsettia", "description": "A festive plant with bright red and green foliage.", "price": "5.86", "image": "Poinsettia.webp"},
    {"name": "Bougainvillea", "description": "A tropical vine with cascades of colorful bracts.", "price": "5.89", "image": "Bougainvillea.webp"},
    {"name": "Chrysanthemum", "description": "A symbol of autumn, known for its variety of colors.", "price": "25.75", "image": "Chrysanthemum.webp"},
    {"name": "Hibiscus", "description": "A tropical flowering plant with large, showy blooms.", "price": "21.1", "image": "Hibiscus.webp"},
    {"name": "Zinnia", "description": "A hardy annual with bright, daisy-like flowers.", "price": "12.33", "image": "Zinnia.webp"},
    {"name": "Geranium", "description": "A classic flowering plant with clusters of colorful blooms.", "price": "8.44", "image": "Geranium.webp"},
    {"name": "Anthurium", "description": "An exotic plant with waxy, heart-shaped flowers.", "price": "16.81", "image": "Anthurium.webp"},
    {"name": "Carnation", "description": "A fragrant flower with ruffled petals, popular in bouquets.", "price": "5.63", "image": "Carnation.webp"},
    {"name": "Foxglove", "description": "A tall, stately plant with tubular flowers.", "price": "26.23", "image": "Foxglove.webp"},
    {"name": "Poppy", "description": "A delicate wildflower with paper-thin petals.", "price": "14.67", "image": "Poppy.webp"},
    {"name": "Snapdragon", "description": "A playful flowering plant with colorful blooms.", "price": "14.39", "image": "Snapdragon.webp"},
    {"name": "Camellia", "description": "An elegant shrub with large, rose-like flowers.", "price": "14.14", "image": "Camellia.webp"},
    {"name": "Azalea", "description": "A flowering shrub with bright blooms, thriving in acidic soil.", "price": "7.04", "image": "Azalea.webp"},
    {"name": "Magnolia", "description": "A grand tree with large, fragrant flowers.", "price": "19.6", "image": "Magnolia.webp"},
    {"name": "Freesia", "description": "A fragrant flower with graceful stems, perfect for bouquets.", "price": "21.7", "image": "Freesia.webp"},
    {"name": "Gladiolus", "description": "A striking flower with tall spikes, ideal for garden borders.", "price": "20.44", "image": "Gladiolus.webp"}
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Affiche toutes les plantes par défaut
    return templates.TemplateResponse("index.html", {"request": request, "plants": plants, "query": ""})

@app.post("/", response_class=HTMLResponse)
async def search_plants(request: Request, plant_name: str = Form(...)):
    # Filtrer les plantes en fonction du nom saisi
    filtered_plants = [
        plant for plant in plants if plant_name.lower() in plant["name"].lower()
    ]
    return templates.TemplateResponse("index.html", {"request": request, "plants": filtered_plants, "query": plant_name})

@app.get("/plant_details/{plant_name}", response_class=HTMLResponse)
async def plant_details(request: Request, plant_name: str):
    # Rechercher la plante correspondante
    plant = next((plant for plant in plants if plant["name"] == plant_name), None)
    if not plant:
        return templates.TemplateResponse(
            "404.html", {"request": request, "message": f"Plant '{plant_name}' not found."}
        )
    return templates.TemplateResponse("plant_details.html", {"request": request, "plant": plant})

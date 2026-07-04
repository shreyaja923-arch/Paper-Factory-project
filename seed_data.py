import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaperFactory.settings')
django.setup()

from core.models import Category, Product

def seed():
    print("Seeding database...")
    
    # 1. Clear existing products to prevent duplicates
    Product.objects.all().delete()
    Category.objects.all().delete()
    
    # 2. Create Categories
    cat_kraft, _ = Category.objects.get_or_create(
        name="Kraft Board",
        description="High-strength, durable wrapping and structural board paper."
    )
    
    cat_corrugating, _ = Category.objects.get_or_create(
        name="Corrugating Medium",
        description="Fluting medium paper designed to provide compression resistance in boxes."
    )
    
    cat_duplex, _ = Category.objects.get_or_create(
        name="Duplex Board",
        description="Multi-layered coated board paper used for retail packaging and cartons."
    )
    
    print("Categories created successfully!")
    
    # 3. Create Products
    products_data = [
        {
            "name": "Kraft Liner Board",
            "category": cat_kraft,
            "description": "Premium virgin-fiber liner board engineered for heavy-duty corrugated box packaging, offering excellent burst factor resistance.",
            "gsm": "120 - 250 GSM",
            "size": "Deckle 2400mm / Width Custom",
            "availability": True
        },
        {
            "name": "Ribbed Kraft Paper",
            "category": cat_kraft,
            "description": "High-durability wrapping paper with a distinct ribbed finish, ideal for carrier bags, envelope manufacturing, and decorative packaging.",
            "gsm": "70 - 100 GSM",
            "size": "Sheets & Rolls / Width Custom",
            "availability": True
        },
        {
            "name": "Fluting Medium Standard",
            "category": cat_corrugating,
            "description": "Standard recycled-fiber corrugating medium that provides optimal structural rigidity and cushion resistance for carton layers.",
            "gsm": "110 - 150 GSM",
            "size": "Deckle 2200mm / Width Custom",
            "availability": True
        },
        {
            "name": "High-Performance Fluting",
            "category": cat_corrugating,
            "description": "Extra-strength corrugating medium treated with chemical bonding agents to resist moisture and high compressive loads.",
            "gsm": "140 - 180 GSM",
            "size": "Deckle 2200mm / Width Custom",
            "availability": True
        },
        {
            "name": "White-Back Coated Duplex",
            "category": cat_duplex,
            "description": "Gloss-finished duplex board with a white back, providing premium printability for cosmetics, pharmaceutical boxes, and high-end retail displays.",
            "gsm": "230 - 450 GSM",
            "size": "Sheets 700x1000mm / Rolls Custom",
            "availability": True
        },
        {
            "name": "Grey-Back Duplex Board",
            "category": cat_duplex,
            "description": "Standard packaging board with a grey back, commonly used for shoe boxes, toy boxes, and folded cartons requiring good stiffness.",
            "gsm": "200 - 400 GSM",
            "size": "Sheets 700x1000mm / Rolls Custom",
            "availability": True
        }
    ]
    
    for p_data in products_data:
        Product.objects.create(**p_data)
        
    print("Products seeded successfully!")
    print("Database seeding completed.")

if __name__ == '__main__':
    seed()

from pymongo import MongoClient
from config import Config  # Import your existing config

def populate_products():
    """Populate MongoDB with sample products"""
    
    sample_products = [
        {
            "_id": "p101",
            "name": "iPhone 14",
            "brand": "Apple",
            "category": "smartphone",
            "description": "Powerful A15 Bionic chip, 6.1-inch Super Retina display",
            "price": 799,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p102",
            "name": "MacBook Pro 14",
            "brand": "Apple",
            "category": "laptop",
            "description": "M2 Pro chip, 14-inch Liquid Retina XDR display",
            "price": 1999,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p103",
            "name": "Samsung Galaxy S23",
            "brand": "Samsung",
            "category": "smartphone",
            "description": "Snapdragon 8 Gen 2, 6.1-inch Dynamic AMOLED display",
            "price": 699,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p104",
            "name": "AirPods Pro",
            "brand": "Apple",
            "category": "headphones",
            "description": "Active Noise Cancellation, Spatial Audio",
            "price": 249,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p105",
            "name": "Dell XPS 13",
            "brand": "Dell",
            "category": "laptop",
            "description": "Intel Core i7, 13.4-inch InfinityEdge display",
            "price": 1299,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p106",
            "name": "Sony WH-1000XM4",
            "brand": "Sony",
            "category": "headphones",
            "description": "Industry-leading noise canceling, 30-hour battery life",
            "price": 349,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p107",
            "name": "iPad Air",
            "brand": "Apple",
            "category": "tablet",
            "description": "M1 chip, 10.9-inch Liquid Retina display",
            "price": 599,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p108",
            "name": "Samsung Galaxy Tab S8",
            "brand": "Samsung",
            "category": "tablet",
            "description": "Snapdragon 8 Gen 1, 11-inch LTPS TFT display",
            "price": 699,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p109",
            "name": "HP Spectre x360",
            "brand": "HP",
            "category": "laptop",
            "description": "Intel Core i7, 13.5-inch OLED touchscreen",
            "price": 1499,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p110",
            "name": "Google Pixel 7",
            "brand": "Google",
            "category": "smartphone",
            "description": "Google Tensor G2, 6.3-inch OLED display",
            "price": 599,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p111",
            "name": "Nintendo Switch OLED",
            "brand": "Nintendo",
            "category": "gaming",
            "description": "7-inch OLED screen, enhanced audio",
            "price": 349,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        },
        {
            "_id": "p112",
            "name": "Apple Watch Series 8",
            "brand": "Apple",
            "category": "smartwatch",
            "description": "Advanced health sensors, Always-On Retina display",
            "price": 399,
            "img": "https://images.unsplash.com/photo-1613336026275-d6d473084e85?fm=jpg"
        }
    ]
    
    try:
        print("🔗 Connecting to MongoDB...")
        
        # Use your existing config
        client = MongoClient(Config.MONGODB_URI)
        db = client["ecommerce"]
        products_collection = db["products"]
        
        print("✅ Connected to MongoDB successfully!")
        
        # Check existing products
        existing_count = products_collection.count_documents({})
        print(f"📊 Existing products in database: {existing_count}")
        
        # Insert products
        print("📦 Inserting sample products...")
        
        inserted_count = 0
        skipped_count = 0
        
        for product in sample_products:
            try:
                products_collection.insert_one(product)
                inserted_count += 1
                print(f"  ✅ Inserted: {product['name']}")
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    skipped_count += 1
                    print(f"  ⚠️  Skipped (already exists): {product['name']}")
                else:
                    print(f"  ❌ Error inserting {product['name']}: {str(e)}")
        
        print(f"\n📈 Summary:")
        print(f"  • Inserted: {inserted_count} products")
        print(f"  • Skipped: {skipped_count} products")
        
        # Final count
        total_count = products_collection.count_documents({})
        print(f"📊 Total products in database: {total_count}")
        
        # Show sample products
        print(f"\n📋 Sample products in database:")
        sample_docs = list(products_collection.find({}).limit(5))
        for i, doc in enumerate(sample_docs, 1):
            print(f"  {i}. {doc['name']} by {doc['brand']} - ${doc['price']}")
        
        client.close()
        print("\n✨ Products populated successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        
        if "connection" in str(e).lower():
            print("\n🔧 Connection troubleshooting:")
            print("1. Check your MongoDB connection string in config.py")
            print("2. Ensure your MongoDB server is running")
            print("3. Check your internet connection (if using MongoDB Atlas)")
            print("4. Verify your MongoDB credentials")

if __name__ == "__main__":
    print("🚀 Starting product population script...")
    populate_products()
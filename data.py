import mysql.connector
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/cooking_recipe'
db = SQLAlchemy(app)
# JSON data
data = {
    "recipes": [
        {
            "id": 1,
            "title": "Chicken Curry",
            "images": "images/chicken_curry.jpg",
            "instructions": "1. Heat oil in a pan. 2. Add onions and sauté until golden. 3. Add ginger-garlic paste, followed by tomatoes. 4. Cook until tomatoes are soft. 5. Add chicken and spices. 6. Cook until chicken is tender. 7. Garnish with cilantro and serve."
        },
        {
            "id": 2,
            "title": "Paneer Butter Masala",
            "images": "images/panner_butter_masala.jpg",
            "instructions": "1. Heat butter in a pan. 2. Add onions and sauté until translucent. 3. Add tomatoes and cook until soft. 4. Blend the mixture into a smooth paste. 5. Add paneer cubes and spices. 6. Cook until paneer is well-coated. 7. Garnish with cream and serve."
        },
        {
            "id": 3,
            "title": "Chole Bhature",
            "images": "images/chola_bhature.jpg",
            "instructions": "1. Soak chickpeas overnight. 2. Cook chickpeas with spices until tender. 3. Prepare bhature dough and let it rest. 4. Roll out dough and deep fry. 5. Serve bhature with chole."
        },
        {
            "id": 4,
            "title": "Aloo Gobi",
            "images": "images/aloo_gobi.jpg",
            "instructions": "1. Heat oil in a pan. 2. Add cumin seeds and let them splutter. 3. Add potatoes and cauliflower. 4. Add spices and cook until vegetables are tender. 5. Garnish with cilantro and serve."
        },
        {
            "id": 5,
            "title": "Palak Paneer",
            "images": "images/palak_panner.jpg",
            "instructions": "1. Blanch spinach leaves and blend into a paste. 2. Heat oil and add cumin seeds. 3. Add onions, tomatoes, and cook until soft. 4. Add spinach paste and paneer cubes. 5. Cook until well-mixed and serve."
        },
        {
            "id": 6,
            "title": "Rajma",
            "images": "images/rajma.jpg",
            "instructions": "1. Soak kidney beans overnight. 2. Cook beans with spices until tender. 3. Prepare a tomato-onion gravy. 4. Mix beans with gravy and cook until thickened. 5. Garnish with cilantro and serve."
        },
        {
            "id": 7,
            "title": "Dal Tadka",
            "images": "images/dal_tadka.jpg",
            "instructions": "1. Cook lentils with turmeric and salt. 2. Prepare a tempering of garlic, onions, and spices. 3. Mix tempering with cooked dal. 4. Garnish with cilantro and serve."
        },
        {
            "id": 8,
            "title": "Bhindi Masala",
            "images": "images/bhindhi_masala.jpg",
            "instructions": "1. Heat oil in a pan. 2. Add cumin seeds and let them splutter. 3. Add sliced okra and cook until tender. 4. Add spices and mix well. 5. Serve hot."
        },
        {
            "id": 9,
            "title": "Dosa",
            "images": "images/dosa.jpg",
            "instructions": "1. Soak rice and urad dal overnight. 2. Grind to a smooth batter. 3. Heat a griddle and pour batter to form a thin layer. 4. Cook until crisp and golden. 5. Serve with chutney and sambar."
        },
        {
            "id": 10,
            "title": "Pulao",
            "images": "images/pulao.jpg",
            "instructions": "1. Heat oil and sauté onions and spices. 2. Add rice and vegetables. 3. Cook with water until rice is fluffy. 4. Garnish with cilantro and serve."
        }
    ],
    "ingredients": [
        {
            "id": 1,
            "ingredient_name": "Chicken"
        },
        {
            "id": 2,
            "ingredient_name": "Paneer"
        },
        {
            "id": 3,
            "ingredient_name": "Chickpeas"
        },
        {
            "id": 4,
            "ingredient_name": "Potatoes"
        },
        {
            "id": 5,
            "ingredient_name": "Spinach"
        },
        {
            "id": 6,
            "ingredient_name": "Kidney Beans"
        },
        {
            "id": 7,
            "ingredient_name": "Lentils"
        },
        {
            "id": 8,
            "ingredient_name": "Okra"
        },
        {
            "id": 9,
            "ingredient_name": "Rice"
        },
        {
            "id": 10,
            "ingredient_name": "Vegetables"
        },
        {
            "id": 11,
            "ingredient_name": "Cilantro"
        },
        {
            "id": 12,
            "ingredient_name": "Turmeric"
        },
        {
            "id": 13,
            "ingredient_name": "Cumin Seeds"
        },
        {
            "id": 14,
            "ingredient_name": "Garam Masala"
        },
        {
            "id": 15,
            "ingredient_name": "Red Chili Powder"
        },
        {
            "id": 16,
            "ingredient_name": "Coriander Powder"
        },
        {
            "id": 17,
            "ingredient_name": "Yogurt"
        },
        {
            "id": 18,
            "ingredient_name": "Fenugreek Leaves"
        },
        {
            "id": 19,
            "ingredient_name": "Bay Leaf"
        },
        {
            "id": 20,
            "ingredient_name": "Cinnamon Stick"
        },
        {
            "id": 21,
            "ingredient_name": "Cloves"
        },
        {
            "id": 22,
            "ingredient_name": "Green Cardamom"
        },
        {
            "id": 23,
            "ingredient_name": "Mustard Seeds"
        },
        {
            "id": 24,
            "ingredient_name": "Coconut Milk"
        },
        {
            "id": 25,
            "ingredient_name": "Green Chilies"
        },
        {
            "id": 26,
            "ingredient_name": "Tamarind"
        },
        {
            "id": 27,
            "ingredient_name": "Curry Leaves"
        },
        {
            "id": 28,
            "ingredient_name": "Black Pepper"
        },
        {
            "id": 29,
            "ingredient_name": "Ghee"
        },
        {
            "id": 30,
            "ingredient_name": "Mint Leaves"
        }
    ],
    "recipe_ingredient": [
        {
            "id": 1,
            "recipe_id": 1,
            "ingredient_id": 1,
            "quantity": 500,
            "units": "grams"
        },
        {
            "id": 2,
            "recipe_id": 1,
            "ingredient_id": 13,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 3,
            "recipe_id": 1,
            "ingredient_id": 12,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 4,
            "recipe_id": 1,
            "ingredient_id": 14,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 5,
            "recipe_id": 2,
            "ingredient_id": 2,
            "quantity": 250,
            "units": "grams"
        },
        {
            "id": 6,
            "recipe_id": 2,
            "ingredient_id": 13,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 7,
            "recipe_id": 2,
            "ingredient_id": 24,
            "quantity": 200,
            "units": "ml"
        },
        {
            "id": 8,
            "recipe_id": 3,
            "ingredient_id": 3,
            "quantity": 200,
            "units": "grams"
        },
        {
            "id": 9,
            "recipe_id": 4,
            "ingredient_id": 4,
            "quantity": 300,
            "units": "grams"
        },
        {
            "id": 10,
            "recipe_id": 4,
            "ingredient_id": 13,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 11,
            "recipe_id": 5,
            "ingredient_id": 5,
            "quantity": 500,
            "units": "grams"
        },
        {
            "id": 12,
            "recipe_id": 5,
            "ingredient_id": 2,
            "quantity": 200,
            "units": "grams"
        },
        {
            "id": 13,
            "recipe_id": 6,
            "ingredient_id": 6,
            "quantity": 200,
            "units": "grams"
        },
        {
            "id": 14,
            "recipe_id": 7,
            "ingredient_id": 7,
            "quantity": 200,
            "units": "grams"
        },
        {
            "id": 15,
            "recipe_id": 8,
            "ingredient_id": 8,
            "quantity": 250,
            "units": "grams"
        },
        {
            "id": 16,
            "recipe_id": 9,
            "ingredient_id": 9,
            "quantity": 200,
            "units": "grams"
        },
        {
            "id": 17,
            "recipe_id": 10,
            "ingredient_id": 10,
            "quantity": 150,
            "units": "grams"
        },
        {
            "id": 18,
            "recipe_id": 10,
            "ingredient_id": 13,
            "quantity": 1,
            "units": "tsp"
        },
        {
            "id": 19,
            "recipe_id": 10,
            "ingredient_id": 14,
            "quantity": 1,
            "units": "tsp"
        }
    ]
}

def add_ingredients_to_recipes():
    recipe_ingredients = [
        (6, 11, '1', 'cup'),         
        (6, 12, '2', 'tbsp'),
        (7, 13, '2', 'tsp'),        
        (7, 14, '1', 'cup'),
        (8, 15, '100', 'grams'),    
        (8, 16, '2', 'pieces'),
        (9, 17, '500', 'ml'),       
        (9, 18, '1', 'tsp'),
        (10, 19, '3', 'pieces'),    
        (10, 20, '200', 'grams')
    ]

    with app.app_context():
        for recipe_id, ingredient_id, quantity, units in recipe_ingredients:
            db.session.execute(
                text("""
                    INSERT INTO recipe_ingredient (recipe_id, ingredient_id, quantity, units)
                    VALUES (:recipe_id, :ingredient_id, :quantity, :units)
                """), {'recipe_id': recipe_id, 'ingredient_id': ingredient_id, 'quantity': quantity, 'units': units}
            )
        
        db.session.commit()

if __name__ == "__main__":
    add_ingredients_to_recipes()

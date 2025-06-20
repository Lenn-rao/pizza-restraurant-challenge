Pizza Restaurant API Challenge

This is a RESTful API for a Pizza Restaurant built with Flask, Flask-SQLAlchemy, and Flask-Migrate. It manages restaurants, pizzas, and their relationships through a join table (RestaurantPizza). The API follows the MVC pattern and includes validations, cascading deletes, and comprehensive documentation.

Prerequisites





Python 3.6+



SQLite (used as the database)



Postman (for testing)



pipenv (for dependency management)

Validation Rules





RestaurantPizza.price: Must be a number between 1 and 30 (inclusive).



restaurant_id and pizza_id in RestaurantPizza: Must correspond to existing Restaurant and Pizza records.

Postman Usage Instructions





Import Collection:





Open Postman.



Click Import → Upload File.



Select challenge-1-pizzas.postman_collection.json.



Test Routes:





Ensure the Flask app is running (flask run).



Run each request in the collection to test GET, POST, and DELETE endpoints.



Verify responses match the expected status codes and data.

Notes





Cascading Deletes: Deleting a Restaurant automatically deletes associated RestaurantPizza records due to cascade='all, delete-orphan'.



Error Handling: The API returns appropriate error messages and status codes for invalid requests.



MVC Structure: Models handle data, controllers manage route logic, and app.py ties everything together.
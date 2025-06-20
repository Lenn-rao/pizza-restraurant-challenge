from server.app import db
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)

    # Relationships
    restaurant = relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = relationship('Pizza', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError('Price must be between 1 and 30')
        return price

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id,
            'pizza': self.pizza.to_dict(),
            'restaurant': self.restaurant.to_dict()
        }
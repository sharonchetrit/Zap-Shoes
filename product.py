from database import connect

class Product:
  def __init__(self, id, name, price, image, rating):
    self.id = id
    self.name = name
    self.price = price
    self.image = image
    self.rating = rating

  def __repr__(self):
    return "<Product {}>".format(self.name)

  def save_to_db(self):
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("INSERT INTO products(name, price, image, rating) VALUES(%s, %s, %s, %s)", (self.name, self.price, self.image, self.rating))



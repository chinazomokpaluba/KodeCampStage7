#Call Shell
# python manage.py shell

#Import model/table
# from home.models import Product

#Insert a new record into the Product Model
# pro1 = Product(pro_name="Coke",quantity="3",price="200",store_name="roban")
# pro1.save()

#Get all the records in the Product table
# p = Project.objects.all()
# p

#Filter products by their name
# Product.object.filter(pro_name="Coke")

#Get a single record from the product table
# p = Product.object.get(pro_name="Coke")
# p

# Change a product price
# p = Product.object.get(price="200")
# p.price = "300"
# p.save()

#exiting shell
# exit()

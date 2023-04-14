from restaurant.models import *

user1 = User.objects.create(email='nikname21@gmail.com', password='defender42')

user2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')

client1 = Client.objects.create(name='Азат Соколов', card_number='4147 5657 9878 9009', user=user1)

worker1 = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=user2)

ingredient1 = Ingredient.objects.create(name='Сыр', extra_price=10)
ingredient2 = Ingredient.objects.create(name='Курица', extra_price=70)
ingredient3 = Ingredient.objects.create(name='Говядина', extra_price=80)
ingredient4 = Ingredient.objects.create(name='Салат', extra_price=15)
ingredient5 = Ingredient.objects.create(name='Фри', extra_price=15)

food1 = Food.objects.create(name='Шаурма', start_price=50, ingredients=ingredient1)
food2 = Food.objects.create(name='Гамбургер', start_price=25)



order1 = Order.objects.create(food=food1, ingredient=ingredient3+ingredient1+ingredient4+ingredient5, client=client1, worker=worker1)



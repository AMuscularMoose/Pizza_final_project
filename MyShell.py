import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping, Comment

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()
comments = Comment.objects.all()

for p in pizzas:
    print(f"Pizza ID: {p.id}    Pizza: {p}")

for t in toppings:
    print(f"Pizza: {t.pizza}    Topping: {t}")

for c in comments:
    print(f"Comment: {c.pizza}      Comment: {c}")
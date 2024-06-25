from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestLunchOrder(TransactionCase):

    def setUp(self):
        super().setUp()
        self.user = self.env.ref('base.user_admin')
        self.product = self.env['lunch.product'].create({
            'name': 'Cake',
            'category_id': 2,
            'supplier_id': 1,
            'price': 10.0,
            'active': True,
        })

    def test_create_lunch_order(self):
        order_values = {
            'product_id': self.product.id,
            'date': fields.Date.today(),
            'user_id': self.user.id,
            'quantity': 2.0,
        }
        lunch_order = self.env['lunch.order'].create(order_values)
        self.assertEqual(lunch_order.state, 'new', "Lunch order should be in 'new' state after creation")


    def test_order_toppings(self):
        topping_1 = self.env['lunch.topping'].create({'name': 'Topping 1', 'topping_category': 1, 'price': 2})
        topping_2 = self.env['lunch.topping'].create({'name': 'Topping 2', 'topping_category': 2, 'price': 2})
        topping_3 = self.env['lunch.topping'].create({'name': 'Topping 3', 'topping_category': 3, 'price': 2})

        order_values = {
            'product_id': 1,
            'date': fields.Date.today(),
            'user_id': self.user.id,
            'price': 2,
            'quantity': 1.0,
            'topping_ids_1': [(6, 0, [topping_1.id])],  # Adding a topping
            'topping_ids_2': [(6, 0, [topping_2.id])],  # Adding a topping
        }
        lunch_order = self.env['lunch.order'].create(order_values)
        self.assertEqual(lunch_order.display_toppings, 'Topping 1 + Topping 2',
                         "Toppings should be displayed correctly")

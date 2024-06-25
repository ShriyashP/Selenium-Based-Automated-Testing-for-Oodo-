from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestLunchOrder(TransactionCase):

    def setUp(self):
        super().setUp()
        self.user = self.env.ref('base.user_admin')
        self.product = self.env['lunch.product'].create({
            'name': 'Test Product',
            'category_id': 2,
            'supplier_id': 1,
            'price': 10.0,
            'active': True,
        })


    def test_order_quantity_validation(self):
        order_values = {
            'product_id': self.product.id,
            'date': fields.Date.today(),
            'user_id': self.user.id,
            'quantity': 24,  # Negative quantity should raise validation error
        }
        with self.assertRaises(ValidationError):
            self.env['lunch.order'].create(order_values)


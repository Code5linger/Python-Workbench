# 8.1
"""
from sales import calc_shipping, calc_tax
import sales

sales.calc_shipping()


calc_shipping()
calc_tax()
"""
# 8.2
"""
import sales
import sys

print(sys.path)
"""
# 8.3
"""
from ecommerce.sales import calc_tax, calc_shipping
from ecommerce import sales

sales.calc_tax()
calc_tax()
"""
# 8.4
"""
from ecommerce.shopping import sales

sales.calc_tax()
"""
# 8.6
"""
from ecommerce.customer import contact
from ..customer import contact

contact.contact_customer()

def calc_shipping():
    pass

def calc_tax():
    pass
"""
# 8.7
"""
from ecommerce.shopping import sales

# print(dir(sales))
print(sales.__name__)
print(sales.__package__)
"""
###IMPORTS###
import shopify
from creds import*

###API ACTIVATION###
api_session = shopify.Session(merchant, '2023-01', token)
shopify.ShopifyResource.activate_session(api_session)
print("boom")
###GET PRODUCT DETAIL METHOD###
def get_product_detail():
    products = shopify.Product.find(limit=100)
    for product in products:
        print(f"Product: {product.title}")
        for variant in product.variants:
            print(f"Price: {variant.price}")
            print(f"Availability: {variant.inventory_quantity}")
get_product_detail()
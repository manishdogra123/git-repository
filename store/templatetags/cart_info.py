from django import template


register = template.Library()
@register.filter(name='in_cart')
def in_cart(data,cart):
    key = cart.keys()
    # print(data,cart)
    for id in key:
        if int(id) == data.id:
            return True
    else:
        return False

@register.filter(name='total_item_in_cart')
def total_item_in_cart(data,cart): 
    key = cart.keys()
    for id in key:
        if int(id) == data.id:
            return cart.get(id)
           
    return 0;
    print(product,cart)

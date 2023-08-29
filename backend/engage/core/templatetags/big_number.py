from django import template

register = template.Library()


@register.filter(name='big_number')
def big_number(value, num_decimals=2):
    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('0').rstrip('.') + 'K'
    else:
        return formatted_number.format(int_value/1000000.0).rstrip('0').rstrip('.') + 'M'
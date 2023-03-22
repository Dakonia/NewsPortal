from django import template


register = template.Library()


@register.filter()
def censor(value):
    x='теракт'
    c='редиска'
    if x in value:
        a= value.replace('теракт', 'т*****')
        return a
    if c in value:
        d= value.replace('редиска', 'р******')
        return d
    try:
        x = str(x)
        c = str(c)
    except:
        print('Введено не слово')
    else:
        return value


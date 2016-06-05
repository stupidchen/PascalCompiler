def gattrs(o):
    return [i for i in dir(o) if not callable(getattr(o,i)) and not i.startswith('__')]

_Type_Boolean=0
_Type_Char=1
_Type_Int=2
_Type_Float=3

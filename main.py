#Exercise Exceptions in Python
true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    if isinstance(value, str):
       value = value.lower();
    else:
        raise TypeError("Not supported type.")
    
    if value in true_values:
        return True;
    elif value in false_values:
        return False;
    else:
        raise ValueError("Not valid value.")

try:
    print(str_to_bool("False"));
except TypeError as ex:
    print(ex);
except Exception as e:
    print(e);
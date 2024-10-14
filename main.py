#Exercise Exceptions in Python
true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    if(type(value) != "str"):
       raise TypeError("Not supported type.")
    else:
        value = value.lower();
    
    if value in true_values:
        return True;
    elif value in false_values:
        return False;
    else:
        raise ValueError("Not valid value.")

try:
    print(str_to_bool(1));
except Exception as ex:
    print(ex);
except Exception as e:
    print(e);
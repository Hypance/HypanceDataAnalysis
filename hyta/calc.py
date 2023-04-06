def calc(class_name):
    #all funtion of object were listed ,and lastest function was found
    last_funtion_name = dir(class_name)[-1]
    #the object was returned without needing to call the last function manually
    return getattr(class_name,last_funtion_name)()
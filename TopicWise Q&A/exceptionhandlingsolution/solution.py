def divide(a,b):
    try:
        result = a / b
    except  ZeroDivisionError as e:
        print(f"error : {e}")
        result = None
    finally:
        print("exicution complete.")
        return result

    
# print(divide(10,5))
print(divide(10,0))

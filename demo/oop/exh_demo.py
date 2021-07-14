try:
    v = input("Enter count :")
    count = int(v)
    print('Share :', 1000 / count)
except ValueError:
    print("Invalid input. Please provide a valid number!")
except Exception as ex:   # Catch all
    print('Error : ', ex)
else:
    print("Else")
# except ZeroDivisionError:
#     print("Sorry! Count cannot be zero!")
finally:
    print("Finally")

print("The End")

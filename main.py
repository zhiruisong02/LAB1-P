# Author: Song Zhirui zjs5301@psu.edu
# Collaborator: Jack Hillman jsh5719@psu.edu
# Collaborator:  Shrey Hillman sxs6588@psu.edu
# Collaborator: Alexandros Condeelis afc5865@psu.edu
# Section:5

tem = input("Enter temperature: ")
tem = float(tem)
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  Celsius = float((tem - 32 )/1.8)
  print(f"{str(tem)}{chr(176)} in Fahrenheit is equivalent to {str(Celsius)}{chr(176)} Celsius.")
elif unit == "C" or unit == "c":
  Fahrenheit = float((tem *1.8 + 32))
  print(f"{str(tem)}{chr(176)} in Celsius is equivalent to {str(Fahrenheit)}{chr(176)} Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
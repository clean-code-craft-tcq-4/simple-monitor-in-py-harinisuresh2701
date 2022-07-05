def battery_is_ok(feature, value, minimum_value, maximum_value):
  def string_formatter():
    printable_string = feature + " is out of range!"
    return printable_string
  def check_if_value_in_range(value, minimum_value, maximum_value):
    if minimum_value < value < maximum_value :
      return True
    else:
      output_message = string_formatter()
      print_on_console(output_message)
      return False
  check_if_value_in_range(value, minimum_value, maximum_value)
     
def print_on_console(string):
  print(string)

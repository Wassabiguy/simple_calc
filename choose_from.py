import basic_calculations

def pick(option_number):
    match option_number:
        case "1":
             basic_calculations.substitution()
        case "2":
             basic_calculations.add()
        case "3":
             basic_calculations.divide()
        case "4":
             basic_calculations.multiplying()     
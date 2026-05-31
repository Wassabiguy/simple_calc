import basic_calculations
import number_grabber
def pick(option_number):
    match option_number:
        case "1":
             p = number_grabber.number_grabber()
             print(basic_calculations.substitution(p))
        case "2":
             p = number_grabber.number_grabber()
             print(basic_calculations.add(p))
        case "3":
             p = number_grabber.number_grabber()

             print(basic_calculations.divide(p))
        case "4":
             p = number_grabber.number_grabber()
             print(basic_calculations.multiplying(p))     
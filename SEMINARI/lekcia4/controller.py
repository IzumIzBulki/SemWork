import model_2
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_2.init(value_a, value_b)
    result = model_2.mult()
    view.view_data(result)

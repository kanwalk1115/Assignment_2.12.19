total_bill = float(input('Enter the total amount'))
tip_percentage = float(input('Enter tip percentage'))

def tip_amount(bill, percentage):
    return(float(bill * percentage/100))

print (tip_amount(total_bill, tip_percentage))

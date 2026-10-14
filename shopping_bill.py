
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Sample values given in the PDF
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = Rs. {total:.2f}")
print(f"Discount = Rs. {discount:.2f}")
print(f"Final payable amount = Rs. {final_amount:.2f}")

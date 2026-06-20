# Problem 15
# Display formatted output in three ways.
product="Laptop"
price=75000.5
discount=10
print(f"Product:{product} Price:{price:.2f} Discount:{discount}%")
print("Product:{} Price:{:.2f} Discount:{}%".format(product,price,discount))
print("Product:%s Price:%.2f Discount:%d%%"%(product,price,discount))
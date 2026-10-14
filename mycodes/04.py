# 练习 4：变量和命名

cars = 100
# 写成 4.0 不是 4，差别就在这儿：后面 carpool_capacity 会算成 120.0，不是 120。一般来讲记个 int、记个 float 就够了，我记得还有个是 long int，其他都记不清了。string倒是常用
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about" , average_passengers_per_car,
"in each car.")

car_list=["swift","mustang","porsche","jaguar","mercedes","buggati","bellgadi"]

with open("car.txt","w") as fp:
    for i in car_list:
        fp.write("%s\n" %i)
print("done")

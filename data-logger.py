a=['no','No','n','N','NO']
with open("info.csv","a") as f:
    while True:
        yes_no=input("do you want to continue (y/n)?")
        if yes_no in a:
            break
        name=input("Name :")
        
        phone=input("Phone Number :")
        place=input("Place :")
        temp=input("Temperature(F) :")
        f.writelines(f'\n{name},{phone},{place},{temp}')
f.close()

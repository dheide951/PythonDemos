musicans = ["Five Finger Death Punch", "Beatles", "Last Night", "Three days grace"]
coordinates = [("3.32N","12.3W"), ("4.22E","13.3W")]

person = {

    "height": 6,
    "weight": 180,
    "hair_color": "brown"

    }

result = input("Ask a question\n");

if "height" in result:
    print(person["height"])
elif "weight" in result:
    print(person["weight"])
elif "hair color" in result:
    print(person["hair_color"])
else:
    print("I dont know")


music = {

    musicans[0]: "bad company",
    musicans[1]: "cant by me love",
    musicans[2]: "gone forever"
    
    }


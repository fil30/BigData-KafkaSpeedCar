import sys
import datetime
import random
from random import randrange
import json


# Set number of simulated messages
if len(sys.argv) > 1:
  num_msgs = int(sys.argv[1])
else:
  num_msgs = 1

car_list = ['Ferrari', 'Alfa Romeo', 'Audi', 'Suzuki', 'Hyundai', 'Lancia', 'Honda', 'Mercedes-Benz',
           'Mazda', 'Nissan', 'Volkswagen', 'Subaru', 'Toyota', 'Lamborghini', 'Chevrolet', 'Ford',
           'Volvo', 'Porsche', 'Bentley', 'MAZDA']
street_type = ['urban street', 'secondary extra urban road', 'main suburban road', 'highway']
speed_limit = [50, 90, 110, 130]

plate = ""

# Fixed values
id_base = "ZZZ12345678-"
destination = "AAA12345678"

# Choice for random letter
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

list = []

# Generate text output:
if __name__ == "__main__":
    for counter in range(0, num_msgs):
        rand_num = str(random.randrange(0, 9)) + str(random.randrange(0, 9))
        rand_letter = random.choice(letters)
        
        id_sensor = id_base + rand_num + rand_letter
        
        rand_choice = random.randrange(0, 3)
        rand_street = street_type[rand_choice]
        rand_limit = speed_limit[rand_choice]
        
        rand_first_plate = random.choice(letters) + random.choice(letters)
        rand_second_plate = str(random.randrange(0, 9)) + str(random.randrange(0, 9)) + str(random.randrange(0, 9))
        rand_third_plate = random.choice(letters) + random.choice(letters)
        
        rand_plate = rand_first_plate + rand_second_plate + rand_third_plate
        
        rand_car = car_list[random.randrange(0, len(car_list) - 1)]
        
        car_speed = str(random.randrange(30, 150))
        
        today = datetime.datetime.today()
        datestr = today.isoformat()
        
        list.append({"id_sensor": str(id_sensor), "destination": str(destination), "road_type": str(rand_street),
                "speed_limit": int(rand_limit), "model": str(rand_car), "plate": str(rand_plate),
                "time": str(datestr), "speed": int(car_speed)})
        
    count = 1
    jsonFile = open("input/testdata.json", "w")
    for obj in list:
        jsonString = json.dumps(obj)
        jsonFile.write(jsonString)
        if (count != len(list)):
            jsonFile.write(",")
            jsonFile.write("\n")
        count = count + 1
    jsonFile.close()

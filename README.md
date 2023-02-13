# BigData-KafkaSpeedCar
The aim of this project is to set up a Kafka environment to manage a real time data streaming, following these steps:
* Created data directly by the script car-data.py in a random way
* Memorized data in a JSON file and published in Kafka Broker
* Data are consumed through Spark Streaming
* Finally, the result of the computation is returned in the console output


I used simulated data for this project. The script car-data.py generates JSON data characterized by the above schema:
```
  <Example>
       
      {
           "id_sensor": "ZZZ12345678-85E",
           "destinaation": "AAA12345678",
           "road_type": "highway",
           "speed_limit": 130,
           "model": "Mercedes-Benz",
           "plate": "GD853GQ",
           "time": "2023-02-10T01:30:09.019439",
           "speed": 112
     }
```

## Technogies
* Spark (3.3.0)
* Kafka (3.3.2)
* Zookeeper
* PySpark (3.3.0)
* Python (3.9.13)

## Usage
* Start all the components with the script ```start-all.bash```
* Execute bash ```run-all.bash```
* Close the application with the script ```stop-all.bash```


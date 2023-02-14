#!/bin/bash

echo 
echo "Insert the number of data you want to produce"

read data

re="^[0-9]+$as"
if ! [[ $data =~ $re ]]; then
  echo "Error: invalid format"
  exit
else
  input=$(cat input/execution.txt)
  python3 car-data.py "$data"
  
  echo "Data successfully created"
  echo
  
  echo "Producing data for testtopic..."
  kafka_2.12-3.3.2/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic testtopic < input/testdata.json
  echo "Done"
  echo

  echo "Executing..."
  
  if [[ $input = "first" ]]; then
    unset PYSPARK_DRIVER_PYTHON
  
    gnome-terminal -- "${SPARK_HOME}"/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 kafka-spark-car.py localhost:9092 testtopic
    
    echo "opened" > input/execution.txt
    sleep 100
  fi

  sleep 15
fi


while true
do
  echo "Do you want to insert new data?(y/n)"
  read firstanswer

  if [[ "$firstanswer" = "y" ]]; then
    echo "Insert new data"
    read newdata
    re="^[0-9]+$as"
    if ! [[ $newdata =~ $re ]]; then
      echo "Error: invalid format"
      exit
    else
      python3 car-data.py "$newdata"
      echo "Data successfully created"
      echo
      echo "Producing data for testtopic..."
      kafka_2.12-3.3.2/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic testtopic < input/testdata.json
 
      echo "Done"
      echo
      echo "Executing..."
      sleep 15
    fi
  elif [[ "$firstanswer" = "n" ]]; then
    echo "Do you want to exit?(y/n)"
    read secondanswer
    if [[ "$secondanswer" = "y" ]]; then
      exit
    elif [[ "$secondanswer" = "n" ]]; then
      echo
    else
      echo "Invalid command: retry"
    fi
  else
    echo "Invalid command: retry"
  fi
done

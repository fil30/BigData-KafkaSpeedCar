#!/bin/bash

echo "Press enter to stop all the components"
read continue

echo "Initializing shotdown for all the components..."
echo

rm input/execution.txt

echo "Delete Kafka topic"
./kafka_2.12-3.3.2/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic testtopic --delete
./kafka_2.12-3.3.2/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic __consumer_offsets --delete

echo
echo "Shotdown Kafka"
./kafka_2.12-3.3.2/bin/kafka-server-stop.sh kafka_2.12-3.3.2/config/server.properties

sleep 10

echo

echo "Shotdown Zookeeper"
./kafka_2.12-3.3.2/bin/zookeeper-server-stop.sh kafka_2.12-3.3.2/config/zookeeper.properties

sleep 10

sleep 1

echo "Execution terminated"
sleep 1
echo "Press enter to exit"
read continue

kill $(pgrep gnome-terminal)

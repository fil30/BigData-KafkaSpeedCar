#!/bin/bash

echo "Press enter to stop all the components"
read continue

echo "Initializing shotdown for all the components..."
echo

rm input/execution.txt

echo "Deleting kafka topic"
./kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic testtopic --delete
./kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic __consumer_offsets --delete

echo "Shotdown Zookeeper"
./kafka/bin/zookeeper-server-stop.sh kafka/config/zookeeper.properties

sleep 10

echo
echo "Shotdown Kafka"
./kafka/bin/kafka-server-stop.sh kafka/config/server.properties

sleep 10

echo

sleep 1

echo "Execution terminated"
sleep 1
echo "Press enter to exit"
read continue

kill $(pgrep gnome-terminal)

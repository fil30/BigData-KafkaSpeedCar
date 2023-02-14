#!/bin/bash

echo "Starting project components..."
sleep 1

echo "Press enter to continue..."
read continue

sleep 5

echo "Starting Zookeeper"
gnome-terminal -- sh kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties

sleep 20

echo "Starting Kafka"
gnome-terminal -- sh kafka/bin/kafka-server-start.sh kafka/config/server.properties

sleep 50

echo "Setting kafka-topic"
sh kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic testtopic --create --partitions 1 --replication-factor 1

sleep 5

echo "first" > input/execution.txt

echo "Components starting sequence complete"



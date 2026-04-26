## Create a Topic

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic user-events \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

## Details of a Topic

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --describe \
  --topic user-events \
  --bootstrap-server localhost:9092
```


## List all Topics
```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```


## Start a Producer (Send events int the topic)

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh \
  --topic user-events \
  --bootstrap-server localhost:9092
```

## Start a Consumer (Read events in a topic)

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --topic user-events \
  --bootstrap-server localhost:9092 \
  --from-beginning
```
//read config file
zookeeper &
broker &
for number in instances:
  python Driver.py --port  &
python Ops.py &
python Mongo.py &
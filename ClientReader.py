from KeyValueStore import KVS

kvs = KVS("/src/database")

for tupple in kvs.GetAll():
	print(tupple[0] + ": " + tupple[1])
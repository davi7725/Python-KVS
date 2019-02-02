from KeyValueStore import KVS

kvs = KVS("/src/database")

kvs.SetData("bananas","3")
kvs.SetData("ananas","42")
kvs.SetData("bananas","70")
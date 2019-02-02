# Python-KVS

## Features

- Create a key-value store database
- Re-generate hash map when a new object is instantiated
- Write data to a database file
- Read data from a database file

## Requirements

* Docker ✅

## How to run
1. Clone the project using the  following command **or** download the repository zip file
`git clone https://github.com/davi7725/Python-KVS.git`
1. Navigate to the cloned folder on a shell
1. Run the following command
`docker run -it --rm -v $(pwd):/src -w /src python sh -c "python3 ClientWriter.py"`
	-  This step executes the ClientWriter.py file which will write to a file "database" in the repository's root folder some predefined values.

	NB! If you have *Windows*, replace **$(pwd)** with the path to the directory of the repository
1. Then run the following command
`docker run -it --rm -v $(pwd):/src -w /src python sh -c "python3 ClientReader.py"`
	-  Now the ClientReader.py file will be run, and it reads from the previous database file and prints all the stored records.

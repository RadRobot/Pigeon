pigeon
======

Python JSON configuration library

installation:
-------------

```
	git clone git@github.com:RadRobot/pigeon.git
	cd pigeon
	python setup.py install

	(sorry, no pip yet)
```

usage:
------

```
	from pigeon.pigeon import PConf

	schema = {
		'user': str,
		'name': str,
		'age': int,
		'address': {
			'country': str,
			'region': str,
			'street#': int
		},
		'weight': float,
		'items': [
			{
				'something': str,
				'something_else': int
			}
		],
		'simple': [str]
	}

	config_object = PConf('sample.conf', schema)

	config_object.pretty()
```

sample configuration file:
--------------------------

```
	{
		"user": "bob",
		"name": "jimbob",
		"age": 25,
		"address": {
			"country": "Canada",
			"region": "Ontario",
			"street#": 123
		},
		"weight": 180.75,
		"items": [
			{
				"something": "idunno",
				"something_else": 13
			},
			{
				"something": "not sure",
				"something_else": 1923
			}
		],
		"simple": [
			"asdf",
			"second",
			"third"
		]
	}
```

rationale:
----------

Simplicity. Most other python config libraries have complex design, and their own
schema format. JSON already handles complex structures and types and is easily translated
to a python dictionary - why not use it for configuration?

schema rules:
-------------

```
	- thou shal not make lists of lists
	- each list item must follow the same type, or sub-schema
	- thou shal only use primitive types
	- its recursive
```

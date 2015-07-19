# pigeon

=========================================

Python JSON configuration library

installation:

```
	git clone git@github.com:RadRobot/pigeon.git
	cd pigeon
	python setup.py install

	(sorry, no pip yet)
```

usage:

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

The rationale behind using a python dictionary for a schema is for simplicity.
You may even import the schema from another .py file this way.
If it were a pure JSON schema, the schema file would have been a lot more verbose.

schema rules:

```
	- thou shal not make lists of lists
	- each list item must follow the same type, or sub-schema
	- thou shal only use primitive types
```

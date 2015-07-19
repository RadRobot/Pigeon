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

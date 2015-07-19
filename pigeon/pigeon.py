import simplejson as json

class PConf():

	def __init__(self, filename="", schema={}):
		"""initialize with a schema dictionary"""
		if not filename or not isinstance(schema, dict):
			return None

		with open(filename, "r") as f:
			self.conf = json.loads(f.read())

		self.schema = schema

		self.validate(self.conf, self.schema)

	def pretty(self):
		"""pretty print the config"""
		print json.dumps(self.conf, indent=4)

	def validate(self, config, schema):
		"""recursively check against types in schema"""
		for key, val in config.iteritems():
			if key not in schema:
				raise Exception(key + " not in schema")

			if isinstance(val, list):
				if val == []:
					continue

				type_first_element = type(val[0])
				schema_first_element = schema[key][0]

				if isinstance(schema_first_element, list):
					# don't allow multi dimensional lists!
					raise Exception("Can't have list in a list")

				for index, item in enumerate(val):
					if not isinstance(item, type_first_element):
						# lists have standardized items so we reference all of them with the first one
						raise Exception(str(val) + " not of type " + repr(type_first_element))
					if isinstance(item, dict):
						self.validate(item, schema[key][0])
					else:
						pass

			elif isinstance(val, dict):
				self.validate(val, schema[key])
			else:
				if not isinstance(schema[key], type):
					raise Exception (repr(schema[key]) + " not a type ")
				if not isinstance(val, schema[key]):
					raise Exception (repr(val) + " not of type " + repr(schema[key]))


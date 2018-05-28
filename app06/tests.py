from django.test import TestCase

# Create your tests here.

d = {'name': "maotai", 'age': 22}
import json

# print(json.loads(d))
# TypeError: the JSON object must be str, bytes or bytearray, not 'dict'

# arr = [1,2,3]
# print(json.loads(arr))
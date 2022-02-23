import requests
import json


class PetClient:
	address = "https://petstore.swagger.io/v2"
	headers = {"Content-type": "application/json", "Accept": "application/json"}

	@classmethod
	def add_pet(cls, body):
		final_url = cls.address + "/pet"
		if not isinstance(body, str):
			body = json.loads(json.dumps(json.dumps(body, default=lambda x: x.__dict__)))
		return requests.post(url=final_url, data=body, headers=cls.headers)

	@classmethod
	def update_pet(cls, body):
		final_url = cls.address + "/pet"
		if not isinstance(body, str):
			body = json.loads(json.dumps(json.dumps(body, default=lambda x: x.__dict__)))
		return requests.put(url=final_url, data=body, headers=cls.headers)

	@classmethod
	def get_pet_by_id(cls, pet_id):
		final_url = cls.address + "/pet/" + str(pet_id)
		return requests.get(url=final_url, headers=cls.headers)

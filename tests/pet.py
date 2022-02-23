from api.models.pet import Pet
from api.clients.pet_client import PetClient


def test_should_see_200_after_add_pet():
    pet = Pet(name="bobik", photoUrls=["test"])

    response = PetClient.add_pet(pet)
    assert response.status_code == 200

    result_pet = Pet.from_json(response.text)

    pet["id"] = result_pet["id"]
    pet["tags"] = []

    assert result_pet == pet


def test_should_see_200_after_get_pet():
    pet = Pet(name="bobik", photoUrls=["test"])

    response_add = PetClient.add_pet(pet)
    result_add_pet = Pet.from_json(response_add.text)

    response_get = PetClient.get_pet_by_id(result_add_pet['id'])
    assert response_get.status_code == 200

    result_pet = Pet.from_json(response_get.text)

    pet["id"] = result_add_pet["id"]
    pet["tags"] = []

    assert result_pet == pet


def test_should_see_200_after_update_pet():
    pet = Pet(name="bobik", photoUrls=["test"])

    response_add = PetClient.add_pet(pet)
    result_add_pet = Pet.from_json(response_add.text)
    pet["name"] = "neBobik"

    response_update = PetClient.update_pet(pet)
    assert response_update.status_code == 200

    result_pet = Pet.from_json(response_update.text)

    pet["id"] = result_pet["id"]
    pet["tags"] = []

    assert result_pet == pet
    assert result_pet["id"] != result_add_pet["id"]

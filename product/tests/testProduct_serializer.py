import pytest

from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    data = {
        "title": "Testando o serializer",
        "description": "Testando o serializer com pytest",
        "price": 777
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    product = serializer.save()

    assert product.title == data["title"]
    assert product.description == data["description"]
    assert product.price == data["price"]

    serializer = ProductSerializer(product)
    serialized_data = serializer.data

    assert serialized_data["title"] == data["title"]
    assert serialized_data["description"] == data["description"]
    assert serialized_data["price"] == data["price"]
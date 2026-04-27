import pytest
from inventory import Inventory

@pytest.fixture
def empty_inventory():
    """Fixture que retorna uma instância vazia de Inventory."""
    return Inventory()

@pytest.fixture
def populated_inventory():
    """Fixture que retorna uma instância de Inventory com itens."""
    inventory = Inventory()
    inventory.add_item("Laptop", 10)
    inventory.add_item("Mouse", 50)
    return inventory

# --- TESTES QUE PASSAM ---

def test_add_item_success(empty_inventory):
    """Testa a adição bem-sucedida de um item."""
    assert empty_inventory.add_item("Teclado", 5)
    assert empty_inventory.get_quantity("Teclado") == 5

def test_remove_item_success(populated_inventory):
    """Testa a remoção bem-sucedida de um item."""
    assert populated_inventory.remove_item("Laptop", 5)
    assert populated_inventory.get_quantity("Laptop") == 5

# --- TESTES QUE VÃO FALHAR (PARA DEMONSTRAÇÃO) ---

def test_fail_wrong_quantity(populated_inventory):
    """
    ESTE TESTE VAI FALHAR.
    Objetivo: Mostrar que o Pytest detecta quando o valor retornado é diferente do esperado.
    Cenário: Esperamos 10 laptops, mas o assert diz que deveria haver 15.
    """
    print("\n[DEMONSTRAÇÃO DE FALHA 1]")
    assert populated_inventory.get_quantity("Laptop") == 15

def test_fail_item_not_found(populated_inventory):
    """
    ESTE TESTE VAI FALHAR.
    Objetivo: Mostrar como o Pytest lida com retornos booleanos incorretos.
    Cenário: Tentamos remover um item que não existe (Monitor) e esperamos que retorne True,
    mas o sistema retornará False.
    """
    print("\n[DEMONSTRAÇÃO DE FALHA 2]")
    # O método remove_item retorna False se o item não existe. 
    # Ao forçar o assert para True, causamos a falha.
    assert populated_inventory.remove_item("Monitor", 1) == True
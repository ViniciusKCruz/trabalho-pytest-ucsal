class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not item_name:
            raise ValueError("Nome do item inválido.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantidade inválida.")
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        return True

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not item_name:
            raise ValueError("Nome do item inválido.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantidade inválida.")
        if item_name not in self.items:
            return False # Item não encontrado
        if self.items[item_name] < quantity:
            return False # Quantidade insuficiente
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]
        return True

    def get_quantity(self, item_name):
        return self.items.get(item_name, 0)

    def list_items(self):
        return self.items.copy()
class Replacement:
    def __init__(self, products: list):
        self.products = products

    def find_replacement(self):
        category = input("Ingrese la categoría del producto que busca: ")
        brand = input("Ingrese la marca del producto que busca: ")

        try:
            max_price = float(input("Ingrese el precio máximo (o presione Enter para omitir): ") or float('inf'))
        except ValueError:
            print("Precio no válido, se ignorará este filtro.")
            max_price = float('inf')

        color = input("Ingrese el color deseado (o presione Enter para omitir): ")

        filtered_products = [p for p in self.products
                             if p.category.lower() == category.lower()
                             and p.brand.lower() == brand.lower()
                             and p.price <= max_price
                             and (color.lower() in map(str.lower, p.colors) if color else True)]

        if filtered_products:
            print("Productos disponibles:")
            for p in filtered_products:
                print(f"{p.name} - ${p.price} - {p.colors}")
        else:
            print("No se encontraron productos con esos criterios.")
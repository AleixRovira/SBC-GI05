import textwrap

class InfoProduct:
    def __init__(self, products: list, translated_categories, translated_colors):
        self.products = products
        self.translated_categories = translated_categories
        self.translated_colors = translated_colors

    def show_info(self) -> None:
        input_string = input("¿Sobre qué producto quieres información? ")
        # Buscar un producto mencionado en el texto
        for product in self.products:
            if product.name.lower() in input_string.lower():
                # Construir el párrafo informativo
                new_colors = []
                for color in product.colors:
                    new_colors.append(self.translated_colors[color])
                colores = ', '.join(new_colors)
                tallas = ', '.join(map(str, product.size_availability))
                texto = (
                    f"El producto **{product.name}** es un {product.category.lower()} de la marca {product.brand}."
                    f"{product.description} Su precio es de {product.price}€."
                    f"Está disponible en los colores: {colores}."
                    f"Y puedes encontrarlo en las tallas: {tallas}."
                )
                texto_formateado = textwrap.fill(texto, width=80)
                print(texto_formateado)
                return

        # Si no se encuentra ningún producto
        print("Lo siento, no he encontrado información sobre ese producto. ¿Podrías verificar el nombre?")

# GreenLandMXBot

## Grup

SBC-GI05

### Integrants

- Adrià Martínez Gallifa
- Ignasi Ràfols Llusà
- Raquel Riteco Cabañas
- Aleix Rovira Massana

## Requisits

Executar el fitxer de requirements.txt per instal·lar totes les dependències:
- pip install -r requirements.txt
¡Cal tindre Microsoft Visual C++ 14.0 o superior si no hi ha dependències que no s'instal·len correctament!

## Execució

### **1. Genera un dataset de productes**

Executa el main del script ``datasetGenerator.py`` per poder generar el dataset de productes o per si el vols
sobreescriure. Pots modificar les variables ``NUM_LINES`` i ``FILE_NAME`` per canviar el nombre de productes i
el nom del fitxer.

### **2. Executa el xatbot**

Executa la funció main del script ``main.py``.

## Alguns Exemples de preguntes

### Substitucions

Xat: (X - xatbot, U - usuari)

- U: ``Quiero cambiar mis guantes por otros de otra marca``
- X: ``¿Cuál es tu marca favorita? ``
- U: ``LS2``
- X: ``¿Tienes en mente algún precio máximo?``
- U: ``900``
- X: ``¿Lo quieres de algún color específico? ``
- U: ````
- X: ``Productos encontrados:``

### Pressupost

- ``Tengo 1000 euros como maximo presupuesto, que recomiendas comprar?``

### Disponibilitat

- ``¿Hay stock de guantes de invierno?``
- ``¿Teneis disponible el mono Alpinestars?``

### Preguntes frequents

- ``¿Dónde solicito la eliminación de mi cuenta?``
- ``¿Puedo revisar las órdenes que he hecho antes?``
# GreenLandMXBot

## Grup

SBC-GI05

### Integrants

- Adrià Martínez Gallifa
- Ignasi Ràfols Llusà
- Raquel Riteco Cabañas
- Aleix Rovira Massana

## Requisits

Tindre instal·lats els paquets:

- ``nltk``
- ``faker`` (només si es vol generar un dataset de prova)

## Execució

### **1. Genera un dataset de productes**

Executa el main del script ``datasetGenerator.py`` per poder generar el dataset de productes o per si el vols
sobreescriure. Pots modificar les variables ``NUM_LINES`` i ``FILE_NAME`` per canviar el nombre de productes i
el nom del fitxer.

### **2. Executa el xatbot**

Executa la funció main del script ``main.py``.

## Exemples de preguntes

### Substitucions

Xat: (X - xatbot, U - usuari)

- U: ``I want a replacement``
- X: ``¿What type of item do you want for your replacement?``
- U: ``helmet``
- X: ``¿What is your favourite brand?``
- U: ``rst``

Full query
- ``I want the replacement of an airbag from TCX that costs less than 900 dollars and its black``

### Comparacions

- ``Can you compare all the boots``
- ``Can you compare product1 with product2`` (sent el product1 i el product2 els noms dels productes en els datasets)

### Pressupost

- ``I need a budget``
- ``I need a budget for a helmet, boots and gloves``
- ``I need to buy a helmet, boots and gloves with a budget of 3000``

### Disponibilitat

- ``Give me the abailability for products of the brand Dainese``
- ``Give me tha abailability for all green products``

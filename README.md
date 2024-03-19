# Advanced Python Practices #1: Magic methods and dunders

1. **Magic Methods en Python:**
   Los "magic methods" en Python son métodos especiales que comienzan y terminan con doble guion bajo (`__`). Estos métodos se utilizan para realizar diversas operaciones especiales en objetos, como la inicialización, representación, comparación, entre otros. También se les conoce como "métodos especiales" o "métodos dunder" (abreviatura de "double underscore").

   Aquí hay algunos ejemplos de magic methods comunes:

   - `__init__`: Este método se utiliza para inicializar un objeto después de su creación.
   - `__str__`: Define la representación de cadena de un objeto cuando se utiliza la función `str()`.
   - `__repr__`: Define la representación "oficial" de un objeto. Se utiliza cuando se llama a la función `repr()`.
   - `__eq__`, `__lt__`, `__gt__`, etc.: Métodos de comparación utilizados para implementar operaciones de comparación como igualdad, menor que, mayor que, etc.
   - `__add__`, `__sub__`, `__mul__`, etc.: Métodos utilizados para definir operaciones aritméticas como la suma, resta, multiplicación, etc.

   Estos son solo algunos ejemplos. Existen muchos otros magic methods que se pueden utilizar para personalizar el comportamiento de tus clases en Python.

2. **Dunder en Python:**
   "Dunder" es simplemente una forma abreviada de "double underscore" (doble guion bajo). En Python, los "dunders" se refieren específicamente a los identificadores que comienzan y terminan con doble guion bajo (`__`). Estos son utilizados para ciertos propósitos especiales, como los mencionados anteriormente en los magic methods.

   Los dunders son una convención en Python y tienen un significado especial dentro del lenguaje. Por ejemplo, `__init__` es un dunder utilizado para inicializar objetos, `__str__` y `__repr__` son dunder utilizados para representar objetos como cadenas, y así sucesivamente.

   Es importante destacar que no todos los identificadores que contienen doble guion bajo son magic methods. Algunos pueden ser simplemente convenciones de nombres específicos para indicar que un atributo o método es "privado" o interno a una clase.

En resumen, los magic methods en Python son métodos especiales que permiten definir comportamientos personalizados para objetos, mientras que los dunders son identificadores que comienzan y terminan con doble guion bajo, utilizados para diversos fines especiales, incluidos los magic methods.
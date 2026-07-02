from django.test import TestCase
from apl.models import Categoria


class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        "una prueba simple para validar que CI/CD funciona"
        self.assertTrue(1+1,2)

    def test_crear_categoria(self):
        "Prueba basica de base de datos en memoria"
        Categoria.objects.create(nombre='frijol')
        consulta= Categoria.objects.filter(nombre='frijol')
        self.assertEqual(consulta.exists())
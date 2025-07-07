import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from data import phone_number
from localizadores import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})  # esto habilita los logs.
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.urban = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.urban.set_rutas(data.address_from, data.address_to)  # diligenciamos campos desde y hasta.
        assert self.urban.get_from() == data.address_from
        assert self.urban.get_to() == data.address_to
        self.urban.dar_clic_pedir_taxi()

    def test_seleccionar_tarifa_confort(self):  # Seleccionamos la tarifa confort.
        self.urban.seleccionar_tarifa_confort()
        #assert "Manta y panuelos" in self.urban.confirmo_tarifa_confort()
        assert self.urban.get_mantas_y_panuelos() == 'Manta y pañuelos'

    def test_ingresar_numero_telefono(self):
        pagina = UrbanRoutesPage(self.driver)
        pagina.completar_numero_telefono(data.phone_number)
        assert data.phone_number[-4:] in pagina.obtener_texto_numero()

    def test_confirmar_y_cerrar_pago(self):
        self.urban.set_seleccionar_metodo_de_pago_tarjeta(data.card_number,data.card_code)  # Agregamos tarjeta como medio de pago con su número y código.
        assert self.urban.get_numero_de_tarjeta() == data.card_number
        assert self.urban.get_codigo_de_tarjeta() == data.card_code
        self.urban.close_seleccionar_metodo_de_pago_tarjeta()
        assert self.urban.verifica_texto_campo_metodo_de_pago() == "Tarjeta"

    def test_escribir_mensaje_conductor(self):
        self.urban.mensaje_para_el_conductor(data.message_for_driver)
        assert self.urban.verifica_mensaje() == data.message_for_driver

    def test_solicitar_manta_y_panuelos(self):
        self.urban.solicito_manta_y_pañuelos()  # Activamos la casilla verificación, manta y pañuelo.
        assert self.urban.check_swich_manta_y_pañuelos() == True

    def test_solicitar_helados(self):
        self.urban.solicito_agregar_helados()  # Solicito un par de helados.
        self.urban.solicito_agregar_helados()  # hacer doble click.

    def test_buscar_taxi(self):
        assert self.urban.verifico_boton_pedir_taxi_enabled() == True, "El botón pedir taxi no esta activado"  # Verificamos que el botón pedir un taxi está activado.
        self.urban.clic_boton_final_pedir_un_taxi()  # Clic en pedir un taxi a final del formulario
        assert self.urban.verifico_espera_contador() == True, "El contador no muestra la solicitud del taxi"  # Espera el tiempo necesario para verificar que se asignó un conductor al servicio.

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()

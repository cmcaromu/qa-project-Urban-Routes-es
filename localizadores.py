from helpers import retrieve_phone_code
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import phone_number, address_to


#conocer los elementos de la página, cada elemento contiene el localizador
class UrbanRoutesPage:
    origen_input = (By.XPATH, '//input[@id="from"]')
    destino_input = (By.XPATH, '//input[@id="to"]')
    modo_personal_button = (By.XPATH, '//div[@class = "mode" and contains(text(),"Personal")]')
    solicitar_taxi_button = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    opcion_tarifa_confort = (By.XPATH, '//div[text() = "10"]')
    confirmacion_tarifa_confort = (By.XPATH, '//div[@class= "r-sw-label" and contains(text(), "Manta y pañuelos")]')
    iniciar_ingreso_telefono = (By.XPATH, '//div[@class="np-button"]')
    texto_numero_telefono = (By.XPATH, '//div[@class="np-text"]')
    contenedor_input_telefono = (By.XPATH, '//div[@class="np-input"]/div')
    input_telefono = (By.ID, 'phone')
    enviar_telefono_button = (By.CLASS_NAME, "button.full")
    input_codigo_telefono = (By.ID, 'code')
    confirmar_codigo_button = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    abrir_metodos_pago_button = (By.XPATH, '//div[contains(@class,"pp-text")]/..')
    seleccionar_pago_tarjeta = (By.XPATH, '//img[contains(@class,"pp-plus")]')
    input_numero_tarjeta = (By.XPATH, '//input[contains(@id,"number")]')
    input_codigo_tarjeta = (By.XPATH, '//input[contains(@name,"code")]')
    espacio_tarjeta_codigo_boton = (By.XPATH, '//div[@class="card-wrapper"]')
    submit_tarjeta_button = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    cerrar_modal_pago_button = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    verificar_tarjeta_agregar = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")
    input_comentarios = (By.XPATH, '//input[@name="comment"]')
    switch_manta_panuelos_contenedor = (By.XPATH, '(//span[@class="slider round"])[1]/..')
    switch_manta_panuelos = (By.XPATH, '(//span[@class="slider round"])[1]')
    verificar_swich_mantas_y_panuelos = (By.XPATH, "//div[@class='r-sw-container'][.//div[contains(text(), 'Manta y pañuelos')]]//input[@type='checkbox' and contains(@class, 'switch-input')]")
    text_manta_panuelos = (By.XPATH, "//div[@class='r-sw-label' and text()= 'Manta y pañuelos']")
    contador_helados_valor = (By.XPATH, '(//div[@class="counter-value"])[1]')
    incrementar_helados_button = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    boton_confirmar_pedido = (By.XPATH, '//span[@class= "smart-button-main" and contains(text(), "Pedir un taxi")]')
    grupo_botones_pedido = (By.CLASS_NAME, "order-btn-group")

    def __init__(self, driver):
        self.driver = driver

    #se va a buscar seleccionar una ruta
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    #defino método para llenar el campo desde
    def desde(self, address_from):
        txt_campo_desde = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.origen_input))
        txt_campo_desde.send_keys(address_from)

    # defino método para llenar el campo hasta
    def hasta(self, address_to):
        txt_campo_hasta = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.destino_input))
        txt_campo_hasta.send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.origen_input).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.destino_input).get_property('value')

    #Vamos a diligenciar los campos desde y hasta
    def set_rutas(self, address_from, address_to):
        self.desde(address_from)
        self.hasta(address_to)

    #Definimos el método para seleccionar el modo "personal"
    def clic_personal_button(self):
        clic_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.modo_personal_button))
        clic_button.click()

    #seleccionar formato para solicitar taxi
    def solicitar_taxi(self):
    # boton = self.driver.find_element(*self.solicitar_taxi_button)
        boton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.solicitar_taxi_button))
        boton.click()

    def dar_clic_pedir_taxi(self):
        self.clic_personal_button()
        self.solicitar_taxi()

    #selecciono opción confort
    def seleccionar_tarifa_confort(self):
        # self.wait_for_element(self.opcion_tarifa_confort)
        # self.driver.find_element(self.opcion_tarifa_confort).click()
        selec_confort = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.opcion_tarifa_confort))
        selec_confort.click()

    #verifico el texto confort
    def confirmo_tarifa_confort(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.confirmacion_tarifa_confort)).text

    def get_mantas_y_panuelos(self):
        txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.text_manta_panuelos))
        return txt.text

    def set_tarifa_confort(self):
        self.clic_personal_button()
        self.solicitar_taxi()
        self.seleccionar_tarifa_confort()


    #rellenar número de teléfono
    def clic_agregar_el_numero(self):
        # self.driver.find_element(*self.iniciar_ingreso_telefono).click()
        clic_numero = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.iniciar_ingreso_telefono))
        clic_numero.click()

    #agregar número
    def clic_campo_numero(self):
        #self.driver.find_element(*self.contenedor_input_telefono).click()
        clic_nmr = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contenedor_input_telefono))
        clic_nmr.click()

    #ingresar número
    def agregar_numero_telefono(self, phone_number):
        #self.driver.find_element(*self.input_telefono).send_keys(phone_number)
        add_telefono = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_telefono))
        add_telefono.send_keys(phone_number)

    #dar clic en enviar telefono
    def clic_button_enviar_telefono(self):
        #self.driver.find_element(*self.enviar_telefono_button).click()
        clic_env_telefono = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.enviar_telefono_button))
        clic_env_telefono.click()


    def ingresar_codigo_telefono(self):
        code = retrieve_phone_code(self.driver)
        #self.driver.find_element(*self.input_codigo_telefono).send_keys(code)
        add_cod_telefono = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_codigo_telefono))
        add_cod_telefono.send_keys(code)

    #botón para confirmar código
    def clic_button_confirmar_codigo(self):
        #self.driver.find_element(*self.confirmar_codigo_button).click()
        clic_conf_cod = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirmar_codigo_button))
        clic_conf_cod.click()

    #obtener número
    def obtener_texto_numero(self):
        #return self.driver.find_element(*self.texto_numero_telefono).text
        obtener_numero = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.texto_numero_telefono))
        return obtener_numero.text

    #obtener número de telefono completo
    def completar_numero_telefono(self, phone_number):
        self.clic_agregar_el_numero()
        self.clic_campo_numero()
        self.agregar_numero_telefono(phone_number)
        self.clic_button_enviar_telefono()
        self.ingresar_codigo_telefono()
        self.clic_button_confirmar_codigo()

    #verifico método de pago
    def clic_metodo_de_pago(self):
        clic_metodo_de_pago = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.abrir_metodos_pago_button))
        clic_metodo_de_pago.click()

    # Defino metodo para dar clic en agregar medio de pago con tarjeta
    def medio_de_pago_tarjeta(self):
        clic_agregar_tarjeta = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.seleccionar_pago_tarjeta))
        clic_agregar_tarjeta.click()

    # Defino metodo para escribir número de tarjeta
    def numero_tarjeta(self, card_number):
        escribir_numero_de_tarjeta = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.input_numero_tarjeta))
        escribir_numero_de_tarjeta.send_keys(card_number)

    # Defino metodo para obtener el número la tarjeta
    def get_numero_de_tarjeta(self):
        #return self.driver.find_element(*self.input_codigo_tarjeta).get_property('value')
        numero_tarjeta = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_numero_tarjeta))
        return numero_tarjeta.get_property('value')

    # Defino el metodo para escribir el código de la tarjeta
    def codigo_tarjeta(self, card_code):
        escribir_codigo_de_tarjeta = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.input_codigo_tarjeta))
        escribir_codigo_de_tarjeta.send_keys(card_code)

    def get_codigo_de_tarjeta(self):
        #return self.driver.find_element(*self.input_codigo_tarjeta).get_property('value')
        numero_tarjeta = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_codigo_tarjeta))
        return numero_tarjeta.get_property('value')

    # Defino metodo para dar clic en cualquier parte de la pantalla y habilitar botón agregar tarjeta
    def dar_clic_en_cualquier_lugar_de_la_pantalla(self):
        clic_en_la_pantalla = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.espacio_tarjeta_codigo_boton))
        clic_en_la_pantalla.click()

   # Defino metodo para dar clic en botón agregar
    def agregar_tarjeta (self):
        clic_agregar = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.submit_tarjeta_button))
        clic_agregar.click()

   # Defino metodo para dar click en boton cerrar ventana del metodo de pago
    def metodo_de_pago(self):
        clic_boton_cerrar = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.cerrar_modal_pago_button))
        clic_boton_cerrar.click()


    def verifica_texto_campo_metodo_de_pago(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.verificar_tarjeta_agregar)).text

    '''
        Para ingresar la tarjeta como medio de pago, debemos realizar lo siguiente:
        1. Dar clic en el campo "método de pago"
        2. Dar clic en "agregar tarjeta"
        3. escribir el número de tarjeta.
        4. escribir el código de la tarjeta.
        5. Dar clic en cualquier zona de la pantalla.
        6. Dar clic en el botón agregar.
        7. Dar clic en el botón cerrar.
        '''

    def set_seleccionar_metodo_de_pago_tarjeta(self, card_number, card_code):
        self.clic_metodo_de_pago()
        self.medio_de_pago_tarjeta()
        self.numero_tarjeta(card_number)
        self.codigo_tarjeta(card_code)

    def close_seleccionar_metodo_de_pago_tarjeta(self):
        self.dar_clic_en_cualquier_lugar_de_la_pantalla()
        self.agregar_tarjeta()
        self.metodo_de_pago()

    # Envía mensaje al conductor
    def mensaje_para_el_conductor(self, message_for_driver):
        mensaje_conductor = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.input_comentarios))
        mensaje_conductor.send_keys(message_for_driver)

    # Defino metodo para obtener el mensaje al conductor
    def verifica_mensaje(self):
        return self.driver.find_element(*self.input_comentarios).get_property('value')

    # Solicitar manta y pañuelos
    def solicito_manta_y_pañuelos(self):
        activar_boton_manta_y_pañuelos = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.switch_manta_panuelos))
        activar_boton_manta_y_pañuelos.click()

    def check_swich_manta_y_pañuelos(self):
        check = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(self.verificar_swich_mantas_y_panuelos))
        return check.is_selected()
        #checkbox = self.driver.find_element(*self.verificar_swich_mantas_y_panuelos)
        #return checkbox.is_selected()

    # Solicitar helados
    def solicito_agregar_helados(self):
        boton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.incrementar_helados_button))
        boton.click()

    # Defino metodo para dar clic en el botón final de pedir un taxi
    def verifico_boton_pedir_taxi_enabled(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.boton_confirmar_pedido)).is_enabled()

    def clic_boton_final_pedir_un_taxi(self):
        clic_boton_pedir_un_taxi = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.boton_confirmar_pedido))
        clic_boton_pedir_un_taxi.click()

    def verifico_espera_contador(self):
        return WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located(self.grupo_botones_pedido)).is_displayed()

Feature: Crear un ticket

Scenario: se crea un ticket
  Given una lista de clientes y un producto
  When quiera informar un nuevo ticket de un producto
  Then deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario
  And se creara un ticket con estado "en curso"
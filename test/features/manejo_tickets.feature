Feature: Manejo de tickets
  Chequeando el manejo de tickets

Scenario: Creacion de ticket
    Given un cliente y un producto
    When quiera informar un nuevo ticket de un producto debere informar: <"nombre ticket">, <"severidad">, <"des problema">, <"des escenario">
    Then se creará un ticket con estado "Nuevo"


Scenario: Cambio de estado de un ticket
  Given Ticket con estado "En curso"
  When Se Completa un Ticket
  Then Ticket no debe tener estado "En curso"


  Scenario: Asignacion de un ticket a un producto
    Given una lista de clientes y un producto
    When quiera informar un nuevo ticket de un producto
    Then deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario
    And se creara un ticket con estado "en curso"

Feature: Manejo de tickets
  Chequeando el manejo de tickets

Scenario: Cambio de estado de un ticket
  Given Ticket con estado "En curso"
  When Se Completa un Ticket
  Then Ticket no debe tener estado "En curso"


  Scenario: Asignacion de un ticket a un producto
    Given una lista de clientes y un producto
    When quiera informar un nuevo ticket de un producto
    Then deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario
    And se creara un ticket con estado "en curso"


  Scenario: Creacion de un ticket
    Given un producto en especifico
    When trato de crear un ticket sin especificar su estado
    Then el ticket se creará con estado "nuevo".
Feature: Manejo de tickets
  Chequeando el manejo de tickets

Scenario Outline: Creacion de ticket
  Given un cliente y una version de producto
  When quiera informar un nuevo ticket de un producto debere informar: "<nombre_ticket>", "<severidad>", "<des_problema>", "<des_escenario>"
  Then se creará un ticket con "<estado>" Nuevo

  Examples: Ticket
		| nombre_ticket | severidad | des_problema | des_escenario | estado |
		| audio rapi    | s3		| no audio	   | se reincio    | Nuevo  |

Scenario Outline: Cambio de estado de un ticket
  Given Ticket con "<estado_curso>" "En curso"
  When Se Completa un Ticket
  Then Ticket debe tener "<estado_cerrado>" "Cerrado"

  Examples: Estados
		| estado_curso | estado_cerrado |
		| En curso     | Cerrado        |
  


#Scenario: Creo un ticket para un empleado que no se encuentra en la empresa
#  Given Soy empleado de mesa de ayuda
#  When Creo un ticket con un responsable asignado con id "1000"
#  And Ese responsable no se encuentra en el sistema
#  Then Se emite un error

#Scenario: Crear un ticket sin alguno de los atributos
#  Given Soy empleado de mesa de ayuda
#  When Creo un ticket sin alguno de los atributos obligatorios
#  Then El ticket no es creado
#  And Se emite un error


#  Scenario: Asignacion de un ticket a un producto
#    Given una lista de clientes y un producto
#    When quiera informar un nuevo ticket de un producto
#    Then deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario
#    And se creara un ticket con estado "en curso"

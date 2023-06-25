Feature: Creacion de tickets
  Chequeando creacion de tickets ...

Scenario Outline: Creacion de ticket
  Given un cliente y una version de producto
  When quiera informar un nuevo ticket de un producto debere informar: "<nombre_ticket>", "<severidad>", "<des_problema>", "<des_escenario>"
  Then se creará un ticket con "<estado>" Nuevo

  Examples: Ticket
		| nombre_ticket | severidad | des_problema | des_escenario | estado |
		| audio rapi    | s3		| no audio	   | se reincio    | Nuevo  |


Scenario Outline: Creo un ticket para un empleado que no se encuentra en la empresa
  Given Soy empleado de mesa de ayuda
  When Creo un ticket con un responsable asignado con id "<un_id>"
  And Ese responsable no se encuentra en el sistema
  Then Se emite un error

  Examples: Id
  | un_id |
  |1000|

#Scenario: Crear un ticket sin alguno de los atributos
#  Given Soy empleado de mesa de ayuda
#  When Creo un ticket sin alguno de los atributos obligatorios
#  Then El ticket no es creado
#  And Se emite un error


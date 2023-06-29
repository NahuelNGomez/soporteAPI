Feature: Creacion de tickets
  Chequeando creacion de tickets ...

Scenario Outline: Creacion de ticket
  Given un cliente y una version de producto
  When quiera informar un nuevo ticket de un producto debere informar: "<nombre_ticket>", "<severidad>", "<des_problema>", "<des_escenario>"
  Then se creará un ticket con "<estado>" Nuevo

  Examples: Ticket
		| nombre_ticket | severidad | des_problema | des_escenario | estado |
		| audio rapi    | s3		| no audio	   | se reincio    | Nuevo  |



Feature: Modificacion de un Ticket
  Chequeando modificacion de tickets ...

Scenario Outline: Se modifica un ticket existente
  Given un ticket cargado
  When busque un ticket por alguno de los filtros disponibles
  Then podre realizarle alguna modificacion de: "<nombre_ticket>", "<severidad>", "<des_problema>", "<des_escenario>", "<estado>"

  Examples: Ticket_modificado
		| nombre_ticket | severidad | des_problema | des_escenario | estado |
		| ticket modificado | S1 | problema de imagen | reinicio de nuevo | En curso |

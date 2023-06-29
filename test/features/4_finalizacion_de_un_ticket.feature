Feature: Finalizacion de un ticket
  Chequeando resolucion de tickets ...

Scenario Outline: Finalzacion de un ticket
  Given Ticket con "<estado_curso>" "En curso"
  When Se resuelva el problema
  Then Ticket debera tener el "<estado_cerrado>" "Cerrado"

  Examples: Estados
		| estado_curso | estado_cerrado |
		| En curso     | Cerrado        |
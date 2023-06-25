Feature: Visualizacion de tickets
  Chequeando filtro de tickets ...

  Scenario Outline: Se filtran algunos tickets
  Given que debo encontrar un ticket
  Then quiera encontrarlo
  When podre filtrar los tickets por: "<cliente_cuit>", "<severidad>", "<producto>", "<id_ticket>"

  Examples: ticket
  | cliente_cuit | severidad | producto | id_ticket |
  |	20-12345678-3 | S1		| producto_1 | 2	   |

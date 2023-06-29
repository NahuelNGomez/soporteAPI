Feature: Visualizacion de productos y versiones
  Chequeando las consultas de productos y versiones

Scenario: Se consultan productos y versiones existentes
  Given una lista de prodcutos y versiones
  When quiera conocer los productos y sus versiones disponibles
  Then se me informaran todos los productos con sus versiones disponibles


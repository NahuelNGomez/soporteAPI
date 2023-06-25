Feature: Derivacion de un ticket
	Cheaqueando derivacion de tickets ...

 Scenario: Se deriva un ticket mediante una tarea
	Given una tarea necesaria para resolver un ticket
	When se cree la tarea en el proyecto
	Then se podra vincular la tarea con el ticket
 
 Scenario: Se vinculan varias tareas a un ticket
	Given varias tareas necesarias para resolver un ticket
	When se creen las tareas en un proyecto
	Then se podran vincular a un ticket

 Scenario: Se Vincula una tarea con varios tickets
	Given una tarea necesaria para resolver varios tickets
	When se cree la tarea en un proyecto
	Then se podran vincular varios tickets con una tarea


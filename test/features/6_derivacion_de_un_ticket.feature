Feature: Derivacion de un ticket
	Cheaqueando derivacion de tickets ...

 Scenario: Se deriva un ticket mediante una tarea
	Given una tarea necesaria para resolver un ticket
	When se asigne la tarea al ticket
	Then se vinculara el ticket con la tarea
 
 Scenario: Se vinculan varias tareas a un ticket
	Given varias tareas necesarias para resolver un ticket
	When se asignen las tareas al ticket
	Then se vinculara el ticket con las tareas

 Scenario: Se Vincula una tarea con varios tickets
	Given una tarea necesaria para resolver varios tickets
	When se asigne la tarea a los tickets necesarios
	Then se vincularan los tickets con la tarea


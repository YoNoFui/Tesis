#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

Ver como se hace el fitness proporcional al numero de soluciones que domina 

def assign_proportional_fitness(population,fitness_options):
    total_fitness = 0
    for individual in population.get_individuals():
        #Asigning total fitness
        falta ver como se asigna el fitness proporcional

        current_fitness = individual.get_evaluated_function(x)

        individual.set_fitness(current_fitness)
        total_fitness += current_fitness 

    population.set_total_fitness(total_fitness)
    population.calculate_population_properties()


#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#El fitness proporcional es numero de soluciones que domina x a y 
#Malo si se usan pocos elementos


def assign_fitness(population,fitness_options):
    total_fitness = 0.0
    individuals = population.get_individuals()   
    for x in range(population.get_size()):
        current = individuals[x]
        for y in range(population.get_size()):        
            if y != x:
               dominated = individuals[y]
               #Less equal than
               let_condition = True
               #Less than                 
               lt_condition = True
               
               #Checking <=
               for z in range(population.get_length_vector_functions()):
                   current_value = current.get_evaluated_function(z)
                   dominated_value = dominated.get_evaluated_function(z)
                   if current_value > dominated_value:
                      let_condition = False
                      break     

               #Checking <
               for z in range(population.get_length_vector_functions()):
                   current_value = current.get_evaluated_function(z)
                   dominated_value = dominated.get_evaluated_function(z)
                   if current_value >= dominated_value:
                      lt_condition = False
                      break          
               
               if let_condition == True and lt_condition == True:
                  current.set_pareto_dominates(current.get_pareto_dominates() + 1)                   
         
        current.set_fitness(current.get_pareto_dominates())
        total_fitness += current.get_pareto_dominates()

    population.set_total_fitness(total_fitness)
    population.calculate_population_properties()


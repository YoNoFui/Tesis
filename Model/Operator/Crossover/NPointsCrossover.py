#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random

"""Método donde se implementa la cruza en n puntos. 
Algo importante a considerar es que si el tamaño del cromosoma de un Individuo 
es de "n", entonces el número máximo de puntos de cruza es "n-1"."""    
def execute_crossover_technique(chromosome_a,chromosome_b,crossover_options):     
    """Este método presenta básicamente 2 etapas, en la primera se utilizan
    valores aleatorios que simularán ser los puntos de , dependiendo
    del número de puntos de cruce (dado por el parámetro "puntos") serán los
    números al azar creados para simular cortes al azar; después cada punto
    de corte será agregado a una lista llamada "sections_list".
          
    Cabe mencionar que como medida de relajación de complejidad, considerando
    que para un cromosoma de length_chromosome "n" hay a lo más "n-1" puntos de cruce,
    entonces si se piden los "n-1" puntos de cruce, esto se toma como
    un caso especial y entonces se toma la lista "sections_list" con los 
    valores de 0 a n.
          
    Nota: se considera "n" y no "n-1" porque los rangos en una cadena tienen
    distintos índices que si tomamos un elemento de la misma. 
                    
    La segunda etapa ocurre cuando se cruzan los cromosomas; con base en la
    lista "sections_list" se toman secciones de los cromosomas y se cruzan
    entre sí. Al final habrán dos hijos.
          
    Es preciso mencionar que todo este proceso anterior describe a la cruza
    si el valor de la probabilidad es acertado, en otro caso no se hace
    nada y se regresan a los mismos cromosomas padres."""
          
    crossover_probability = crossover_options["probability_crossover_general"]    
    how_many_points = crossover_options["how_many_points_npoints_crossover"]
    

    """Se inicializan los cromosomas hijos, los cuales contendrán la información
    de la cruza entre los padres."""
    chromosome_son_1 = ""
    chromosome_son_2 = ""
           
    crossover_number = random.random()
          
    if crossover_number <= crossover_probability:
             my_chromosome_a = chromosome_a
             my_chromosome_b = chromosome_b
             mutated_chromosome_1 = [] 
             mutated_chromosome_2 = []
             length_chromosome = len(chromosome_a)
             sections_list = []
             flag = 0
           
             """Aquí se considera el caso en que el número de puntos de cruza sea
             "n-1", se utiliza una lista por comprensión para llenar la lista
             más rápidamente"""
             if length_chromosome == how_many_points + 1:
                real_sections_list = [x for x in range(length_chromosome + 1)]
             
             else: 
                sections_list.append(0)
                sections_list.append(length_chromosome)
                how_many_points_auxiliar = how_many_points
          
                while how_many_points_auxiliar != 0:
                      number = 1 + random.randint(0,length_chromosome - 2)
                
                      if not(number in sections_list):
                         sections_list.append(number) 
                         how_many_points_auxiliar -= 1            
                   
                real_sections_list = sorted(sections_list)
          
             for x in range(1,len(real_sections_list)):
                 #print "Limite_inferior: " + str(real_sections_list[x-1])
                 #print "Limite_superior: " + str(real_sections_list[x])
              
                 if flag == 0:
                    mutated_chromosome_1 += my_chromosome_a[real_sections_list[x-1]:real_sections_list[x]]
                    mutated_chromosome_2 += my_chromosome_b[real_sections_list[x-1]:real_sections_list[x]]
                    
                 
                 elif flag == 1:
                      mutated_chromosome_1 += my_chromosome_b[real_sections_list[x-1]:real_sections_list[x]]
                      mutated_chromosome_2 += my_chromosome_a[real_sections_list[x-1]:real_sections_list[x]]
                    
                 flag = (flag + 1) % 2        
 
             chromosome_son_1 = mutated_chromosome_1
             chromosome_son_2 = mutated_chromosome_2
              
    else:
        chromosome_son_1 = chromosome_a
        chromosome_son_2 = chromosome_b
              
    return [chromosome_son_1,chromosome_son_2]

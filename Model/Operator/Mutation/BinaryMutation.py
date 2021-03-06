#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín

import random as aleatorio

"""Recordar que 0.0 es el 0% y 1.0 es el 100%"""     
def execute_mutation_technique(chromosome,mutation_options):
    mutation_probability = mutation_options["probability_mutation_general"]
    mutated_chromosome = []  
    for gen in chromosome: 
        number = aleatorio.random()
        if number <= mutation_probability:
           if gen == 0:
              mutated_chromosome += [1]
        
           elif gen == 1:
              mutated_chromosome += [0]
             
        else:
            mutated_chromosome += [gen]       
             
    return mutated_chromosome

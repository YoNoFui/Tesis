#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio

def calculate_length_subchromosomes(vector_variables,decimal_precision,representation_options):
    return [1]*len(vector_variables)


def create_chromosome(length_subchromosomes,vector_variables,decimal_precision,representation_options):
    precision_string = "{0:." + str(decimal_precision) + "f}"
    chromosome = []
    for single_variable in vector_variables:     
        variable_range = single_variable[1]
        lower_limit = variable_range[0]
        upper_limit = variable_range[1]
        number = aleatorio.uniform(lower_limit,upper_limit)
        chromosome.append(float(precision_string.format(number)))

    return chromosome

def evaluate_subchromosomes(complete_chromosome,length_subchromosomes,vector_variables,decimal_precision,representation_options): 
    value = 0
    variable_name = ""
    single_variable = ""
    variable_name = ""
    decision_variables = {}
    for i in range(len(complete_chromosome)):
        value = complete_chromosome[i]
        single_variable = vector_variables[i]
        variable_name = single_variable[0]
        decision_variables[variable_name] = value

    return decision_variables 

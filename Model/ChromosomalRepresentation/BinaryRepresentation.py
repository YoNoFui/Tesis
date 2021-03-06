#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math
import random

"""Método que calcula la longitud de todos los subcromosomas. Para ello
se hace uso del vector de rangos, así como de la precisión decimal."""
def calculate_length_subchromosomes(vector_variables,decimal_precision,representation_options):
    true_decimal_precision = 10**decimal_precision
    lower_limit = -1
    upper_limit = -1
    amount = -1
    how_many_bits_around = -1
    how_many_bits_real = -1
    length_subchromosomes = []
    #contador = 0
    for single_variable in vector_variables:
        variable_range = single_variable[1]
        #print "Hola",contador," ",my_range
        #contador+=1
        lower_limit = variable_range[0]
        upper_limit = variable_range[1]
        #print "Lower: ",lower_limit
        #print "Upper: ",upper_limit 
        amount = (upper_limit - lower_limit)*true_decimal_precision
        #print "Amount: ",amount
        how_many_bits_around = math.log(amount,2) 
        #print "Mas o menos: ",how_many_bits_around
        how_many_bits_real = int(math.ceil(how_many_bits_around))
        #print "Real: ",how_many_bits_real
        length_subchromosomes.append(how_many_bits_real)
        #print "----------------------------------------------"

    return length_subchromosomes



"""Método que crea un cromosoma binario completo con base en subcromosmas."""
def create_chromosome(length_subchromosomes,vector_variables,decimal_precision,representation_options):
    final_chromosome = []
    for length_subchromosome in length_subchromosomes:
        chromosome = [] 
        for x in range(0,length_subchromosome):
            number = random.randint(0,1)
            chromosome.append(number)

        final_chromosome += chromosome
         
    return final_chromosome


def binary_to_decimal(chromosome):
    m = len(chromosome) - 1
    number = 0
    for i in range (m,-1,-1):
        number += chromosome[m-i]*(2**i)
          
    return number


def evaluate_subchromosomes(complete_chromosome,length_subchromosomes,vector_variables,decimal_precision,representation_options): 
    lower_limit = 0
    upper_limit = 0
    subchromosome = []
    variable_range = []
    variable_name=""
    decision_variables = {}    
    precision_string = "{0:." + str(decimal_precision) + "f}"
    gray_coding = representation_options["gray_coding_binary_representation"]
    for i in range (0,len(length_subchromosomes)):
        m = length_subchromosomes[i]
        single_variable = vector_variables[i]
        variable_name = single_variable[0]
        variable_range = single_variable[1]        
        a = variable_range[0]
        b = variable_range[1]
        upper_limit += m
        subchromosome = complete_chromosome[lower_limit:upper_limit]
        #print "El subcromosoma del agente: ",self.__individual_id," es:",subchromosome
        if gray_coding == True:
           gray_subchromosome = [subchromosome[0]]
           for j in range (1,len(subchromosome)):
               gray_subchromosome.append(subchromosome[j]^subchromosome[j-1])
                     
           subchromosome = gray_subchromosome   
                          
        decimal_number = binary_to_decimal(subchromosome)
        number = a + (decimal_number*((b-a)/((2.0**m) - 1)))
        #print "El number del agente ", self.__individual_id, " es: ",number             
              
        decision_variables[variable_name] = float(precision_string.format(number))
        lower_limit = upper_limit

    return decision_variables

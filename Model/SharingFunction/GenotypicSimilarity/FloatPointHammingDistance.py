#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

def calculate_distance(individual_i,individual_j,shared_fitness_options):
    chromosome_i = individual_i.get_complete_chromosome()
    chromosome_j = individual_j.get_complete_chromosome()
    hamming_distance = 0.0
    epsilon = shared_fitness_options["epsilon_floatpoint_hamming_distance"]

    for x in range (len(chromosome_i)):
        gen_i = chromosome_i[x]
        gen_j = chromosome_j[x]
        if abs(gen_i - gen_j) < epsilon:
           hamming_distance += 1

    return hamming_distance
     

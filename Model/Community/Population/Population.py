#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math as m
import random as r
import Individual as i

falta el numero de elitismos.
Conviene ordenar a los elementos por fitness para así hacer el elitismo de n n metodos.
El elitismo hay que ponerlo en blackboard.


class Population:
      #fitness options, en caso de que se requiera se añaden elementos adicionales en fitness options.
      #There's no need for using the population size as a parameter, because we already have the chromosome_set.
      #The complete population flag will be used in the corresponding methods, not here.
      """Método para inicializar los elementos de la Poblacion."""
      def __init__(self,representation,chromosome_set,length_subchromosomes,decimal_precision,vector_functions,vector_ranges,fitness_class,fitness_method,fitness_options):
          
          
          #valor que se usa muchas veces, por eso se pone como atributo.  
          self.__length_vector_functions = len(vector_functions)

          self.__representation = representation
          self.__population_size = len(chromosome_set)
          self.__length_subchromosomes = length_subchromosomes
          self.__decimal_precision = decimal_precision
          self.__vector_functions = vector_functions
          self.__vector_ranges = vector_ranges          
          self.__population = []
          self.__total_fitness = [0]*self.__length_vector_functions
          self.__total_expected_values = [0]*self.__length_vector_functions
          
          self.__initialize(chromosome_set)
          self.__assign_fitness(fitness_mode,fitness_options_extra)
          

      """Método que inicializa una Población con base en el tamaño (número de Individuos)
      el vector de funciones y el vector de rangos."""
      def __initialize(self,chromosome_set):
          for chromosome in chromosome_set:
              self.__population.append(i.Individual(self.__representation,chromosome,self.__decimal_precision,self.__length_subchromosomes,self.__vector_functions,self.__vector_ranges))
          

      def __assign_fitness(self,fitness_method,fitness_options):
          getattr(st,selection_method)(population,fitness_options)
                
         
          for individual in self.__population:
              for x in range (self.__length_vector_functions):
                  #Assigning selection probability
                  individual.set_selection_probability(x,individual.get_fitness(x)/self.__total_fitness[x])
                  #Assigning expected value.
                  individual.set_expected_value(x,individual.get_fitness(x)/(self.__total_fitness[x]/self.__population_size))
                  #Assigning total expected value
                  self.__total_expected_values[x] += individual.get_expected_value(x)        


      def get_length_vector_functions(self):
          return self.__length_vector_functions

      def get_population_size(self):
          return self.__population_size

      def get_total_fitness(self,position):
          return self.__total_fitness[position]

      def set_total_fitness(self,position,value):
          self.__total_fitness[position] = value

      def get_total_expected_value(self,position):
          return self.__total_expected_values[position]

      def get_population(self):
          return self.__population

      #No lo estás evaluando, pero a la siguiente vuelta de la generación se evalúa.
      def set_individual(self,position,new_individual):
          self.__population[position] = new_individual


      #calcular la posicion del peor individuo en el fitness mode  
      def get_position_worst_individual(self,fitness_position):
          pivot = self.__population[0]
          position = 0
          for x in range (1,self.__population_size):
              provisional = self.__population[x]
              if pivot.get_fitness(fitness_position) > provisional.get_fitness(fitness_position):
                 pivot = provisional
                 position = x

          return position


      #poner el mejor individuo en el fitness mode
      def get_best_individual(self,fitness_position):
          pivot = self.__population[0]
          position = 0
          for x in range (1,self.__population_size):
              provisional = self.__population[x]
              if pivot.get_fitness(fitness_position) < provisional.get_fitness(fitness_position):
                 pivot = provisional
                 position = x

          return pivot
             
     
      def print_population(self):
          print "Total fitness: " + str(self.__total_fitness)
          print "Total expected value: " + str(self.__total_expected_values)
          print "Individuals: "
          for x in range (self.__population_size):
              print "Number: " + str(x)
              self.__population[x].print_info()      
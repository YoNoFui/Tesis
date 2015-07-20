#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import Population.Population as poblacion

#asignar fitness implica de una vez evaluar en funciones objetivo.
#Cambiarle nombre a length subchromosomes
class Community:
      def __init__(self,vector_functions,vector_variables,available_expressions,decimal_precision,representation_instance,representation_options,fitness_instance,fitness_method,fitness_options,selection_instance,selection_method,selection_options,crossover_instance,crossover_method,crossover_options,mutation_instance,mutation_method,mutation_options):
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables
          self.__available_expressions = available_expressions
          self.__decimal_precision = decimal_precision
          self.__representation_instance = representation_instance
          self.__representation_options = representation_options
          self.__fitness_instance = fitness_instance
          self.__fitness_method = fitness_method
          self.__fitness_options = fitness_options
          self.__selection_instance = selection_instance
          self.__selection_method = selection_method
          self.__selection_options = selection_options
          self.__crossover_instance = crossover_instance
          self.__crossover_method = crossover_method
          self.__crossover_options = crossover_options
          self.__mutation_instance = mutation_instance
          self.__mutation_method = mutation_method
          self.__mutation_options = mutation_options
          
          #Agregados para el create population.
          self.__length_chromosomes = []


      def init_population(self,population_size):
          population = []
          chromosome = []
          self.__length_subchromosomes = getattr(self.__representation_instance,"calculate_length_subchromosomes")(self.__vector_variables,self.__decimal_precision,self.__representation_options)              
          population = poblacion.Population(population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          for x in range (population_size):
              complete_chromosome =  getattr(self.__representation_instance,"create_chromosome")(self.__length_subchromosomes,self.__decimal_precision,self.__vector_variables,self.__representation_options)
              population.add_individual(x,complete_chromosome)
  
          return population


      def create_population(self,set_chromosomes):
          population = poblacion.Population(len(set_chromosomes),self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          for x in range(len(set_chromosomes)):
              population.add_individual(x,set_chromosomes[x])

          return population

    
      #This evaluates only functions
      def __evaluate_population_functions(self,population):
          complete_chromosome = ""
          decision_variables = {}
          individuals = population.get_population()
          #print "Len individuals: ",len(individuals)
          #print "Individuals: ", individuals
          for individual in individuals:
              complete_chromosome = individual.get_complete_chromosome()          
              decision_variables = getattr(self.__representation_instance,"evaluate_subchromosomes")(complete_chromosome,self.__length_subchromosomes,self.__vector_variables,self.__decimal_precision,self.__representation_options)
              individual.evaluate_functions(decision_variables)


      def assign_population_fitness(self,population):
          self.__evaluate_population_functions(population)
          getattr(self.__fitness_instance,self.__fitness_method)(population,self.__fitness_options)
          

      def evolve_next_generation(self,parents,position):
          size = parents.get_population_size()
          children = poblacion.Population(size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          selected_parents_chromosomes = getattr(self.__selection_instance,self.__selection_method)(parents,position,self.__selection_options)
          print "Len: ", len(selected_parents_chromosomes)   
          for x in range(1,size,2):
              #print "Perro: ", x
              chromosome_a = selected_parents_chromosomes[x - 1]
              chromosome_b = selected_parents_chromosomes[x]
              [child_1,child_2] = getattr(self.__crossover_instance,self.__crossover_method)(chromosome_a,chromosome_b,self.__crossover_options)
              modified_child_1 = getattr(self.__mutation_instance,self.__mutation_method)(child_1,self.__mutation_options)
              modified_child_2 = getattr(self.__mutation_instance,self.__mutation_method)(child_2,self.__mutation_options)
              children.add_individual(x - 1,modified_child_1)
              children.add_individual(x,modified_child_2)

          return children


      def elitism(self,parents,children,function,position,is_descendent,elitism_amount):
          parents.sort_individuals(function,position,is_descendent)
          children.sort_individuals(function,position,is_descendent)
          parents_population = parents.get_population()
          offset = parents.get_population_size() - elitism_amount
          for x in range(0,elitism_amount):
              parent_complete_chromosome = parents_population[x].get_complete_chromosome()
              children.add_individual(x + offset,parent_complete_chromosome)


      def get_best_individual(self,population,position):
          individuals = population.get_population()
          best_individual = individuals[0].get_decision_variables()

          return best_individual 

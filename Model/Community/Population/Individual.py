#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import math


#Decimal precision used as a parameter because python doesnt want to truncate precision by itself.     
class Individual:
      def __init__(self,complete_chromosome,vector_functions,available_expressions,decimal_precision):
          self.__complete_chromosome = complete_chromosome
          self.__vector_functions = vector_functions
          self.__available_expressions = available_expressions
          self.__precision_string = "{0:." + str(decimal_precision) + "f}"

          self.__decision_variables = {}
          self.__evaluated_functions = []
          self.__fitness = [0]*len(vector_functions)
          self.__selection_probabilities = [0]*len(vector_functions)
          self.__expected_values = [0]*len(vector_functions)
                    

      def get_complete_chromosome(self):
          return self.__complete_chromosome

      def get_decision_variables(self):
          return self.__decision_variables
           

      def get_evaluated_function(self,position):
          return self.__evaluated_functions[position]

      
      def get_fitness(self,position):
          return self.__fitness[position]


      def set_fitness(self,position,value):
          self.__fitness[position] = value     


      def get_selection_probability(self,position):
          return self.__selection_probabilities[position]

      
      def set_selection_probability(self,position,value):
          self.__selection_probabilities[position] = value
      
     
      """Número de copias"""    
      def get_expected_value(self,position):
          return self.__expected_values[position]


      def set_expected_value(self,position,value):
          self.__expected_values[position]= value
   

      # Expressions = variables + constants + user built-in functions
      def __evaluate_single_function(self,function,expressions): 
          evaluation = eval(function,expressions)
          return float(self.__precision_string.format(evaluation))


      def evaluate_functions(self,decision_variables):
          self.__decision_variables = decision_variables
          #print "Decision variables: ", self.__decision_variables
          all_expressions = {}
          all_expressions.update(self.__decision_variables)
          all_expressions.update(self.__available_expressions)
          #print "All expressions: ", all_expressions
          #print "Available expressions: ",self.__available_expressions
          for function in self.__vector_functions:
              result = self.__evaluate_single_function(function,all_expressions)
              self.__evaluated_functions.append(result)
                            

      def print_info(self):
           print "    Complete chromosome: " + str(self.__complete_chromosome)
           print "    Decision variables: " + str(self.__evaluated_subchromosomes)
           print "    Evaluated functions: " + str(self.__evaluated_functions)
           print "    Fitness: " + str(self.__fitness)
           print "    Selection probabilites: " + str(self.__selection_probabilities)
           print "    Expected values: " + str(self.__expected_values)
           print "\n"

#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

import random as aleatorio
import Population.Population as poblacion

#cambiar los imports por palabras en español para hacer la diferencia.          
#asignar fitness implica de una vez evaluar en funciones objetivo.
#Cambiarle nombre a length subchromosomes
class Community:
      def __init__(self,vector_functions,vector_variables,available_expressions,decimal_precision,representation_instance,representation_options,
                   fitness_instance,fitness_options,shared_fitness_instance,shared_fitness_options,selection_instance,selection_options,
                   crossover_instance,crossover_options,mutation_instance,mutation_options):

          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables
          self.__available_expressions = available_expressions
          self.__decimal_precision = decimal_precision
          self.__representation_instance = representation_instance
          self.__representation_options = representation_options
          self.__fitness_instance = fitness_instance
          self.__fitness_options = fitness_options
          self.__shared_fitness_instance = shared_fitness_instance 
          self.__shared_fitness_options = shared_fitness_options
          self.__selection_instance = selection_instance
          self.__selection_options = selection_options
          self.__crossover_instance = crossover_instance
          self.__crossover_options = crossover_options
          self.__mutation_instance = mutation_instance
          self.__mutation_options = mutation_options
          
          #Agregados para el create population.
          self.__length_chromosomes = []


      def init_population(self,population_size):
          population = []
          chromosome = []
          self.__length_subchromosomes = getattr(self.__representation_instance,"calculate_length_subchromosomes")(self.__vector_variables,self.__decimal_precision,self.__representation_options)              
          population = poblacion.Population(population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          for x in range (population_size):
              complete_chromosome =  getattr(self.__representation_instance,"create_chromosome")(self.__length_subchromosomes,self.__vector_variables,self.__decimal_precision,self.__representation_options)
              population.add_individual(x,complete_chromosome)
  
          return population


      def create_population(self,set_chromosomes):
          population = poblacion.Population(len(set_chromosomes),self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)
          for x in range(len(set_chromosomes)):
              population.add_individual(x,set_chromosomes[x])

          return population

    
      #This evaluates only functions
      def evaluate_population_functions(self,population):
          complete_chromosome = ""
          decision_variables = {}
          individuals = population.get_individuals()
          for individual in individuals:
              complete_chromosome = individual.get_complete_chromosome()          
              decision_variables = getattr(self.__representation_instance,"evaluate_subchromosomes")(complete_chromosome,self.__length_subchromosomes,self.__vector_variables,self.__decimal_precision,self.__representation_options)
              individual.evaluate_functions(decision_variables)


      def calculate_population_pareto_dominance(self,population):
          individuals = population.get_individuals()
          for x in range(population.get_size()):
              current = individuals[x]
              for y in range(population.get_size()):      
                  if y != x:
                     about_being_dominated = individuals[y]
                     #Less equal than
                     let_condition = True
                     #Less equal                 
                     lt_condition = True
               
                     #Checking <=
                     for z in range(population.get_length_vector_functions()):
                         current_value = current.get_evaluated_function(z)
                         about_being_dominated_value = about_being_dominated.get_evaluated_function(z)
                         if current_value > about_being_dominated_value:
                            let_condition = False
                            break    
               
                     #Checking <
                     for z in range(population.get_length_vector_functions()):
                         current_value = current.get_evaluated_function(z)
                         dominated_value = about_being_dominated.get_evaluated_function(z)
                         if current_value >= about_being_dominated_value:
                            lt_condition = False
                            break    
               
                     #It means that about-being-dominated is dominated by current
                     #And current dominates about-being-dominated.
                     if let_condition == True and lt_condition == True:
                        current.set_pareto_dominates(current.get_pareto_dominates() + 1)
                        about_being_dominated.set_pareto_dominated(about_being_dominated.get_pareto_dominated() + 1)
           


      #Menos dominados -> mayor fitness -> ultima posicion
      def assign_rank_based_on_pareto_dominance(self,population):
          total_fitness = 0.0
          position = 0
          position_dictionary = {}
          #Primero asignar el rango como fitness   
          for individual in population.get_individuals():
              individual.set_fitness(1 + individual.get_pareto_dominated())
    
          #Ordenar descendente con base en el rango (que es el fitness).
          population.sort_individuals("get_fitness",True)

          #Asignar fitness de acuerdo a una funcion lineal (y=x)
          for individual in population.get_individuals():
              if position_dictionary.has_key(individual.get_fitness()):
                 position_dictionary[individual.get_fitness()].append(position)
     
              else:
                 position_dictionary[individual.get_fitness()] = []

              individual.set_fitness(position + 1)
              position += 1

          #promediar los fitness con los mismos rangos
          individuals = population.get_individuals()
          for key in position_dictionary.keys():
              positions = position_dictionary[key]
              total = len(positions)
              sume = 0.0
        
              #Getting sume of fitnesses.    
              for position in positions:
                  sume += individuals[position].get_fitness()
                 
              #Setting average of fitnesses.
              for extra_position in positions:
                  individuals[extra_position].set_fitness(sume/total)
                  total_fitness += individuals[extra_position].get_fitness()
        

          population.set_total_fitness(total_fitness) 
          population.calculate_population_properties()


      def assign_population_fitness(self,population):
          getattr(self.__fitness_instance,"assign_fitness")(population,self.__fitness_options)
  

      def __using_sharing_function(self,individual_i,individual_j):
            sigma = self.__shared_fitness_options["sigma_sharing_function"]
            alpha_sharing_function = self.__shared_fitness_options["alpha_sharing_function"]
            result = 0.0
            dij = getattr(self.__shared_fitness_instance,"calculate_distance")(individual_i,individual_j,self.__shared_fitness_options)
            if dij < sigma:
               result = 1 - (dij/sigma)**alpha_sharing_function

            return result
        

      def calculate_population_niche_count(self,population):
          for individual_i in population.get_individuals():
              result = 0.0
              for individual_j in population.get_individuals():
                  if individual_i != individual_j:
                     result += self.__using_sharing_function(individual_i,individual_j)
        
              individual_i.set_niche_count(result)
              

      def calculate_population_shared_fitness(self,population):
          for individual in population.get_individuals():
              individual.set_fitness(individual.get_fitness()/individual.get_niche_count())          
 
  
      def execute_selection(self,parents):
          return getattr(self.__selection_instance,"execute_selection_technique")(parents,self.__selection_options)
      

      def execute_crossover_and_mutation(self,selected_parents_chromosomes):
          size = len(selected_parents_chromosomes)          
          children = poblacion.Population(size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__decimal_precision)

          #Si se tiene una población impar simplemente se añade un elemento al azar de los seleccionados automáticamente a la siguiente generación
          if size % 2 != 0:
             size -= 1  
             index = aleatorio.randint(0,size)
             lucky_chromosome = selected_parents_chromosomes[index]
             selected_parents_chromosomes.remove(selected_parents_chromosomes[index])
             modified_lucky_chromosome = getattr(self.__mutation_instance,"execute_mutation_technique")(lucky_chromosome,self.__mutation_options)
             children.add_individual(size,modified_lucky_chromosome)
          
          count = 0
          for x in range(1,size,2):
              chromosome_a = selected_parents_chromosomes[x - 1]
              chromosome_b = selected_parents_chromosomes[x]
              [child_1,child_2] = getattr(self.__crossover_instance,"execute_crossover_technique")(chromosome_a,chromosome_b,self.__crossover_options)
              modified_child_1 = getattr(self.__mutation_instance,"execute_mutation_technique")(child_1,self.__mutation_options)
              modified_child_2 = getattr(self.__mutation_instance,"execute_mutation_technique")(child_2,self.__mutation_options)
              children.add_individual(x - 1,modified_child_1)
              children.add_individual(x,modified_child_2)
              count +=2

          return children
      

      def elitism(self,parents,children,function,is_descendent,elitism_amount):
          parents.sort_individuals(function,is_descendent)
          children.sort_individuals(function,is_descendent)
          parents_population = parents.get_individuals()
          offset = parents.get_size() - elitism_amount
          for x in range(0,elitism_amount):
              parent_complete_chromosome = parents_population[x].get_complete_chromosome()
              children.add_individual(x + offset,parent_complete_chromosome)


          #Verificar al mejor de la poblacion, probablemente no siempre sea el elemetno 0
      def get_best_individual(self,population,position):
          individuals = population.get_individuals()
          best_individual = individuals[0].get_decision_variables()

          return best_individual 

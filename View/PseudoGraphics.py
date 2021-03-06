#!/usr/bin/python
#-*- coding: utf-8 -*-

#Version 2.0
#Author: Castillo Medina Aarón Martín.

#Agregado
#Clase que será por ahora la parte "gráfica" del programa.

import Controller.Controller as controlador
import math

def start_sequence():
    variables = "Variables.xml"
    functions = "Functions.xml"
    features = "Features.xml"
    settings = "Settings.xml"

    generations = 4
    population_size = 10
    vector_functions = ["12*(x-y)","pi**y","11*(x+y)"]
    vector_variables = [["x",[-5,7]],["y",[3,6]],["z",[-8,-2]]]
    available_expressions = {"pi":math.pi,"cos":math.cos}#,"hola":math.tan}
    decimal_precision = 4
    community_class = "Model.Community.Community"
    #algorithm_class = "Model.MOEA.VEGA"
    #algorithm_class = "Model.MOEA.MOGA"
    #algorithm_class = "Model.MOEA.SPEAII"
    algorithm_class = "Model.MOEA.NSGAII"
    
    algorithm_options = {"length_external_set_e_spea_ii":6}

    #representation_class = "Model.ChromosomalRepresentation.BinaryRepresentation"
    representation_class = "Model.ChromosomalRepresentation.FloatPointRepresentation"
    representation_options  = {"gray_coding_binary_representation":False}
 
 
    #fitness_class = "Model.Fitness.LinearRankingFitness"
    fitness_class = "Model.Fitness.LinearScalingFitness"
    #fitness_class = "Model.Fitness.NonLinearRankingFitness"
    #fitness_class = "Model.Fitness.ProportionalFitness"
    fitness_options = {"sp_linear_ranking_fitness":0.5,
                       "alpha_linear_scaling_fitness":1,
                       "beta_linear_scaling_fitness":0.5,
                       "sp_non_linear_ranking_fitness":0.5}


    #shared_fitness_class = "Model.SharingFunction.GenotypicSimilarity.BinaryHammingDistance"
    shared_fitness_class = "Model.SharingFunction.GenotypicSimilarity.FloatPointHammingDistance"
    #shared_fitness_class  = "Model.SharingFunction.PhenotypicSimilarity.EuclideanDistance"
    shared_fitness_options = {"alpha_sharing_function":5,
                              "sigma_sharing_function":800,
                              "epsilon_floatpoint_hamming_distance":0.5}


    #revisar por qué no dan los individuos que deben
    #selection_class = "Model.Operator.Selection.Roulette" 
    #selection_class = "Model.Operator.Selection.StochasticUniversalSampling"
    selection_class = "Model.Operator.Selection.ProbabilisticTournament"
    selection_options = {"contenders_amount_probabilistic_tournament":8}
    
    #crossover_class = "Model.Operator.Crossover.UniformCrossover"
    #crossover_class = "Model.Operator.Crossover.NPointsCrossover"
    crossover_class = "Model.Operator.Crossover.FloatPointCrossover"
    crossover_options = {"probability_crossover_general":0.70,
                         "how_many_points_npoints_crossover":2,
                         "flip_floatpoint_crossover":0.50,
                         "pmask_uniform_crossover":0.5}
    
    #mutation_class = "Model.Operator.Mutation.BinaryMutation"
    mutation_class = "Model.Operator.Mutation.FloatPointMutation"
    mutation_options = {"probability_mutation_general":0.08,
                        "decimal_precision_floatpoint_mutation":decimal_precision,
                        "vector_variables_floatpoint_mutation":vector_variables}
    
    elitism_amount = 1

    print controlador.execute_algorithm(generations,population_size,vector_functions,vector_variables,available_expressions,decimal_precision,
                                        community_class,algorithm_class,algorithm_options,representation_class,representation_options,
                                        fitness_class,fitness_options,shared_fitness_class,shared_fitness_options,selection_class,selection_options,
                                        crossover_class,crossover_options,mutation_class,mutation_options,elitism_amount)

    #print con.save_settings("Mutation","Otro","aaron","Hola")
    #print con.delete_settings("Mutation","Otro","aaron","Hola")





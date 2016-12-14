#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:14:02 2016

@author: Joaquin & Josef
"""

import numpy as np
import pandas as pd
import networkx as nx
import pylab as pl


friends = pd.read_csv("/Users/joaquincoitino/Desktop/peoplepickinganonymisedwoselfvotes.csv", header=0, index_col=0)

cosine_similarity = pd.read_csv("/Users/joaquincoitino/Desktop/GroupProjectCosineSimilarityExcelTable.csv", header=0, index_col=0)

       
def mean(numbers):
   return float(sum(numbers)) / max(len(numbers), 1)     


### Average PageRank for Creativity:

creat_pagerank = pd.read_csv("/Users/joaquincoitino/Desktop/CreativityPageRank.csv", usecols = ['x'])

creat_adj_matrix = friends.loc[:,'creat_01':'creat_60'].as_matrix()

creat_graph = nx.from_numpy_matrix(creat_adj_matrix, create_using = nx.DiGraph())

creat_pr_successors = []

for i in creat_graph.nodes_iter():
    list_pr =[]

    for j in creat_graph.successors(i):
        list_pr.append(creat_pagerank.loc[j,'x'])
    creat_pr_successors.append(mean(list_pr))
    
   
### Average PageRank for Influence:
    
infl_pagerank = pd.read_csv("/Users/joaquincoitino/Desktop/InfluencePageRank.csv", usecols = ['x'])

infl_adj_matrix = friends.loc[:,'infl_01':'infl_60'].as_matrix()

infl_graph = nx.from_numpy_matrix(infl_adj_matrix, create_using = nx.DiGraph())

infl_pr_successors = []

for i in infl_graph.nodes_iter():
    list_pr =[]

    for j in infl_graph.successors(i):
        list_pr.append(infl_pagerank.loc[j,'x'])
    infl_pr_successors.append(mean(list_pr))


### Average PageRank for Implementation:
    
impl_pagerank = pd.read_csv("/Users/joaquincoitino/Desktop/ImplementationPageRank.csv", usecols = ['x'])

impl_adj_matrix = friends.loc[:,'impl_01':'impl_60'].as_matrix()

impl_graph = nx.from_numpy_matrix(impl_adj_matrix, create_using = nx.DiGraph())

impl_pr_successors = []

for i in impl_graph.nodes_iter():
    list_pr =[]

    for j in impl_graph.successors(i):
        list_pr.append(impl_pagerank.loc[j,'x'])
    impl_pr_successors.append(mean(list_pr)) 

    
### Average pagerank for all categories

avg_pagerank_succe = [(x+y+z)/3 for x,y,z in zip(creat_pr_successors, infl_pr_successors, impl_pr_successors)]
    
### Frienship indegree

friend_adj_matrix = friends.loc[:,'friend_01':'friend_60'].as_matrix()

friend_graph = nx.from_numpy_matrix(friend_adj_matrix, create_using = nx.DiGraph())

friend_indegree = friend_graph.in_degree()

list_f_indegree = []

for i in friend_indegree:
    list_f_indegree.append(friend_indegree[i])

## pagerank/degree ratio

ratio_pr_findegree_creat = [x/y for x, y in zip(creat_pagerank.loc[:,'x'], list_f_indegree)]
ratio_pr_findegree_infl = [x/y for x, y in zip(infl_pagerank.loc[:,'x'], list_f_indegree)]
ratio_pr_findegree_impl = [x/y for x, y in zip(impl_pagerank.loc[:,'x'], list_f_indegree)]
                           
cosine = cosine_similarity.loc[:,'Score'].tolist()

pr_creat = creat_pagerank.loc[:,'x'].tolist()
pr_infl = infl_pagerank.loc[:,'x'].tolist()
pr_impl = impl_pagerank.loc[:,'x'].tolist()
                           
creat_dataframe = pd.DataFrame.from_items([('id', list(range(1,61))), ('Creativity Page Rank', pr_creat), ('Cosine similarity', cosine), ('Overall Average Page Rank of Successors', avg_pagerank_succe), ('Average Creativity Page Rank Successors', creat_pr_successors), ('Frienship indegree', list_f_indegree), ('Creativity Ratio', ratio_pr_findegree_creat)])
creat_dataframe.to_csv('Creativity Table.csv', index = False)

infl_dataframe = pd.DataFrame.from_items([('id', list(range(1,61))), ('Influence Page Rank', pr_infl), ('Cosine similarity', cosine), ('Overall Average Page Rank of Successors', avg_pagerank_succe), ('Average Influence Page Rank Successors', infl_pr_successors), ('Frienship indegree', list_f_indegree), ('Influence Ratio', ratio_pr_findegree_infl)])
infl_dataframe.to_csv('Influence Table.csv', index = False)

impl_dataframe = pd.DataFrame.from_items([('id', list(range(1,61))), ('Implementation Page Rank', pr_impl), ('Cosine similarity', cosine), ('Overall Average Page Rank of Successors', avg_pagerank_succe), ('Average Implementation Page Rank Successors', impl_pr_successors), ('Frienship indegree', list_f_indegree), ('Implementation Ratio', ratio_pr_findegree_impl)])
impl_dataframe.to_csv('Implementation Table.csv', index = False)
# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Ya1M9wGC4fhc4g25vb2lW_KkXeUO_vf
"""

!pip install networkx==2.3

import networkx as ntw
import json
import matplotlib.pyplot as plt

with open('ProVtweets3.json', 'r') as f:
  data = json.load(f)

data[0]

print(type(data))

G = ntw.Graph()

for tweet in data:
  G.add_nodes_from(tweet['id_str'])

for tweet in data:
  for mentions in tweet['entities']['user_mentions']:
    G.add_edge(mentions['id_str'],tweet['id_str'])

ntw.draw(
    G,cmap=plt.cm.PiYG, edge_color="green", linewidths=0.3, node_size=6, alpha=0.6, with_labels=False
)

largest_subgraph = max(ntw.connected_component_subgraphs(G), key=len)



ntw.draw(largest_subgraph,cmap=plt.cm.PiYG, edge_color="black", linewidths=0.3, node_size=[v * 10 for v in d.values()], alpha=0.6, with_labels=False)

G = ntw.Graph()

for tweet in data:
  G.add_nodes_from(tweet['id_str'])

for tweet in data:
  for user_mentions in tweet['entities']['user_mentions']:
    G.add_edge(user_mentions['id_str'],tweet['id_str'])

ntw.draw(
    G,cmap=plt.cm.PiYG, 
edge_color="black", linewidths=0.3, node_size=6, alpha=0.6, with_labels=False
)

largest_subgraph = max(ntw.connected_component_subgraphs(G), key=len)

ntw.draw(largest_subgraph,cmap=plt.cm.PiYG, edge_color="green", linewidths=0.3, node_size=60, alpha=0.6, with_labels=True)

import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()

plot_degree_dist(nx.gnp_random_graph(100, 0.5, directed=True))

d = dict(largest_subgraph.degree)

ntw.draw(largest_subgraph,cmap=plt.cm.PiYG, edge_color="black", linewidths=0.3, node_size=[v * 10 for v in d.values()], alpha=0.6, with_labels=False)

import json

with open('AntiVtweets3.json', 'r') as f:
  Adata = json.load(f)

A = ntw.Graph()

for tweet in data:
  A.add_nodes_from(tweet['id_str'])

for tweet in data:
  for user_mentions in tweet['entities']['user_mentions']:
    A.add_edge(user_mentions['id_str'],tweet['id_str'])

ntw.draw(
    A,cmap=plt.cm.PiYG, edge_color="black", linewidths=0.3, node_size=6, alpha=0.6, with_labels=False
)

#node size based on number of followers?

A_largest_subgraph = max(ntw.connected_component_subgraphs(A), key=len)

ntw.draw(A_largest_subgraph,cmap=plt.cm.PiYG, edge_color="blue", linewidths=0.3, node_size=60, alpha=0.6, with_labels=False)

sorted(ntw.connected_component_subgraphs(A), key = len, reverse=True)

f=0

for cc in sorted(ntw.connected_component_subgraphs(A), key = len, reverse=True):
    if cc.number_of_nodes()>10 :
        ntw.draw(cc ,cmap=plt.cm.PiYG, edge_color="blue", linewidths=0.3, node_size=60, alpha=0.6, with_labels=False)
        plt.savefig('_'+str(f)+'graph.png')
        f+=1
        plt.close()

from nltk import bigrams
from nltk.collocations import *
from nltk.corpus import stopwords
import itertools
import collections
import pandas as pd
import json

user_description = []

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

bigram_finder = nltk.BigramCollocationFinder.from_words('user_description.txt')

terms_bigram = [list(bigrams(tweet)) for tweet in tweets_nsw]
bigramsList = list(itertools.chain(*terms_bigram))
bigram_counts = collections.Counter(bigramsList)
bigram_counts.most_common(200)
bigram_df = pd.DataFrame(bigram_counts.most_common(200),
                            columns=['bigram', 'count'])
bigram_df

bigram_measures = nltk.collocations.BigramAssocMeasures()
bigram_finder.nbest(bigram_measures.pmi, 10)


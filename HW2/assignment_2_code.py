import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import operator

def calc_num_nodes_link_density(df):
    stacked_df = np.vstack((df[:, 1].reshape(-1, 1), df[:, 2].reshape(-1, 1)))
    tot_nodes = np.unique(stacked_df)
    num_nodes = len(tot_nodes)
    num_links = len(df[:, 0])                     ### Directed network
    density = num_links/(num_nodes*(num_nodes-1)) ### Country does not aid itself

    ### Save the outputs in a csv file
    pd.DataFrame([['num_nodes', 'num_links', 'density'], 
                  [num_nodes, num_links, density]]).to_csv('.\\network_params.csv', header=None, index=None)
    # print(num_nodes, num_links, density)

    ### Calculate the in-strength, out-strength and total strength
    node_degree = []
    strength_in = []
    strength_out = []
    strength_tot = []
    for i in range(len(tot_nodes)):
        node_degree.append(len(np.argwhere(stacked_df==tot_nodes[i])))
        # if(tot_nodes[i]=='China'):
        #     print(tot_nodes[i], np.argwhere(df[:, 2].reshape(-1)==tot_nodes[i]).reshape(-1))
        try:
            strength_in.append(np.sum(df[np.argwhere(df[:, 2].reshape(-1)==tot_nodes[i]).reshape(-1), -1])/1e9)  ### WF in km3
        except:
            strength_in.append(0)

        try:
            strength_out.append(np.sum(df[np.argwhere(df[:, 1].reshape(-1)==tot_nodes[i]).reshape(-1), -1])/1e9) ### WF in km3
        except:
            strength_out.append(0)
        
        strength_tot.append(np.nansum([strength_in[-1], strength_out[-1]]))

    ##### Outputting the results
    strength_arr = np.hstack((np.array(tot_nodes, dtype=object).reshape(-1, 1), np.array(node_degree).reshape(-1, 1), 
                              np.array(strength_in).reshape(-1, 1), np.array(strength_out).reshape(-1, 1), np.array(strength_tot).reshape(-1, 1)))
    strength_arr = np.vstack((np.array(['Node', 'Degree', 'In Strength', 'Out Strength', 
                                        'Total Strength'], dtype=object).reshape(1, -1), strength_arr))

    pd.DataFrame(strength_arr).to_csv('.\\node_strength_degree.csv', header=None, index=None)

    ##### Plotting the distribution   
    plt.figure()
    sns.histplot(data=strength_arr[1:, 1], bins=int(300/5), 
                 stat="density", alpha=0.4, kde=True, kde_kws={"cut": 3}) # x="Degree", ax=ax_hist, stat= 'count'
    plt.xlim([0, 80])
    plt.title('Degree Distribution')
    plt.savefig("degree_distribution.png")
    plt.close()

    plt.figure()
    # sns.displot(strength_arr[1:, -1], hist=True, kde=True, 
    #          bins=int(180/5), color = 'darkblue', 
    #          hist_kws={'edgecolor':'black'}) # kde_kws={'linewidth': 4}
    sns.histplot(data=strength_arr[1:, -1], bins=int(300/5), 
                 stat="density", alpha=0.4, kde=True, kde_kws={"cut": 3}) # ax=ax_hist, x="Strength (km^3)", 
    plt.title("Strength Distribution")
    plt.xlim([0, 8])
    plt.savefig("strength_distribution.png")
    plt.close()

def create_graph_calc_params(df): #### Function to calculate betweenness and clustering coefficient
    
    ###### Generating the non-directional graph from edgelist data
    graph=nx.from_pandas_edgelist(pd.DataFrame(df), source=1, target=2, edge_attr=[3]) # create_using=nx.DiGraph()
    
    bet_centrality = nx.betweenness_centrality(graph, normalized = True,  
                                                endpoints = False)  #### Measing the betweenness centralitu
    bet_centrality = dict( sorted(bet_centrality.items(), key=operator.itemgetter(1),reverse=True))

    # clustering_coeff = nx.clustering(graph)
    clustering_coeff = nx.triangles(graph) #### Calculating the number of triangles formed by each node
    clustering_coeff = dict( sorted(clustering_coeff.items(), key=operator.itemgetter(1),reverse=True))

    # print(bet_centrality)
    ####### Saving the results in a csv
    pd.DataFrame(np.array(list(bet_centrality.items()), dtype=object)).to_csv('.\\betweenness_centrality.csv', header=None, index=None)
    pd.DataFrame(np.array(list(clustering_coeff.items()), dtype=object)).to_csv('.\\clustering_coeff.csv', header=None, index=None)

    bet_centrality = pd.read_csv('.\\betweenness_centrality.csv', header=None).to_numpy()
    clustering_coeff = pd.read_csv('.\\clustering_coeff.csv', header=None).to_numpy()

    ##### Plotting the distributions
    plt.figure()
    sns.histplot(data=bet_centrality[:, 1], bins=int(300/5), 
                 stat="density", alpha=0.4, kde=True, kde_kws={"cut": 3}) # x="Degree", ax=ax_hist, stat= 'count'
    plt.xlim([0, 0.7])
    plt.title('Betweenness Centrality')
    plt.savefig("betweenness_centrality_dist.png")
    plt.close()

    plt.figure()
    sns.histplot(data=clustering_coeff[:, 1], bins=int(300/5), 
                 stat="density", alpha=0.4, kde=True, kde_kws={"cut": 3}) # ax=ax_hist, x="Strength (km^3)", 
    plt.title("Clustering (# triagles)")
    plt.xlim([0, 8])
    plt.savefig("clustering_coeff_dist.png")
    plt.close()


######## Main code to run the functions
#### AWF file contained the aggregated water trade footprint between nations
read_file = '.\\AWF.csv'
df = pd.read_csv(read_file, header=0).to_numpy()

calc_num_nodes_link_density(df)

create_graph_calc_params(df)
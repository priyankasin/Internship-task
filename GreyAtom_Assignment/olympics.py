# olympics-mini-project

import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import operator
import sys

# take a input data from termainal
row_data=sys.argv[1]
def load_data():

	 # read CSV file and convert CSV data to dataframe and Skip first row
    df = pd.read_csv("olympics.csv",index_col=0,skiprows=[0])  # read CSV file and convert CSV data to dataframe and Skip first row

    df=df.rename(columns = {"01 !":"Gold"})
    df=df.rename(columns = {"02 !":"Silver"})
    df=df.rename(columns = {"03 !":"Bronze"})
    df=df.rename(columns = {"01 !.1":"Gold.1"})
    df=df.rename(columns = {"02 !.1":"Silver.1"})
    df=df.rename(columns = {"03 !.1":"Bronze.1"})
    df=df.rename(columns = {"01 !.2":"Gold.2"})
    df=df.rename(columns = {"02 !.2":"Silver.2"})
    df=df.rename(columns = {"03 !.2":"Bronze.2"})

# Split country name and country code and add country name as data frame index
    names_ids = df.index.str.split('\s\(')
    df.index = names_ids.str[0] 
    df['ID'] = names_ids.str[1].str[:3] 

    
# Drop the column Totals
    last_row = len(df)-1
    df = df.drop(df.index[last_row])
# return dataframes
    return df

def first_country(df):
    # return the details of first country
    return df.iloc[0]			


def gold_medal(df):
     # reutrn the name of country who won the most gold medals in summer games
	return df['Gold'].argmax()  

def biggest_difference_in_gold_medal(df):
    # return the name of country who has biggest difference between their summer and winter gold medal counts.
    return (df['Gold']-df['Gold.1']).argmax()  

def get_points(df):
    df['Points'] = df['Gold']*3 + df['Silver']*2 + df['Bronze']+df['Gold.1']*3 + df['Silver.1']*2 + df['Bronze.1']+df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    return df['Points']

def kmean(df):
	X = df
    # drop ID column
	X = X.drop('ID', 1)
    # empty dictionary
	sil_coeffs = {}

    # here cluster range from 2 to 11
	for n_cluster in range(2, 11):
        # KMeans return the centroid & lable of cluster
	    kmeans = KMeans(n_clusters=n_cluster).fit(X)
	    label = kmeans.labels_
        #returns the mean Silhouette Coefficient over all samples
	    sil_coeff = silhouette_score(X, label, metric='euclidean')
        # all sil_coeff in dictionary
	    sil_coeffs[n_cluster] = sil_coeff
    # select optimize value of no. of cluster
	k_optimal = max(sil_coeffs, key=lambda k: sil_coeffs[k])

	kmeans = KMeans(n_clusters=k_optimal).fit(X)
	centroid=kmeans.cluster_centers_
	return k_optimal,centroid


df=load_data()

print(first_country(df))
print("")
print(gold_medal(df))
print("")
print(biggest_difference_in_gold_medal(df))
print("")
print(get_points(df))
print("")
# print(list(df.columns.values))
print(kmean(df))
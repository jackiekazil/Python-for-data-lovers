#building queen contiguity weights

import pysal

#pysal will read in shapefiles and create a topology for them
dcSHP = pysal.open('shapefile_name.shp', 'r')
dcW = pysal.weights.weights.queen(dcSHP)
#this will give you the number of observations in your data set
dcW.n
#the number or observations is returned 

dcW.mean_neighbors
#this returns the mean number of neighbors for each geography (observation) in the shapefile


#but we also might want to look at the matrix that's created. this is what we will rely on for the rest of the analysis






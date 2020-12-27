#!/usr/bin/env python
# coding: utf-8

# In[92]:


import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import elevation
import richdem as rd
import os, gdal, subprocess, sys
import gdal
from subprocess import call
import ogr
import subprocess
import argparse
import rasterio
import numpy as np


# In[195]:



parser = argparse.ArgumentParser(description='Clip Raster using Shapefile')
parser.add_argument('input_file', type=str, help='input raster file')
parser.add_argument('out_file', type=str, help='output file name with destination')
parser.add_argument('mask', type=str, help='shapefile destination for clipping extent')
parser.add_argument('dst', type=str, help='shapefile destination for clipping extent')
parser._optionals.title = "This script clips dem data using Shapefile"
args = parser.parse_args()

input_file=sys.argv[2]
mask = sys.argv[1]
out_file=sys.argv[3]


# In[ ]:

# This is an empty commennt to check changes




# In[94]:


args = ['gdalwarp', '-of', 'Gtiff', '-cutline', mask, input_file, out_file ]
subprocess.Popen(args)
args = None


# In[95]:


print("Output Generated Succesfully")


# In[96]:


from osgeo import gdal

filepath = r"c:\Users\Darshan\Desktop\nagpur\output.tif"

# Open the file:
raster = gdal.Open(filepath)


# In[97]:


raster = os.path.join(os.getcwd(), filepath)
nagpur_dem = rd.LoadGDAL(raster)


# In[98]:


slope = rd.TerrainAttribute(nagpur_dem, attrib='slope_riserun')
rd.rdShow(slope, axes=False, cmap='magma', figsize=(8, 5.5))
plt.show()


# In[161]:


slope


# In[130]:


slope.shape


# In[163]:


driver = "GTiff"


# In[164]:


dim = slope.shape


# In[165]:


dim


# In[166]:


height = dim[0]


# In[167]:


height


# In[168]:


width = dim[1]


# In[169]:


width


# In[170]:


count = 1


# In[171]:


dtype = slope.dtype


# In[186]:


dtype


# In[187]:


from rasterio.crs import CRS


# In[188]:


crs = CRS.from_epsg(32644)


# In[189]:


from rasterio.transform import from_origin


# In[190]:


transform = from_origin(186058.860, 2435882.462,28.1468,28.1468)


# In[191]:


transform


# In[194]:


with rasterio.open("nag1.tif", "w",
                  driver=driver,
                  height=height,
                  width=width,
                   count=count,
                  dtype = dtype,
                  crs=crs,
                  transform=transform) as dst:
    dst.write(slope, indexes = 1)


x



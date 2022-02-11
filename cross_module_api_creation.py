#!/usr/bin/env python
# coding: utf-8

# In[1]:


import flask
from flask import request, jsonify
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# In[3]:


df = pd.read_csv('E:/Research in Data/Assignments/Proposal/Olympics/data_2/api_dataset.csv')
df.head()


# In[7]:


@app.route('/', methods=['GET'])
def home():return '''Olympics Data API'''


# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:24:07 2018

@author: Mei
"""

import pandas as pd
import ast

def flatten_dict(d):
    """Flattens a dictionary where certain values are string representations 
    of a dictionary."""
    new_dict = {}
    for k, v in d.items():
        if v[0] == '{': #handle dictionary string
            nested_dict = ast.literal_eval(v)
            for k1, v1 in nested_dict.items():
                new_dict['_'.join([k,k1])] = v1
        else:
            new_dict[k] = v
    return new_dict

def flatten_series(s):
    """Takes a Panda Series of sparse dictionaries and returns a dataframe 
    with new columns for each key that exists"""
    new_columns = []
    for i, v in s.iteritems():
        if v is None:
            new_columns.append({})
        else:
            new_columns.append(flatten_dict(v))
        
    new_df = pd.DataFrame(new_columns)    
    return new_df

def get_categories(s, subset):
    """Create dummy variables from a series with multiple values in each element
        input:
            s - Series
            subset - the list of values that should be encoded
        output:
            df - a dataframe of the new variables
    """
    df = pd.DataFrame()
    for category in subset:
        df[category] = s.str.contains(category)
    return df

def process_business(business_df, categories):
    """Make the needed fixes in the business data"""
    fixed_df = pd.DataFrame()
    
    # Fix attributes column
    attributes_df = flatten_series(business_df.attributes)
    
    # Fix booleans
    attributes_df.replace({'True': True, 'False': False}, inplace=True)
    
    # Fill missing values with False
    attributes_df.fillna(False, inplace=True)
    
    fixed_df = pd.concat([business_df, attributes_df], axis='columns')
    
    # Fix categories    
    cat_df = get_categories(business_df.categories, categories)
    
    # Fill missing values with False
    cat_df.fillna(False, inplace=True)
    
    fixed_df = pd.concat([fixed_df, cat_df], axis='columns')

    return fixed_df




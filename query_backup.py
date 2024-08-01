from skimage import io
import matplotlib.pyplot as plt
import os
import math
import streamlit as st
from scipy import spatial
import h5py

def get_similar_images(query_features, h5_file_path="CustomFeatures.h5", max_matches=5):
    with h5py.File(h5_file_path, 'r') as h5f:
        feats = h5f['dataset_1'][:]
        imgNames = h5f['dataset_2'][:]

    scores = []
    for i in range(feats.shape[0]):
        score = 1 - spatial.distance.cosine(query_features, feats[i])
        if score != 1:
            scores.append((score, imgNames[i]))

    sorted_scores = sorted(scores, key=lambda x: x[0], reverse=True)
    imlist = [imgName for score, imgName in sorted_scores[:max_matches]]

    return imlist


def display_images(query_img_path, top_matches, base_path, num_columns=4):
    num_images = len(top_matches) + 1 
    num_rows = math.ceil(num_images / num_columns) 

    plt.figure(figsize=(15, num_rows * 5)) 

    query_img = io.imread(query_img_path)
    plt.subplot(num_rows, num_columns, 1)  
    plt.imshow(query_img)
    plt.title("Query Image")
    plt.axis('off')
    
    for i, img_name in enumerate(top_matches):
        img_path = os.path.join(base_path, img_name.decode('utf-8'))
        img = io.imread(img_path)
        plt.subplot(num_rows, num_columns, i + 2)  
        plt.imshow(img)
        plt.title(f"Match {i + 1}")
        plt.axis('off')

    st.pyplot(plt)

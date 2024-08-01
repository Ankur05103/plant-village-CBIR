import streamlit as st
import numpy as np
from PIL import Image
from extraction_backup import extract_features
from query_backup import display_images, get_similar_images


st.title('CBIR System for Tomato Plant Diseases')


uploaded_image = st.file_uploader("Please Select an Image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Finding similar images")
    image_array = np.array(image)

    
    if image_array.shape[-1] == 4:
        image_array = image_array[:, :, :3]
    
    #extract features of input image
    query_features = extract_features(image_array)

    #get matching images
    image_list = get_similar_images(query_features)

    #display matching images
    display_images(uploaded_image, image_list, "") 
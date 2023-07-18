import streamlit as st                       
from PIL import Image, ImageFilter,ImageFont,ImageDraw
import os                                                                

#create a folder images
if not os.path.exists('images'):
    os.makedirs('images')

def save_image(image):
    img=Image.open(image)
    img.save(f'images/{image.name}.png')

st.title('Image Processing App')

upload=st.file_uploader(
    label='Upload your image',
    type=['png','jpg','jpeg']

)
if upload is not None:
    save_image(upload)
    img=Image.open(upload)
    col1,col2=st.columns(2)
    filters=['contour','emboss','edge_enhance','blur','smooth','sharpen']
    option=st.sidebar.selectbox('select a filter',filters)
    col1.image(upload,caption='Uploaded image',use_column_width=True)
    
    if option=='contour':
        col2.image(img.filter(ImageFilter.CONTOUR),caption='Contour Filter',use_column_width=True)
    if option=='emboss':
        col2.image(img.filter(ImageFilter.EMBOSS),caption='Emboss Filter',use_column_width=True)
    if option=='edge_enhance':
        col2.image(img.filter(ImageFilter.EDGE_ENHANCE),caption='Edge_enhance Filter',use_column_width=True)
    if option=='blur':
        col2.image(img.filter(ImageFilter.BLUR),caption='Blur Filter',use_column_width=True)       
    if option=='smooth':
        col2.image(img.filter(ImageFilter.SMOOTH),caption='Smooth Filter',use_column_width=True)  
    if option=='sharpen':
        col2.image(img.filter(ImageFilter.SHARPEN),caption='Sharpen  Filter',use_column_width=True)

    message = st.sidebar.text_input("Enter a massage",value="MONDAY")
    font_size = st.sidebar.number_input("Enter font size",value=20)
    font_color= st.sidebar.color_picker("select font color")
    c1,c2= st.sidebar.columns(2)
    x = c1.number_input('X coordinate',value=img.width//2)
    y = c2.number_input('Y coordinate',value=img.height//2)

    imgc=img.copy()
    draw=ImageDraw.Draw(imgc)
    font=ImageFont.truetype('My font.TTF',font_size)
    draw.text((x,y),message,font_color,font)
    st.image(imgc,use_column_width=True)
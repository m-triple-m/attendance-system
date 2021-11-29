from os import times

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import time
import csv
import streamlit as st
import pandas as pd

present_students = set()

video = cv2.VideoCapture(0)


st.title('Attendence system')
name = st.text_input('Eter your name ')
btn = st.button('Submit')
if btn:
    st.text(f"you entered name {name}")


students = []

sidebar = st.sidebar

sidebar.title('Present student list')


# for stu in present_students:


with open('Book1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        students.append((row[1]))

print(f's : {students}')

run = st.checkbox('Run')
if run:
    while True:
        check, frame = video.read()
        d = decode(frame)
        try:
            for obj in d:
                name = d[0].data.decode()
                name = name.strip()
                print(students)
                if name in students:
                    students.remove(name)
                    present_students.add(name)
                    sidebar.subheader(name)
                    print('deleted.....')
                    st.success('Attendence recorded!')
                    break

        except Exception as e:
            print(e)
            print('error')

        cv2.imshow('Attendence', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            print(students)
            break

video.release()
cv2.destroyAllWindows()


showData = st.checkbox("Show Dataset")
if showData:
    st.dataframe(pd.read_csv('Book1.csv'))

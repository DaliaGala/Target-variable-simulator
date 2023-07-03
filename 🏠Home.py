#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:13:58 2023

@author: daliagala
"""

### LIBRARIES ###
import streamlit as st

### PAGE CONFIG ###
st.set_page_config(page_title='EquiVar', page_icon=':robot_face:', layout='wide')

#Set title
st.title('EquiVar - Target Variable Definition Simulator')

#Project description
st.subheader('Motivation')

st.markdown('''As machine learning techniques advance, algorithmic systems play an increasing role in hiring. Many such systems aim to predict, for example, which job applicants would be good employees for a given job. In order for an algorithmic system to identify potentially good employees, the notion of a “good” employee must be defined in terms that an algorithm can work with. In machine learning, this is called “defining the target variable” (in the case of hiring, the algorithm “aims at the target” of finding good employees).''')

st.markdown('''Defining the target variable is difficult. Imagine that you are hiring a salesperson. What makes for a good salesperson? Simply someone who makes the most profitable sales? Or is a good salesperson also a good leader? Does a good salesperson come up with new ideas that can improve how the sales team operates as a whole, and not just their individual sales? (The list could go on.) Perhaps the answer is: some of everything.''')

st.markdown('''But then we ask: how much of each thing? How much more important are individual sales than leadership, for example? Put another way: there may be different ways of understanding which qualities matter for being a good salesperson, and to what degree; reasonable minds may disagree on these issues (as anyone who’s been on a hiring committee has experienced). Even once it’s decided what makes for a good salesperson, there is a further question of how to make the notion precise in algorithmic terms: how do we identify job applicants with sales ability, leadership qualities, or innovative thinking? In order for the algorithm to be able to positively select those applicants, those qualities have to somehow be encoded numerically.''')

st.markdown('''Defining the target variable is not only difficult; it can also have profound effects on fairness—by resulting in hiring disparities for protected groups (Passi & Barocas 2019). For example, if you define the notion of a “good” employee in one way you might end up hiring more women than if you were to define “good” in another way. Relatedly, machine learning models might behave differently depending on how “good” employee is defined. Defining the notion in one way might lead to your model being less accurate for older applicants than for younger applicants. ''')

st.markdown('''Target variable definition is not a merely technical matter. The question of who counts as a “good” employee, and this question's implications on fairness, is fundamentally value-laden. It calls for close attention and transparency (Fazelpour & Danks, 2021). All too often, though, target variables are defined in technical settings without attention to fairness. Further, stakeholders who aren't a part of the technical process—like managers in non-technical roles, or those working in upper management or human resources—either do not understand, or are simply not aware of, the fraught nature of target variable definition.''')

st.markdown('''EquiVar is an interactive simulator, designed for technical and non-technical audiences alike, that is designed to help address this issue. The simulator makes the implications of target variable definition explicit—and transparent—and offers a blue-print for those who want to address these effects in practice. ''')

st.subheader('Overview of the simulator')
st.markdown('''The simulator has three pages, which are best visited in order.''')
st.markdown('''- **Define target variables.** You can define two different target variables for a “toy” hiring algorithm—two different ways of understanding what counts as a successful employee—by assigning different levels of cognitive characteristics (like reasoning skills, and information processing speed) that employees can have. Once you have defined the two target variables, our dashboard will, drawing on a data-set of the cognitive tests from real-world people, build two hiring models, A and B. Model A predicts which candidates will be successful employees on your first definition; model B predicts which candidates will be successful employees on your second definition.''')
st.markdown("- **See visualizations.** You can explore how the Datasets A and B generated based on your selections, and Models A and B trained on these datasets, differ in issues of fairness and bias. You can see, for example, which model selects more female applicants, or which model is more accurate for older applicants. You can also explore how Models A and B differ not just in matters of bias, but also in their overall performance: for example, in their overall accuracy.")
st.markdown("- **Putting the idea into practice.** A practitioner who is building or using their own hiring algorithms cannot take our dashboard “off the shelf” and apply it directly to their own data or algorithms. In this section, we explain how a practitioner could adapt our dashboard, and implement the ideas behind it, into their own work.")

st.subheader('Example')
st.markdown('''Here, we present an example of the dashboard in action. Minimally changing the weights of the tests results in comlpetely different coutcomes for the models. We assigned the same weights to all cognitive characteristics but one. The change is highlighted in blue. The chosen candidates therefore differ only by one point in behavioral restraint. Based on these datasets, we then trained two separate models, A and B.''')
st.image('./images/tests.png')

st.markdown('''The minor change in the weights of the characteristics has resulted in a major change in the selected candidates demographics.''')
st.image('./images/pie_charts.png')

#Create info boxes for authors, links and GitHub
# Set columns
c1, c2, c3, c4 = st.columns((2.2,2.6,2,1.8))

#Create info boxes for authors, links and GitHub
with c1:
  st.info('**Data Scientist: [Dalia Sara Gala](https://twitter.com/dalia_science)**')
with c2:
  st.info('**Philosophy Lead: [Milo Phillips-Brown](https://www.milopb.com/)**')
with c3:
  st.info('**Accenture team: [@The Dock](https://www.accenture.com/gb-en/services/about/innovation-hub-the-dock)**')
with c4:
  st.info('**GitHub: [Hiring-model](https://github.com/DaliaGala/Hiring-model)**')
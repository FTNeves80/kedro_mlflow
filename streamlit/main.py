import streamlit as st
import requests

def call_inference(data):
    rows = [
        list(data.values())
    ]


    resp = requests.post(
        'http://localhost:5001/invocations',
        json={
            'inputs': rows,
        }
    )

    inference = resp.json()

    return inference['predictions'][0]


#Titulo
st.markdown("""
# Titanic

Página desenvolvida em Streamlit para executar inferêrencia em um modelo de dados do Titanic

""")

#form
pclass = st.number_input("Classe do Passageiro", min_value=1, max_value=3)
age = st.number_input("Idade")
sibsp = st.number_input("Irmãos ou Cônjuges")
parch = st.number_input("Pais ou Filhos")
fare = st.number_input('Preço do Ticket')
sex = st.radio("Sexo",['Maculino', 'Feminino'])
embarked = st.radio("Porto de Embarque",['Cherbourg','Queenstown',"Southmpton"])

impute_data ={
    'pclass': pclass,
    'age': age,
    'sibsp': sibsp,
    'parch': parch,
    'fare': fare,
    'Sex_female': sex == 'Feminino',
    'Sex_male': sex == 'Masculino',
    'embarked_c': embarked == 'Cherbourg',
    'embarked_q': embarked == 'Queenstown',
    'embarked_s': embarked == 'Southmpton',
}

st.json(list(impute_data.values()))

survived = call_inference(impute_data)

st.write(f"Sobreviceu? {'Sim' if survived else 'Não :-('}")

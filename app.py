import streamlit as st 
import core.utils as utils


st.title('Calculatrice')

with st.container(border=True):
    property_details, contributions, mortgage = st.tabs(['Property Details', 'Contributions', 'Mortgage'])
    menu_height = 200
    with property_details:
        with st.container(height=menu_height, border=False):
            col1, col2, col3 = st.columns([1,1,1])
            base_price = col1.number_input(label="Base Price ($)", value =500_000, step=1_000)
            expected_date_transaction = col2.date_input('Expected Date of Transaction')
            property_is_new = col3.radio('Is property new?', ('Yes', 'No'), index=1)

            col1, col2 = st.columns([1,1])
            price_variation = col2.slider(
                'Select a range of values',
                0, 100, 
                (25, 75)
            )
            maximum_price = round(base_price + (price_variation[1]/100)*base_price)
            st.caption(f"Maximum Price: {maximum_price}$")

    with contributions:
        with st.container(height=menu_height, border=False):

            st.write('Initial Contribution')
            col1, col2 = st.columns([7,1])
            contribution_money = col1.slider(
                'Initial Contribution',
                0, 
                base_price,
                label_visibility = 'collapsed'
            )
            col2.write(f"{round((contribution_money/base_price)*100,2)}%")
            price_with_contribution = (base_price - contribution_money)
            max_price_with_contribution = (maximum_price - contribution_money)
            # st.caption(f"Contribution represent **{round((contribution_money/base_price)*100,2)}%**")
            
            

    with mortgage:
        with st.container(height=menu_height, border=False):
            col1, col2 = st.columns([1,1])
            duration_mortgage = col1.number_input(
                label='Years of Mortgage',
                step=1,
                min_value=0,
                max_value=35,
                value=25
            )
            mortgage_re_evaluation = col2.selectbox('Mortgage re-evaluation (every x years)', options=[3, 5, 7], index=1)
            mortgage_rate = st.slider(
                'Rate',
                0.0, 10.0, value=5.0
            )
            
overview, scenario_comparisons, optimizations = st.tabs(['Overview', 'Scenarios', 'Optimizations'])
## Pour l'achat - Non recurrent 
# Inspection Pré-achat
# Évaluation de la valeur de la propriété par la banque
# Frais de notaire
# Garantie pour maison neuve
# Frais de cadastre
# Services payés d'avance (gaz natuel, huile, mazout, etc.)


## DÉPENSES RÉCURRENTES LIÉES À L'ACHAT
# Frais de condos (annuel)
# Électricité (annuel)
# Gaz Naturel (annuel)
# Huile (annuel)
# Location de chauffe-eau (annuel)
            
## IMPÔTS
# Taxes Scolaire Annuelle
# Taxes Municipale Annuelle
# Portion de l'année à couvrir
# Taxes Scolaire à payer
# Taxes Municipale à payer          


st.caption(f"Price with contribution: {price_with_contribution}$")
st.caption(f"Maximum price with contribution: {max_price_with_contribution}$")


cmhc_insurance_rate, cmhc_insurance_rate_portability_rate  = utils.calculate_cmhc_premium(
                loan_amount = (base_price-contribution_money),
                property_value=base_price
                )
st.write(cmhc_insurance_rate*100, cmhc_insurance_rate_portability_rate*100)


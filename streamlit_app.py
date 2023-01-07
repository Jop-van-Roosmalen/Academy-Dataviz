import streamlit as st
import voertuigen
import budget

# See readme how to run
if st.checkbox('Laat voertuigen grafiek zien'):
    st.header('Voertuigen')
    fig, ax = voertuigen.get_graph()
    st.pyplot(fig)

st.markdown("""---""")

if st.checkbox('Laat budget grafiek zien'):
    st.header('Budget van MJPV is vergeleken met andere IGA projecten sterk gestegen in de afgelopen jaren')
    fig, ax = budget.get_graph()
    st.pyplot(fig)

    st.subheader("De gebruikte data")
    st.write(budget.get_budget_data())



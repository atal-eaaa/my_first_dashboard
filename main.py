import streamlit as st
import requests as re
import time



st.logo("🎲")


# with st.sidebar:
#     st.selectbox("Choose a model", ["GPT-4", "Claude", "Gemini"])


tab1, tab2, tab3 = st.tabs(["Velkommen", "Slå med terninger", "Scoreboards"])



with tab1:
    st.title("Velkommen til jeres første dashboard 👋")
    st.markdown(
        """ 
        **There's :rainbow[so much] you can build!**
        """
    )

    if st.button("Send :rainbow[balloons]!"):
        st.balloons()

with tab2:
    col1, col2 = st.columns(2)

    st.write("Vælg hvor mange terninger, du vil slå med:")
    number = st.slider("Antal", value=1, max_value=15, min_value=1)
 
    if st.button(f"Kast 🎲", use_container_width=True, type = 'primary'):
        # with st.spinner("Finder terningerne frem.."):
        #     time.sleep(1)
        try:
            resp = re.get(f"http://127.0.0.1:8000/roll_n_dice/{number}")

            data = resp.json()
            for i,t in enumerate(data['Terningekast'],1):
                st.write(f"🎲 :rainbow[{t}]'er")
        except:
            st.error("Der er desværre noget galt med yatzy-api'et.")
        

with tab3:
    st.subheader("Spillernes point fordeler sig således:")
    popover = st.popover("Vælg spiller")

    player1 = "Spiller 1"
    player2 = "Spiller 2"

    red = popover.checkbox(player1, True)
    blue = popover.checkbox(player2, True)

    if red:
        st.write(f"{player1} har x point")
    if blue:
        st.write(f"{player2} har y point")







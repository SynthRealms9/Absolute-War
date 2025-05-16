import streamlit as st

st.title("Mini Total War")
if 'regions' not in st.session_state:
    st.session_state.regions = {
        "Rome": {"owner": "Player", "troops": 10},
        "Carthage": {"owner": "AI", "troops": 8},
        "Gaul": {"owner": "AI", "troops": 5},
    }
    st.session_state.gold = 100
    st.session_state.turn = 1

st.sidebar.markdown(f"**Turn:** {st.session_state.turn}")
st.sidebar.markdown(f"**Gold:** 💰 {st.session_state.gold}")

if st.sidebar.button("Recruit Troops (-10 gold)"):
    if st.session_state.gold >= 10:
        st.session_state.regions["Rome"]["troops"] += 5
        st.session_state.gold -= 10
    else:
        st.sidebar.error("Not enough gold!")

enemy_to_attack = st.selectbox("Choose a region to attack:", ["Carthage", "Gaul"])
if st.button("Attack"):
    attacker = st.session_state.regions["Rome"]
    defender = st.session_state.regions[enemy_to_attack]

    st.write(f"Attacking {enemy_to_attack} with {attacker['troops']} troops...")
    if attacker["troops"] > defender["troops"]:
        st.success(f"You conquered {enemy_to_attack}!")
        defender["owner"] = "Player"
        attacker["troops"] -= defender["troops"]
        defender["troops"] = attacker["troops"] // 2
    else:
        st.error("You lost the battle!")
        attacker["troops"] = attacker["troops"] // 2

st.subheader("Map Overview")
for name, region in st.session_state.regions.items():
    st.write(f"**{name}** - Owner: {region['owner']} | Troops: {region['troops']}")

if st.button("End Turn"):
    st.session_state.gold += 20
    st.session_state.turn += 1

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
import random

# Simulating battle with randomness
def simulate_battle(attacker_troops, defender_troops):
    attacker_strength = attacker_troops * random.uniform(0.8, 1.2)  # Random factor
    defender_strength = defender_troops * random.uniform(0.8, 1.2)  # Random factor
    return attacker_strength, defender_strength
if st.button("Attack"):
    attacker = st.session_state.regions["Rome"]
    defender = st.session_state.regions[enemy_to_attack]
    
    st.write(f"Attacking {enemy_to_attack} with {attacker['troops']} troops...")
    
    attacker_strength, defender_strength = simulate_battle(attacker["troops"], defender["troops"])
    
    if attacker_strength > defender_strength:
        st.success(f"You conquered {enemy_to_attack}!")
        defender["owner"] = "Player"
        attacker["troops"] -= defender["troops"]
        defender["troops"] = int(attacker["troops"] // 2)
    else:
        st.error(f"You lost the battle at {enemy_to_attack}.")
        attacker["troops"] = int(attacker["troops"] // 2)
# Initial troops with types
if 'regions' not in st.session_state:
    st.session_state.regions = {
        "Rome": {"owner": "Player", "infantry": 5, "cavalry": 3, "archers": 2},
        "Carthage": {"owner": "AI", "infantry": 6, "cavalry": 2, "archers": 3},
        "Gaul": {"owner": "AI", "infantry": 4, "cavalry": 2, "archers": 1},
    }
def battle_with_types(attacker, defender):
    # Calculate combat strength based on troop types
    attack_strength = (attacker["infantry"] * 1) + (attacker["cavalry"] * 1.5) + (attacker["archers"] * 1)
    defense_strength = (defender["infantry"] * 1) + (defender["cavalry"] * 1.5) + (defender["archers"] * 1)

    return attack_strength, defense_strength

if st.button("Attack"):
    attacker = st.session_state.regions["Rome"]
    defender = st.session_state.regions[enemy_to_attack]
    
    st.write(f"Attacking {enemy_to_attack} with Infantry: {attacker['infantry']}, Cavalry: {attacker['cavalry']}, Archers: {attacker['archers']}...")

    attacker_strength, defender_strength = battle_with_types(attacker, defender)

    if attacker_strength > defender_strength:
        st.success(f"You conquered {enemy_to_attack}!")
        defender["owner"] = "Player"
        attacker["infantry"] -= defender["infantry"]
        attacker["cavalry"] -= defender["cavalry"]
        attacker["archers"] -= defender["archers"]
    else:
        st.error(f"You lost the battle at {enemy_to_attack}.")
        attacker["infantry"] = int(attacker["infantry"] // 2)
        attacker["cavalry"] = int(attacker["cavalry"] // 2)
        attacker["archers"] = int(attacker["archers"] // 2)
# Modify the Recruit Troops button to use resources
if st.sidebar.button("Recruit Infantry (5 gold, 3 food)"):
    if st.session_state.gold >= 5 and st.session_state.food >= 3:
        st.session_state.regions["Rome"]["infantry"] += 1
        st.session_state.gold -= 5
        st.session_state.food -= 3
    else:
        st.sidebar.error("Not enough resources!")

if st.sidebar.button("Recruit Cavalry (10 gold, 5 food)"):
    if st.session_state.gold >= 10 and st.session_state.food >= 5:
        st.session_state.regions["Rome"]["cavalry"] += 1
        st.session_state.gold -= 10
        st.session_state.food -= 5
    else:
        st.sidebar.error("Not enough resources!")

if st.sidebar.button("Recruit Archers (7 gold, 4 food)"):
    if st.session_state.gold >= 7 and st.session_state.food >= 4:
        st.session_state.regions["Rome"]["archers"] += 1
        st.session_state.gold -= 7
        st.session_state.food -= 4
    else:
        st.sidebar.error("Not enough resources!")
import streamlit as st
import random

# Simulate battle with randomness
def simulate_battle(attacker_troops, defender_troops):
    attacker_strength = attacker_troops * random.uniform(0.8, 1.2)  # Random factor
    defender_strength = defender_troops * random.uniform(0.8, 1.2)  # Random factor
    return attacker_strength, defender_strength

# Battle with troop types
def battle_with_types(attacker, defender):
    attack_strength = (attacker["infantry"] * 1) + (attacker["cavalry"] * 1.5) + (attacker["archers"] * 1)
    defense_strength = (defender["infantry"] * 1) + (defender["cavalry"] * 1.5) + (defender["archers"] * 1)
    return attack_strength, defense_strength

# Initialize game state
if 'regions' not in st.session_state:
    st.session_state.regions = {
        "Rome": {"owner": "Player", "infantry": 5, "cavalry": 3, "archers": 2},
        "Carthage": {"owner": "AI", "infantry": 6, "cavalry": 2, "archers": 3},
        "Gaul": {"owner": "AI", "infantry": 4, "cavalry": 2, "archers": 1},
    }
    st.session_state.gold = 100
    st.session_state.food = 50
    st.session_state.turn = 1

# UI for displaying resources
st.sidebar.markdown(f"**Turn:** {st.session_state.turn}")
st.sidebar.markdown(f"**Gold:** 💰 {st.session_state.gold}")
st.sidebar.markdown(f"**Food:** 🍞 {st.session_state.food}")

# Recruitment options
if st.sidebar.button("Recruit Infantry (5 gold, 3 food)"):
    if st.session_state.gold >= 5 and st.session_state.food >= 3:
        st.session_state.regions["Rome"]["infantry"] += 1
        st.session_state.gold -= 5
        st.session_state.food -= 3
    else:
        st.sidebar.error("Not enough resources!")

if st.sidebar.button("Recruit Cavalry (10 gold, 5 food)"):
    if st.session_state.gold >= 10 and st.session_state.food >= 5:
        st.session_state.regions["Rome"]["cavalry"] += 1
        st.session_state.gold -= 10
        st.session_state.food -= 5
    else:
        st.sidebar.error("Not enough resources!")

if st.sidebar.button("Recruit Archers (7 gold, 4 food)"):
    if st.session_state.gold >= 7 and st.session_state.food >= 4:
        st.session_state.regions["Rome"]["archers"] += 1
        st.session_state.gold -= 7
        st.session_state.food -= 4
    else:
        st.sidebar.error("Not enough resources!")

# Select region to attack
enemy_to_attack = st.selectbox("Choose a region to attack:", ["Carthage", "Gaul"])

if st.button("Attack"):
    attacker = st.session_state.regions["Rome"]
    defender = st.session_state.regions[enemy_to_attack]
    
    st.write(f"Attacking {enemy_to_attack} with Infantry: {attacker['infantry']}, Cavalry: {attacker['cavalry']}, Archers: {attacker['archers']}...")

    attacker_strength, defender_strength = battle_with_types(attacker, defender)

    if attacker_strength > defender_strength:
        st.success(f"You conquered {enemy_to_attack}!")
        defender["owner"] = "Player"
        attacker["infantry"] -= defender["infantry"]
        attacker["cavalry"] -= defender["cavalry"]
        attacker["archers"] -= defender["archers"]
    else:
        st.error(f"You lost the battle at {enemy_to_attack}.")
        attacker["infantry"] = int(attacker["infantry"] // 2)
        attacker["cavalry"] = int(attacker["cavalry"] // 2)
        attacker["archers"] = int(attacker["archers"] // 2)

# Show region statuses
st.subheader("Map Overview")
for name, region in st.session_state.regions.items():
    st.write(f"**{name}** - Owner: {region['owner']} | Infantry: {region['infantry']} | Cavalry: {region['cavalry']} | Archers: {region['archers']}")

# End turn
if st.button("End Turn"):
    st.session_state.gold += 20
    st.session_state.food += 10
    st.session_state.turn += 1

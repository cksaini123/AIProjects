import streamlit as st
import subprocess

st.title("AI Learning Assistant (Local & Free)")
st.set_page_config(page_title="AI Tutor", layout="centered")

st.sidebar.header("About")
st.sidebar.write("Built by Chandrakanta")

st.set_page_config(page_title="Teach Robo Patterns", layout="centered")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

# ---------- TITLE ----------
st.title("🤖 Teach Robo to Spot Patterns")
st.write("Help Robo learn how patterns work!")

st.divider()

# ---------- PHASE 0: INTRO ----------
if st.session_state.step == 0:
    st.subheader("👋 Meet Robo")
    st.write(
        "Hi! I’m **Robo** 🤖.\n\n"
        "I’m learning to become smart, but I’m very bad at spotting patterns.\n\n"
        "**Can you help me learn?**"
    )
    st.button("Yes! Let's help Robo 🚀", on_click=next_step)

# ---------- PHASE 1: SIMPLE PATTERN ----------
elif st.session_state.step == 1:
    st.subheader("🍎 Pattern Game 1")

    st.write("Look at this pattern:")
    st.markdown("### 🍎 🍌 🍎 🍌 🍎 ?")

    answer = st.radio(
        "What comes next?",
        ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]
    )

    if st.button("Check Answer"):
        if "Banana" in answer:
            st.success("🎉 Correct! You noticed the repeating pattern.")
            st.write("Apples and bananas are taking turns.")
            st.button("Next ➡️", on_click=next_step)
        else:
            st.info("Good try! Look carefully at what repeats.")

# ---------- PHASE 1B: TRICKY PATTERN ----------
elif st.session_state.step == 2:
    st.subheader("🔵 Pattern Game 2")

    st.markdown("### 🔵 🔵 🔴 🔵 🔵 🔴 ?")

    answer = st.radio(
        "What comes next?",
        ["🔴 Red", "🔵 Blue"]
    )

    if st.button("Check"):
        if "Blue" in answer:
            st.success("👏 Well done!")
            st.write(
                "You spotted a group pattern: **two blues, one red**.\n\n"
                "You didn’t guess — you **noticed**."
            )
            st.button("Next ➡️", on_click=next_step)
        else:
            st.info("Almost! Try grouping the colors.")

# ---------- PHASE 2: WHAT IS AI ----------
elif st.session_state.step == 3:
    st.subheader("🧠 How Robo Learns")

    st.write(
        "You can see patterns quickly.\n\n"
        "But I don’t have eyes like you.\n\n"
        "I look at **many examples** and try to find what repeats."
    )

    choice = st.radio(
        "Who learns faster?",
        ["👧 You", "🤖 Robo"]
    )

    if st.button("Check"):
        st.success("Yes! Humans learn faster with fewer examples.")
        st.button("Next ➡️", on_click=next_step)

# ---------- PHASE 3: TRAIN THE AI ----------
elif st.session_state.step == 4:
    st.subheader("🎮 Train Robo")

    st.write("Group these shapes in a way that makes sense to you:")

    grouping = st.radio(
        "How would you group them?",
        ["By color 🔴🔵", "By shape 🔺⚫"]
    )

    if st.button("Teach Robo"):
        st.success("Robo learned from you!")
        st.write(
            f"You grouped by **{grouping.lower()}**.\n\n"
            "Different people teach me in different ways.\n\n"
            "That’s why AI can learn **different patterns**."
        )
        st.button("Next ➡️", on_click=next_step)

# ---------- PHASE 4: AI MAKES A MISTAKE ----------
elif st.session_state.step == 5:
    st.subheader("❌ Robo Makes a Mistake")

    st.markdown("### 🦅 🐦 🦅 🐦 🦇")

    st.write("Robo says: *All of these can fly!*")

    correct = st.radio(
        "Is Robo correct?",
        ["Yes", "No"]
    )

    if st.button("Answer"):
        if correct == "No":
            st.success("🎯 You caught Robo’s mistake!")
            st.write(
                "I learned from how things **look**, not how they really are.\n\n"
                "**AI can be wrong if it is taught badly.**"
            )
            st.button("Next ➡️", on_click=next_step)
        else:
            st.info("Look carefully — is a bat the same as a bird?")

# ---------- PHASE 5: REFLECTION ----------
elif st.session_state.step == 6:
    st.subheader("💬 Think About It")

    st.write(
        "Answer these questions in your head:\n\n"
        "- What was easy for Robo?\n"
        "- What was hard for Robo?\n"
        "- Who is smarter right now — you or Robo?"
    )

    st.success(
        "🤖 Robo says:\n\n"
        "You are smarter!\n\n"
        "I only copy patterns.\n"
        "You understand them."
    )

    st.button("Finish 🎉", on_click=next_step)

# ---------- FINAL ----------
else:
    st.balloons()
    st.subheader("🌟 Great Job!")
    st.write(
        "**Today’s lesson:**\n\n"
        "AI becomes smart by finding patterns — but **humans decide what patterns matter**."
    )

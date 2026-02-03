import uuid
import streamlit as st
import subprocess
import json



st.title("AI Learning Assistant (Local & Free)")

st.sidebar.header("About")
st.sidebar.write("Built by Chandrakanta")

st.set_page_config(page_title="Teach Robo Patterns", layout="centered")

LESSON_PATTERN = "How AI Finds Patterns"
LESSON_BIAS = "When AI Learns Unfairly"
LESSON_CONFIDENT_WRONG = "AI Can Be Confident and Wrong"
LESSON_PREDICT_DECIDE = "AI Predicts, Humans Decide"
LESSON_NEEDS_HUMANS = "AI Needs Humans"
LESSON_TOOL_NOT_BRAIN = "AI Is a Tool, Not a Brain"





if "lesson" not in st.session_state:
    st.session_state.lesson = LESSON_PATTERN

if "step" not in st.session_state:
    st.session_state.step = 0

st.sidebar.subheader("📘 Choose a Lesson")

selected_lesson = st.sidebar.radio(
    "Lesson",
    [LESSON_PATTERN, LESSON_BIAS,LESSON_CONFIDENT_WRONG,LESSON_PREDICT_DECIDE,LESSON_NEEDS_HUMANS,LESSON_TOOL_NOT_BRAIN]
)

# If lesson changes, reset steps
if selected_lesson != st.session_state.lesson:
    st.session_state.lesson = selected_lesson
    st.session_state.step = 0


#---------------------Progress------------------
if "progress" not in st.session_state:
    st.session_state.progress = {
        "How AI Finds Patterns": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        },
        "When AI Learns Unfairly": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        },
        "AI Can Be Confident and Wrong": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        },
        "AI Predicts, Humans Decide": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        },
        "AI Needs Humans": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        },
        "AI Is a Tool, Not a Brain": {
            "completed": False,
            "mistakes": 0,
            "time_spent": 0
        }
    }


#--------------AI generated encouragement-----------
def ai_encouragement():
    try:
        prompt = (
            "You are a kind teacher for children aged 7 to 10. "
            "Say ONE short encouraging sentence. "
            "Do not ask questions. "
            "Keep it under 12 words."
        )

        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            timeout=10
        )

        text = result.stdout.strip().split("\n")[0]
        return text[:100]

    except Exception:
        return "Great job! You are helping Robo learn."
	

#-------------speech addition-----------------------

def say(display_text, spoken_text=None):
    st.write(display_text)
    if spoken_text:
        speak_block(spoken_text)

def speak_block(text):
    safe_text = text.replace("\n", " ")
    js_text = json.dumps(safe_text)  # THIS is the key fix

    uid = str(uuid.uuid4()).replace("-", "")
    st.components.v1.html(
        f"""
        <button id="{uid}" style="
            font-size:16px;
            padding:8px 12px;
            border-radius:8px;
            background-color:#ffdd57;
            border:none;
            cursor:pointer;">
            🔊 Hear Robo Speak
        </button>

        <script>
        const btn = document.getElementById("{uid}");
        btn.onclick = () => {{
            const msg = new SpeechSynthesisUtterance({js_text});
            msg.rate = 0.85;
            msg.pitch = 1.1;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
        }};
        </script>
        """,
        height=70
    )



# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

# ---------- TITLE ----------
st.title("🤖 Teach Robo to Spot Patterns")
st.write("Help Robo learn how patterns work!")

st.divider()

#--------------Lesson-1---------------

# ---------- PHASE 0: INTRO ----------
def lesson_pattern():
    if st.session_state.step == 0:
        st.subheader("👋 Meet Robo")
        MESSAGES = {
        "intro": {
            "display": "Hi! I’m **Robo** 🤖\n\nCan you help me learn?",
            "spoken": "Hi. I am Robo. Can you help me learn?"
        }
        }
        
        say(MESSAGES["intro"]["display"], MESSAGES["intro"]["spoken"])
    
        
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
                spoken_success = ai_encouragement()
                speak_block(spoken_success)
                st.success("🎉 Correct! You noticed the repeating pattern.")
                st.write("Apples and bananas are taking turns.")
                st.button("Next ➡️", on_click=next_step)
            else:
                st.info("Good try! Look carefully at what repeats.")
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


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
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


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
            st.success("Humans learn faster with fewer examples.")
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
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


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
        st.session_state.progress[st.session_state.lesson]["completed"] = True


#-----------lesson-2----------------------
def lesson_bias():
    st.title("⚖️ When AI Learns Unfairly")

    if st.session_state.step == 0:
        display = "🤖 I learned something new today!\n\nI can sort toys fast."
        spoken = "I learned something new today. I can sort toys fast."
        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    elif st.session_state.step == 1:
        st.subheader("Robo says: Toys with wheels are the best toys.")
        st.markdown("### 🚗 🚗 🚗 🚗 🧸")

        choice = st.radio("Is Robo right?", ["Yes", "No"])

        if st.button("Answer"):
            if choice == "No":
                st.success("Good thinking!")
                speak_block("Robo learned from unfair examples.")
                st.button("Next ➡️", on_click=next_step)
            else:
                st.info("Did Robo see many kinds of toys?")
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


    elif st.session_state.step == 2:
        display = (
            "🤔 **Robo learned from examples.**\n\n"
            "But the examples were not fair.\n\n"
            "Robo saw many cars and only one teddy."
        )
        spoken = (
            "I learned from examples. "
            "But the examples were not fair. "
            "I saw many cars and only one teddy."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    elif st.session_state.step == 3:
        st.subheader("🧠 Help Robo Learn Fairly")

        st.write("Which toys should we show Robo?")

        toys = st.multiselect(
            "Choose toys:",
            ["🚗 Cars", "🧸 Teddies", "🧩 Puzzles", "🏀 Balls"]
        )

        if st.button("Teach Robo"):
            if len(toys) >= 3:
                st.success("🌟 Great choice! Robo learned more fairly.")
                speak_block("Thank you. Now my learning is fairer.")
                st.button("Next ➡️", on_click=next_step)
            else:
                st.info("Try showing Robo more kinds of toys.")
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1

        
    elif st.session_state.step == 4:
        display = (
            "🤖 **Robo is not mean.**\n\n"
            "Robo only copies what it is shown."
        )
        spoken = (
            "I am not mean. "
            "I only copy what I am shown."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)
    elif st.session_state.step == 5:
        st.subheader("💬 Think About It")

        st.write(
            "- Who taught Robo?\n"
            "- Can Robo decide what is fair?\n"
            "- Who must be careful when teaching AI?"
        )

        speak_block("Humans must be careful. I only learn from them.")
        st.button("Finish Lesson 🎉", on_click=next_step)
    elif st.session_state.step == 6:
        st.balloons()
        st.subheader("🌟 Lesson Complete")

        display = "**Today’s lesson:**\n\nAI can be unfair if we teach it unfairly."
        spoken = "AI can be unfair if we teach it unfairly."

        say(display, spoken)
        st.session_state.progress[st.session_state.lesson]["completed"] = True


#------------------lesson-3---------------------------
def lesson_confident_wrong():
    st.title("🧠 AI Can Be Confident and Wrong")

    # ---------- Phase 0: Setup ----------
    if st.session_state.step == 0:
        display = (
            "🤖 **I am getting very smart now!**\n\n"
            "I can explain things very confidently."
        )
        spoken = (
            "I am getting very smart now. "
            "I can explain things very confidently."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 1: Show example ----------
    elif st.session_state.step == 1:
        st.subheader("🦅 Look Carefully")

        st.markdown("### 🦅 🐦 🦅 🐦 🦇")

        display = "Robo is looking at these animals."
        spoken = "Look carefully at these animals."

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 2: Robo makes confident statement ----------
    elif st.session_state.step == 2:
        display = (
            "🤖 Robo says:\n\n"
            "**“All these animals can fly.”**"
        )
        spoken = "All these animals can fly."

        say(display, spoken)

        choice = st.radio(
            "Is Robo right?",
            ["Yes", "No"]
        )

        if st.button("Answer"):
            if choice == "No":
                st.success("🎯 Good thinking!")
                speak_block("Good thinking. Robo sounded confident, but made a mistake.")
                st.button("Next ➡️", on_click=next_step)
            else:
                st.info("Look carefully again. Is a bat the same as a bird?")
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


    # ---------- Phase 3: Explain mistake ----------
    elif st.session_state.step == 3:
        display = (
            "🦇 **A bat can fly, but it is not a bird.**\n\n"
            "Robo sounded sure, but learned the wrong rule."
        )
        spoken = (
            "A bat can fly, but it is not a bird. "
            "Robo sounded sure, but learned the wrong rule."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 4: Key takeaway ----------
    elif st.session_state.step == 4:
        display = (
            "⚠️ **Important lesson:**\n\n"
            "AI can sound confident and still be wrong."
        )
        spoken = "AI can sound confident and still be wrong."

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 5: Reflection ----------
    elif st.session_state.step == 5:
        st.subheader("💬 Think About It")

        st.write(
            "- Should we always trust Robo?\n"
            "- What should we do when Robo sounds very sure?"
        )

        speak_block(
            "You should think and check. That makes you smarter than me."
        )

        st.button("Finish Lesson 🎉", on_click=next_step)

    # ---------- Final ----------
    else:
        st.balloons()
        display = (
            "**You learned:**\n\n"
            "Even confident AI can make mistakes.\n\n"
            "Humans must think and check."
        )
        spoken = (
            "Even confident AI can make mistakes. "
            "Humans must think and check."
        )

        say(display, spoken)
        st.session_state.progress[st.session_state.lesson]["completed"] = True


#=------------------lesson-4-------------------------\
def lesson_predict_decide():
    st.title("🧠 AI Predicts, Humans Decide")

    # ---------- Phase 0: Setup ----------
    if st.session_state.step == 0:
        display = (
            "🤖 **I am very good at guessing!**\n\n"
            "I can predict what you might like."
        )
        spoken = (
            "I am very good at guessing. "
            "I can predict what you might like."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 1: Prediction example ----------
    elif st.session_state.step == 1:
        st.subheader("🍦 Ice Cream Time")

        st.markdown("### 🍫 🍫 🍫 🍓")

        display = (
            "Robo saw that chocolate was chosen many times.\n\n"
            "**Robo predicts:** Chocolate ice cream!"
        )
        spoken = (
            "I saw chocolate chosen many times. "
            "I predict chocolate ice cream."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 2: Child makes a decision ----------
    elif st.session_state.step == 2:
        st.subheader("🧒 Your Turn")

        choice = st.radio(
            "What do YOU choose?",
            ["🍫 Chocolate", "🥭 Mango", "🍓 Strawberry"]
        )

        if st.button("Choose"):
            st.success(f"You chose {choice}!")
            speak_block(
                "Good choice. Even if I predict something, you decide."
            )
            st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 3: Key explanation ----------
    elif st.session_state.step == 3:
        display = (
            "🤖 **Robo can guess…**\n\n"
            "**But Robo cannot decide for you.**"
        )
        spoken = (
            "I can guess, but I cannot decide for you."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 4: Takeaway ----------
    elif st.session_state.step == 4:
        display = (
            "⚠️ **Important lesson:**\n\n"
            "AI predicts.\n"
            "Humans decide."
        )
        spoken = "AI predicts. Humans decide."

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 5: Reflection ----------
    elif st.session_state.step == 5:
        st.subheader("💬 Think About It")

        st.write(
            "- Should we always follow AI suggestions?\n"
            "- Who is in control: AI or humans?"
        )

        speak_block(
            "Humans are in control. I only help by predicting."
        )

        st.button("Finish Lesson 🎉", on_click=next_step)

    # ---------- Final ----------
    else:
        st.balloons()
        display = (
            "**You learned:**\n\n"
            "AI can suggest and predict.\n\n"
            "But humans always decide."
        )
        spoken = (
            "AI can suggest and predict. "
            "But humans always decide."
        )

        say(display, spoken)
        st.session_state.progress[st.session_state.lesson]["completed"] = True

#------------------lesson-5-----------------------------
def lesson_needs_humans():
    st.title("🤝 AI Needs Humans")

    # ---------- Phase 0: Setup ----------
    if st.session_state.step == 0:
        display = (
            "🤖 **I try my best to help you.**\n\n"
            "But sometimes I make mistakes."
        )
        spoken = (
            "I try my best to help you. "
            "But sometimes I make mistakes."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 1: AI makes a mistake ----------
    elif st.session_state.step == 1:
        st.subheader("🍎 Fruit Sorting")

        st.markdown("### 🍎 🍌 🥕")

        display = (
            "🤖 Robo says:\n\n"
            "**“All these are fruits.”**"
        )
        spoken = "All these are fruits."

        say(display, spoken)

        choice = st.radio(
            "Is Robo correct?",
            ["Yes", "No"]
        )

        if st.button("Answer"):
            if choice == "No":
                st.success("Good catch!")
                speak_block(
                    "Thank you for checking. I made a mistake."
                )
                st.button("Next ➡️", on_click=next_step)
            else:
                st.info("Look carefully. Is carrot a fruit?")
                st.session_state.progress[st.session_state.lesson]["mistakes"] += 1


    # ---------- Phase 2: Human gives feedback ----------
    elif st.session_state.step == 2:
        display = (
            "🧒 **You helped Robo by correcting it.**\n\n"
            "Now Robo can learn better."
        )
        spoken = (
            "You helped me by correcting me. "
            "Now I can learn better."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 3: AI improves ----------
    elif st.session_state.step == 3:
        st.subheader("🔁 Robo Learns Again")

        st.markdown("### 🍎 🍌 🥕")

        display = (
            "🤖 Robo now says:\n\n"
            "**“Apple and banana are fruits. Carrot is a vegetable.”**"
        )
        spoken = (
            "Apple and banana are fruits. "
            "Carrot is a vegetable."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 4: Key lesson ----------
    elif st.session_state.step == 4:
        display = (
            "⚠️ **Important lesson:**\n\n"
            "AI cannot fix itself.\n\n"
            "Humans must guide AI."
        )
        spoken = (
            "I cannot fix myself. "
            "Humans must guide me."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 5: Reflection ----------
    elif st.session_state.step == 5:
        st.subheader("💬 Think About It")

        st.write(
            "- What happens if no one corrects Robo?\n"
            "- Who helps AI learn better?"
        )

        speak_block(
            "Humans help me learn by giving feedback."
        )

        st.button("Finish Lesson 🎉", on_click=next_step)

    # ---------- Final ----------
    else:
        st.balloons()
        display = (
            "**You learned:**\n\n"
            "AI needs humans to correct and guide it."
        )
        spoken = (
            "AI needs humans to correct and guide it."
        )

        say(display, spoken)
        st.session_state.progress[st.session_state.lesson]["completed"] = True


#-------------------lesson-6--------------------------
def lesson_tool_not_brain():
    st.title("🧰 AI Is a Tool, Not a Brain")

    # ---------- Phase 0: Gentle setup ----------
    if st.session_state.step == 0:
        display = (
            "🤖 **Many people think AI is like a brain.**\n\n"
            "But let’s understand what AI really is."
        )
        spoken = (
            "Many people think AI is like a brain. "
            "But let us understand what AI really is."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 1: Tool analogy ----------
    elif st.session_state.step == 1:
        st.subheader("🧮 Think About a Calculator")

        display = (
            "A calculator can add numbers very fast.\n\n"
            "**But does it understand math like you do?**"
        )
        spoken = (
            "A calculator can add numbers very fast. "
            "But it does not understand math like you do."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 2: AI analogy ----------
    elif st.session_state.step == 2:
        display = (
            "🤖 **AI is like a very powerful calculator.**\n\n"
            "It works fast, but it does not think or feel."
        )
        spoken = (
            "AI is like a very powerful calculator. "
            "It works fast, but it does not think or feel."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 3: What AI cannot do ----------
    elif st.session_state.step == 3:
        st.subheader("❌ What AI Cannot Do")

        st.write(
            "- AI cannot feel happy or sad\n"
            "- AI cannot care\n"
            "- AI cannot decide what is right or wrong"
        )

        speak_block(
            "I cannot feel or care. I only follow instructions."
        )

        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 4: What humans do ----------
    elif st.session_state.step == 4:
        st.subheader("❤️ What Humans Can Do")

        st.write(
            "- Humans can think\n"
            "- Humans can feel\n"
            "- Humans can decide\n"
            "- Humans can take responsibility"
        )

        speak_block(
            "Humans think and decide. I only help."
        )

        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 5: Emotional grounding ----------
    elif st.session_state.step == 5:
        display = (
            "🌱 **Important message:**\n\n"
            "You do not need to fear AI.\n\n"
            "AI is a tool that helps humans."
        )
        spoken = (
            "You do not need to fear AI. "
            "AI is a tool that helps humans."
        )

        say(display, spoken)
        st.button("Next ➡️", on_click=next_step)

    # ---------- Phase 6: Reflection ----------
    elif st.session_state.step == 6:
        st.subheader("💬 Think About It")

        st.write(
            "- Who makes AI?\n"
            "- Who is responsible for AI?\n"
            "- Who is smarter: humans or tools?"
        )

        speak_block(
            "Humans are responsible. Tools help humans."
        )

        st.button("Finish Lesson 🎉", on_click=next_step)

    # ---------- Final ----------
    else:
        st.balloons()
        display = (
            "**You learned:**\n\n"
            "AI is a tool.\n"
            "Humans are in control."
        )
        spoken = (
            "AI is a tool. Humans are in control."
        )

        say(display, spoken)
        st.session_state.progress[st.session_state.lesson]["completed"] = True





#--------------------lessons-selection------------------

if st.session_state.lesson == LESSON_PATTERN:
    lesson_pattern()
elif st.session_state.lesson == LESSON_BIAS:
    lesson_bias()
elif st.session_state.lesson == LESSON_CONFIDENT_WRONG:
    lesson_confident_wrong()
elif st.session_state.lesson == LESSON_PREDICT_DECIDE:
    lesson_predict_decide()
elif st.session_state.lesson == LESSON_NEEDS_HUMANS:
    lesson_needs_humans()
elif st.session_state.lesson == LESSON_TOOL_NOT_BRAIN:
    lesson_tool_not_brain()

#--------------------DAshboard UI code
st.sidebar.divider()
st.sidebar.subheader("📊 Parent / Teacher Dashboard")

if st.sidebar.checkbox("View Learning Progress"):
    for lesson, data in st.session_state.progress.items():
        st.sidebar.markdown(f"### {lesson}")

        status = "✅ Completed" if data["completed"] else "⏳ In progress"
        st.sidebar.write(f"Status: {status}")
        st.sidebar.write(f"Mistakes made: {data['mistakes']}")

        if data["mistakes"] == 0:
            st.sidebar.success("Concept looks clear 👍")
        elif data["mistakes"] <= 2:
            st.sidebar.info("Some guidance may help 🙂")
        else:
            st.sidebar.warning("Child may need extra support 💡")

        st.sidebar.divider()

Overview

This project is an interactive AI-literacy learning app for children, designed to help them understand how AI works, where it fails, and why humans must stay in control.
The goal is not to teach coding, but to build correct mental models about AI at an early age.
The app is built using Python + Streamlit, with a strong focus on:
child-safe interaction
explainable AI concepts
human–AI collaboration
ethical and emotional grounding

What Problem Does This Solve?

Children today interact with AI daily, but:
often trust AI blindly
think AI is “smart like humans”
don’t understand bias or mistakes
This app teaches AI literacy, not AI usage.

Curriculum (6 Core Lessons)

1.How AI Finds Patterns
Teaches that AI learns by spotting patterns in examples.
2.When AI Learns Unfairly
Demonstrates how biased or unbalanced data leads to unfair AI behavior.
3.AI Can Be Confident and Wrong
Shows that AI can sound sure while still being incorrect.
4.AI Predicts, Humans Decide
Separates AI prediction from human decision-making.
5.AI Needs Humans (Feedback Loop)
Explains that AI improves only when humans correct it.
6.AI Is a Tool, Not a Brain
Emotionally grounds children by clarifying that AI does not think or feel.

🧩 Key Features
🔊 Voice-based interaction using browser-native text-to-speech
🤖 Controlled local AI usage (for encouragement only)
🧠 Human-in-the-loop learning design
📊 Parent / Teacher dashboard showing learning progress
🔒 No data collection, no open-ended AI chat

🏗️ Technical Architecture
Frontend & Logic: Streamlit (state-driven UI)
State Management: st.session_state
Voice: Browser-native Speech Synthesis (safe & offline)
AI Usage: Local LLM (Ollama) with strict prompt constraints
Design Principle: Deterministic learning flow + constrained AI
Parent / Teacher Dashboard

The dashboard provides:

lesson completion status
mistake counts (learning friction)
simple guidance indicators (no grading or judgment)
This supports guided learning, not surveillance.


🛠️ How to Run Locally
pip install streamlit
streamlit run app.py

Future Enhancements

Progress persistence (JSON)
Time-on-task analytics


🙌 Author

Built by Chandrakanta Saini
Software Engineer | Educator | AI Literacy Advocate

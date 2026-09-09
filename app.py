import streamlit as st
from agents import MultiAgentSystem


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------
# Custom CSS
# ---------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666666;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

.agent-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    margin-top: 10px;
}

.answer-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #dbeafe;
    margin-top: 20px;
}

.small-text {
    color: #64748b;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------
# Header
# ---------------------------------------

st.markdown(
    '<div class="title">🤖 AI Knowledge Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Multi-Agent • RAG • Python • PyTorch • TensorFlow'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------
# Initialize AI System
# ---------------------------------------

@st.cache_resource
def load_system():

    return MultiAgentSystem()


system = load_system()


# ---------------------------------------
# Sidebar
# ---------------------------------------

with st.sidebar:

    st.header("⚙️ AI System")

    st.success("System Online")

    st.markdown("---")

    st.subheader("Technologies")

    st.write("🐍 Python")
    st.write("🔎 RAG Retrieval")
    st.write("🤖 Multi-Agent System")
    st.write("🔥 PyTorch")
    st.write("🧠 TensorFlow")
    st.write("📚 Knowledge Base")

    st.markdown("---")

    st.subheader("How it works")

    st.write(
        """
        1. User asks a question
        2. Retrieval Agent searches the knowledge base
        3. Analysis Agent processes the information
        4. System generates the final response
        """
    )


# ---------------------------------------
# Main Interface
# ---------------------------------------

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("💬 Ask the AI Assistant")

question = st.text_input(
    "Enter your question",
    placeholder="Example: What is artificial intelligence?"
)

ask_button = st.button(
    "🚀 Ask AI",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------
# Example Questions
# ---------------------------------------

st.subheader("💡 Try an example")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("What is AI?", use_container_width=True):
        question = "What is artificial intelligence?"
        ask_button = True

with col2:

    if st.button("What is cybersecurity?", use_container_width=True):
        question = "What is cybersecurity?"
        ask_button = True

with col3:

    if st.button("What is machine learning?", use_container_width=True):
        question = "What is machine learning?"
        ask_button = True


# ---------------------------------------
# Process Question
# ---------------------------------------

if ask_button and question:

    st.markdown("---")

    st.subheader("🔄 AI Processing")

    with st.status(
        "AI agents are working...",
        expanded=True
    ):

        st.write("🔎 Retrieval Agent: Searching knowledge base...")

        st.write("📚 Retrieving relevant information...")

        st.write("🧠 Analysis Agent: Processing retrieved information...")

        st.write("✅ Preparing final response...")


    # Run Multi-Agent System

    answer = system.run(question)


    # -----------------------------------
    # Display Answer
    # -----------------------------------

    st.markdown(
        '<div class="answer-box">',
        unsafe_allow_html=True
    )

    st.subheader("✨ AI Response")

    st.write(answer)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------
    # System Information
    # -----------------------------------

    st.markdown("---")

    st.subheader("📊 AI Pipeline")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Retrieval",
            "Completed"
        )

    with col2:
        st.metric(
            "Analysis",
            "Completed"
        )

    with col3:
        st.metric(
            "AI System",
            "Online"
        )


elif ask_button and not question:

    st.warning("Please enter a question first.")
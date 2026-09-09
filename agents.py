from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_knowledge():

    with open("knowledge.txt", "r", encoding="utf-8") as file:
        text = file.read()

    documents = text.split("\n\n")

    return documents


class RetrievalAgent:

    def __init__(self):

        self.documents = load_knowledge()

        self.vectorizer = TfidfVectorizer()

        self.vectors = self.vectorizer.fit_transform(
            self.documents
        )

    def retrieve(self, question):

        question_vector = self.vectorizer.transform(
            [question]
        )

        similarity = cosine_similarity(
            question_vector,
            self.vectors
        )

        best_index = similarity.argmax()

        return self.documents[best_index]


class AnalysisAgent:

    def analyze(self, question, information):

        answer = f"""
Question:
{question}

Relevant Information:
{information}

Analysis:
The retrieved information is relevant to your question.
"""

        return answer


class MultiAgentSystem:

    def __init__(self):

        self.retrieval_agent = RetrievalAgent()

        self.analysis_agent = AnalysisAgent()

    def run(self, question):

        print("\n[Retrieval Agent] Searching knowledge base...")

        information = self.retrieval_agent.retrieve(question)

        print("[Retrieval Agent] Information retrieved.")

        print("[Analysis Agent] Analyzing information...")

        result = self.analysis_agent.analyze(
            question,
            information
        )

        print("[Analysis Agent] Analysis completed.")

        return result
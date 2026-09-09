from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_knowledge():
    with open("knowledge.txt", "r", encoding="utf-8") as file:
        text = file.read()

    blocks = [
        block.strip()
        for block in text.split("\n\n")
        if block.strip()
    ]

    knowledge = []

    for block in blocks:
        if "Q:" in block and "A:" in block:
            question = block.split("A:", 1)[0]
            answer = block.split("A:", 1)[1].strip()

            question = question.replace("Q:", "").strip()

            knowledge.append({
                "question": question,
                "answer": answer
            })

    return knowledge


class RetrievalAgent:

    def __init__(self):

        self.knowledge = load_knowledge()

        # IMPORTANT:
        # Only questions are converted into TF-IDF vectors.
        self.questions = [
            item["question"]
            for item in self.knowledge
        ]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def retrieve(self, user_question):

        user_question = user_question.strip()

        question_vector = self.vectorizer.transform(
            [user_question]
        )

        similarities = cosine_similarity(
            question_vector,
            self.vectors
        )[0]

        best_index = similarities.argmax()

        best_score = similarities[best_index]

        print("Similarity score:", best_score)
        print(
            "Matched question:",
            self.knowledge[best_index]["question"]
        )

        if best_score < 0.10:

            return {
                "answer": (
                    "I could not find a reliable answer "
                    "to this question in my knowledge base."
                ),
                "matched_question": None
            }

        return {
            "answer": self.knowledge[best_index]["answer"],
            "matched_question":
                self.knowledge[best_index]["question"]
        }


class AnalysisAgent:

    def analyze(self, question, retrieved_information):

        return retrieved_information["answer"]


class MultiAgentSystem:

    def __init__(self):

        self.retrieval_agent = RetrievalAgent()

        self.analysis_agent = AnalysisAgent()

    def run(self, question):

        print("\n[Retrieval Agent] Searching knowledge base...")

        information = self.retrieval_agent.retrieve(question)

        print("[Retrieval Agent] Information retrieved.")

        print(
            "[Retrieval Agent] Matched:",
            information["matched_question"]
        )

        print("[Analysis Agent] Analyzing information...")

        result = self.analysis_agent.analyze(
            question,
            information
        )

        print("[Analysis Agent] Analysis completed.")

        return result

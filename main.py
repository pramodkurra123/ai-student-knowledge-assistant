print("MAIN.PY STARTED")

from agents import MultiAgentSystem
from models import run_pytorch, run_tensorflow

print("IMPORTS COMPLETED")


def main():
    print("MAIN FUNCTION STARTED")

    print("=" * 50)
    print("AI STUDENT DOCUMENT ASSISTANT")
    print("=" * 50)

    pytorch_result = run_pytorch()
    print("PyTorch working:", pytorch_result)

    tensorflow_result = run_tensorflow()
    print("TensorFlow working:", tensorflow_result)

    system = MultiAgentSystem()

    print("\nSystem is ready!")

    while True:
        question = input("\nEnter your question: ")

        if question.lower() == "exit":
            break

        answer = system.run(question)

        print("\nFINAL ANSWER:")
        print(answer)


if __name__ == "__main__":
    main()
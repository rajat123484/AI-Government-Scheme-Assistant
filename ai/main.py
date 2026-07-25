from ai.interview import conduct_interview
from ai.rag import rag_pipeline
from ai.chatbot import local_answer, gemini_chat


def recommendation_session():
    """
    Collect user profile, recommend schemes,
    then start chatbot mode.
    """

    print("\nLet's find the best government schemes.\n")

    # Collect user profile
    user_profile = conduct_interview()

    print("\nCollected User Profile:")
    print(user_profile)

    print("\n🔍 Finding the best schemes for you...\n")

    # Run RAG Pipeline
    recommendation, retrieved_docs = rag_pipeline(user_profile)

    # Display Recommendation
    print("\n" + recommendation)

    # Chat Mode
    print("\n" + "=" * 70)
    print("💬 Chat Mode Started")
    print("=" * 70)
    print("You can now ask follow-up questions.")
    print()
    print("Examples:")
    print("• Am I eligible?")
    print("• What documents are required?")
    print("• Tell me the benefits")
    print("• Explain PM-KISAN")
    print("• How can I apply?")
    print("• Which scheme is best for me?")
    print("• Compare PM-KISAN and PMEGP")
    print("• Type 'exit' to return to the main menu.")
    print("=" * 70)

    while True:

        query = input("\nYou: ").strip()

        if query.lower() == "exit":
            print("\nReturning to Main Menu...\n")
            break

        if not query:
            continue

        # Try answering locally first (No Gemini API)
        answer = local_answer(
            query,
            retrieved_docs
        )

        # If local answer unavailable, ask Gemini
        if answer is None:

            print("\n🤖 Thinking...\n")

            answer = gemini_chat(
                question=query,
                user_profile=user_profile,
                schemes=retrieved_docs
            )

        print("\nAssistant:\n")
        print(answer)


def main():

    while True:

        print("\n" + "=" * 65)
        print("🇮🇳 AI Government Scheme Assistant")
        print("=" * 65)
        print("1. Find Government Schemes")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            recommendation_session()

        elif choice == "2":
            print("\nThank you for using AI Government Scheme Assistant!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
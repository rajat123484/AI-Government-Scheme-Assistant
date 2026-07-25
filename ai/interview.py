from ai.memory import ChatMemory

memory = ChatMemory()


def ask(question, key):
    """
    Ask one question and save the answer.
    """

    answer = input(f"\n🤖 {question}\n> ").strip()

    memory.update(key, answer)

    return answer


def conduct_interview():

    print("=" * 65)
    print("🇮🇳 Welcome to AI Government Scheme Assistant")
    print("=" * 65)

    print("\nHello! 👋")
    print("I'll ask a few simple questions to find the best government schemes for you.")

    ask("What is your age?", "age")

    ask("Which state do you live in?", "state")

    ask("What is your gender?", "gender")

    ask("What is your occupation? (Student / Farmer / Employee / Business)", "occupation")

    ask("What is your annual family income (₹)?", "income")

    ask("Which category do you belong to? (General / OBC / SC / ST)", "category")

    ask("Do you have any disability? (Yes / No)", "disability")

    print("\n✅ Thank you!")
    print("Finding the best schemes for you...")

    return memory.get_profile()
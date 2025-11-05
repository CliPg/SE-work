from .conclusion import quest

if __name__ == "__main__":
    question1 = "大语言模型技术的应用成本的主流看法是什么？"
    question2 = "大语言模型技术的潜在应用领域的主流看法是什么"
    question3 = "大语言模型技术的带来的不利影响有哪些"
    
    questions = [question1, question2, question3]
    
    for question in questions:
        print(f"问题: {question}")
        quest(question)
        print("-" * 50)

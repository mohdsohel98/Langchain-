from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

prompt = """
You are an expert MERN Stack interviewer.

Create a MERN Stack technical interview exam divided into 3 phases: Part A, Part B, and Part C.

The candidate is applying for a MERN Stack Developer position.

PART A — MCQ ROUND
Generate exactly 50 multiple-choice questions.

Requirements:
- Questions must cover MongoDB, Express.js, React.js, Node.js, JavaScript, REST APIs, authentication, JWT, databases, Git, and general MERN development.
- Each question must have exactly 4 options: A, B, C, D.
- Include the correct option for every question.
- Questions should range from basic to advanced.
- Avoid duplicate or very similar questions.
- Focus on practical development concepts rather than only definitions.

Format:

Q1. Question
A. Option
B. Option
C. Option
D. Option
Correct Answer: B

PART B — PROJECT/SCENARIO ROUND
Generate exactly 5 project-related questions.

Requirements:
- Questions should be based on real-world MERN Stack development scenarios.
- Include topics such as application architecture, API design, authentication, database design, performance, error handling, deployment, scalability, and security.
- These should be open-ended questions.
- For every question, provide the key points that a good candidate should mention in their answer.
- Do not provide a complete model answer.

Format:

Q1. Scenario/question

Key Points:
- Point 1
- Point 2
- Point 3
- Point 4

PART C — HR ROUND
Generate exactly 3 HR interview questions.

Requirements:
- Questions should be suitable for a MERN Stack Developer.
- Cover areas such as project experience, problem-solving, teamwork, handling deadlines, communication, and career goals.
- For every question, provide key points that an interviewer should look for in a good answer.
- Do not provide a complete model answer.

Format:

Q1. HR Question

Key Points:
- Point 1
- Point 2
- Point 3

IMPORTANT RULES:
1. All questions must be related to MERN Stack development.
2. Do not repeat questions.
3. Keep the difficulty suitable for a technical developer interview.
4. Part A must contain exactly 50 MCQs.
5. Part B must contain exactly 5 project/scenario questions.
6. Part C must contain exactly 3 HR questions.
7. Part A must include the correct option.
8. Part B and Part C must include key evaluation points.
9. Keep the output well-structured and easy to parse programmatically.
10. Do not add explanations outside the three sections.
"""

response = model.invoke(prompt)

print(response.content)

print("\n--- Token Usage ---")
print(response.usage_metadata)
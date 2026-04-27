from openai import OpenAI
from config import LLM_MODEL

def generate_guidance(question):
    client = OpenAI()
    prompt = f"""
You are an expert AI Interview Coach.

The candidate has just been asked the following interview question:
"{question}"

Your job is to provide a COMPLETE, REALISTIC, AND HIGH-QUALITY example answer that the candidate can use as inspiration or adapt on the fly. 

STRICT RULES:
- Provide a direct, realistic answer to the question.
- Write it in the first person ("I").
- If it is a behavioral question, structure the realistic answer using the STAR method naturally.
- Keep the length to a concise speaking length (around 100-150 words) so they can read or paraphrase it quickly.
- Do NOT output formatting fluff, just provide the answer.

Format:
[Realistic Answer]
<The full first-person response>

[Pro-Tip]
<One quick tip on delivery>
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def crete_resume(data):
    prompt = f'''You are a professional resume writer".
        Create polished resume from the raw details.
        IMPROVE the languge - use action verbs,professional pharsing.
        Name:{data['name']}
        Course:{data['course']}
        Skills:{data['skills']}
        Experinece:{data['experience']}
        Target Role: {data['job_target']} 
        Create this sections:
        - PROFESSIONAL SUMMARY(3 Lines)
        - KEY Skills (bullet points)
        - EDUCATION
        - EXPERIENCE(with action verbs)
        - PROJECTS(with action verbs)
        format it cleanly and make it ready to submit
    '''
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[{"role" : "system" ,"content": "act as resume genrator"},
                 {"role" : "user" ,"content": prompt}],
        max_tokens = 300,
        temperature = 0.5
    )
    
    return response.choices[0].message.content

print("###--Ai Resume Genrator--###")
print("Enter Following Details.")
data = {
    "name" : input("Enter Name : "),
     "course" : input("Enter Course : "),
      "skills" : input("Enter Skills : "),
       "experience" : input("Enter Experience : "),
        "job_target" : input("Enter Job_target : "),
}

print("Building Your Resume...")
resume = crete_resume(data)
print(resume)
filename = data['name'].lower().replace(' ','_')+'_resume.txt'

with open (filename,'w',encoding='utf-8') as f:
    f.write(resume)

print("File Svaed!")
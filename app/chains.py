import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(model_name="llama-3.3-70b-versatile",temperature=0, groq_api_key= os.getenv("GROQ_API_KEY"))

    def extractJobs(self, cleanedText):
        promptExtract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM THE WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job posting and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Ensure the skills field is always a list of strings, even if empty.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):    
            """
        )
        chainExtract = promptExtract | self.llm
        res = chainExtract.invoke(input={'page_data': cleanedText})
        try:
            jsonParser = JsonOutputParser()
            parsed_res = jsonParser.parse(res.content)
            # Ensure we have a list of jobs
            jobs = parsed_res if isinstance(parsed_res, list) else [parsed_res]
            # Ensure each job has a skills list
            for job in jobs:
                if 'skills' not in job:
                    job['skills'] = []
                elif isinstance(job['skills'], str):
                    job['skills'] = [job['skills']]
            return jobs
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        

    def writeEmail(self, job, links):
        promptEmail = PromptTemplate.from_template(
            '''
            ### JOB DESCRIPTION:
            {job_description}

            ### CANDIDATE INFO:
            Name: Shubham
            Current Role: Graduate Software Engineer Researcher at Drexel University
            Work Experience: 
            - Graduate Software Engineer Researcher at Drexel University (AI/ML Research)
            - Software Engineer Co-op at Fleet Foundation (Full-Stack Development)
            - Software Engineer Co-op at Tract (Full-Stack Development)
            Key Skills: [Extract relevant skills from job posting that match candidate background]

            ### INSTRUCTION:
            Write a cold email application following this EXACT format:

            Subject: Application for [Role] Position - Graduate Software Engineer Researcher

            Dear Hiring Manager,

            [First paragraph: Express interest in the role, mention company name, and briefly state how you found the position]

            [Second paragraph: Highlight your experience as a Graduate Software Engineer Researcher at Drexel and your two software engineering co-op roles at Fleet Foundation and Tract, focusing on experiences relevant to the job requirements]

            [Third paragraph: Highlight 2-3 specific technical skills that match their needs, mentioning relevant portfolio links]

            [Fourth paragraph: Brief closing with call to action]

            Best regards,
            Shubham

            Use these portfolio links in the third paragraph: {link_list}
            Keep the tone professional yet enthusiastic.
            Do not use placeholder text - fill in all details based on the job description.
            ### EMAIL (NO PREAMBLE):
            '''
        )
        chainEmail = promptEmail | self.llm
        res = chainEmail.invoke(input={'job_description': str(job), 'link_list': links})
        return res.content


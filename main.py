from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover Top 5 AI technology Innovations in February 2024',
  backstory='A curious mind fascinated by cutting-edge AI innovation and the potential to change the world, you know everything about AI tech.',
  verbose=True,
  tools=[search_tool],
  allow_delegation=False,
)

insight_researcher = Agent(
  role='Insight Researcher',
  goal='Discover Key Insights',
  backstory='You are able to find key insights from the data you are given.',
  verbose=True,
  allow_delegation=False,
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a content strategist known for 
  making complex tech topics interesting and easy to understand.""",
  verbose=True,
  allow_delegation=False,
)

formater = Agent(
  role='Markdown Formater',
  goal='Format the text in markdown',
  backstory='You are able to convert the text into markdown format',
  verbose=True,
  allow_delegation=False,
)

# Tasks
research_task = Task(
  description='Identify the next big trend in AI by searching internet once',
  agent=researcher
)

insight_task = Task(
  description='Find key insights from the data. Dont use any tool',
  agent=insight_researcher
)

write_task = Task(
  description='Write a blog post. Dont use any tool',
  agent=writer
)

format_task = Task(
  description='convert the input to markdown format',
  agent=formater
)

# Instantiate a crew
tech_crew = Crew(
  agents=[researcher, insight_researcher, writer, formater],
  tasks=[research_task, insight_task, write_task, format_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
result = tech_crew.kickoff()
print(result)
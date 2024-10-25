from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, FileReadTool,FileWriterTool
from crewai import llm


# Uncomment the following line to use an example of a custom tool
# from linkedin_creative.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class LinkedinCreativeCrew():
	"""LinkedinCreative crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
   			tools=[SerperDevTool()]
		)

	@agent
	def copywriter(self) -> Agent:
		return Agent(
      config=self.agents_config['copywriter'],
      #tools=[FileReadTool(),FileWriterTool()],
      verbose=True
      )
	
	@agent
	def factchecker(self) -> Agent:
		return Agent(
      config=self.agents_config['factchecker'],
      #tools=[FileReadTool(),FileWriterTool()],
      verbose=True
      )
	
	@agent
	def editor(self) -> Agent:
		return Agent(
      config=self.agents_config['editor'],
      #tools=[FileReadTool(),FileWriterTool()],
      verbose=True
      )
	

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
   			output_file='research.json'
		)

	@task
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
			output_file='post.md'
		)
	@task
	def fact_checking_task(self) -> Task:
		return Task(
			config=self.tasks_config['fact_checking_task'],
			output_file='post_fact_checked.md'
		)
	@task
	def editing_task(self) -> Task:
		return Task(
			config=self.tasks_config['editing_task'],
			output_file='post_edited.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LinkedinCreative crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

from openai import OpenAI

client = OpenAI(
    
)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo"
)
## Prints the assistant object
# print(f"{assistant}\n")


## Creates a thread
thread = client.beta.threads.create()
# print(f"{thread}\n")

## Add MSG to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Solve this problem: 3x + 11 = 14"
)

# print(f"{message}\n")


## Create a run
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  
)



## Display the response
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)



## Print the MSGS
for message in reversed(messages.data):

   print(message.role + ": " + message.content[0].text.value)

# print(print(f"\n\n{assistant}"))

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)

  file = client.files.create(
    file = open("test.py","rb"),
    purpose="assistants"
)
print(file)

assistant = client.beta.assistants.create(
    name="Machine Learning",
    instructions="You are a machine learning expert, answer questions on the research paper",
    tools=[{"type": "file_search"}],
    model="gpt-3.5-turbo",
   
)

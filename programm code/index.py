import json

tasks = {}

with open('test.json') as f:
  tasks = json.load(f)

while True:
  print("Select difficult:")
  difficulty = input("(easy, medium, hard, exit) ")

  task_d = {}
  
  if difficulty == 'easy':
    task_d = tasks["easy"]
  elif difficulty == 'medium':
    task_d = tasks["medium"]
  elif difficulty == 'hard':
    task_d = tasks["hard"]
  else:
    break

  for key, task in task_d.items():
    print("Next task? (yes/no): ")
    next_task = input("")
    if next_task == 'no':
      break

    while True:
      print("\n" + task["question"])
      var = "\n".join(iter(input, ""))

      if1 = False
      if2 = False
      if3 = False

      try:
        exec(var)
        if1 = eval(task["if"])
        if2 = eval(task["if2"])
        if3 = eval(task["if3"])
      except:
        print("Error!")

      if if1 == True and if2 == True and if3 == True:
        print("Success")
        break
      else:
        print("Wrong")
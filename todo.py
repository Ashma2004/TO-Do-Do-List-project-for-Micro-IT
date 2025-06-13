tasks=[]
while True:
  choice=input("what do you want to do?\n1.Add Task\n2.View Tasks\n3.Remove Task\n4.edit details\n5.Mark as complete\nenter your choice:")
  if choice=="1":
    add_task=input("enter a task to add:")
    tasks.append(add_task)
  elif choice=="2":
    print(*tasks,sep="\n")
  elif choice=="3":
    remove_task=input("enter a task to remove:")
    if remove_task in tasks:
      tasks.remove(remove_task)
      print(*tasks,sep="\n")
    else:
      print("the task you entered is not in the tasks list,so it can't be removed")
  elif choice=="4":
    edit_task=input("enter a task to edit:")
    if edit_task in tasks:
      edit=tasks.index(edit_task)
      tasks[edit]=input("enter a updated task:")
      print(*tasks,sep="\n")
    else:
      print("the task you entered to edit is not in the tasks list,so it can't be updated")
  elif choice=="5":
    complete_task=input("enter a task to mark as complete:")
    if complete_task in tasks:
      if  complete_task + " ✅" not in tasks:
          complete=tasks.index(complete_task)
          tasks[complete]=complete_task + " ✅"
          print(*tasks,sep='\n')
      else:
        print("this task is already marked as complete")
    elif complete_task + " ✅"  in tasks:
       print("this task is already marked as complete")
    else:
      print("the task you entered to mark as complete is not in the task list,so it can't be marked as complete")
  else:
    print("Thank you for using to-do list!")
    break

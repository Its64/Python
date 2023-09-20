import flet as ft
from io import StringIO 
import sys
import json

tasks = {}

with open('test.json') as f:
  tasks = json.load(f)

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def main(page: ft.Page):
    page.title = "Program"

    task_count = 0
    task = {}
    task_type = "var"
    tasks_main = {}

    def next_task(args):
      nonlocal task_count
      task_count += 1
      print(task)
      update()
      page.update()

    def update():
      nonlocal task_count
      nonlocal task
      nonlocal task_type
      nonlocal tasks_main
      nonlocal task_text

      match task_type:
        case "var":
          tasks_main = tasks["var"]
        case "func":
          tasks_main = tasks["func"]
        case "if":
          tasks_main = tasks["if"]
        case "while":
          tasks_main = tasks["while"]
      
      task = tasks_main[str(task_count)]
      task_text.value = task["question"]
      code.value = ""
      page.update()

    match task_type:
      case "var":
        tasks_main = tasks["var"]
      case "func":
        tasks_main = tasks["func"]
      case "if":
        tasks_main = tasks["if"]
      case "while":
        tasks_main = tasks["while"]
    
    task = tasks_main[str(task_count)]
    print(task)

    task_text = ft.Text(value=task["question"])

    code = ft.TextField(
      value="# Write your code.",
      multiline=True,
      min_lines=15,
      max_lines=15,
    )

    def run(args=False):
        try:
          with Capturing() as output:
            exec(code.value)

          print("Running")
          exec(code.value)
          output_final = ""

          for i in output:
            output_final += i + "\n"

          output_text.value = output_final
          page.update()
        except:
          with Capturing() as output:
            print("Error")
          output_text.value = output
          page.update()

    output_text = ft.Text(value="Output")

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Variables",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
                ft.ElevatedButton(
                    text="Functions",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
                ft.ElevatedButton(
                    text="If, else",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
                ft.ElevatedButton(
                    text="While, for",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
                ft.ElevatedButton(
                    text="Sandbox",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
            ]
        )
    )

    page.add(task_text)

    page.add(code)

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Run",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=run,
                ),
                ft.ElevatedButton(
                    text="Next task",
                    bgcolor=ft.colors.BLUE_GREY_100,
                    color=ft.colors.BLACK,
                    expand=1,
                    on_click=next_task,
                    # data=0,
                ),
            ]
        )
    )

    page.add(output_text)

ft.app(target=main)
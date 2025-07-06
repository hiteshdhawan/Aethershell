# Created by Hitesh Dhawan
# Main Execution File
# Updated on July 2, 2025
from prompt_engine import generate_action_plan
from step_executor import execute_plan
from memory import remember, recall_all, clear_memory

def main():
    print("Hi This tool should support you in working on linux.")
    print("Type a task, 'memory' to view log, or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ("exit", "quit"):
                print(" Exiting AetherShell.")
                break

            elif user_input.lower() == "memory":
                mem = recall_all()
                if not mem:
                    print("Memory is empty.")
                else:
                    print("\n Memory Log:")
                    for i, entry in enumerate(mem, 1):
                        print(f"[{i}] Task: {entry['task']}")
                        print(f"     Result: {entry['result']}\n")
                continue

            elif user_input.lower() == "clear memory":
                clear_memory()
                print(" Memory cleared.")
                continue

           
            plan = generate_action_plan(user_input)
            if "error" in plan:
                print(f" Error: {plan['error']}")
                continue

            print(f"\n Goal: {plan['goal']}")
            print(" Steps:")
            for step in plan['steps']:
                print(f"  - {step}")

            print(f"\n Final Command:\n{plan['final_command']}")
            confirm = input("\nRun final command? [y/N]: ").strip().lower()

            if confirm == 'y':
                execute_plan(plan['final_command'])
                remember(user_input, plan['final_command'])  # Save to memory
            else:
                print("Command not executed.")

        except KeyboardInterrupt:
            print("\nExiting AetherShell.")
            break
        except Exception as e:
            print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()

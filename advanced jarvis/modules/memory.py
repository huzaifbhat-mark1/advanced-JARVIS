import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return {}

def save_memory(question, answer):
    memory = load_memory()
    memory[question] = answer
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=2)

def read_memory():
    memory = load_memory()
    if not memory:
        return "I don't remember anything yet."
    return "\n".join([f"Q: {q}\nA: {a}" for q, a in memory.items()])

def clear_memory():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
        return "Memory cleared."
    else:
        return "No memory found to clear."

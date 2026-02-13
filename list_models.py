
import azure.ai.projects.models
with open("models_list.txt", "w") as f:
    for name in dir(azure.ai.projects.models):
        f.write(name + "\n")

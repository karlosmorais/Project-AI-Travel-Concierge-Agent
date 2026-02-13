import azure.ai.projects.models as models
print("Classes with Agent:")
for x in dir(models):
    if "Agent" in x:
        print(x)

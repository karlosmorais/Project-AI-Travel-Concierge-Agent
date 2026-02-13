
try:
    import azure.ai.projects.models
    print("azure.ai.projects.models contents:")
    print(dir(azure.ai.projects.models))
except Exception as e:
    print(f"Error importing models: {e}")

try:
    import azure.ai.projects
    print("\nazure.ai.projects contents:")
    print(dir(azure.ai.projects))
except Exception as e:
    print(f"Error importing projects: {e}")

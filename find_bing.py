
try:
    import azure.ai.projects.models
    names = dir(azure.ai.projects.models)
    bing_names = [n for n in names if "Bing" in n]
    print(f"Bing related in models: {bing_names}")
    
    import azure.ai.projects
    names2 = dir(azure.ai.projects)
    bing_names2 = [n for n in names2 if "Bing" in n]
    print(f"Bing related in projects: {bing_names2}")

except Exception as e:
    print(f"Error: {e}")

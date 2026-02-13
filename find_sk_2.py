
locations = [
    "semantic_kernel.connectors.ai.open_ai",
    "semantic_kernel.connectors.ai.function_choice_behavior",
    "semantic_kernel.functions.function_choice_behavior",
    "semantic_kernel.core_plugins",
]

for loc in locations:
    try:
        module = __import__(loc, fromlist=['FunctionChoiceBehavior'])
        if hasattr(module, 'FunctionChoiceBehavior'):
            print(f"FOUND in {loc}")
        else:
            print(f"Not in {loc}")
    except ImportError:
        print(f"ImportError for {loc}")
    except Exception as e:
        print(f"Error checking {loc}: {e}")

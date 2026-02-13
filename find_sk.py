
try:
    import semantic_kernel
    print(f"SK Version: {semantic_kernel.__version__}")
    
    import semantic_kernel.functions
    if hasattr(semantic_kernel.functions, 'FunctionChoiceBehavior'):
        print("Found in semantic_kernel.functions")
    else:
        print("Not in semantic_kernel.functions")
        
    import semantic_kernel.connectors.ai.open_ai
    if hasattr(semantic_kernel.connectors.ai.open_ai, 'FunctionChoiceBehavior'):
        print("Found in semantic_kernel.connectors.ai.open_ai")

    # Search recursively?
    # Or just check dir of some modules
    
except Exception as e:
    print(f"Error: {e}")

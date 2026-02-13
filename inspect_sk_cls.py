
import semantic_kernel.connectors.ai.open_ai as sk_openai
print(f"SK OpenAI dir: {dir(sk_openai)}")

try:
    from semantic_kernel.connectors.ai.open_ai import OpenAIPromptExecutionSettings
    print("OpenAIPromptExecutionSettings found.")
    print(dir(OpenAIPromptExecutionSettings))
except:
    print("OpenAIPromptExecutionSettings NOT found.")

# Try to find FunctionChoiceBehavior
import semantic_kernel
import pkgutil
print("Listing submodules of semantic_kernel...")
# Recursive search is too much output. 
# Let's search by string in specific likely places.

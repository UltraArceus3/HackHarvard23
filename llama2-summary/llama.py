from transformers import AutoTokenizer, AutoModelForCausalLM

access_token = "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"



tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-chat-hf", use_auth_token=access_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-chat-hf", use_auth_token=access_token)

with open("pizza_full.txt", "r") as f:
    pizz = f.readline()

tok = tokenizer(pizz)

print(model(pizz))
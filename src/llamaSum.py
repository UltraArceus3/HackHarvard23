from transformers import AutoTokenizer, AutoModelForCausalLM

access_token = ""



tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=access_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=access_token)
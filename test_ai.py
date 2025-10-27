from transformers import pipeline

generator = pipeline('text-generation', model='distilgpt2')
result = generator("Once upon a time in a haunted forest", max_length=50, num_return_sequences=1)
print(result[0]['generated_text'])
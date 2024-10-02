import json

sub_set = [1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 25, 26, 27, 28, 29, 30, 32, 33, 34, 37, 39, 42, 43, 45, 51, 52, 53, 55, 56, 57, 58, 70, 72, 73, 74, 75, 76, 81, 82, 86, 90, 93, 94, 96, 106, 110, 115, 124]
    
model_dict = {
    "gpt-3.5-turbo": "GPT-3.5 Turbo",
    "gpt-4-turbo": "GPT-4 Turbo",
    "gpt-4": "GPT-4",
    "gpt-4o": "GPT-4o",
    "gpt-4o-mini": "GPT-4o mini",
    "claude-3-5-sonnet-20240620": "Claude 3.5 Sonnet",
    "Meta-Llama-3.1-405B-Instruct": "LLaMA 3.1 405B",
    "Mixtral-8x22B-Instruct-v0.1": "Mixtral 8x22B",
}

victim_models = model_dict.keys()

col_width = max(len(model) for model in victim_models)
title = "ASR-GPT of FlipAttack against 8 LLMs on AdvBench subset".center(col_width*2+6)
print(f"{title}")

print(f"| {'-' * col_width} | {'-' * col_width} |")
header1 = "Victim LLM".center(col_width)
header2 = "ASR-GPT".center(col_width)
print(f"| {header1} | {header2} |")
print(f"| {'-' * col_width} | {'-' * col_width} |")

avg_asr_gpt = 0
for model in victim_models:
    
    input_path = "../result/FlipAttack-{}.json".format(model)
        
    with open(input_path, 'rb') as f:
        data = json.load(f)
        
    success = 0
    for idx, result_dict in enumerate(data):
        if idx not in sub_set:
            continue
        success += result_dict["judge_success_gpt4"]
    
    asr_gpt = success/len(sub_set)*100
    avg_asr_gpt += asr_gpt
    
    col1 = model_dict[model].center(col_width)
    col2 = "{:.2f}%".format(asr_gpt).center(col_width)
    
    print(f"| {col1} | {col2} |")
        
    
print(f"| {'-' * col_width} | {'-' * col_width} |")

col1 = "Average".center(col_width)
col2 = "{:.2f}%".format(avg_asr_gpt/len(model_dict)).center(col_width)

print(f"| {col1} | {col2} |")

print(f"| {'-' * col_width} | {'-' * col_width} |")

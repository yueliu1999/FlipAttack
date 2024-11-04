import json

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

col_width = 20

sub_category_path = "../result/sub_category_gpt4.json"
with open(sub_category_path, 'rb') as f:
    sub_category = json.load(f)


for model in victim_models:
    input_path = "../result/FlipAttack-{}.json".format(model)
    with open(input_path, 'rb') as f:
        data = json.load(f)
    save_dict = {}
    print(f"| {'-' * col_width} | {'-' * col_width} |")
    header1 = model_dict[model].center(col_width*2)
    
    print(f"|   {header1}  |")
    
    print(f"| {'-' * col_width} | {'-' * col_width} |")
    header1 = "Category".center(col_width)
    header2 = "ASR-GPT".center(col_width)
    print(f"| {header1} | {header2} |")
    print(f"| {'-' * col_width} | {'-' * col_width} |")
    
    for idx, item in enumerate(data):
        
        success = item['judge_success_gpt4']
        
        # merge
        if sub_category[idx]["model_output"] == '1':
            sub_category[idx]["model_output"] = '0'

        if sub_category[idx]["model_output"] == '11':
            sub_category[idx]["model_output"] = '6'

        if sub_category[idx]["model_output"] == '9':
            sub_category[idx]["model_output"] = '8'
        
        if int(sub_category[idx]["model_output"]) not in save_dict.keys():
            save_dict[int(sub_category[idx]["model_output"])] = {}
            save_dict[int(sub_category[idx]["model_output"])]["total"] = 0
            save_dict[int(sub_category[idx]["model_output"])]["success"] = 0
            
        save_dict[int(sub_category[idx]["model_output"])]["total"] += 1
        
        if success:
            save_dict[int(sub_category[idx]["model_output"])]["success"] += 1
            
    success = 0
    total = 0
    for idx, item in enumerate(save_dict):
        success += save_dict[item]['success']
        total += save_dict[item]['total']
        
        if item == 3:
            col1 = "Malware".center(col_width)
            
        if item == 8:
            col1 = "Privary Violence".center(col_width)

        if item == 4:
            col1 = "Phsical Harm".center(col_width)
        
        if item == 2:
            col1 = "Hate Speech".center(col_width)
        
        if item == 5:
            col1 = "Economic Harm".center(col_width)
        
        if item == 6:
            col1 = "Fraud".center(col_width)
        
        if item == 0:
            col1 = "Illegal Activity".center(col_width)
        
        col2 = "{:.2f}%".format(save_dict[item]['success']/save_dict[item]['total']*100).center(col_width)
        
        print(f"| {col1} | {col2} |")
            
    print(f"| {'-' * col_width} | {'-' * col_width} |")
    print()
    print()

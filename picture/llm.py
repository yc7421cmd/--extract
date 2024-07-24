import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
base_path = './StyleShot'
os.system('apt install git')
os.system('apt install git-lfs')
os.system(f'git clone https://code.openxlab.org.cn/houshaowei/StyleShot.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
tokenizer = AutoTokenizer.from_pretrained(base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path,trust_remote_code=True, torch_dtype=torch.float16)
print("Model loading done!")

# 准备文本数据  
text_data = "There is a clock and a table in the picture. There is a computer on the table."  

# 对文本进行编码  
input_ids = tokenizer.encode(text_data, return_tensors="pt")  

# 生成图片  
output = model.generate(input_ids, max_length=100)  

# 可视化图片  
output_image_path = 'output_image.png'  
with open(output_image_path, 'wb') as f:  
    f.write(output)  

print(f"生成的图片已保存到 {output_image_path}")
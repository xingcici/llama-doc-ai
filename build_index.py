import logging
import os
import sys
from langchain import OpenAI
from llama_index import (SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext)
import openai

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


def find_md_files(path):
    md_files = []

    for entry in os.scandir(path):
        if entry.is_file() and entry.name.endswith('.md'):
            md_files.append(entry.path)
        elif entry.is_dir():
            md_files.extend(find_md_files(entry.path))

    return md_files


if __name__ == '__main__':
    # 读取data文件夹下的文档
    documents = SimpleDirectoryReader(input_files=find_md_files('data')).load_data()

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=512))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    index = GPTSimpleVectorIndex.from_documents(documents)
    # 保存索引
    index.save_to_disk('index.json')

from flask import Flask
import logging
import os
import sys

from flask import Flask
from flask import request
from gevent import pywsgi
from langchain import OpenAI
from llama_index import (GPTSimpleVectorIndex, LLMPredictor, ServiceContext)
import openai

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

app = Flask(__name__)

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=512))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
index = GPTSimpleVectorIndex.load_from_disk('index.json',
                                            service_context=service_context)


def query(prompt, new_index):
    os.environ["OPENAI_API_KEY"] = 'xxx'
    # 查询索引
    response = new_index.query(prompt + "请用简体中文回答", mode="embedding")
    # 打印答案
    print(response)
    return response

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    prompt = data['prompt']

    res = query(prompt, index)

    return {
        "code": 200,
        "data": {
            "prompt": prompt,
            "answer": res,
        },
    }


if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0', 8082), app)
    # server.serve_forever()
    app.run(host='0.0.0.0', port=8082)

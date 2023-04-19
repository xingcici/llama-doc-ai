# vdian-doc-ai
base `openai` `llama_index`

### env prepare
```angular2html
export OPENAI_API_KEY = xx

pyenv is recommended !

1. python version >= 3.9

2. python -m pip install -r requirements.txt --index http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
```

### if need refresh index
```angular2html
# proxychains for proxy

proxychains nohup python build_index.py &

notice : after refresh index need restart server

```

### run sever
```angular2html
# if you don't need proxy, skip this -------
1. yum install -y proxychains-ng

2. vim /etc/proxychains.conf

3. proxychains nohup python main.py &
# skip end                           -------

4. python main.py

blind on port 8082 🚀
```

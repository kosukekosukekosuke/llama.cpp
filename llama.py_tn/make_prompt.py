from llama_cpp import Llama
import get_data

llm = Llama(model_path="/home/amsl/src/llama.cpp/models/llama-2-7b-chat.q4_K_M.gguf")
#変数
filename="/home/amsl/src/llama.cpp/llama.py_tn/ikuta_graph.yaml"
ids=[]
labels=[]
choices=""

#コマンドプロンプトからリクエストを取得
q=input("Please enter your request: ")

#yamlファイルからIDとlabelを取得
ids,labels=get_data.from_yaml(filename)
for i in range(len(ids)):
        choices+=str(ids[i]) + "." + labels[i] + ", "

prompt = "User: " + q + " Please choose the most suitable destination from the following options and answer with numbers only. " + choices +"\n" + "Assistant: "

output = llm(
    prompt,
    temperature=0.1,
    stop=["User:", "Assistant:", "\n"],
    echo=True,
)

print(output["choices"][0]["text"])
#print(output["choices"])
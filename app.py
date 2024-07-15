import gradio as gr
from openai import OpenAI

client = OpenAI(
    api_key=""
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {
        "role": "system",
        "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手"
    }
]

output = ""


def chat(query):
    global history
    global output

    history.append({
        "role": "user",
        "content": query
    })
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    if result is not None:
        history.append({
            "role": "assistant",
            "content": result
        })
        output = output + result + "\n\n"

    return output


# 使用 Gradio 2.0+ 的新 API 创建接口
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=10, placeholder="请输入你的问题..."),
    outputs=gr.Text(lines=10),
    examples=["你好，Kimi！"],
)

# 启动 Gradio 应用
iface.launch(share=True)

import openai  
import sys  
from flask import Flask, render_template, request, jsonify  

app = Flask(__name__, template_folder='web')  

class OpenAIClient:  
    def __init__(self, base_url, api_key):  
        openai.api_base = base_url  
        openai.api_key = api_key  

    def chat(self, messages):  
        try:  
            # Gọi đến phương thức openai.ChatCompletion.create với danh sách tin nhắn  
            response = openai.ChatCompletion.create(  
                model="gemma2:2b",  # Hoặc tên mô hình bạn đang sử dụng  
                messages=messages,  
            )  
            return response.choices[0].message['content']  # Trả về nội dung phản hồi  
        except Exception as e:  
            print(f"Error: {e}")  
            return None  

client = OpenAIClient(base_url="http://localhost:11434/v1", api_key="ollama")  

# Set the stdout encoding to utf-8  
sys.stdout.reconfigure(encoding='utf-8')  

# Danh sách để lưu các tin nhắn  
messages = []  

@app.route('/')  
def home():  
    return render_template('index.html')  

@app.route('/chat', methods=['POST'])  
def chat():  
    user_message = request.json['message']  
    
    # Thêm tin nhắn của người dùng vào danh sách  
    messages.append({"role": "user", "content": user_message})  

    # Gửi một tin nhắn và nhận phản hồi từ AI   
    response = client.chat(messages)  

    if response:  # Nếu có phản hồi hợp lệ từ AI  
        # Thêm phản hồi của AI vào danh sách tin nhắn  
        messages.append({"role": "assistant", "content": response})  

        # Trả về phản hồi cho client  
        return jsonify({'response': response})  
    else:  
        return jsonify({'response': "Đã xảy ra lỗi trong quá trình xử lý."}), 500  # Trả về lỗi nếu không có phản hồi  

if __name__ == '__main__':  
    app.run(debug=True)
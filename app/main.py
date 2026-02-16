from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from backend import save_thought, analyze_thought_with_ai

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
      <body>
        <h2>CBT 思考記録フォーム</h2>
        <form action="/submit" method="post">
          思考: <input type="text" name="thought" size="50"><br>
          気分 (1-10): <input type="number" name="mood" min="1" max="10"><br>
          <input type="submit" value="送信">
        </form>
      </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit(thought: str = Form(...), mood: int = Form(...)):
    # 1. 保存
    save_thought(thought, mood)
    # 2. AI分析
    result = analyze_thought_with_ai(thought)
    # 3. 結果表示
    return f"""
    <html>
      <body>
        <h2>分析結果</h2>
        <p><strong>あなたの思考:</strong> {thought}</p>
        <p><strong>AIの分析と改善提案:</strong></p>
        <pre>{result}</pre>
        <a href="/">戻る</a>
      </body>
    </html>
    """

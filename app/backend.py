#CBT分析とAIの呼び出し
import json, os
import openai  # OpenAI API を利用する想定

openai.api_key = "YOUR_OPENAI_API_KEY"  # 環境変数推奨

DATA_FILE = "data.json"

def save_thought(thought: str, mood: int):
    """ユーザーの気分と思考を保存"""
    entry = {"thought": thought, "mood": mood}
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    data.append(entry)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def analyze_thought_with_ai(thought: str):
    """OpenAI APIを呼び出して分析・改善提案"""
    prompt = f"""
あなたは認知行動療法の専門家です。
以下のユーザーの思考を分析してください。
1. ネガティブ思考の判定
2. 思考の歪み（全か無か思考、過剰一般化、感情的推論など）の検出
3. ポジティブな置き換え思考の提案
4. 実行可能な行動課題（簡単な運動やタスクなど）の提案

ユーザーの思考: "{thought}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content":prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

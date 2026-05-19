import os
from openai import OpenAI

# 初始化客户端，针对小米 Token Plan 专属端点进行配置
# 申请通过后，请在环境变量中设置您的 Token Plan 专属 Key (以 tp- 开头)
client = OpenAI(
    api_key=os.environ.get("MIMO_API_KEY", "tp-your-token-plan-key-here"),
    base_url="https://token-plan-cn.xiaomimimo.com/v1" 
)

def query_radio_expert(prompt: str):
    """
    调用 MiMo-V2.5-Pro 模型，解答通信设备相关问题
    """
    try:
        response = client.chat.completions.create(
            model="mimo-v2.5-pro",
            messages=[
                {
                    "role": "system", 
                    "content": "你是一位资深的专家，精通全球各类电台的通信协议、频段技术规格、组网方式以及装备分类体系。请提供严谨、专业的技术解答。"
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.3, # 使用较低的温度参数以保证技术规格输出的严谨性
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"通信链路异常或 API 认证失败: {e}"

if __name__ == "__main__":
    print("MIMO Tactical Radio Agent 初始化完成...")
    print("-" * 50)
    
    # 核心测试用例
    test_query = "请从专家的角度，向我介绍目前主流的战术电台有哪些分类，以及它们在跳频抗干扰方面的核心技术规格。"
    print(f"用户提问: {test_query}\n")
    
    answer = query_radio_expert(test_query)
    print(f"Agent 回复:\n{answer}")
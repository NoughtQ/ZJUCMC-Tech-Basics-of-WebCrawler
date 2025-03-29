import requests  # 用于发送HTTP请求
from urllib.parse import urljoin  # 用于处理URL拼接
import time  # 用于添加延时

# 定义一个展示多种 requests 功能的爬虫函数
def advanced_web_crawler():
    # 目标URL（这里使用一个测试网站，可以替换为其他URL）
    base_url = "http://httpbin.org"
    
    # 1. 基本的 GET 请求
    print("=== 1. 发送基本的 GET 请求 ===")
    try:
        response = requests.get(f"{base_url}/get", timeout=5)
        print(f"状态码: {response.status_code}")
        print(f"响应头: {response.headers}")
        print(f"响应内容 (前100字符): {response.text[:100]}")
    except requests.RequestException as e:
        print(f"GET 请求出错: {e}")

    # 添加延时，避免请求太频繁
    time.sleep(1)

    # 2. 带参数的 GET 请求
    print("\n=== 2. 带参数的 GET 请求 ===")
    params = {"name": "Python", "version": "3.11"}
    response = requests.get(f"{base_url}/get", params=params, timeout=5)
    print(f"请求的URL: {response.url}")  # 查看带参数的完整URL
    print(f"JSON响应: {response.json()}")  # 解析JSON格式的响应

    time.sleep(1)

    # 3. POST 请求
    print("\n=== 3. 发送 POST 请求 ===")
    data = {"username": "test_user", "password": "123456"}
    response = requests.post(f"{base_url}/post", data=data, timeout=5)
    print(f"状态码: {response.status_code}")
    print(f"POST返回的JSON: {response.json()}")

    time.sleep(1)

    # 4. 使用会话对象 (Session) 保持状态
    print("\n=== 4. 使用会话对象 ===")
    session = requests.Session()
    # 设置自定义请求头
    session.headers.update({
        "User-Agent": "MyCustomCrawler/1.0",
        "Accept": "application/json"
    })
    response = session.get(f"{base_url}/cookies/set?user_id=12345", timeout=5)
    print(f"设置cookie后的响应: {response.json()}")
    # 再次请求，检查cookie是否保留
    response = session.get(f"{base_url}/cookies", timeout=5)
    print(f"当前cookies: {response.json()}")

    time.sleep(1)

    # 5. 处理重定向
    print("\n=== 5. 处理重定向 ===")
    response = requests.get(f"{base_url}/redirect/3", allow_redirects=True, timeout=5)
    print(f"最终URL: {response.url}")
    print(f"重定向历史: {response.history}")

    time.sleep(1)

    # 6. 下载二进制内容（如图片）
    print("\n=== 6. 下载二进制内容 ===")
    image_url = f"{base_url}/image/png"
    response = requests.get(image_url, timeout=5)
    if response.status_code == 200:
        # 保存图片到本地
        with open("downloaded_image.png", "wb") as f:
            f.write(response.content)
        print("图片已保存为 downloaded_image.png")
    else:
        print(f"下载失败，状态码: {response.status_code}")

    # 7. 设置超时和异常处理
    print("\n=== 7. 超时和异常处理 ===")
    try:
        response = requests.get("http://example.com", timeout=0.1)  # 故意设置很短的超时
    except requests.Timeout:
        print("请求超时，已捕获异常")
    except requests.RequestException as e:
        print(f"其他请求错误: {e}")

# 主程序入口
if __name__ == "__main__":
    print("开始运行爬虫示例...")
    advanced_web_crawler()
    print("爬虫示例运行结束！")
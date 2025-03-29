import urllib.request
import urllib.parse
import urllib.error

# 目标 URL
url = "https://httpbin.org/get"

# 构造请求对象（添加 User-Agent 伪装成浏览器）
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)

try:
    # 发送 GET 请求
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
    print("网页内容获取成功！")
except urllib.error.HTTPError as e:
    print(f"HTTP 错误: {e.code} {e.reason}")
except urllib.error.URLError as e:
    print(f"URL 错误: {e.reason}")

# 解析 URL
parsed_url = urllib.parse.urlparse(url)
print("\nURL 解析结果：", parsed_url)

# 发送 POST 请求（模拟登录）
post_url = "https://httpbin.org/post"
post_data = {"username": "admin", "password": "123456"}
encoded_data = urllib.parse.urlencode(post_data).encode("utf-8")  # 编码为 x-www-form-urlencoded 格式

req_post = urllib.request.Request(post_url, data=encoded_data, headers=headers)
with urllib.request.urlopen(req_post) as response:
    post_response = response.read().decode("utf-8")
print("\nPOST 请求返回结果：", post_response, sep="\n")

# 使用代理访问网页
proxy_handler = urllib.request.ProxyHandler({"http": "http://127.0.0.1:8080"})
opener = urllib.request.build_opener(proxy_handler)

try:
    with opener.open(req) as response:
        proxy_html = response.read().decode("utf-8")
    print("\n使用代理获取的网页内容：", proxy_html, sep="\n")
except urllib.error.URLError as e:
    print("\n代理访问失败：", e.reason)

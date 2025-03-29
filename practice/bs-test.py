import requests  # 用于发送HTTP请求
from bs4 import BeautifulSoup  # 用于解析HTML内容
import time  # 用于添加延时

# 定义一个展示 BeautifulSoup 功能的爬虫函数
def beautifulsoup_crawler():
    # 目标URL（这里使用 example.com 作为示例，可以替换为其他URL）
    url = "http://httpbin.org"
    
    # 设置请求头，模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124"
    }
    
    # 发送GET请求获取网页内容
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # 检查请求是否成功
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return

    # 创建 BeautifulSoup 对象来解析网页内容
    soup = BeautifulSoup(response.text, "html.parser")  # 使用 html.parser 解析器
    
    # 1. 获取网页标题
    print("=== 1. 获取网页标题 ===")
    title = soup.title  # 直接获取<title>标签
    if title:
        print(f"标题标签完整内容: {title}")
        print(f"标题文本: {title.string}")
    else:
        print("未找到标题")

    # 2. 查找单个元素
    print("\n=== 2. 查找单个元素 ===")
    first_link = soup.find("a")  # 查找页面中的第一个<a>标签
    if first_link:
        print(f"第一个链接的完整标签: {first_link}")
        print(f"链接文本: {first_link.text}")
        print(f"链接地址: {first_link.get('href')}")
    else:
        print("未找到链接")

    # 3. 查找所有匹配元素
    print("\n=== 3. 查找所有链接 ===")
    all_links = soup.find_all("a")  # 查找所有<a>标签
    print(f"找到 {len(all_links)} 个链接:")
    for i, link in enumerate(all_links[:5], 1):  # 只显示前5个
        href = link.get("href", "无href属性")
        text = link.text.strip() or "无文本内容"
        print(f"{i}. 文本: {text}, URL: {href}")

    # 4. 根据属性查找
    print("\n=== 4. 根据属性查找 ===")
    # 查找带有特定id的元素（example.com可能没有id，这里是示例用法）
    element_with_id = soup.find(id="swagger-ui")
    print(f"ID为'swagger-ui'的元素: {element_with_id if element_with_id else '未找到'}")
    
    # 查找特定class的元素
    elements_with_class = soup.find_all(class_="swagger-ui")
    print(f"class为'swagger-ui'的元素数量: {len(elements_with_class)}")

    # 5. 使用CSS选择器
    print("\n=== 5. 使用CSS选择器 ===")
    paragraphs = soup.select("p")  # 选择所有<p>标签
    print(f"找到 {len(paragraphs)} 个段落:")
    for i, p in enumerate(paragraphs[:3], 1):  # 显示前3个
        print(f"{i}. {p.text.strip()}")

    # 6. 导航树结构
    print("\n=== 6. 导航树结构 ===")
    first_p = soup.find("p")
    if first_p:
        print(f"第一个段落的父元素标签名: {first_p.parent.name}")
        print(f"第一个段落的下一个兄弟元素: {first_p.next_sibling}")
        # 获取子元素
        children = list(first_p.children)
        print(f"第一个段落的子元素数量: {len(children)}")
    else:
        print("未找到段落")

    # 7. 处理文本内容
    print("\n=== 7. 处理文本内容 ===")
    all_text = soup.get_text(separator="\n")  # 获取所有文本，用换行符分隔
    print(f"网页所有文本内容 (前100字符): {all_text[:100]}")

    # 8. 修改HTML内容（示例）
    print("\n=== 8. 修改HTML内容 ===")
    if first_link:
        first_link["href"] = "https://www.python.org"  # 修改第一个链接的href属性
        print(f"修改后的第一个链接: {first_link}")
    
    # 添加延时，避免频繁请求
    time.sleep(1)

# 主程序入口
if __name__ == "__main__":
    print("开始运行 BeautifulSoup 爬虫示例...")
    beautifulsoup_crawler()
    print("爬虫示例运行结束！")
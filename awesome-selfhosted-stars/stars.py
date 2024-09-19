from bs4 import BeautifulSoup
import pandas as pd

#从这个网址“https://awesome-selfhosted.net/”保存网页为“awesome-selfhosted.html”，然后生成表格，以便找出stars最多的项目。

# 读取本地HTML文件
with open('awesome-selfhosted.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 提取项目数据
projects = []
for item in soup.select('section'):
    name = item.find('h3').text if item.find('h3') else 'No Name'
    description = item.find('p').text if item.find('p') else 'No description'
    stars = item.find('span', class_='stars')  # class表示星数
    stars_count = stars.text if stars else '0'
    
    projects.append({
        'Name': name,
        'Description': description,
        'Stars': stars_count
    })

# 创建DataFrame
df = pd.DataFrame(projects)

# 输出为CSV文件
df.to_csv('selfhosted_projects.csv', index=False)

print("表格已保存为 selfhosted_projects.csv")

import json
import pandas as pd
import sys
import os

semester = ''
# 沒有參數
if len(sys.argv) < 2:
    print("No argument.")
    sys.exit()

# 取第一個參數當作學期
semester = sys.argv[1]
print('semester:', semester)

# 課程資料是否存在
if not os.path.exists(f"data/course{semester}.json"):
    print(f"course{semester}.json not found.")
    sys.exit()

# 開啟課程資料
with open(f"data/course{semester}.json", "r", encoding="utf-8") as f:
    data = json.load(f)

dept_set = set()    # 系所
code_set = set()    # 課程代碼

# 課程dataframe
df1 = pd.DataFrame(columns=['id', 'cName', 'cEn_name',
                            'cProfessor', 'cDept', 'cType', 'cCredit', 'cLang'])

i = 0
for course in data["course"]:
    code = course["code"]
    name = course["title_parsed"]["zh_TW"]
    en_name = course["title_parsed"]["en_US"]
    professor = course["professor"]
    dept = course["department"]
    type = course["obligatory"]
    credit = course["credits"]
    lang = course["language"]

    dept_set.add(dept)

    if not code in code_set:    # 課程代碼為主鍵，因此不能重複
        df1.loc[i] = [code, name, en_name,
                      professor, dept, type, credit, lang]
        i += 1
        code_set.add(code)

df1.to_excel(f"data/class{semester}.xlsx", index=False)  # 儲存xlsx檔

# 系所dataframe
df2 = pd.DataFrame(columns=['id', 'dDept'])

df2.loc[0] = [0, "不公開"]
i = 1
for dept in dept_set:
    df2.loc[i] = [i, dept]
    i += 1

df2.to_excel(f"data/dept{semester}.xlsx", index=False)   # 儲存xlsx檔

print("Done!")

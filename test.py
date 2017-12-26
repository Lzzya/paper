import pandas as pd
mypd = pd.DataFrame([range(1,10)])
print mypd

# writer = pd.ExcelWriter("C:\\Users\\liuzhi\\PycharmProjects\\paper\\output.xlsx")


writer2 = pd.ExcelWriter(path="C:\\Users\\liuzhi\\PycharmProjects\\paper\\output.xlsx")
mypd.to_excel(writer2)
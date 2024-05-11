from math import floor
#TODO: finish this class
class SimpleModel():
    def __init__(self, data: list[tuple[int, int]]):
        self.data = data
        self.data.sort(key=lambda x: (x[1], x[0]))
        self.w, self.b = None, None

    def __str__(self):
        return f"簡單模型，w = {round(self.w, 4) if self.w else None}，b = {round(self.b, 4) if self.b else None}，訓練資料共 {len(self.data)} 筆。"
    def fit(self):
        length = len(self.data)
        if (length < 2): 
            print("資料太少啦在幹嘛＞＜")
            return

        d1, d2 = self.data[floor(length * 0.25)], self.data[floor(length * 0.75)]
        if (d1[0] - d2[0] == 0):
            print("資料有問題RRRRR")
            return
        self.w = (d1[1] - d2[1]) / (d1[0] - d2[0])
        self.b = d1[1] - self.w * d1[0]
        print("成功訓練啦~~")

    def predict(self, num):
        if (self.w == None or self.b == None):
            print("模型還沒有擬合RRRRR")
            return

        print(f"{round(self.w * num + self.b, 4)}")

    def extend(self, data):
        self.data.extend(data)
        self.data.sort(key=lambda x: (x[1], x[0]))
        self.fit()


# the class will be used as below
command = []
while True:
    try:
        command.append(input().split())
    except EOFError:
        break
data = [tuple(map(int, i.split(','))) for i in command[0]]
model = SimpleModel(data)
for c in command[1:]:
    if c[0] == 'Fit':
        model.fit()
    if c[0] == 'Predict':
        model.predict(int(c[1]))
    if c[0] == 'Extend':
        model.extend([tuple(map(int, i.split(','))) for i in c[1:]])
    if c[0] == 'Print':
        print(model)



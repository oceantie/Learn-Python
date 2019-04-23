import os
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.join(os.path.dirname(os.path.dirname(__file__)),'images'))
images_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
if not os.path.exists(images_path):
    os.mkdir(images_path)
    print("images文件夹不存在")
else:
    print("存在")
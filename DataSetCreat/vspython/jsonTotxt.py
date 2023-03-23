import os
import json

# 定义函数，用于读取json文件中的points信息
def read_points_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        points = [shape['points'][0] for shape in data['shapes']]

        # 打印结果
        print("first print",points)
    return points

# 定义函数，用于遍历文件夹中的所有json文件，并将其绝对路径和points信息写入txt文件中
def write_json_info_to_txt(folder_path, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.json'):
                    print("unprocessedPath",file)
                    file_path = os.path.join(root, file)
                    filename, ext = os.path.splitext(file_path)
                    points = read_points_from_json(file_path)
                    try:
                       x1, y1 = points[0]
                       
                    except IndexError:
                       x1, y1=  None, None
                    
                    try:
                       x2, y2 = points[1]
                    except IndexError:
                        x2, y2 =  None, None

                    # f.write(file_path + '\t' + str(x1) + '\t' + str(y1) + '\t' + str(x2) + '\t' + str(y2) + '\n')
                    print("second print",points)
                    if ext =='.json':
                       file_path = filename + '.png'
                   
                    
                    sub_path = "/".join(file_path.split("/")[-3:])
                    
                  
                    f.write('../'+sub_path + '\t' + str(x1)+ '\t' +str(y1)+ '\t' + str(x2) + '\t'+str(y2) +'\n')


# 调用函数，将json文件信息写入txt文件中
folder_path = '/Users/lidenghui/vspython/rectangelJson'
relative_path = os.path.relpath(folder_path)

output_file = 'data_center.txt'
write_json_info_to_txt(relative_path, output_file)
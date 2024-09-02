import time

from Crypto.SelfTest.Cipher.test_CFB import file_name

from MODNet_entry import get_model, infer2
from combined import combined

# 抠图模型
model = get_model('modnet_photographic_portrait_matting.ckpt')
# 抠图相关路径
path_before = "C:/HelloWord/photo/camera/"
path_after = "C:/HelloWord/photo/cutout/"
file_name = "2024-08-30-15-06-57.png"
# 背景路径
path_background = "C:/HelloWord/photo/background/"
file_bgname = "2024-09-02 085617.png"
# 结果
path_success = "C:/HelloWord/photo/success/"
# 抠图
infer2(model, path_before + file_name, path_after + "1-" + file_name, path_after + "2-" + file_name)
# 合并
combined(path_after + "2-" + file_name, path_background + file_bgname,
         path_success + str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + ".png")

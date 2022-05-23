![LOGO](https://images.weserv.nl/?url=https://i0.hdslb.com/bfs/article/21ddb2eccb0ec77eef89708e5dbb3d14000872e7.png)

# Birthday Video Maker

---

生日视频生成器

---

⚠️ 当前基本功能已经实现，可供优化的地方太多，正在边学，边做，进程缓慢，见谅，如果项目存在侵权行为，请立即联系删除
⚠️ 请注意，项目中的字体名称和字体 仅做测试使用，不建议使用，如果需要使用，请联系字体作者购买

## 项目描述

根据生日自动生成生日祝福视频

### 使用方法

1. 下载 / 克隆仓库文件到本地

2. 修改配置文件内容【目前还不支持统一配置，我会不断优化的】

3. 创建本地虚拟环境

```shell
# pip install virtualvenv
virtualvenv venv
```

4. 安装 Python 的必要模块

```shell
source ./venv/bin/activate
pip install -r requirements.txt
```



5. 构建视频

```shell
chmod +x *.sh

./build.sh -> 主要用于最后输出
或者
./run.sh -> 主要用于日常预览
```

## TODO

-   [ ] 计算农历生日 

<!-- TODO 项目结构 -->

<!-- TODO 设计图 -->

## 致谢 🙏

- [Manim](https://github.com/ManimCommunity/manim)
- [微软 TTS](https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/#overview)
- 沐瑶软笔手写体、锤子字体

## 更新日志



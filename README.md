# KINETIC — 手势粒子场

一个通过摄像头实时识别手部姿态的 3D 粒子网页。手势识别使用 MediaPipe Hands，全部在浏览器本地完成，画面不会上传。

## 操作

- **张开手掌**：粒子扩散成旋转星云。
- **握紧拳头**：粒子汇聚成粉色、发亮的 3D 爱心。
- **双指比耶**：爱心放大并持续进行 360° 立体旋转，同时跟随两根手指的倾斜方向改变转轴。
- 手的位置会带动粒子场一起移动。
- 右下角显示无文字的实时摄像头预览和手部关键点。
- 未开启摄像头时，页面会自动循环演示粒子聚合与扩散，也可以按住画面模拟握拳。

## 快速开始

只需要 Python 3，用来启动一个本地静态文件服务器。

### macOS / Linux

```bash
cd particle-handscape
python3 serve.py
```

macOS 也可以直接双击 `start.command`。

### Windows

在 PowerShell 或 Windows Terminal 中运行：

```powershell
cd particle-handscape
py serve.py
```

如果 `py` 不可用，改用 `python serve.py`。也可以双击 `start.bat`。

启动后访问终端显示的地址，默认是：

```text
http://127.0.0.1:8787/
```

如果 8787 端口被占用，`serve.py` 会自动尝试 8788–8798。

> 摄像头需要安全上下文，请通过 `http://127.0.0.1` 或 HTTPS 打开页面，不要直接双击 `index.html`。

## 使用摄像头

页面打开后会自动播放演示。点击右下角的摄像头图标，浏览器询问时允许摄像头，即可用手势控制粒子。再次点击图标会关闭摄像头并回到自动演示。

## 项目结构

```text
.
├── index.html      # 页面、样式和粒子/手势逻辑
├── serve.py        # 本地静态文件服务器
├── start.command   # macOS 启动脚本
├── start.bat       # Windows 启动脚本
└── vendor/         # MediaPipe Hands 模型与 WASM 资源
```

## 隐私

摄像头画面只在浏览器本地由 MediaPipe 处理，不会上传到任何服务器。

## 第三方资源

`vendor/` 中的 MediaPipe Hands 资源来自 [MediaPipe](https://github.com/google-ai-edge/mediapipe)，遵循 Apache-2.0 许可证。

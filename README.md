校园流浪猫信息共享与管理平台 (Campus Cat Platform)

1. 项目简介本项目是一个基于 GIS 地图与数字化档案的校园生态管理平台，旨在通过师生互动打卡、AI 识别与空间分析，实现校园流浪猫的科学监测与救助管理 。
2. 技术栈后端 (Backend): Python 3.x + Flask (轻量级 Web 框架)数据库 (Database): SQLite 3 (本地文件型数据库，无需配置服务)前端 (Frontend): HTML5 + Tailwind CSS (UI 框架) + Iconify (图标库)可视化与地图: 高德地图 JS API 2.0 (GIS 底图) + ECharts (数据看板趋势图)
3. 核心功能GIS 底图集成： 展示校园 2D/卫星底图，支持猫咪出没点位标注与档案联动查看 。数字化档案： 记录猫咪 ID、性别、毛色、性格标签（如“亲人”、“社恐”）及绝育状态 。偶遇与投喂打卡： 支持调用手机 GPS 和摄像头进行位置上报，并预留 AI 识别接口自动关联档案 。用户与权限管理： 分为普通用户（查看、打卡、上报）与管理员（审核内容、维护档案、管理权限） 。故事墙与数据看板： 师生互动轶事分享，以及校园猫咪活跃趋势和投喂频次统计分析 。
4. 启动步骤
    4.1 数据库配置说明本项目使用 SQLite 数据库，无需安装额外的数据库软件。激活虚拟环境：Windows: venv\Scripts\activatemacOS/Linux: source venv/bin/activate导入/初始化 SQL：
运行项目根目录下的初始化脚本，它将自动创建 campus_cats.db 文件并生成所需的表结构（含主键、外键及索引设计） 。Bashpython init_db.py
    4.2 后端运行命令安装依赖：Bashpip install flask
启动 Flask 服务：Bashpython app.py
    4.3 前端运行说明本项目采用前后端不分离模式，前端页面由 Flask 模板引擎渲染。访问地址： 在浏览器打开 http://127.0.0.1:5000 即可进入系统首页。
5. 接口入口API 基础路径： http://127.0.0.1:5000/api/v1核心接口说明：GET /api/cats : 获取所有猫咪档案列表。POST /api/checkins : 提交新的打卡记录（需包含位置坐标与照片）。GET /api/stats/trend : 获取近 24 小时活跃趋势数据（供看板调用）。
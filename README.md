# Sales Lead Agent

一个AI驱动的销售线索管理平台，帮助销售人员更有效地跟踪潜在客户、生成销售话术并跟进销售机会。

## 功能特性

- 1:1 复刻首页，包含数据卡片、快捷按钮和底部对话窗口
- 点击卡片跳转到【标讯列表页】和【客户列表页】二级页面
- 点击数据自动在对话窗口生成销售跟进话术
- AI驱动的销售建议和客户分析

## 技术栈

- 前端: Vue 3 + TypeScript + Vue Router
- 后端: Python Flask
- AI逻辑: Python销售代理模块

## 项目结构

```
├── src/                    # 前端源码目录
│   ├── assets/             # 静态资源
│   ├── components/         # Vue组件
│   ├── views/              # 页面视图
│   ├── router/             # 路由配置
│   └── main.ts             # 入口文件
├── skill/                  # AI技能模块
│   ├── SKILL.md            # 技能文档
│   └── sales_agent.py      # 销售代理核心逻辑
├── server.py               # Python后端服务器
├── requirements.txt        # Python依赖
├── package.json            # 前端依赖
├── vite.config.ts          # 构建配置
└── README.md               # 项目说明
```

## 安装和运行

### 前提条件

- Node.js (>=16.x)
- Python (>=3.8)

### 安装步骤

1. 克隆项目

```bash
git clone <your-repo-url>
cd sales-lead-agent
```

2. 安装前端依赖

```bash
npm install
```

3. 安装后端依赖

```bash
pip install -r requirements.txt
```

### 运行项目

1. 启动后端服务器

```bash
python server.py
```

2. 在另一个终端启动前端开发服务器

```bash
npm run dev
```

3. 访问 http://localhost:3000 查看应用

## 部署

### 构建生产版本

```bash
npm run build
```

## API 接口

- `POST /api/generate-talk`: 生成销售话术
- `POST /api/analyze-needs`: 分析客户需求
- `POST /api/suggest-action`: 建议下一步行动
- `GET /health`: 健康检查

## 开发指南

此项目遵循以下开发原则：

- 使用TypeScript确保代码质量和可维护性
- 组件化开发，便于复用和测试
- API调用统一处理错误情况
- 响应式设计适配不同屏幕尺寸

## 许可证

MIT
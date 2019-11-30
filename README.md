# Vue Flask Template

📦 一个快速搭建 Web 应用的模版！前端使用渐进式框架 [Vue](https://github.com/vuejs/vue)，后端使用微框架 [Flask](https://github.com/pallets/flask)。

## 使用方法

1. 点击本项目右上角的绿色按钮 `Use this template`（使用此模板），输入名称和说明，完成创建。

2. 将刚刚创建好的项目克隆到本地，这里以本项目为例，实际操作时这里需要替换你自己的项目。

    ```bash
    git clone https://github.com/Ailln/vue-flask-template.git --depth 1
    ```

3. 安装环境依赖，本项目需要 Node 环境 和 Python 环境，如果对这部分不熟悉的看本文档最后的参考文章。

    ```bash
    # 前端环境依赖安装
    cd front
    yarn
    
    # 后端环境依赖安装
    cd back
    pip install -r requirements.txt
    ```

4. 打开两个终端，分别启动前端和后端。

    ```bash
    # 启动前端
    cd front
    yarn serve
    
    # 启动后端
    cd back
    python app.py
    ```

5. 在浏览器中打开：`http://localhost:8080/` 即可预览。

6. 根据你的需求修改代码。

## 项目结构

```
.
├── README.md
├── LICENSE # 许可证
├── .gitignore
├── front # 前端
│   ├── README.md
│   ├── babel.config.js
│   ├── package.json # 前端依赖
│   ├── public
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src
│   │   ├── App.vue
│   │   ├── assets # 静态资源
│   │   │   └── logo.png
│   │   └── main.js
│   └── yarn.lock
└── back # 后端
    ├── app.py
    └── requirements.txt # 后端依赖
```

## 附加

### 添加 View UI

1. 添加库

    ```bash
    cd front
    yarn add view-design
    ```

2. 在 `/front/src/main.js` 中的 `new Vue()` 之前添加

    ```javascript
    import ViewUI from 'view-design'
    import 'view-design/dist/styles/iview.css'

    Vue.use(ViewUI)
    ```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 参考

- [vue document](https://cn.vuejs.org/v2/guide/)
- [vue-cli guide](https://cli.vuejs.org/zh/guide/)
- [View UI](https://www.iviewui.com/)
- [flask document](https://dormousehole.readthedocs.io/en/latest/)
- [如何安装 Node 开发环境？](https://v2ai.cn/linux/2018/11/11/LX-10.html)
- [如何安装 Python 开发环境？](https://v2ai.cn/linux/2018/04/29/LX-2.html)

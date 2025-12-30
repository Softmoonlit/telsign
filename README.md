# Telegram Auto Sign-in

自动签到 Telegram 机器人，使用 GitHub Actions 定时执行。

## 功能

每天定时向指定的 Telegram 频道发送签到消息。

## 配置说明

### 1. 设置 GitHub Secrets

在仓库的 Settings → Secrets and variables → Actions 中添加以下 secrets：

- `API_ID`: Telegram API ID
- `API_HASH`: Telegram API Hash
- `SESSION_STR`: Telegram Session String

### 2. 定时任务

工作流配置在 `.github/workflows/run_bot.yml`，当前设置为：
- Cron 时间: `17 2 * * *` (UTC时间每天 02:17)
- 对应北京时间: 每天上午 10:17 (UTC+8，中国不使用夏令时)

## 常见问题

### 为什么定时任务没有触发？

GitHub Actions 的 scheduled workflows 可能因为以下原因不触发：

1. **新仓库延迟**: 新添加的定时任务可能需要 24 小时后才会开始工作
2. **仓库不活跃**: 如果仓库 60 天内没有提交，scheduled workflows 会被自动禁用
3. **权限问题**: 确保 Actions 在仓库设置中已启用
4. **首次运行**: 第一次设置后，建议手动运行一次 workflow 来激活

### 解决方案

本仓库已配置了以下措施来确保定时任务正常运行：

1. ✅ 添加了 `push` 触发器，保持仓库活跃
2. ✅ 明确指定了 `permissions` 配置
3. ✅ 支持手动触发 (workflow_dispatch)

### 手动运行

如果需要手动运行签到：
1. 进入仓库的 Actions 页面
2. 选择 "Telegram Auto Sign-in" workflow
3. 点击 "Run workflow" 按钮

## 验证定时任务

可以通过以下方式验证定时任务是否正常工作：

1. 检查 Actions 页面的运行历史
2. 查看是否有 `schedule` 类型的运行记录
3. 如果只有 `workflow_dispatch` 类型，说明都是手动触发的

## 注意事项

- 确保 Session String 有效且未过期
- GitHub Actions 的 scheduled workflows 有 5-10 分钟的延迟是正常的
- 如果长时间不工作，可以提交一个小的代码更改来保持仓库活跃

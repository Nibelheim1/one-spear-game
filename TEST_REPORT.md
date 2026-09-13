# v1.5.0 全屏单按钮 / 距离选台验证

- 内嵌 JavaScript 已通过 `node --check`。根目录 `index.html` 与 `one-spear-play.html` 保持字节一致。
- 核心状态机直接复跑固定教学：三次成功落地依次到 step 1/2/3，累计计分 1→3→7。
- 教学三个典型时长按当前线性映射约为 **0.39s / 0.75s / 1.10s**，分别对应近单人、中双人、远回血。
- 正式局面同样按住 0.64s（约 50% power），分别从画面左上、中央、右下开始按压，得到完全相同的力度与自动目标，证明触摸坐标不参与路线选择。
- 正式阶段直接越过第一台命中第二台：在前三跳 combo 未断的情况下，本跳结算 `+8 + 越台32`，总分从 7 到 47。
- 使用明显过长的 100% 蓄力攻击只有近/中台的局面，结果为投空→坠崖→HP 0，证明自动选台不会把明显错误射程强行救回。
- 线性射程采样：power 0 / .25 / .5 / .75 / 1 对应 120 / 312.5 / 505 / 697.5 / 890 px，20 段单调性检查全部通过。
- 世界生成检查：**320 Seeds × 4 阶段 = 1280 组**；按距离排序的平台理想力度始终严格递增，最小相邻力度间隔约 0.250；新生成近台理想力度约 0.284～0.321，最远台最高约 0.892。
- 本沙箱 Chromium 直接导航本地 URL 仍被 `ERR_BLOCKED_BY_ADMINISTRATOR` 拒绝；随后使用 Playwright `set_content` 注入**同一交付 HTML**完成真实 Canvas/PointerEvent 复跑。第三跳后从画面左上、中央、右下三个位置分别真实按住约 640ms，读取到的 power 均约 **0.508**，自动目标均为同一第 2 平台；页面脚本异常 0。
- 浏览器实际截图 `docs/one-button-clean.png` 确认第三跳完成后不再显示蓄力条、目标准星或选中平台高亮，只保留正常 HUD 与“教学完成”提示。该测试仍不是实体 iPhone/Android 真机认证。

> 下文历史版本中“轻拖切换目标”的通过记录仅描述旧版测试，不再代表 v1.5.0 的当前操作。

# v1.4.1 最近敌人射击 / 2 秒首箭验证

- Chromium 844×390，使用与交付页相同的单文件脚本，通过 `set_content` 运行；测试注入仅用于暴露运行状态，不改玩法逻辑。
- 双人台初始两个敌人的首次攻击计时均为 **2.00s**。运行约 0.9s 后：最近敌人剩余约 **1.13s**，更远敌人仍保持 **2.00s**，证明远端计时被冻结。
- 最近敌人第一次出手发生在 `elapsed ≈ 2.0167s`（一帧误差），此时更远敌人仍为 `firstAttack=true, timer=2.00s`。
- 强制击杀当前最近敌人后，下一敌人接管 `activeShooterId`，并从完整 **2.00s** 首次攻击窗口开始倒计时。
- 页面脚本异常：0。
- `index.html` 与 `one-spear-play.html` 已分别通过 `node --check` 的内嵌脚本语法检查。

# v1.3.2 首次攻击 1.5 秒验证

- Chromium 1280×720 实际运行，`?debug=1&seed=123&autostart=1`。
- 教学第一跳弓手初始首次攻击计时为 **1.50s**；浏览器采样时游戏已经运行约 0.067s，因此读取到剩余约 1.433s。
- 第一次出手时游戏 `elapsed ≈ 1.5001s`，证明原有 1.1s 开局保护没有额外叠加到首次攻击等待时间。
- 第一次出手后 `firstAttack=false`，计时恢复为该弓手原后续周期 **2.90s**。
- 本轮页面脚本异常：0。

# v1.3.1 HUD / attack interval verification addendum

- 浏览器实际启动无页面脚本异常。
- 教学第一跳弓手运行时 timer/period 实测约 **2.9s**，对应 v1.3 同逻辑约 5.8s 的 50%。
- 常规敌人最终生成周期统一应用 `enemyAttackIntervalScale = 0.50`。
- 残敌 `meleeInterval` 检查为 **0.17s**。
- 总分 HUD 已通过 1280×720 Chromium 截图检查：独立面板、“总分”标签、52px 金色主数字均正常显示。

# v1.3 scoring verification addendum

本版新增验证：连跳分严格为 1/2/4/8/16/32 并封顶；敌人完成攻击会打断连跳；越过最近台直达第二平台额外 +32；击杀/爆头/多杀不再直接增加竞技分；旧版分数记录与新计分隔离。

# 测试报告与交付边界

## 结论

**共享 TypeScript 玩法的离线 Canvas 交付版已编译并实际运行。标准 Phaser 3 / Vite 开发入口的依赖安装、严格构建及浏览器运行验证尚未完成。不能把本次交付说成原始验收表的全部项目均已通过。**

离线版不是录像、概念图或伪代码：v1.2 使用实际鼠标/触屏事件重跑了固定三跳教学、穿透、回血、第三跳后撤掉力度 UI、正常路线换路、可见平台持久化、投空坠崖、残敌近战、暂停、死亡、续命及重开。自动化测试不等于真实新手评估，也不能证明留存率或主观“上瘾”。

## 环境与方法

- Node.js 22.16.0、npm 10.9.2；本轮实际离线编译器为全局 TypeScript 5.8.3。package.json 为正常联网开发固定声明 TypeScript 5.9.2，二者不混称为同一已测版本。
- Chromium 144.0.7559.96，Debian Linux，Python Playwright，桌面 1280×720；模拟移动视口 844×390、DPR 2、触屏事件。没有真实手机。
- npm 安装实际失败，错误为 npm 源域名解析/连接不可用；原始输出见 `docs/dependency-install.log`。没有假造 package-lock 或替代 Phaser 包。
- 当前浏览器策略拒绝直接导航 localhost 和 file URL，错误为 `ERR_BLOCKED_BY_ADMINISTRATOR`。因此将生成的完整单文件 HTML 用 Playwright `set_content` 载入，仍运行同一实际脚本、Canvas 渲染和输入处理。
- 测试在内存中的入口给构造函数添加 `?debug=1&seed=…`，以读取状态；默认交付页未开启调试。十分钟脚本没有加速游戏时钟、无敌、锁血或后台直接改分。
- 部分短流程测试为节省时间预设低 HP、难度阶段或显示局面；随后使用真实输入/实际敌箭完成检查。自动化中的直接状态设置不作为正常玩家操作能力。

## 编译与启动

| 项目 | 实际结果 | 边界 |
|---|---|---|
| `npm install` | 未通过：外部依赖不可下载 | 已保留错误日志，不以离线版替代这一验收项 |
| `npm run build` | 通过，明确进入离线 fallback | 真实 TypeScript 编译 + 本地模块封装，不是 Vite 构建 |
| `npm run build:offline` | 通过 | 输出 dist 和完整内嵌 HTML |
| `npm run dev` | 无依赖静态服务分支已启动，HTTP 可响应 | 不宣称 Vite/HMR；浏览器直接导航受环境策略阻止 |
| `npm run build:vite` / Phaser 场景运行 | 未验证 | 需要安装真实依赖后检查，不把源码存在当作运行通过 |
| 单文件脚本运行及画面 | 通过页面注入检查 | 原始 file URL 与普通站点导航未在本沙箱验证 |
| `npm test` | 通过 | 下面列出的有限核心检查，不是全覆盖 |

本包同时附带 `.offline-build/` 的预编译模块供当前 `npm test` 使用。修改源码后应先 `npm run build:offline` 再测试；不要拿旧编译产物检验新源码。

## 核心逻辑检查

`tests/core.cjs` 检查 20 个基础局面定义，以及 **64 Seeds × 5 个时间阶段 = 320 组生成结果**。检查 2–3 路线、相同输入可复现、近路敌种约束、可达范围、敌人数量上限；这是受测输入范围的保证，不是所有状态的数学证明。

另外实际检查固定教程序列（单人→双人→回血）、首投头部命中、明显欠蓄投空、重甲身体需补刀/头部可击破、闭盾挡枪、同一弹道的双杀与三杀、`powerAt` 的单调线性关系、`rangeForPower` 等距增量，以及“已显示前方平台在落地合并后保持同一对象”。日志为 `docs/core-test.log`。

## 浏览器操作流程

原始结果：`docs/smoke-results.json`；复跑脚本：`tests/browser_smoke.py`。

| 检查 | 结果 |
|---|---|
| 第 1 跳固定单人台并显示力度教学 | 通过 |
| 第 1 跳成功后，第 2 跳固定双人穿透台 | 通过 |
| 双人台一矛清场 → 第 3 跳固定回血台 | 通过 |
| 第 3 跳前手动降至 50 HP，落地后恢复到 82 HP | 通过 |
| 第 3 次成功落地后进入正常路线，运行截图不再出现下方力度条 | 通过；见 `docs/post-tutorial.png` |
| 已看到的前方平台：落近台前后 ID / kind / 敌种数组保持一致 | 通过 |
| 正常路线中真实轻拖仍能切换候选目标 | 通过 |
| 明显弱投 → 进入 falling → 坠崖死亡 | 通过 |
| 双人台只杀 1 人仍飞跃，残敌落地连续近战扣血 | 通过 |
| 暂停取消蓄力、冻结计时、恢复可投 | 通过 |
| pointercancel 不造成幽灵投枪 | 通过 |
| 切竖屏出现提示并冻结计时 | 通过 |
| 可见预警敌人实际放箭扣血并导致死亡结算 | 通过 |
| 明确标注的 Mock 续命恢复 36 HP，每局仅一次 | 通过 |
| 结算后重新进入 ready | 本环境记录约 15.0 ms；不代表任意手机显示延迟 |
| 模拟移动触屏按住 + 松手 + 首跳飞渡 | 通过；不等于真实移动浏览器兼容验证 |
| 本轮页面脚本异常 | 0 |

## 十分钟连续运行（1.0 基线记录）

基线原始结果：`docs/soak-results-v1.0-baseline.json`；复跑脚本：`tests/browser_soak.py`。

**这组 605.033 秒（10 分 5 秒）的长测来自 1.0 规则基线，发生在“投空收枪”改成“投空坠崖”之前。** 它仍可证明当时共享渲染/生成系统没有明显持续恶化，但不能冒充 v1.2 新生成/教学规则后的十分钟重测。本次 v1.2 重跑的是核心规则与浏览器 smoke。

| 指标 | 实测 |
|---|---:|
| 本轮场次 | 1 |
| 输入投矛次数 | 312 |
| 成功推进平台 | 308 |
| 击破数 / 精准数 | 392 / 391 |
| 失误次数 | 4 |
| 多杀事件次数 | 104；计数器名称 double，同时覆盖三杀事件 |
| 页面对外报出的脚本异常 / 自动化超时记录 | 0 / 0 |
| 独立 rAF 记录帧数 | 35379 |
| 全程平均 rAF 频率 | 58.46 FPS |
| 大于 25 ms 的帧间隔 | 456 帧，约 1.29% |
| 抽样 JS 已用堆 | 1.53–2.79 MiB |
| 抽样 DOM Nodes | 45–59 |
| 活跃路线 / 历史平台 | 稳定为最多 3 / 5 |
| 特效系统记录的最高活跃粒子 | 93，配置上限 150 |

首次约 60 秒的平滑 FPS 抽样曾降至 **43.51**；其后 120–549 秒的采样约为 **59.73–60.01**。不能只挑 60 FPS 的点声称全程绝对稳定。堆占用有回落和波动，未呈现本次样本中持续单调上升；这并非严格的无泄漏证明，也不是对真实中低端手机 60 FPS 的承诺。

本轮实际出现了全部 20 个基础 pattern ID，外加 `boss`。脚本使用读取精准窗口的熟练策略，最终 HP 为 100；这说明该策略可以持续执行，**不说明真人可以如此精准，也不构成适中难度或五分钟留存的证明**。受伤、回血和死亡在独立短流程中实际验证，不由这一无伤长局代替。

## 画面检查与实际修复

本轮继续保留 v1.1 的 `docs/charging.png`（无轨迹引导线）、`docs/falling.png`（投空坠崖）与 `docs/melee.png`（残敌近战）；v1.2 新增 `docs/tutorial-1.png`、`docs/tutorial-2.png` 和 `docs/post-tutorial.png`，其中最后一张用于确认第三次成功落地后正常游戏画面没有力度条。具体修改见 `TUNING.md` 和 `CHANGELOG.md`。

历史版本已修复穿透对齐、风险得分倍率、模态 UI 点击穿透、数字 Seed 和粒子重力等问题。v1.2 新修复两项核心行为：满蓄力回弹导致的手感非单值映射，以及落地后整组候选重生成导致的“视野信息变化”。

## 尚未验证 / 未接入

1. 标准 Phaser / Vite 入口的实际安装、严格编译与运行——这是原需求技术栈的一项未完成验收，不是被删除的要求。
2. 实体 Android、iPhone / Safari、微信内置浏览器的触摸、旋转、声音及性能；手机真实震动。
3. 普通 HTTP(S) origin 的 localStorage 跨刷新持久化。本轮页面注入 origin 不允许存储；内存存储单元测试和禁用回退通过，不冒充真实持久化测试。
4. 原生设备音量、音色、延迟、触觉强度与真实新手的可读性、挑战感、疲劳感。
5. 真实广告 SDK 与有效激励回调。当前只有明确标识的演示续命，未播放真实广告，未接入支付或服务器。
6. 网络部署、平台发行、广告审核、权利合规审核均未执行。

## 有限复跑

先执行 `npm run build:offline` 与 `npm test`。浏览器复跑需要本机 Python Playwright 和 Chromium；通过环境变量 `CHROMIUM` 指定可执行文件路径，再运行：

```bash
python tests/browser_smoke.py
python tests/browser_soak.py
```

十分钟脚本需要实际等待约十分钟。测试输出会覆盖 docs 中同名结果和截图；保留这份报告可以对照本次已交付记录。不要求进行额外哈希、安全扫描或无限覆盖率扩张。


## v1.4.0 viewport checks
Target viewport classes: 640×360, 667×375, 736×414, 800×360, 844×390, 852×393, 915×412, 932×430, and 1024×768 portrait/landscape behavior. The 1280×720 logical playfield remains aspect-preserving and touch mapping is based on the rendered canvas rect.

### Mobile viewport verification details

A deterministic geometry check (`scripts/test_mobile_viewports.py`) verifies the fixed 16:9 gameplay core stays inside the usable safe area at all target sizes. Representative iPhone landscape cases include simulated 47 px and 59 px left/right safe areas. The smallest 640×360 case yields an effective button hit height of about 44 CSS px after touch slop. JavaScript syntax checks for both inline scripts pass with `node --check`, and `index.html` is byte-identical to the standalone playable build.

The container's headless Chromium process did not terminate reliably in this environment, so this release does **not** claim physical-device or automated screenshot-browser certification. Real iOS/Android device QA remains recommended before store/public launch.

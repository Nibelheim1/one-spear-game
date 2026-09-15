# v1.6.0 图片素材映射

## 运行时关键素材

### 背景
- `assets/background/arena_bg.png`：1280×720 竞技场底图。

### 主角
- `assets/hero/idle.png`
- `assets/hero/charge.png`
- `assets/hero/throw.png`
- `assets/hero/pull.png`
- `assets/hero/land.png`
- `assets/hero/hurt.png`
- `assets/hero/fall.png`
- `assets/hero/victory.png`
- `assets/hero/portrait_serious.png`
- `assets/hero/portrait_smile.png`

### 敌人
- `assets/enemies/melee_idle.png`
- `assets/enemies/melee_attack.png`
- `assets/enemies/shield_idle.png`
- `assets/enemies/shield_defend.png`
- `assets/enemies/ranged_aim.png`
- `assets/enemies/ranged_shoot.png`
- `assets/enemies/icon_question.png`
- `assets/enemies/icon_alert.png`
- `assets/enemies/icon_target.png`

### 平台
- `assets/platforms/start.png`
- `assets/platforms/round_blue.png`
- `assets/platforms/rect_cyan.png`
- `assets/platforms/tall_pink.png`
- `assets/platforms/heal_green.png`
- `assets/platforms/wide_purple.png`
- `assets/platforms/danger_red.png`
- `assets/platforms/crown_gold.png`

### UI
- `assets/ui/logo.png`
- `assets/ui/heart.png`
- `assets/ui/crown.png`

### 道具
- `assets/decor/health_bottle.png`
- `assets/decor/anchor.png`

## 扩展素材

`assets/decor/`、`assets/effects/`、`assets/background/` 中还保留了应援牌、LED、横幅、飞艇、VFX 等拆分资源，可用于后续活动皮肤、场景轮换和更重的特效升级。它们未全部放进当前主循环，避免首屏下载和视觉噪音过大。

## v1.8 敌兵朝向
运行中的六种小兵素材统一朝左。`shield_idle.png`、`ranged_aim.png`、`ranged_shoot.png` 使用原图水平镜像修复；其余动作保持原素材。

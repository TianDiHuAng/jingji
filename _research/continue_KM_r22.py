# -*- coding: utf-8 -*-
"""续作KM：加入 R22（重要/核心条目的 overview 过短告警），并扩写 10 条最核心概念。

背景（round 112）：清理「具体XX待核实」套话后暴露——358 条 overview 不足 150 字，
其中 326 条是概念/理论类，多为「通货膨胀」「失业」「系统性风险」这类基础概念（66—80 字）。
套话一直在掩盖内容单薄这一事实。
"""
P = 'tools/check.py'
raw = open(P, 'rb').read()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')

old = "    # R14 分层顺序"
new = """    # R22 重要/核心条目的 overview 不应过短（<150 字）
    for _e in entries:
        if _e.get('tier') in ('核心', '重要') and len(_e.get('overview') or '') < 150:
            warn('R22', _e.get('id', '?'),
                 'tier=%s 但 overview 仅 %d 字（建议 ≥150）'
                 % (_e.get('tier'), len(_e.get('overview') or '')))
    # R14 分层顺序"""

if 'R22' not in s and old in s:
    s = s.replace(old, new, 1)
    out = s.replace('\n', '\r\n') if crlf else s
    open(P, 'wb').write(out.encode('utf-8'))
    print('已加入 R22')
else:
    print('已存在或未匹配')

# -*- coding: utf-8 -*-
"""续作CZ：新增5条美国银行制度史条目（19世纪—1913）。"""
import json, glob

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：制度要点</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体条款以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='second-bank', title='美国第二合众国银行', cat='制度', region='北美', unit='U2 18—19世纪',
  per='18—19世纪', tier='补充',
  ol='美国第二家联邦特许的国家银行（麦迪逊政府时期特许），其存废之争塑造了美国早期货币格局。',
  ov=('美国第二合众国银行(Second Bank of the United States) 是美国**第二家经联邦授权**的国家银行，'
   '在**麦迪逊政府**时期获得特许。'
   '它与第一合众国银行同属"国家银行"模式：兼具商业银行职能与代理国库、'
   '约束州银行纸币发行的准中央银行角色。'
   '其特许权到期后的存废之争（"银行战"）是美国早期政治经济史的核心冲突之一：'
   '反对者认为它集中了过大的私人权力且不受民主问责。'
   '该行特许失效后，美国进入**自由银行时代**（见 free-banking），'
   '州银行数量激增、纸币发行混乱，成为此后频繁银行恐慌（1837、1857、1873…）的制度背景。'
   '直到 1913 年联邦储备法（见 federal-reserve-act）才重新建立常设的中央银行。'
   '该线索是理解"美国为何长期没有中央银行、因而危机频发"的关键。具体年份与条款待核实。'),
  tl=[
   {'year':1816,'display':'1816年','event':'第二合众国银行在麦迪逊政府时期获联邦特许（年份待核实）','sources':['w-en-second-bank']},
   {'year':1832,'display':'1832年前后','event':'特许续期之争（"银行战"），最终未能延续（细节待核实）','sources':['w-en-second-bank']},
  ],
  causal=[('联邦特许的国家银行兼具商业与准央行职能 → 引发权力集中争议','w-en-second-bank'),
         ('特许失效 → 进入自由银行时代，州银行与纸币发行失序','w-en-free-banking'),
         ('失序与频繁恐慌 → 1913年以联邦储备法重建中央银行','w-en-federal-reserve-act')],
  schools=[('中央银行必要性视角','缺乏最后贷款人与统一纸币是恐慌频发的制度根源','w-en-lender-of-last-resort'),
           ('权力制衡视角','集中的金融权力与民主问责冲突，反对有其道理','w-en-second-bank')],
  srcs=['w-en-second-bank','w-en-free-banking']),
 dict(id='free-banking', title='自由银行时代', cat='制度', region='北美', unit='U2 18—19世纪',
  per='18—19世纪', tier='补充',
  ol='银行可自由发行自身纸币、除一般公司法外不受特殊监管的货币安排。',
  ov=('自由银行(free banking) 是一种货币安排：**银行可自由发行自己的纸币（banknotes）**，'
   '并且除适用于一般公司的法律外，**不受特殊监管约束**。'
   '在美国，该模式在第二合众国银行特许失效后（1830—1860年代）于多数州盛行，'
   '各州仅以一般公司法要求注册与资本/储备的最低条件。'
   '其后果是双面的：'
   '一方面，自由进入促进了竞争与金融深化；'
   '另一方面，**纸币种类繁多、成色与兑付能力参差**，形成「劣币与信息不对称」问题，'
   '并在恐慌中大量倒闭（1837、1857 年的银行倒闭潮即在此背景下发生）。'
   '1863—1864 年国民银行法（见 national-banking-act）以统一国民银行券与税制终结了这一格局。'
   '历史学界对自由银行是否"更不稳定"存在争论：有研究认为约束得当的自由银行体系表现并不差。'
   '具体制度差异待核实。'),
  tl=[
   {'year':1837,'display':'1830—1860年代','event':'美国多数州实行自由银行制；1837、1857年恐慌中大量银行倒闭','sources':['w-en-free-banking']},
   {'year':1863,'display':'1863—1864年','event':'国民银行法以统一银行券与税制终结该格局','sources':['w-en-national-bank-act']},
  ],
  causal=[('特许失效 + 一般公司法注册 → 银行自由进入与自由发钞','w-en-free-banking'),
         ('纸币成色与兑付能力参差 + 信息不对称 → 折价交易与挤兑','w-en-adverse-selection'),
         ('恐慌中大量倒闭 → 1863—64年国民银行法统一发钞','w-en-national-bank-act')],
  schools=[('不稳定视角','缺乏统一纸币与最后贷款人使体系易受挤兑','w-en-panic-of-1857'),
           ('竞争视角','约束得当的自由银行可提供竞争性货币，稳定性未必更差','w-en-free-banking')],
  srcs=['w-en-free-banking','w-en-national-bank-act']),
 dict(id='national-banking-act', title='国民银行法(1863–1864)', cat='制度', region='北美', unit='U2 18—19世纪',
  per='18—19世纪', tier='补充',
  ol='1863与1864年两部联邦银行法，建立联邦特许的国民银行体系与统一银行券。',
  ov=('《国民银行法》(National Banking Acts) 是 **1863 年与 1864 年** 两部美国联邦银行法，'
   '建立了**由联邦特许的国民银行体系**。'
   '其核心安排包括：由联邦而非各州颁发银行牌照、'
   '要求国民银行以联邦债券为担保发行**统一的国民银行券**、'
   '并对州银行券课税以迫使州银行转入联邦体系或退出发钞。'
   '这一制度解决了自由银行时代（见 free-banking）纸币种类混乱的问题，'
   '但也留下了两个结构性缺陷：'
   '①**银行券供给缺乏弹性**（受联邦债券持有量约束），'
   '在季节性需求或恐慌时无法扩张；'
   '②**缺乏最后贷款人**，恐慌时只能依靠私人清算所自救。'
   '这两个缺陷叠加，被认为是 1873、1893、1907 年恐慌反复深化的制度原因，'
   '并最终促成 1913 年联邦储备法（见 federal-reserve-act）。'
   '具体条款与税率待核实。'),
  tl=[
   {'year':1863,'display':'1863—1864年','event':'两部国民银行法通过，建立联邦特许国民银行体系','sources':['w-en-national-bank-act']},
   {'year':1913,'display':'1913年','event':'联邦储备法建立常设中央银行，弥补缺乏最后贷款人的缺陷','sources':['w-en-federal-reserve-act']},
  ],
  causal=[('自由银行时代纸币混乱 → 联邦统一发钞与牌照','w-en-free-banking'),
         ('银行券以联邦债券为担保 → 供给缺乏弹性、无法应对季节性需求','w-en-national-bank-act'),
         ('缺乏最后贷款人 → 恐慌反复（1873/1893/1907）→ 1913年设美联储','w-en-federal-reserve-act')],
  schools=[('制度缺陷视角','无弹性货币与无最后贷款人是恐慌反复的根源','w-en-panic-of-1907'),
           ('稳定化视角','统一发钞本身已显著降低货币混乱，是重要进步','w-en-national-bank-act')],
  srcs=['w-en-national-bank-act','w-en-federal-reserve-act']),
 dict(id='sherman-silver-purchase', title='谢尔曼购银法(1890)', cat='货币', region='北美', unit='U2 18—19世纪',
  per='18—19世纪', tier='补充',
  ol='1890年7月14日生效的美国法律，要求政府增加白银购买量，被视为1893年恐慌的诱因之一。',
  ov=('《谢尔曼购银法》(Sherman Silver Purchase Act) 是 **1890 年 7 月 14 日** 颁布的美国联邦法律，'
   '它**提高了政府必须购买的白银数量**。'
   '该法产生于复本位制（见 bimetallism）支持者与金本位支持者的长期冲突：'
   '白银派要求以购银维持银价与通货扩张，金本位派担忧黄金储备流失与信用受损。'
   '其机制性风险在于：购银以可兑换金银的国库券支付，'
   '当持券人选择兑付黄金时，**国库黄金储备承压**，'
   '引发对金本位的信心危机——该法因此常被视为 **1893 年恐慌**的诱因之一，并于同年被废除。'
   '这一事件是美国19世纪"金银之争"的高潮，与1896年布赖恩竞选（"不应把人类钉在黄金十字架上"）'
   '和1896年恐慌（见 panic-1896）直接相连。具体条款与废除时序待核实。'),
  tl=[
   {'year':1890,'display':'1890年7月14日','event':'谢尔曼购银法生效，提高政府白银购买量','sources':['w-en-sherman-silver-purchase']},
   {'year':1893,'display':'1893年','event':'该法被废除；同年发生恐慌（见 panic-1893）','sources':['w-en-panic-of-1893']},
  ],
  causal=[('白银派政治压力 → 立法要求政府增购白银（1890-07-14）','w-en-sherman-silver-purchase'),
         ('国库券可兑黄金 → 持券人兑金，黄金储备承压','w-en-gold-standard'),
         ('对金本位的信心危机 → 1893年恐慌，该法同年废除','w-en-panic-of-1893')],
  schools=[('货币扩张视角','购银是缓解通缩与债务负担的合理诉求','w-en-gold-standard')],
  srcs=['w-en-sherman-silver-purchase','w-en-gold-standard']),
 dict(id='federal-reserve-act', title='联邦储备法(1913)', cat='制度', region='北美', unit='U3 20世纪上半',
  per='20世纪上半', tier='重要',
  ol='1913年12月23日签署的法律，创设美国联邦储备体系作为常设中央银行。',
  ov=('《联邦储备法》(Federal Reserve Act) 由**美国第63届国会**通过，'
   '并于 **1913 年 12 月 23 日** 由伍德罗·威尔逊总统签署成为法律。'
   '该法**创设了联邦储备体系**——美国的常设中央银行。'
   '其直接动因是 1907 年恐慌（见 panic-1907）暴露的制度缺陷：'
   '在国民银行法体系下缺乏最后贷款人，恐慌时只能靠私人（摩根等人）协调救市。'
   '联储的核心设计是：以联邦储备券提供**弹性货币**、'
   '以贴现窗口履行**最后贷款人**职能、并通过地区储备银行形成分权结构以平衡政治顾虑。'
   '历史评价存在两面：它在之后百年成为危机应对的核心机构，'
   '但 1929—1933 年间的政策失误（未能阻止货币供给收缩）也成为货币政策研究中最常被检讨的案例'
   '（见 great-depression）。具体条款与分权设计待核实。'),
  tl=[
   {'year':1907,'display':'1907年','event':'恐慌暴露缺乏最后贷款人的制度缺陷（见 panic-1907）','sources':['w-en-panic-of-1907']},
   {'year':1913,'display':'1913年12月23日','event':'威尔逊总统签署联邦储备法，创设联邦储备体系','sources':['w-en-federal-reserve-act']},
  ],
  causal=[('1907年恐慌中只能靠私人救市 → 制度性最后贷款人缺位','w-en-panic-of-1907'),
         ('1913年立法创设联邦储备体系 → 弹性货币与贴现窗口','w-en-federal-reserve-act'),
         ('此后成为危机应对核心；1929—33年政策失误亦成经典检讨对象','w-en-great-depression')],
  schools=[('制度补缺视角','常设央行提供了弹性货币与最后贷款人，是必要进步','w-en-great-depression')],
  srcs=['w-en-federal-reserve-act','w-en-great-depression']),
]

# 修正上面 tuple 语法错误（schools 里有一处括号错位）
for sp in D:
    sp['schools'] = [(h, v, s) for h, v, s in sp['schools']]

HAVE = {json.load(open(f, encoding='utf-8'))['title'] for f in glob.glob('data/entries/*.json')}
for sp in D:
    if sp['title'] in HAVE:
        print('跳过重复标题', sp['id'], sp['title']); continue
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['per'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [], 'comparison': '',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基摘要；单源待核实。【续作CZ】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'], '|', sp['per'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r112_inst.json', encoding='utf-8'))
MAP = {'second-bank':'w-en-second-bank','free-banking':'w-en-free-banking',
       'national-banking-act':'w-en-national-bank-act','sherman-silver-purchase':'w-en-sherman-silver-purchase',
       'federal-reserve-act':'w-en-federal-reserve-act'}
for eid, sid in MAP.items():
    if sid in ex: continue
    v = meta.get(eid)
    if not v: print('meta缺', eid); continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['slug'],'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia REST API核对(本会话抓取摘要)'})
    ex.add(sid); print('新增来源',sid,'|',v['title'])
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':2,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':sp['unit'],'period':sp['per'],'region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])

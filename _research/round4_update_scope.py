# -*- coding: utf-8 -*-
"""轮次4：把9条新条目同步到 scope.md。"""
NEW={
 'U2 18—19世纪':[('black-friday-1869','黑色星期五黄金恐慌(1869)','18—19世纪','北美','货币','重要','S3,轮次4')],
 'U4 20世纪下半':[('russian-1998','1998年俄罗斯金融危机','20世纪下半','欧洲','货币','重要','S3,轮次4'),
   ('finnish-banking-1990','1990年代芬兰银行危机','20世纪下半','欧洲','银行','补充','S3,轮次4'),
   ('indian-1991','1991年印度经济危机','20世纪下半','亚洲','货币','重要','S3,轮次4'),
   ('ltcm','长期资本管理公司倒闭(1998)','20世纪下半','北美','银行','重要','S3,轮次4')],
 'U5 21世纪':[('uruguay-2002','2002年乌拉圭银行危机','21世纪','拉美','银行','补充','S3,轮次4'),
   ('cypriot-2013','2012–2013塞浦路斯金融危机','21世纪','欧洲','银行','重要','S3,轮次4'),
   ('myanmar-2003','2003年缅甸银行危机','21世纪','亚洲','银行','补充','S3,轮次4'),
   ('henan-2022','2022年河南银行危机','21世纪','亚洲','银行','补充','S3,轮次4')],
}
text=open('scope.md',encoding='utf-8').read()
for unit, rows in NEW.items():
    start=text.find('## '+unit)
    if start<0: continue
    nxt=text.find('\n## ',start+4)
    if nxt<0: nxt=len(text)
    block=text[start:nxt].rstrip('\n')
    add='\n'.join('| '+' | '.join(r)+' |' for r in rows)
    text=text[:start]+block+'\n'+add+'\n'+text[nxt:]
open('scope.md','w',encoding='utf-8').write(text)
print('scope.md 追加',sum(len(r) for r in NEW.values()),'条')

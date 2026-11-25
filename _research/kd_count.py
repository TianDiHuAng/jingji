# 用多种口径统计 key_data 单一来源条数，找出 README 原 551 的口径
import json,glob,sys,subprocess,re
def load(rev):
    if rev=='HEAD~':
        fs=subprocess.run(['git','ls-tree','--name-only','21b6dfd','data/entries/'],capture_output=True,text=True).stdout.split()
        return [json.loads(subprocess.run(['git','show','21b6dfd:'+f],capture_output=True).stdout.decode('utf-8')) for f in fs]
    return [json.load(open(f,encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
sys.path.insert(0,'tools')
for rev in ('HEAD~','now'):
    E=load(rev);K=[k for e in E for k in e.get('key_data') or []]
    a=sum(1 for k in K if len(k.get('sources',[]))<2)
    b=sum(1 for k in K if len(set(k.get('sources',[])))<2)
    c=sum(1 for k in K if '单一来源' in str(k.get('note','')))
    d=sum(1 for k in K if '待核实' in str(k.get('note','')))
    print(rev,'total',len(K),'len<2',a,'set<2',b,'note单一来源',c,'note待核实',d)

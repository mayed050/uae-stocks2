#!/usr/bin/env python3
# سكربت تجريبي: يحدّث حقل as_of فقط. سنبدله لاحقًا بجالب البيانات الحقيقي.
import json, time, os
p = os.path.join('data','daily.json')
with open(p,'r',encoding='utf-8') as f: d = json.load(f)
d['as_of'] = time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())
with open(p,'w',encoding='utf-8') as f: json.dump(d, f, ensure_ascii=False, indent=2)
print('daily.json updated as_of')

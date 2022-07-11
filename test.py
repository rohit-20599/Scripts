import requests
import base64
value= ('copy_char',
  'value',
  '207aLjBod',
  '1301420SaUSqf',
  '233ZRpipt',
  '2224QffgXU',
  'check_flag',
  '408533hsoVYx',
  'instance',
  '278338GVFUrH',
  'Correct!',
  '549933ZVjkwI',
  'innerHTML',
  'charCodeAt',
  './aD8SvhyVkb',
  'result',
  '977AzKzwq',
  'Incorrect!',
  'exports',
  'length',
  'getElementById',
  '1jIrMBu',
  'input',
  '615361geljRK')
for i in value:
   print i
   r=requests.get("http://mercury.picoctf.net:34588/"+i)
   if "pico" in r.text:
       print(r.text)


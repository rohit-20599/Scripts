s = " Aipgsqi fego, xlmw pizip mw rsx ew iewc ew xli pewx fyx wxmpp rsx xss gleppirkmrk. Ws ks elieh erh irxiv xlmw teww: wlmjxxlexpixxiv"
new =str("")
a= "abcdefghijklmnopqrstuvwxyz"
c=s.lower()
b = list(a)
print(b)
z=""
txt=""
print(b[1]+"    "+b[4])
print(c)
for i in c:
	if i.isalpha():
		txt=txt+a[(a.find(i)-4)%26]
	else:
		txt=txt+i
	
print(txt)


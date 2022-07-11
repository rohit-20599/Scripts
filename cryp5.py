s = "  qoymlNlpY :ccdf lpy yzJ .qoh ln lxigqoh qlxlm eeiw zot ydpy gmipylnoC ,zot gmiyqdncyzo ho ydpy ci lniqk tN .lsie sooe tlpy ydpw yom ,smipy amd tdc tlpy ydpw tj lefolf gmigazb ho ydpy ci lniqk tN .tyicoiqzk ho ydpy ci lniqk tN .edminiqk d nd i clT"




new =str("")
a= "abcdefghijklmnopqrstuvwxyz"
c=s.lower()
b = list(a)


z=""
txt=""

print(c)
print("----------------")



for i in range(len(c)):
	z=z+c[len(c)-1-i]

print(z)

print("-----------------")

c=z




switcher={

'c':'s',
'd':'a',
'f':'p',
'n':'m',
't':'y',
'h':'f',
'm':'n',
'a':'d',
'l':'e',


}


for i in c:
	if i in switcher:
		i=switcher.get(i)
		txt=txt+i
		
			
	else:
		txt=txt+i
	
print(txt)



test="Dc, gdcl cl h lcrcshn ckqh gz sqwqs guz. Gdcl gcrq qhyd sqggqn cl hllcomqk h ljqycacqk nqshgczmldcj ucgd hmzgdqn sqggqn. Jhll: cdhwqancqmkl"
test=test.lower()
test=test.replace('l','s')
test=test.replace('h','a')
test=test.replace('j','p')
test=test.replace('d','h')
test=test.replace('c','i')
test=test.replace('g','t')
test=test.replace('u','w')
test=test.replace('z','o')
test=test.replace('n','r')
test=test.replace('q','e')
test=test.replace('m','n')
test=test.replace('k','d')


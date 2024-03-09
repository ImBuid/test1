import pyzstd as ZS
DICT=open('dict','rb').read()
def ENC(path):
	try:
		with open(path,'rb')as r:r=r.read()
		if r[:4]!=b'"Jg\x00':
			out=bytearray(ZS.compress(r,17,ZS.ZstdDict(DICT,True)))
			out[0:0]=len(r).to_bytes(4,'little',signed=False)
			out[0:0]=b'\x22\x4a\x00\xef'
			with open(path,'wb') as w:w.write(out)
			return 1
		else:return 0
	except:return 0
def DEC(path):
	try:
		with open(path,'rb')as r:r=r.read()
		out=r[r.find(b'\x28\xb5\x2f\xfd'):]
		out=ZS.decompress(out,ZS.ZstdDict(DICT,True))
		with open(path,'wb') as w:w.write(out)
		return 1
	except:pass
	return 0
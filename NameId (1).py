import os
def G(kb):return int.from_bytes(kb,"little")
def HDC(String):
    if True:
        with open(os.path.join("Languages","languageMap_Xls.txt"),"rb") as f:
            dl=f.read().replace(b"\r",b"\r\n").replace(b"\n\n",b"\n")
            Find10=0
            A=[]
            Find=0
            while Find10!=-1:
                Find=dl.find(b" = "+String+b"\r\n",Find+1)
                if Find==-1:
                  return ""
                Find10=dl.find(b" = "+String+b"\r\n",Find+1)
                A.append(dl[Find-19:Find])
            return A
def N(H1,H):
    Hero,Skin=b'',b''
    for i in os.listdir("Languages"):
        with open(os.path.join("Languages","languageMap_Xls.txt"),"rb") as f:
            dl=f.read().replace(b"\r",b"\r\n").replace(b"\n\n",b"\n")
            Find=dl.find(H)
            if Find!=-1:
                Find2=dl.find(b"\r\n",Find)
                Skin=dl[Find+21: Find2]
            Find=dl.find(H1)
            if Find!=-1:
                Find2=dl.find(b"\r\n",Find)
                Hero=dl[Find+22: Find2]
            break
    return (Hero+Skin). decode()
class ID_Main():
    def AllSkin(I):
        Full=f"All Skin {I}"
        A=HDC(I.encode())
        if A=="":
            return f"Không Tìm Thấy {I}"
        with open("languages/Heroskin.bytes","rb") as f:
            d=f.read(16)
            K=int.from_bytes(d[12:],"little")
            d+=f.read(140-16)
            for i in range(K):
                kb=f.read(4)
                Code=f.read(G(kb))
                for O in A:
                    if Code.find(O)!=-1:
                        H=Code[40:19+40]
                        del A[(A.index(O))]
                        P=N(O,H)
                        if "[ex][DNT]" not in P:
                            Full+=f"\n{G(Code[:4])} "+P
                        break
        return Full
    def Ten(id):
        with open("languages/Heroskin.bytes","rb") as f:
            d=f.read(16)
            K=int.from_bytes(d[12:],"little")
            d+=f.read(140-16)
            for i in range(K):
                kb=f.read(4)
                Code=f.read(G(kb))
                if Code.find(id.to_bytes(4,'little')+int(str(id)[:3]).to_bytes(4,'little'))!=-1:
                    H1=Code[12:19+12]
                    H=Code[40:19+40]
                    return N(H1,H)
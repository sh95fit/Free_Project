from LoraData_Extraction import data

# data 정상 업로드 확인
#print(data)
src, phase, multi, code, lerr, inv, inv2, inv3, inv4, inv5, inv6, ina, ina2, ina3, ina4, ina5, ina6, inp, outv, outvr, outvs, outvt, outa, outar, outas, outat, outp, pf, frq, cpg, ec = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

#parser
data = ''.join(data)

if len(data) == 126 :
    src = int(data[2:4],16)
    phase = int(data[4:6],16)
    multi = int(data[6:8],16)
    code = int(data[6:8],16)
    lerr = int(data[8:10],16)
    inv1 = int(data[10:14],16)
    inv2 = int(data[14:18],16)
    inv3 = int(data[18:22],16)
    inv4 = int(data[22:26],16)
    inv5 = int(data[26:30],16)
    inv6 = int(data[30:34],16)
    ina1 = int(data[34:38],16)/10
    ina2 = int(data[38:42],16)/10
    ina3 = int(data[42:46],16)/10
    ina4 = int(data[46:50],16)/10
    ina5 = int(data[50:54],16)/10
    ina6 = int(data[54:58],16)/10
    inp = int(data[58:66],16)
    outvr = int(data[66:70],16)
    outvs = int(data[70:74],16)
    outvt = int(data[74:78],16)
    outar = int(data[78:82],16)
    outas = int(data[82:86],16)
    outat = int(data[86:90],16)
    outp = int(data[90:98],16)
    pf = int(data[98:102],16)/10
    frq = int(data[102:106],16)/10
    cpg = int(data[106:122],16)
    ec = int(data[122:126],16)
elif len(data) == 102 :
    src = int(data[2:4],16)
    phase = int(data[4:6],16)
    multi = int(data[6:8],16)
    code = int(data[6:8],16)
    lerr = int(data[8:10],16)
    inv1 = int(data[10:14],16)
    inv2 = int(data[14:18],16)
    inv3 = int(data[18:22],16)
    inv4 = int(data[22:26],16)
    inv5 = int(data[26:30],16)
    inv6 = int(data[30:34],16)
    ina1 = int(data[34:38],16)/10
    ina2 = int(data[38:42],16)/10
    ina3 = int(data[42:46],16)/10
    ina4 = int(data[46:50],16)/10
    ina5 = int(data[50:54],16)/10
    ina6 = int(data[54:58],16)/10
    inp = int(data[58:62],16)
    outv = int(data[62:66],16)
    outa = int(data[66:70],16)/10
    outp = int(data[70:74],16)
    pf = int(data[74:78],16)
    frq = int(data[78:82],16)
    cpg = int(data[82:98],16)
    ec = int(data[98:102],16)

res = {
'src' : src, 'phase' : phase, 'multi' : multi, 'code' : code, 'lerr' : lerr,
'inv' : inv1, 'inv2' : inv2, 'inv3' : inv3, 'inv4' : inv4, 'inv5' : inv5, 'inv6' : inv6, 
'ina' : ina1, 'ina2' : ina2, 'ina3' : ina3, 'ina4' : ina4, 'ina5' : ina5, 'ina6' : ina6, 'inp' : inp,
'outv' : outv, 'outvr' : outvr, 'outvs' : outvs, 'outvt' : outvt, 
'outa' : outa, 'outar' : outar, 'outas' : outas, 'outat' : outat, 'outp' : outp,
'pf' : pf, 'frq' : frq, 'cpg' : cpg, 'ec' : ec
}

#print(res)
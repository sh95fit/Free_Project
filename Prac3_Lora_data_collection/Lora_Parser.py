from LoraData_Extraction import data

# data 정상 업로드 확인
#print(data)
#src, phase, multi, code, lerr, inv, inv2, inv3, inv4, inv5, inv6, ina, ina2, ina3, ina4, ina5, ina6, inp, outv, outvr, outvs, outvt, outa, outar, outas, outat, outp, pf, frq, cpg, ec = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

#parser
data = ''.join(data)

if len(data) == 126 :
    src = int(data[2:4])
    phase = int(data[4:6])
    multi = int(data[6:8])
    code = int(data[6:8])
    lerr = int(data[8:10])
    inv1 = int(data[10:14])
    inv2 = int(data[14:18])
    inv3 = int(data[18:22])
    inv4 = int(data[22:26])
    inv5 = int(data[26:30])
    inv6 = int(data[30:34])
    ina1 = int(data[34:38])/10
    ina2 = int(data[38:42])/10
    ina3 = int(data[42:46])/10
    int4 = int(data[46:50])/10
    int5 = int(data[50:54])/10
    int6 = int(data[54:58])/10
    inp = int(data[58:66])
    outvr = int(data[66:70])
    outvs = int(data[70:74])
    outvt = int(data[74:78])
    outar = int(data[78:82])
    outas = int(data[82:86])
    outat = int(data[86:90])
    outp = int(data[90:98])
    pf = int(data[98:102])/10
    frq = int(data[102:106])/10
    cpg = int(data[106:122])
    ec = int(data[122:126])
elif len(data) == 102 :


res = {
'src' : src, 'phase' : phase, 'multi' : multi, 'code' : multi, 'lerr' : 0,
'inv' : 0, 'inv2' : 0, 'inv3' : 0, 'inv4' : 0, 'inv5' : 0, 'inv6' : 0, 
'ina' : 0, 'ina2' : 0, 'ina3' : 0, 'ina4' : 0, 'ina5' : 0, 'ina6' : 0, 'inp' : 0,
'outv' : 0, 'outvr' : 0, 'outvs' : 0, 'outvt' : 0, 
'outa' : 0, 'outar' : 0, 'outas' : 0, 'outat' : 0, 'outp' : 0,
'pf' : 0, 'frq' : 0, 'cpg' : 0, 'ec' : 0
}


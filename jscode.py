patch_eval_code="""
function setTimeout(a,b){};
document={ 
    createElement:function(a){
                       return {innerHTML:{},firstChild:{href:"http://www.gsxt.gov.cn/"}}
                    },
    addEventListener:function(a,b,c){b();},
    attachEvent:function(a,b){}
}; 
window={
addEventListener:function(a,b,c){},
};
"""
patch_load_code="""
var eval_code="";%s;eval_code;
"""

test_code="""function setTimeout(a,b){};
document={ 
    createElement:function(a){
                       return {innerHTML:{},firstChild:{href:"http://www.gsxt.gov.cn/"}}
                    },
    addEventListener:function(a,b,c){b();},
    attachEvent:function(a,b){}
}; 
window={
addEventListener:function(a,b,c){},
};
var x = "@length@KSx@DOMContentLoaded@@@@addEventListener@2tn6d@try@@RegExp@@3@@19@false@@0@@setTimeout@fromCharCode@d@g@innerHTML@1@__p@var@Apr@catch@firstChild@@@e@Path@8@@document@@split@@return@for@442@createElement@@JgSe0upZ@@@@cookie@replace@0xFF@@match@if@@eval@as@while@@String@@3D@@@@20@@@href@Array@search@join@@@@a@@18@36@challenge@__jsl_clearance@1500@toString@Thu@div@pathname@2@hantom@charAt@E0U@@jKg@new@window@attachEvent@@@@captcha@chars@toLowerCase@onreadystatechange@@reverse@@0xEDB88320@charCodeAt@location@https@@5@function@@@substr@@else@09@GMT@1555575560@f@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@Expires@@4@parseInt".replace(/@*$/, "").split("@"),
y = "s 31=30(){l('2y.1x=2y.2c+2y.1z.1e(/[\\?|&]2p-26/,\\'\\')',28);10.1d='27=38.16|j|'+(30(){s 34=[30(31){14 31},30(34){14 34},(30(){s 31=10.17('2b');31.p='<22 1x=\\'/\\'>1j</22>';31=31.v.1x;s 34=31.1h(/2z?:\\/\\//)[j];31=31.33(34.2).2r();14 30(34){15(s 1j=j;1j<34.2;1j++){34[1j]=31.2f(34[1j])};14 34.1A('')}})(),30(31){14 1k('1o.m('+31+')')}],1j=['9',[{}+[]+[]][j].2f(((+!!/!/)|-~(+!!/!/))-~(+!!/!/)-~((-~{}+[-~{}-~{}]>>-~{}-~{}))),[[-~[]]+(~~![]+[[]][j])+(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j])],[[-~[]]+(~~![]+[[]][j])],[[-~[]]+(~~![]+[[]][j])+[(-~{}<<2d)]],'3',[[-~[]]+[-~[-~{}-~{}]],[2B]],'2i',[(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j])+[-~(+[])-~[]+3d]],'2g',(2k['r'+'2e'+'1l']+[]+[[]][j]).2f((+!{}))+[[(-~[]<<-~[])]/~~{}+[]+[[]][j]][j].2f(-~[-~{}-~{}]+(-~[]<<-~[])+(-~[]<<-~[])),[(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j])+(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j])],(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j]),[[-~[]]+[-~[]]+[-~[-~{}-~{}]],[-~[]+(-~![]+[-~((-~{}+[-~{}-~{}]>>-~{}-~{}))]>>-~![])]+[-~((-~{}<<((+!!/!/)|-~(+!!/!/))))],[-~[-~{}-~{}]]+(-~[(-~{}+[-~{}-~{}]>>-~{}-~{})+(-~{}+[-~{}-~{}]>>-~{}-~{})]+[]+[[]][j])],'1q'];15(s 31=j;31<1j.2;31++){1j[31]=34[[q,j,e,2d,e,q,2d,q,e,q,j,e,j,e,q][31]](1j[31])};14 1j.1A('')})()+';3b=2a, 24-t-g 36:g:1u 37;z=/;'};1i((30(){a{14 !!2k.8;}u(y){14 h;}})()){10.8('4',31,h)}35{10.2l('2s',31)}",
f = function(x, y) {
    var a = 0,
    b = 0,
    c = 0;
    x = x.split("");
    y = y || 99;
    while ((a = x.shift()) && (b = a.charCodeAt(0) - 77.5)) c = (Math.abs(b) < 13 ? (b + 48.5) : parseInt(a, 36)) + y * c;
    return c
},
z = f(y.match(/\w/g).sort(function(x, y) {
    return f(x) - f(y)
}).pop());
while (z++) try {
    console.log(z+"hahahhahah");
    console.log(y.replace(/\b\w+\b/g,
    function(y) {
        return x[f(y, z) - 1] || ("_" + y)
    }));
    break
} catch(_) {}
console.log(document.cookie);"""
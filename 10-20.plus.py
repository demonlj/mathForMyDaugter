import random

strheader='''\\documentclass[a5paper,UTF8]{article} 
\\usepackage{geometry}
\\usepackage{xcolor}
\\usepackage{tikz}
\\usetikzlibrary{arrows,shapes,chains}
\\geometry{a5paper,scale=1.0}
\\begin{document}'''

strfooter='\n\\end{document}`'

strinterval="\n\\clearpage\n"

tikz='''
\\begin{figure}  
\\centering
\\scriptsize  
\\begin{tikzpicture}
\\coordinate (A) at (0,0);
\\coordinate (B) at (1.4,0);
\\coordinate (C) at (2.8,0);
\\coordinate (D) at (4.2,0);
\\coordinate (E) at (5.6,0);
\\coordinate (H) at (7,0);
\\coordinate (F) at (1.4,-2.8);
\\coordinate (G) at (4.2,-2.8);
\\draw (A) node{\\Huge FIRST};
\\draw (B) node{\\Huge +};
\\draw (C) node{\\Huge SECOND};
\draw (D) node{\\Huge =};
\\foreach \\P in {E,F,G,H}
{
    \\draw (\\P) ++ (-0.7,-0.7) rectangle ++ (1.4,1.4);
    \\draw[dashed,gray](\\P) -- +(-0.7,0 );
    \\draw[dashed,gray](\\P) -- +(+0.7,0 );
    \\draw[dashed,gray](\\P) -- +( 0,-0.7);
    \\draw[dashed,gray](\\P) -- +( 0,+0.7);
}
\\draw[-] (C) ++ (0,-0.7) --  +(-1.4,-1.4) 
\\draw[-] (C) ++ (0,-0.7) --  +(1.4,-1.4) 
\\end{tikzpicture}
\\end{figure}
'''


mm=10
a=[]
for x in range(1,mm):
  for y in range(1,mm):
     if x+y>10:
         m=x
         n=y
         if n>m:
             m=y
             n=x
         string=tikz.replace("FIRST", str(m))
         string=string.replace("SECOND", str(n))
         a.append(string)
 
random.shuffle(a)

fo = open("test.txt", "w")
fo.write(strheader)
lin = 0
for e in a:
   fo.write(e)
   lin+=1
   if lin==4:
     lin=0
     fo.write(strinterval)
fo.write(strfooter)
fo.close()

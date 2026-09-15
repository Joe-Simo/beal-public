"""Check the claimed q=409 unit elimination without discarding Gaussian scale."""
from __future__ import annotations
import json


def power(r: int, s: int, q: int) -> tuple[int, int]:
    a, b = 1, 0
    for _ in range(17):
        a, b = (a*r-b*s) % q, (a*s+b*r) % q
    return a, b


def main() -> None:
    q = 409
    roots = [w for w in range(q) if (w*w-w-1) % q == 0]
    pows = {pow(a,17,q): a for a in range(q)}
    rows=[]
    for k in (0,15):
        cases=[]
        # r:s = t:1, together with 1:0. Input rescaling multiplies H
        # by a 68th power, hence cannot change 17th-power membership.
        for r, s in [(t,1) for t in range(q)]+[(1,0)]:
            m,n=power(r,s,q)
            h=[(m**4+30*m*m*n*n+n**4-16*m*m*n*n*w) % q for w in roots]
            targets=[h[j]*pow(pow(w,k,q),-1,q) % q for j,w in enumerate(roots)]
            if all(value in pows for value in targets):
                aa=[pows[value] for value in targets]
                bb=(aa[0]-aa[1])*pow(roots[0]-roots[1],-1,q) % q
                a=(aa[0]-bb*roots[0]) % q
                cases.append({'r':r,'s':s,'m':m,'n':n,'alpha':[a,bb], 'h_embeddings':h})
        rows.append({'k':k,'projective_input_cases':len(cases),'witnesses':cases[:4],
                     'non_axes':sum(1 for c in cases if c['m']*c['n'] % q !=0)})
    print(json.dumps({'status':'completed','q':q,'roots_omega':roots,'rows':rows}, indent=2))

if __name__=='__main__': main()

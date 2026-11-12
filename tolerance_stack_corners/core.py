import math
from .common import number,unique_ids
def run(data):
 terms=data['terms']
 if not isinstance(terms,list)or len(terms)>1000:raise ValueError('terms')
 unique_ids(terms);center=0.;radius=0.;variance=0.;corners=[]
 for t in terms:
  a=number(t['coefficient'],-1e6,1e6);nominal=number(t['nominal'],-1e9,1e9);half=number(t['half_width'],0,1e9);center+=a*nominal;radius+=abs(a)*half;variance+=(a*half)**2/3
  corners.append({'id':t['id'],'at_minimum':nominal-half if a>=0 else nominal+half,'at_maximum':nominal+half if a>=0 else nominal-half})
 return {'interval':[center-radius,center+radius],'nominal':center,'independent_uniform_std':math.sqrt(variance),'extreme_witnesses':corners,'independence_assumed_for_std':True,'guaranteed_by_std':False}

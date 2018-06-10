def MultiM (MatA,MatB):
	if isinstance (MatA,list) and (MatB,list):
		return MultiM_aux (MatA, MatB, 0, 0, 0, 0, [],[])
	else:
		return "Por Favor ingrese dos matrices para su multiplicacion"
def MultiM_aux (MatA, MatB, IA, IB, IC, NV, NF, NM):
	if IC == len(MatA):
		return NM
	elif IB !=len (MatB):
		if IA != len(MatA):
			return MultiM_aux (MatA, MatB, IA, IB +1, IC, MatA [IC][IB] * MatB [IB][IA] + NV, NF, NM)
		else:
			return MultiM_aux (MatA, MatB, 0, 0, IC +1, 0,[], NM+[NF])
	else:
		return MultiM_aux (MatA, MatB, IA+1, 0, IC, 0, NF+[NV], NM)

print (MultiM([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]]))

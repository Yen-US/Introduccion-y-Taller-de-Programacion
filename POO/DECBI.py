class Decimal_y_Binario:

    def __init__ (self):
        pass

    def DECYBI (self,N):
        if isinstance (N,int):
            return self.Ver_BD (N,N)
        else: return "Por Favor Ingrese un Número"
        
    def Ver_BD (self,BD,R):
        if BD==0:return self.BIDEC (R)
        elif BD%10==0 or BD%10==1:return self.Ver_BD(BD//10,R)
        else:return self.DECBI (R)
        
    def DECBI (self,D):
        if isinstance (D,int):return self.DECBI_aux (D,0)
        else:return "Por Favor Ingrese un Número Válido"
    def DECBI_aux (self,D,E):
        if D==0:return 0
        elif D%2==1:return (1*10**E) + self.DECBI_aux(D//2,E+1)
        else:return self.DECBI_aux(D//2,E+1)
        
    def BIDEC (self,B):
        if isinstance (B,int):return self.BIDEC_aux (B,0)
        else: return "Por Favor Ingrese un Número Válido"
    def BIDEC_aux (self,B,E):
        if B==0:return 0
        elif B%10 == 1:return (2**E) + self.BIDEC_aux (B//10,E+1)
        else:return self.BIDEC_aux (B//10,E+1)




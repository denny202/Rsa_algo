import random

class RSA_Algo():
    
    #instance class here
    n=0
    phi=0
    e=2
    d=0
    c=1
 
#Constructor          
    def __init__(self,p,q,m):
        #instance attributes
        self.p=p
        self.q=q
        self.m=m
        

#Key generation        
    def find_n(self):
        self.n=(self.p*self.q)
        print("n: ",self.n)
        return self.n
        
    #Calculate the value of phi        
    def totient(self):
        self.phi=(self.p-1)*(self.q-1)
        print("phi: ",self.phi)
        return self.phi 
    
    
    #Euclid's algorithm for determining the greatest common divisor
    def ggcd(self,a, b):
        if(b == 0):
            return abs(a)
        else:
            return self.ggcd(b, a % b)
        
    #public key ( e , n)
    #Choose an e such that 1 and e < phi 
    #gcd (e , phi)   
    def choose_e(self):
            #return only e if e and phi are coprime  using euclidian algorithm 
            while self.ggcd(self.e, self.phi) != 1 and self.ggcd(self.e, self.phi) <self.phi :
                self.e = random.randrange(1, self.phi)
            return self.e
 

    #private key  (d,n)
    #Extended euclidian algorithm       
    def choose_d(self):
        a=self.e
        b=self.phi
        x = 0
        y = 1
        lx = 1 ###
        ly = 0 ###
        while b != 0 and lx <=1:
            q = a // b    ##a
            (a, b) = (b, a % b)
            (x, lx) = ((lx - (q * x)), x)
            (y, ly) = ((ly - (q * y)), y)
          
        self.d=lx
        return lx  # Return only positive values

        
    
      
        
    
#Run all the functions inside the class  
    def run_all(self):
        self.find_n()
        self.totient()
        print(f"debug 1 : p: {self.p} q: {self.q} m: {self.m} n: {self.n} phi: {self.phi} e: {self.e}  ")     
        self.choose_e() 
        print(f"debug 2 : p: {self.p} q: {self.q} m: {self.m} n: {self.n} phi: {self.phi} e: {self.e}  ")
        self.choose_d()
        print(f"debug 3 : p: {self.p} q: {self.q} m: {self.m} n: {self.n} phi: {self.phi} e: {self.e}  ")
        
    def encrypt(self):
        self.run_all()
        self.m=((self.m ** self.e)%self.n)
        print("The encrypted message is :",self.m)
        self.c=self.m
        return self.m

    def decrypt(self):
            print("cypher:", self.c," d: ",self.d," n: ",self.n)
            self.message=((self.c**self.d)%self.n)
            print("The decrypted message is :",self.message)
            return self.message
            
            
if __name__ == "__main__":
    
    
    print("Choose p")
    p= int(input ())
    print("Choose q")
    q= int(input ())
   
    print("input message to encrypt")
    m=int(input ())

    rsa1= RSA_Algo(p,q,m)
   #s rsa1.run_all()
    print(rsa1.encrypt())
    
       
           
    
    

        
    
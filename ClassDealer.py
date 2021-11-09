import random

class Dealer:
   
     def __init__(self):
         self.Secret = 0;
         self.Coefs = [];

     def InputSecret(self):
         while 1:
             try:
                 S = int(input('Введите секрет: '));
                 self.Secret = S;
                 return;
             except:
                 print('Неверный ввод. Введите число!');
                 continue;
     
     def GenerateCoefs(self, PolynomDegree, p):
         RandomCoefs = [];
         for i in range(0, PolynomDegree):
             Coef = random.randint(1,p);
             RandomCoefs.append(Coef);

         self.Coefs = RandomCoefs;

     def ForgetCoefs(self):
         self.Coefs = [];

     def ShareOfThePartSecret(self, KeeperNumber, p):
         CoefsWithSecret = self.Coefs.copy();
         CoefsWithSecret.append(self.Secret);

         F = 0;#полином
         Degree = len(CoefsWithSecret);#степень полинома + Secret
         for i in range(len(CoefsWithSecret)):
             Degree -= 1;
             F += CoefsWithSecret[i]*KeeperNumber**(Degree);
         
         Pair = [KeeperNumber, F%p];

         return Pair;



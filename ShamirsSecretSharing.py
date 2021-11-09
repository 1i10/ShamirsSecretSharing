from ClassDealer import Dealer
from ClassKeeperPartOfTheSecret import KeeperPartOfTheSecret
import sympy.ntheory as nt
from sympy import mod_inverse

def ShowSecretsCheck(DealerSecret, GroupSecret):
    print('Секрет диллера: ' + str(DealerSecret) + '; Расшифрованный секрет: ' + str(GroupSecret));
    if DealerSecret == GroupSecret:
        print('Секреты совпадают!');
    else:
        print('Секрет расшифрован неверно!');

def RecoverSecret(Group, p):
    
    ListOfX = [];
    ListOfY = [];
    for Keeper in Group:
        ListOfX.append(Keeper.PairKey[0]);
        ListOfY.append(Keeper.PairKey[1]);

    #интерполяционный полином лагранжа
    LenX = len(ListOfX);
    InterPoly = 0;

    for i in range(LenX):
        Yi = ListOfY[i];
        Part = 1;
        for j in range(LenX):
            if j == i:
                continue;
            InverseDenom = mod_inverse(ListOfX[j]-ListOfX[i],p);
            Part *= (ListOfX[j]%p)*InverseDenom;
            
        InterPoly += Yi*Part;  

    Secret = InterPoly%p;

    return Secret;

def CreateGroup(ListOfParticipants):
    while(1):
        GroupOfParticipants = [];
        NumberOfParticipants = list(map(int,input('Введите номера участников для восстановления секрета через пробел: ').split()));

        for i in NumberOfParticipants:
            try:
                FindParticipant = next(j for j in ListOfParticipants if j.PairKey[0] == i);
            except:
                print('Участник ' + str(i) + ' не найден. Повторите ввод участников!');
                print('=======');
                break;
            GroupOfParticipants.append(FindParticipant);

        if len(GroupOfParticipants) == len(NumberOfParticipants):
            return GroupOfParticipants;

def GeneratePrime(NumberParticipants, Secret):
    if NumberParticipants > Secret:
        PrevPrime = NumberParticipants;
    else:
        PrevPrime = Secret;

    return nt.nextprime(PrevPrime);


def InputNumber(Message):
    while 1:
        try:
            Number = int(input(Message));
            return Number;
        except:
            print('Неверный ввод. Введите число!');
            continue;

if __name__ == '__main__':

    Dealer1 = Dealer();
    Dealer1.InputSecret();

    while 1:
        n = InputNumber('Введите количество хранителей части секрета: ');
        if n <= 1:
            print('Количество участников должно быть строго больше 1');
            print('=======');
        else:
            break;

    p = GeneratePrime(n, Dealer1.Secret);
    print('Сгенерированное простое число: ' + str(p));

    while 1:
        k = InputNumber('Минимальное количество участников для расшифровки секрета: ');
        if k > n or k <= 1:
            print('Минимальное количество участников должно быть меньше или равно общему количеству участников (от 2-ух)');
            print('=======');
        else:
            break;

    Dealer1.GenerateCoefs(k-1, p);
    print('Сгенерированные коэф-ты полинома: ', Dealer1.Coefs);

    ListOfKeepers = [];

    for i in range(1, n+1):
        Keeper = KeeperPartOfTheSecret(Dealer1.ShareOfThePartSecret(i, p));
        ListOfKeepers.append(Keeper);

    Dealer1.ForgetCoefs();

    for KeeperKey in ListOfKeepers:
        print('Часть ключа участника ' + str(KeeperKey.PairKey[0]) + ': ', KeeperKey.PairKey);

    
    GroupOfKeepers = CreateGroup(ListOfKeepers);
  
    GroupSecret = RecoverSecret(GroupOfKeepers, p);
    ShowSecretsCheck(Dealer1.Secret, GroupSecret);




     
""""
დავალება  იური გაგარიზნე
შევქმნათ ფუნქცია yuri_gagarini()
იური გაგარინის წნევა აღწვევდა 120-გულის წნევას პულსი 80-ს თქვენი დავალეება რომ შექმნათ ფუქნცია რომელიც 
მომახარებელს user -ს შეეკითხება თუ რამდენი აქვს გულის წნევა და პუსლი თუ დაემთხვევა პულსი იურინი გაგარინს პულს მაშინ Ture გამოიტანოს წინააღმდეგ შემთხვევაში Falase
"""
def yuri_gagarini(pulsi , wneva):
    useris_wneva = input("შეიყვანეთ თქვენი წნევა: ")
    useris_pulsi = input("შეიყვანეთ თვენი პულსი: ")
    if int(useris_wneva) == 120 and int(useris_pulsi) == 80:
        return True
    else:
        return False
print(yuri_gagarini(80 , 120))
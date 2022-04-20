class Test:
    contador = 0
    
    def __init__(self):
        Test.contador += 1
        print("Nueva instancia. Total :", Test.contador)

for i in range(10):
    Test()

print(Test.contador)
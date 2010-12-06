from unittest import TestCase

__author__ = 'GCCSD'
__authors__ = ['Apu', 'InFog', 'Paulo', 'Sigano']

class FizzBuzz(object):
    def execute(self, numero):
        if numero % 3 == 0 and numero % 5 == 0:
            return "FizzBuzz"
        elif numero % 3 == 0:
            return "Fizz"
        elif (numero % 5 == 0):
            return "Buzz"
        else:
            return str(numero)

class TestFizzBuzz(TestCase):

    def testDivTres(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual("Fizz", fizzbuzz.execute(3))
        self.assertEqual("Fizz", fizzbuzz.execute(6))
        self.assertEqual("Fizz", fizzbuzz.execute(27))

    def testNaoDivTres(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual("2", fizzbuzz.execute(2))
        self.assertEqual("4", fizzbuzz.execute(4))

    def testNaoDivCinco(self):
        fizzbuzz = FizzBuzz()

        self.assertEqual("4", fizzbuzz.execute(4))
        self.assertEqual("7", fizzbuzz.execute(7))

    def testDivCinco(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual("Buzz", fizzbuzz.execute(5))
        self.assertEqual("Buzz", fizzbuzz.execute(20))
        self.assertEqual("Buzz", fizzbuzz.execute(55))

    def testDivTresCinco(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual("FizzBuzz", fizzbuzz.execute(15))
        self.assertEqual("FizzBuzz", fizzbuzz.execute(30))
        self.assertEqual("FizzBuzz", fizzbuzz.execute(60))



    def testeUmDez(self):
        fizzbuzz = FizzBuzz()

        expectedValue = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz"
        generatedValue = ""

        for i in range(1,11):
            generatedValue += fizzbuzz.execute(i) + " "
        generatedValue = generatedValue.rstrip()

        self.assertEqual(expectedValue, generatedValue)

if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    for i in range(1, 101):
        print(fizzbuzz.execute(i))



class Investment:
    def __init__(self,principal,intrest):
        self._principal=principal
        self._intrest=intrest

    def value_after(self,years):
        val=self._principal*(self._intrest+1)**years
        return round(val,2)

    def __str__(self) -> str:
        return 'Principal - ${}, interest rate- {}%'.format(self._principal, self._intrest*100)


def main():
    invest=Investment(1000,0.0512)
    #value=invest.value_after(5)
    print(invest)
    print(__name__)
  

if __name__ == '__main__':
    main()

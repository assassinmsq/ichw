"""Currency.py: currency translation.

__author__ = "Ma Siqi"
__pkuid__  = "1800011760"
__email__  = "1800011760@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):

    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.
    """

    from urllib.request import urlopen
    Amount_from=str(amount_from)
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?'+'from='+currency_from+'&to='+currency_to+'&amt='+Amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    if '"success" : true' in jstr:
        import json
        re_jstr = json.loads(jstr)
        ori = re_jstr.get('to')

        list = ori.split()
        result = float(list[0])
        return(result)


code = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "USD", "EUR"]


def test_typecf(a):
    """test the type of the currency_from input
        """

    assert a in code, 'currency_from is a string for a valid currency code'


def test_typect(b):
    """test the type of the currency_to input
        """

    assert b in code, 'currency_to is a string for a valid currency code'


def test_exchange(currency_from, currency_to, amount_from, result):
    """test the result of the amount_to
        """

    assert exchange(currency_from, currency_to, amount_from) == result


def testAll(currency_from, currency_to, amount_from, result):
    """test all cases"""
    test_typecf(currency_from)
    test_typect(currency_to)
    test_exchange(currency_from, currency_to, amount_from, result)
    print("All tests passed")


testAll("USD", "EUR", 2.5, 2.1589225)


def main():
    """main module
    """
    currency_from = input()
    currency_to = input()
    amount_from = input()

    exchange(currency_from, currency_to, amount_from)


if __name__ == '__main__':
    main()


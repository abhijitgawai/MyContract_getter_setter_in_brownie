from brownie import Wei, reverts, accounts, chain, MyContract

def test_name(isolation, owner, MyContract):

    # Defining Things
    myContarctObject = MyContract[-1]
    print(myContarctObject.address)

    print(myContarctObject.get())

    # Test Case
    assert myContarctObject.get() == 'MyValueDefault' # 1st test case

    # Acting
    myContarctObject.set("MySecondValue", {"from":owner})

    # Test Case
    assert myContarctObject.get() == 'MyValueDefault' # 2nd test case
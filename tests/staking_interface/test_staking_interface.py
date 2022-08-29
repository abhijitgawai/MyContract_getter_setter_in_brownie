from brownie import Wei, reverts, accounts, chain, OwnerTransfer

def test_name(isolation, owner, alice, OwnerTransfer, bob):

    contractObject  = OwnerTransfer[-1]

    assert contractObject.variable() == 0 # 1st test case

    assert contractObject.owner() == owner.address

    contractObject.IsOwner(4, {"from":owner})

    assert contractObject.variable() == 4

    contractObject.transferOwnership(alice , {"from":owner})

    assert contractObject.owner() == alice.address

    # Expecting an error
    with reverts("Ownable: caller is not the owner"):
        contractObject.transferOwnership(alice , {"from":bob})

    assert False







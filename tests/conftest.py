import pytest
from brownie import accounts, Wei, chain
from brownie import (MyContract)
from scripts.utils.helpful_scripts import *

@pytest.fixture(scope="module", autouse="True")
def shared_setup(module_isolation):
    pass

@pytest.fixture(scope="module")
def owner():
    return accounts[0]

@pytest.fixture(scope="module")
def alice():
    return accounts[1]

@pytest.fixture(scope="module")
def bob():
    return accounts[2]

@pytest.fixture(scope="module")
def charlie():
    return accounts[3]

@pytest.fixture(scope="module")
def katy():
    return accounts[4]

@pytest.fixture(scope="module")
def lauren():
    return accounts[5]

@pytest.fixture(scope="module")
def extWallet():
    return accounts[6]

@pytest.fixture(scope="module")
def treasuryWalllet():
    return accounts[7]

@pytest.fixture(scope="module")
def users():
    return accounts[8:]

@pytest.fixture(scope="module", autouse=True)
def deploy(owner, alice, bob, katy, lauren, charlie):
    owner =  accounts[1]
    newContarctAddress = MyContract.deploy({"from":owner})
    print(newContarctAddress)
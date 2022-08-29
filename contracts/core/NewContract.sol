// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract OwnerTransfer is Ownable{                                  // Python syntax of inheritance -> OwnerTransfer(Ownable)

    uint public variable;

    function IsOwner(uint _variable) public  onlyOwner {   
        variable = _variable;
    }

    // function variable() view public returns (uint) { 
    //     return varialbe;
    // }

    // modifier onlyOwner() {                                       
    //     _checkOwner(); 
    //     _;
    // }

    function _checkOwner() internal view virtual {
        require(owner() == _msgSender(), "Ownable: caller is not the owner");
    }



}
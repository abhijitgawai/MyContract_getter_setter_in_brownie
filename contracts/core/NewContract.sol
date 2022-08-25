// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;





contract MyContract{

    string value;
    
    constructor() public {
        value="MyValueDefault";
    }
    
    function get() public view returns (string memory){
        return value;
    }
    
    function set(string memory _value) public {
        value=_value;
    }
}


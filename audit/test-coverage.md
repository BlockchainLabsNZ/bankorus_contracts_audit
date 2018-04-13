# Test Coverage
performed by Blockchain Labs, 12 April, 2018


File                    |  % Stmts | % Branch |  % Funcs |  % Lines |Uncovered Lines |
------------------------|----------|----------|----------|----------|----------------|
  flat_bankorus.sol     |    89.47 |    78.26 |    91.67 |    89.74 |... 4,72,74,352 |


Full coverage report of related contracts is [here](https://github.com/BlockchainLabsNZ/bankorus_pre/tree/master/audit/coverage).

<br>

### SafeMath.sol

```
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        assert(c / a == b);
        return c;
    }
 
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        // assert(b > 0); // Solidity automatically throws when dividing by 0
        uint256 c = a / b;
        // assert(a == b * c + a % b); // There is no case in which this doesn't hold
        return c;
    }
```
These two functions are in the SafeMath library. They are not been used in the token contract at all. 

### Bankorus.sol
```
function transferToAddresses(address[] _addresses, uint256[] _values) onlyOwner public returns (bool success) {
    require(_addresses.length == _values.length);
    require(_addresses.length <= arrayLimit);
 
    if (allow == false) {
      require(msg.sender == owner);
    }
 
    uint8 i = 0;
    for (i; i < _addresses.length; i++) {
      require(super.transfer(_addresses[i], _values[i]));
    }
    return true;
}
```
The if statement is redundant. Suggest to remove it and no need to be tested. Refer to [Issue #4](https://github.com/BlockchainLabsNZ/bankorus_pre/issues/4)

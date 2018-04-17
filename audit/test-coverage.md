# Test Coverage
performed by Blockchain Labs, 18 April, 2018


File                    |  % Stmts | % Branch |  % Funcs |  % Lines |Uncovered Lines |
------------------------|----------|----------|----------|----------|----------------|
  flat_bankorus.sol     |    87.72 |    78.13 |    88.89 |    87.93 |... 63,64,72,74 |



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

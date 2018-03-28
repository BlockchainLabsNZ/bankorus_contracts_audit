# Bankorus pre-audit

here we put our initial concerns and issues to discuss.

<br>

## Questions

- **RBAC and roles**

	Why do you need all of that roles, de(in)creaseable approvals and so on. Any reasons for that? Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner?


<br>

## Suggestions

- **Check role**<br>
	For `frozen()` and `unFrozen()` functions, it is cheaper to use modifier `onlyAdmin()` which cost only 200gas rather than `checkRole()` function of the [RBAC.sol](https://github.com/OpenZeppelin/zeppelin-solidity/blob/master/contracts/ownership/rbac/RBAC.sol), which will read the storage.
	
- **Declaration missed**<br>
	[Line 36](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/7f403decb4f8ad1463f903b5e8c149d7d3ee5e62/contracts/bankorus.sol#L36): `contractAddress = this;` – the variable is not used. Whould you consider its declaration `address public contractAddress;` or removal?
		
- **Total supply**<br>
	[Line 34](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/7f403decb4f8ad1463f903b5e8c149d7d3ee5e62/contracts/bankorus.sol#L34): 

	```	
	 function BankorusToken (uint256 initialSupply) public {
        totalSupply_ = totalSupply * 10 ** uint256(decimals);
        ...
     }
	```
	
	probably mistyped: totalSupply_ = <b>initialSupply</b> * 10 ... ?

# Bankorus pre-audit

here we put our initial concerns and issues to discuss.

<br>

## Questions

- **RBAC and roles**

	Why do you need all of that roles, de(in)creaseable approvals and so on. Any reasons for that? Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner?

- **Unclear purpose variable**
	What is the purpose of `roleFrozen`? The comment says it is the initial state, then should it be a Boolean flag? After reading the codes, this variable looks more like a fixed role name. Then we would suggest change the name and comment of this variable.
	[bankorus.sol, Line 21](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/932bdf8163dc7c654528cd185474902471c8bc7a/contracts/bankorus.sol#L21)

<br>

## Suggestions

- **Check role**<br>
	For `frozen()` and `unFrozen()` functions, it is cheaper to use modifier `onlyAdmin()` which cost only 200gas rather than `checkRole()` function of the [RBAC.sol](https://github.com/OpenZeppelin/zeppelin-solidity/blob/master/contracts/ownership/rbac/RBAC.sol), which will read the storage.
	
- **Declaration missed**<br>
	[Line 36](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/7f403decb4f8ad1463f903b5e8c149d7d3ee5e62/contracts/bankorus.sol#L36): `contractAddress = this;` – the variable is not used. Whould you consider its declaration `address public contractAddress;` or removal?
		

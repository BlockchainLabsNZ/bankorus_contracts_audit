# Bankorus pre-audit

<br>

## Questions

- **RBAC and roles**
<br>Why do you need all of that roles? A mapping(address => bool) would be cheaper for gas consumption and easier for understanding. Any reasons for using all set of that? 

- **onlyOwner modifier**
<br>Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner?

- **Which functions from StandardToken.sol are needed?**
<br>Just to understand

<br>

## Suggestions

- **Check role**<br>
	For `frozen()` and `unFrozen()` functions, it is cheaper to use modifier `onlyAdmin()` which cost only 200gas rather than `checkRole()` function of the [RBAC.sol](https://github.com/OpenZeppelin/zeppelin-solidity/blob/master/contracts/ownership/rbac/RBAC.sol), which will read the storage.
	
- **transver vs withdraw**<br>Push(transfer) approach is chosen, which is not a [best practice](https://ethereum-contract-security-techniques-and-tips.readthedocs.io/en/latest/recommendations/#favor-pull-over-push-for-external-calls).  	

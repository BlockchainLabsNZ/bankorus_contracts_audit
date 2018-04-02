# Bankorus pre-audit

<br>

## Questions

- **RBAC and roles**
<br>Now only one function of RBAC.sol is used: `onlyAdmin()`. Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner? 
It will be clearer and cheaper.


<br>

## Suggestions

	
- **Self-made checks vs standard modifiers**<br>
	consider to replace 
	
	```
	if (!paused) {
      require(msg.sender == owner);
    }
	```
	to standard modifiers `whenNotPaused()` and `onlyOwner()` from the Pausable.sol and Ownable.sol respectively.

- **Checks if sale is Paused**<br>
	`transfer()` function checks if the sale is Paused or not, but `transferFrom()` doesn't have same check. Do you need to check it? 

- **ArrayLimit**<br>
	`uint256 public arrayLimit = 20;`<br>uint256 could be replaced with uint8.

- **Function overload without reason**<br>
	```
	function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
	    return super.transferFrom(_from, _to, _value);
	  }
	```
	This function overload doesn't change anything and just call super function. Consider to remove it. 

- **transver vs withdraw**<br>Push(transfer) approach is chosen, which is not a [best practice](https://ethereum-contract-security-techniques-and-tips.readthedocs.io/en/latest/recommendations/#favor-pull-over-push-for-external-calls).  	

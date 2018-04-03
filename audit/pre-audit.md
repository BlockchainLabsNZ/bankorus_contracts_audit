# Bankorus pre-audit

<br>

## Questions

- **RBAC and roles**
<br>Now only one function of RBAC.sol is used: `onlyAdmin()`. Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner? 
It will be clearer and cheaper.


<br>

## Suggestions

	
- **1. Self-made checks vs standard modifiers**, [Line 19](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L19):<br>
	consider to replace 
	
	```
	if (!paused) {
      require(msg.sender == owner);
    }
	```
	to standard modifiers `whenNotPaused()` and `onlyOwner()` from the Pausable.sol and Ownable.sol respectively.

- **2. Checks if sale is Paused**:<br>
	`transfer()` function checks if the sale is Paused or not, but `transferFrom()` doesn't have same check. Do you need to check it? 
	
- **3. ArrayLimit**, [Line 11](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L11):
	
	`uint256 public arrayLimit = 20;`<br>uint256 could be replaced with uint8.

- **4. Function overload without reason**<br>

	```
	function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
      return super.transferFrom(_from, _to, _value);
	}
	```
	
	This function overload doesn't change anything and just call super function. Consider to remove it. 

- **5. Function allowance() has a mistake**, [line 45](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L45):
	
	```
  function allowance(address _spender) public view returns (uint256) {
      return super.allowance(msg.sender, _spender);
  }
	```

	Overloaded `allowance()` send the address of the contract (`msg.sender`), not the contract owner. It is assumed to approve token transfer from the contract address, which is nonsense, because tokens was minted to the contract owner, not to the contract. 

	
- **6. transfer vs withdraw**<br>Push(transfer) approach is chosen, which is not a [best practice](https://ethereum-contract-security-techniques-and-tips.readthedocs.io/en/latest/recommendations/#favor-pull-over-push-for-external-calls).  	

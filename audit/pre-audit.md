# Bankorus pre-audit suggestions

<br>

- **0. No Transfer() event fired**, [Line 13](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L13), bankorus.sol:

	```
  	function bankorus(uint256 _totalSupply) public {
	    totalSupply_ = _totalSupply * 10 ** uint256(decimals);
	    balances[owner] = totalSupply_;
	}
	```
	There is no Transfer() event from the zero address when the tokens are created which is required by token tracking software like Etherscan.io. See line 35 of the MintableToken.sol for example.

- **1. Self-made checks vs standard modifiers**, [Line 19](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L19), bankorus.sol:<br>
	consider to replace 
	
	```
	if (!paused) {
      require(msg.sender == owner);
    }
	```
	to standard modifiers `whenNotPaused()` and `onlyOwner()` from the Pausable.sol and Ownable.sol respectively.
	
- **2. Anyone can transfer tokens even after pause() function has been called**, [Line 18](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L18), bankorus.sol:

	```
  	function transfer(address _to, uint256 _value) public returns (bool success) {
    	  if (!paused) {
            require(msg.sender == owner);
    	  }
          return super.transfer(_to, _value);
  	}
	```
	This function in its current state allows for transfers to take place by any token holder while tokens are paused.

	One possible solution would be to change `if (!paused) {` to `if (paused) {`

	See `pause()` in block [6688132](https://kovan.etherscan.io/tx/0x248e80205db524fe8af214bbcda4f58eb2550fa9e344b875416b76f491f84eac). 
Subsequently see `transfer()` in block [6688268](https://kovan.etherscan.io/tx/0xefba4b037a0af91a71b459313f7355086574fb976cc989df22433dc964b287e0).
	
- **3. Checks if sale is Paused**:<br>
	`transfer()` function checks if the sale is Paused or not, but `transferFrom()` doesn't have same check. Do you need to check it? 

- **4. Standard transfer() function doesn't check for allowance** , [line 22](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L22), bankorus.sol:

	```
	    return super.transfer(_to, _value);
	```
	    
	Standard  ERC20 `transfer()` function from OpenZeppelin framework (BasicToken.sol) doesn't check for allowance. If you want check allowance before sending BKT use `transferFrom()`.

- **5. Function overload without reason**, [line 25](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L25), bankorus.sol:<br>

	```
	function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
      return super.transferFrom(_from, _to, _value);
	}
	```
	
	Calls the `transferFrom()` function of the base contract, without any changes. 
	You can remove this code and just call the original function from the base contract.

- **6. Function allowance() has a mistake**, [line 45](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L45), bankorus.sol:
	
	```
  function allowance(address _spender) public view returns (uint256) {
      return super.allowance(msg.sender, _spender);
  }
	```

	Overloaded `allowance()` send the address of the contract (`msg.sender`), not the contract owner. It is assumed to approve token transfer from the contract address, which is nonsense, because tokens was minted to the contract owner, not to the contract. 

	
- **7. RBAC and roles** [line 34](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/cbba53880d3b26e37f6c3b0840b14034ca4159d3/contracts/bankorus.sol#L34), bankorus.sol:

	```
	   function transferToAddresses(address[] _addresses, uint256[] _values) onlyAdmin public returns (bool success) {
	      ...
	   }
  	```

	Now only one function of RBAC.sol is used: `onlyAdmin()`. Why not to use standard approach with `onlyOwner` modifier and multisig account as an Owner? It will be clearer and cheaper.

- **8. transfer vs withdraw**<br>Push(transfer) approach is chosen, which is not a [best practice](https://ethereum-contract-security-techniques-and-tips.readthedocs.io/en/latest/recommendations/#favor-pull-over-push-for-external-calls).  	

- **9. companycoin.py - run the script**<br>`self.endpoint.eth.enable_unaudited_features()` should be added before the line that builds transaction in order to run the script.   	

- **10. companycoin.py - multiple addresses**<br>`eth.getTransactionCount` returns the same number for the the same block. To be able run the script multiple times without waiting for the next block it is necessary to change the way of getting unique nonce for every built transaction. 



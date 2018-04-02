pragma solidity ^0.4.18;

import 'zeppelin-solidity/contracts/token/ERC20/MintableToken.sol';
import 'zeppelin-solidity/contracts/lifecycle/Pausable.sol';
import 'zeppelin-solidity/contracts/ownership/rbac/RBAC.sol';

contract bankorus is MintableToken, Pausable, RBAC {
  string public name = "Bankorus";
  string public symbol = "BKT";
  uint8 public decimals = 18;
  uint256 public arrayLimit = 20;

  function bankorus(uint256 _totalSupply) public {
    totalSupply_ = _totalSupply * 10 ** uint256(decimals);
    balances[owner] = totalSupply_;
  }

  function transfer(address _to, uint256 _value) public returns (bool success) {
    if (!paused) {
      require(msg.sender == owner);
    }
    return super.transfer(_to, _value);
  }

  function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
    return super.transferFrom(_from, _to, _value);
  }

  function setArrayLimit(uint256 _newLimit) onlyAdmin public {
    require(_newLimit > 0);
    arrayLimit = _newLimit;
  }

  function transferToAddresses(address[] _addresses, uint256[] _values) onlyAdmin public returns (bool success) {
    require(_addresses.length == _values.length);
    require(_addresses.length <= arrayLimit);

    uint8 i = 0;
    for (i; i < _addresses.length; i++) {
      require(transferFrom(msg.sender, _addresses[i], _values[i]));
    }
    return true;
  }

  function allowance(address _spender) public view returns (uint256) {
    return super.allowance(msg.sender, _spender);
  }

}

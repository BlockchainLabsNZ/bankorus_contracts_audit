pragma solidity ^0.4.18;

import 'zeppelin-solidity/contracts/token/ERC20/MintableToken.sol';
import 'zeppelin-solidity/contracts/lifecycle/Pausable.sol';
import 'zeppelin-solidity/contracts/ownership/rbac/RBAC.sol';

contract bankorus is MintableToken, Pausable, RBAC {
  string public name = "Bankorus";
  string public symbol = "BKT";
  string public roleFrozen = "FROZEN";
  uint8 public decimals = 18;

  function bankorus(uint256 _totalSupply) public {
    totalSupply_ = _totalSupply * 10 ** uint256(decimals);
    balances[owner] = totalSupply_;
  }

  function transfer(address _to, uint256 _value) public returns (bool success) {

    require(!hasRole(_to, roleFrozen));
    require(!hasRole(msg.sender, roleFrozen));

    if (!paused) {
      require(msg.sender == owner);
    }
    return super.transfer(_to, _value);
  }

  function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
    require(!hasRole(_to, roleFrozen));
    require(!hasRole(msg.sender, roleFrozen));

    return super.transferFrom(_from, _to, _value);
  }

  function frozen(address target) public {    
    checkRole(msg.sender, ROLE_ADMIN);
    addRole(target, roleFrozen);
  }

  function unFrozen(address target) public {
    checkRole(msg.sender, ROLE_ADMIN);
    removeRole(target, roleFrozen);
  }

  function allowance(address _spender) public view returns (uint256) {
    return super.allowance(msg.sender, _spender);
  }

}

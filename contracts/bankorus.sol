pragma solidity ^0.4.18;

import 'zeppelin-solidity/contracts/token/ERC20/MintableToken.sol';
import "zeppelin-solidity/contracts/math/SafeMath.sol";

contract Bankorus is MintableToken {

  using SafeMath for uint256;

  string public name = "Bankorus";
  string public symbol = "BKT";
  uint8 public decimals = 18;
  uint256 public arrayLimit = 20;
  uint256 public totalAllocated = 0;
  bool public allow = true;

  event LogAllow(bool allow);

  function Bankorus(uint256 _totalSupply) public {
    totalSupply_ = _totalSupply * 10 ** uint256(decimals);
    balances[owner] = totalSupply_;
    Transfer(address(0), owner, totalSupply_);
  }

  function transfer(address _to, uint256 _value) public returns (bool success) {
    if (allow == false) {
      require(msg.sender == owner);
    }

    require(super.transfer(_to, _value));
    return true;
  }

  function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
    if (allow == false) {
      require(msg.sender == owner);
    }
    return super.transferFrom(_from, _to, _value);
  }

  function setArrayLimit(uint256 _newLimit) onlyOwner public {
    require(_newLimit > 0);
    arrayLimit = _newLimit;
  }

  function transferToAddresses(address[] _addresses, uint256[] _values) onlyOwner public returns (bool success) {
    require(_addresses.length == _values.length);
    require(_addresses.length <= arrayLimit);

    if (allow == false) {
      require(msg.sender == owner);
    }

    uint256 i = 0;
    for (i; i < _addresses.length; i++) {
      require(super.transfer(_addresses[i], _values[i]));
      totalAllocated = totalAllocated.add(_values[i]);
    }
    return true;
  }

  function changeAllow(bool newValue) onlyOwner public {
    allow = newValue;
    LogAllow(newValue);
  }

  function grandTotalAllocated() public view returns (uint256) {
    return totalSupply_.sub(totalAllocated);
  }

}

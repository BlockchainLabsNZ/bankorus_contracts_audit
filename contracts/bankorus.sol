pragma solidity ^0.4.18;

import 'zeppelin-solidity/contracts/token/ERC20/MintableToken.sol';
import 'zeppelin-solidity/contracts/lifecycle/Pausable.sol';
import 'zeppelin-solidity/contracts/ownership/rbac/RBAC.sol';


/**
 * @title BankorusToken
 * @dev ERC20 Bankorus Token (BKT)
  *
 * All initial BKT tokens are assigned to the creator of
 * this contract.
 *
 */


contract BankorusToken is MintableToken, Pausable, RBAC {
    string public name = "Bankorus";    // Set the token name for display
    string public symbol = "BKT";        // Set the token symbol for display
    string public roleFrozen = "FROZEN";  // Set the initial RBAC state to “FROZEN”
    uint8 public decimals = 18;          // Set the number of decimals for display

    // initialize balances
    mapping (address => uint256) balances;


    /**
     * @dev BankorusToken Constructor
     * Runs only on initial contract creation.
     */

    function BankorusToken (uint256 initialSupply) public {
        totalSupply_ = totalSupply * 10 ** uint256(decimals);
        balances[owner] = totalSupply_;  // Creator address is assigned all initial tokens
        contractAddress = this;
        Transfer(0x0, owner, totalSupply_); // Send initial supply of tokens to creator
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
        require(paused);

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


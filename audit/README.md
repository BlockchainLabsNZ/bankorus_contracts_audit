# Bankorus Token Contract Audit Report

## Preamble
This audit report was undertaken by **BlockchainLabs.nz** for the purpose of providing feedback to **Bankorus**.

It has subsequently been shared publicly without any express or implied warranty.

Solidity contracts were sourced from the Ethereum mainnet at [BlockchainLabsNZ/bankorus_pre](https://github.com/BlockchainLabsNZ/bankorus_pre)

We would encourage all community members and token holders to make their own assessment of the contracts.

## Scope
The following contracts were subject for static, dynamic and functional analyses:

- [Bankorus.sol](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/contracts/bankorus.sol)


## Focus areas
The audit report focuses on the following key areas, although this list is not exhaustive.

### Correctness
- No correctness defects uncovered during static analysis?
- No implemented contract violations uncovered during execution?
- No other generic incorrect behaviour detected during execution?
- Adherence to adopted standards such as ERC20?

### Testability
- Test coverage across all functions and events?
- Test cases for both expected behaviour and failure modes?
- Settings for easy testing of a range of parameters?
- No reliance on nested callback functions or console logs?
- Avoidance of test scenarios calling other test scenarios?

### Security
- No presence of known security weaknesses?
- No funds at risk of malicious attempts to withdraw/transfer?
- No funds at risk of control fraud?
- Prevention of Integer Overflow or Underflow?

### Best Practice
- Explicit labeling for the visibility of functions and state variables?
- Proper management of gas limits and nested execution?
- Latest version of the Solidity compiler?

## Analysis Reports

- [Functional Analysis](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/audit/functional-tests.md)
- [Dynamic Analysis](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/audit/dynamic-analysis.md)
- [Gas Consumption](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/audit/gas-consumption-report.md)
- [Test Coverage](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/audit/test-coverage.md)

## Issues

### Severity Description
<table>
<tr>
  <td>Minor</td>
  <td>A defect that does not have a material impact on the contract execution and is likely to be subjective.</td>
</tr>
<tr>
  <td>Moderate</td>
  <td>A defect that could impact the desired outcome of the contract execution in a specific scenario.</td>
</tr>
<tr>
  <td>Major</td>
  <td> A defect that impacts the desired outcome of the contract execution or introduces a weakness that may be exploited.</td>
</tr>
<tr>
  <td>Critical</td>
  <td>A defect that presents a significant security vulnerability or failure of the contract across a range of scenarios.</td>
</tr>
</table>

### Minor

- **LogAllow event missing parameter** - `Best practice`
<br>The LowAllog event is currently not logging anything, see here on #L56 ... [View on GitHub](https://github.com/BlockchainLabsNZ/bankorus_pre/issues/3)

- **uint256 can be used in replacement of uint8 to save gas** - `Gas Optimization`
<br>We recommend using uint256 instead of uint8 on line #L47 as this will cost less gas. ... [View on GitHub](https://github.com/BlockchainLabsNZ/bankorus_pre/issues/2)

- **If statement is redundant because onlyOwner has been used to transferToAddresses()**
<br>This if statement checks whether the msg.sender is the contract owner. But this function, transferToAddresses(), has onlyOwner in the declaration, which makes this if statement redundant ... [View on GitHub](https://github.com/BlockchainLabsNZ/bankorus_pre/issues/4)

### Moderate

- None found

### Major

- None found

### Critical

- None found

## Observations
The Bankorus team will use a Python script to distribute tokens to an array of addresses after [`Bankorus.sol`](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/contracts/flat_bankorus.sol) has successfully been deployed.  The script [`companycoin.py`](https://github.com/BlockchainLabsNZ/bankorus_pre/blob/master/scripts/companycoin.py) is currently not ready for production as it is only being used with sending tokens to a single address, and will need to be adapted to be compatible with distributing tokens to multiple addresses. It is also possible that this script will need adapting to support multiple token values being sent as well. 

## Conclusion

Overall we have not identified any potential vulnerabilities. This contract has a low level risk of BKT being hacked or stolen from the inspected contracts.

___

### Disclaimer

Our team uses our current understanding of the best practises for Solidity and Smart Contracts. Development in Solidity and for Blockchain is an emerging area of software engineering which still has a lot of room to grow, hence our current understanding of best practices may not find all of the issues in this code and design.

We have not analysed any of the assembly code generated by the Solidity compiler. We have not verified the deployment process and configurations of the contracts. We have only analysed the code outlined in the scope. We have not verified any of the claims made by any of the organisations behind this code.

Security audits do not warrant bug-free code. We encourage all users interacting with smart contract code to continue to analyse and inform themselves of any risks before interacting with any smart contracts.

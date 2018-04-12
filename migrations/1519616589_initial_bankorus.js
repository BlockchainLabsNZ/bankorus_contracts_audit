var bk = artifacts.require("./Bankorus.sol")

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(bk, 1000);
};

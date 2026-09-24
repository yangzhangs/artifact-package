### Generating the fixed peers json

Before any release, we should generate a fresh json with known peers for each network. We usually get the data of alive peers from DNS seeds ran by different people in the ecosystem. We have a tool that helps generating the json, to generate it, just use:

```bash
curl https://bitcoin.sipa.be/seeds.txt.gz | gzip -dc > seeds_main.txt
curl https://signet.achownodes.xyz/seeds.txt.gz | gzip -dc > seeds_signet.txt
curl https://testnet.achownodes.xyz/seeds.txt.gz | gzip -dc > seeds_test.txt
curl https://testnet4.achownodes.xyz/seeds.txt.gz | gzip -dc > seeds_testnet4.txt

./contrib/make_seeds.py seeds_main.txt crates/floresta-wire/seeds/mainnet_seeds.json
./contrib/make_seeds.py seeds_signet.txt crates/floresta-wire/seeds/signet_seeds.json
./contrib/make_seeds.py seeds_test.txt crates/floresta-wire/seeds/testnet_seeds.json
./contrib/make_seeds.py seeds_testnet4.txt crates/floresta-wire/seeds/testnet4_seeds.json
```

If you have any questions, related to this process or the codebase in general. Don't hesitate to reach us out, we are happy to help newcomers in their amazing journey. Overall, have fun :)

LLM and AI Agent Usage
----------------------

This project does not accept contributions from AI bots. All PRs that appear to come from such accounts will be closed.

Patches created by LLMs and AI agents are also viewed with suspicion unless a human has reviewed them.
All LLM generated patches MUST have text in the git log and in the PR description that indicates the
patch was created using an LLM. First time contributions by way of LLM generated patches are not welcome.

Thanks for your time, please be respectful of ours.

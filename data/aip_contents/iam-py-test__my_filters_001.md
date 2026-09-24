## Contributing
Please contribute. _Please_. Maintaining a filterlist is not an easy thing and I can only spend a finite amount of time on maintaining a filterlist. I welcome contributions, even if they are just to fix a typo or remove a redundant entry.

#### Rules
Please be respectful to other people even if their beliefs or opinions differ from yours. <br/>
Before opening an issue, please be sure there is not another issue open about the exact same thing. If there is, you can add your opinion or fix to that issue's comments. <br/>
If your issue was closed as `invalid`, please avoid immediately opening another issue without correcting the problem. Doing so will result in that issue being closed as well. Before opening an issue, please check https://github.com/iam-py-test/my_filters_001/blob/main/wiki/incompatible.md to ensure the issue is not a conflict. <br/>
Please understand that I am only one person, and that I will not be able to respond to or correct your issue immediately. If something is important, please @ reference me in that issue and I will check it out.<br/>
Please follow the [GitHub Community Guidelines](https://docs.github.com/en/github/site-policy/github-community-guidelines#what-is-not-allowed) or else you will be banned from this Repo and reported to GitHub. Internet pranks - including rickrolling - are prohibited and may result in a ban after repeated violations. <br/><br>

[Please see my general AI policy for my projects for information on usage of AI](https://github.com/iam-py-test/iam-py-test/blob/main/ai.md).

Please open a pull request or issue instead of commenting on commits, as I am unlikely to see commit comments, but regularly check for issues.<br>

### MV3 note
My lists do not support MV3.

### Note about Internet Explorer
I do not - and never will - support Microsoft's Internet Explorer, as it is a complete mess, and isn't even maintained. I recommend you switch to any maintained browser, as Microsoft won't fix any issues with IE, and it is therefore broken and insecure.

### Opera
Opera prevents extensions from accessing search result pages. To allow access, open opera://extensions/ and check the "allow access to search page results" option. Thanks to the uBo team for informing me (and other people) of this. 

### kiwi browser
Kiwi browser [is not supported by uBlock Origin](https://github.com/uBlockOrigin/uBlock-issues/issues/2791), and thus my filterlists. Be aware that Kiwi browser [disables extensions](https://www.reddit.com/r/uBlockOrigin/comments/10xntsr/comment/j7teo9p/) on [a long list of domains](https://github.com/kiwibrowser/src/blob/c51d640a8e984ff0fb24049c53a7ed4e458775ef/extensions/browser/api/web_request/web_request_permissions.cc#L167). Note that this also includes **any** domain containing `bing.com`, `search.yahoo.`, and some other tokens, meaning extensions may be disabled on other websites (such as malware and scam sites).
For this reason, [alleged privacy issues](https://github.com/Tobi823/ffupdater/issues/35), and [the lack of frequent updates](https://github.com/kiwibrowser/src.next/commits/kiwi) ([including slow response times to vulnerabilities](https://github.com/kiwibrowser/src.next/issues/1001)), I would recommend against using this browser.

### Yandex
Yandex Browser is not supported by uBlock Origin (I do not know about other content blockers), [and is known to be problematic](https://github.com/uBlockOrigin/uBlock-issues/issues/2627). Any issues which can not be reproduced in Chrome, Edge, or Firefox will have to be investigated by you.

## Extensions which confict with uBlock Origin

### Any other content filter/ad blocker
Only use one content filter/ad blocker at a time, as using more than one will result in conflicts.

### Malwarebytes Browser Guard
Blocks ads/trackers by default.
To disable: Click the Malwarebytes Browser Guard icon (not the icon for the Malwarebytes program), click the gear icon, then turn off _Ads/Trackers_.
[It seems Malwarebytes may still confict with YouTube even with this disabled.](https://github.com/uBlockOrigin/uAssets/issues/19976#issuecomment-1762785505)

---

# Standalone AI policy file

# iam-py-test's AI policy

Except where otherwise noted, this is the AI policy for all of my projects. I figured I would put it here rather than duplicate it in every repository. By opening an issue or pull request, or contributing to any of my repositories in any form, you agree to comply with this policy.

&emsp;For the purposes of this policy, artificial intelligence refers specifically to generative artificial intelligence. Generative artificial intelligence is a type of AI which learns patterns from its training data, and uses that to generate new data - such as images or code - based on that training data. Code created by generative artificial intelligence frequently contains security vulnerabilities and bugs. Text from generative artificial intelligence frequently contains errors and misrepresentation of sources. Generative artificial intelligence is also bad at handling context, meaning it is vulnerable to taking misinformation, satire, roleplay, fiction, and suggestions as fact. Furthermore, for people learning coding, [AI use hinders learning](https://infosec.exchange/@iampytest1/116035779997788263). For these reasons and many others, I have chosen to greatly restrict usage of AI, stopping short of a full ban *for now*.<br><br>

&emsp;Submitting AI generated issues or code is forbidden; all issue reports and code must be entirely written by real people. If you are going to use AI for research, which I recommend against, such use *must* be disclosed and any information from the AI must be verified using independent sources. This includes citing articles, social media posts, or any other content generated with AI. Any issue report or code suspected to be AI will be subject to extended review, and may be rejected. Use of AI for purposes of translation is permitted, but must be disclosed, and a copy of the text in the original language should be provided when possible.

&emsp;Contributors must seek approval before using any program to create issues or pull requests automatically or en masse. Any account used to submit issue reports or pull requests en masse in an automated manner will be banned. Use of accessability tools obviously does *not* count as submitting an issue in an automated manner, as there is still a real person creating the issue. Using a bot to iterate through every newly added domain in [ThreatFox](https://threatfox.abuse.ch/) and submit an issue report for each one *does* count, as that would flood the issue tracker with hundreds of issues.

&emsp;By default, GitHub and VSCode (both owned by Microsoft) offer the option to generate a commit message using AI. All commit messages used in contributions to this repository must be written by humans, as to ensure they are clear and accurate, since AI may not understand the context and purpose of a change. I recommend turning off these features.<br>

AI bots are not permitted to contribute to these repositories, as their contributions are frequently low quality.<br>

Any permitted AI use must be disclosed. This includes *but is not limited to* disclosing the following information:
- Name and version of the model
- Links to sources cited by the model, if any
- A brief description of the prompts used
- Indicating what parts of the issue/PR are based on the AI output

Contributors may be asked to disclose additional information, including prompts and full AI output. Contributors who fail to disclose this information may face extended review or rejection of issue reports and pull requests.

No provision of this policy shall preclude submitting AI generated content (i.e. AI generated malware, scam sites, etc) made by threat actors as evidence.

Any code, image, or other data deliberately designed to poison AI training data or otherwise interfere with AI will be considered malware, and any contributor knowingly submitting such data will be subject to an investigation and possible permanent ban. This applies to any contributor attempting to add any other form of malware to any project, excluding the submission of malware as evidence.

### Violations
These are general rules about dealing with violations, and I reserve the right to change them at any time without advance notice and comment.

&emsp;Issue reports and pull requests suspected to be generated with AI may be subject to extended review, or rejected.
Suspected AI agents and bots may be asked to provide proof of legitimacy; how this will work depends on the situation. Confirmed AI agents and bots may be banned. AI agents which fail to disclose their nature, or participate in disruptive behavior, may be reported to GitHub or subject to an official investigation.

Future contributions from violators may be subject to extended review. Repeat violators may be temporarily banned, and eventually permanently banned. Ban evasion may result in the violators' alt accounts being permanently banned.

### Legal notes

This policy is copyleft 2026, no rights reserved. No portion of this policy was generated using artificial intelligence.<br>
This policy does not supercede GitHub's terms of service and policies, or national and international laws.<br>
If any section of this policy is held to be void or otherwise unenforceable, all other sections shall remain in effect.


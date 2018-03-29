# Where do we stand as a community on GitHub?

Recently Github designed a survey to gather high quality and novel data on open source software development practices and communities. They published their DataSet online and conducted a survey on its users to determine how we, as users, creaters, maintainers are doing as a community. The results are an open data set about the attitudes, experiences, and backgrounds of those who use, build, and maintain open source software.

They collected responses from 5,500 randomly sampled respondents sourced from over 3,800 open source repositories on GitHub.com, and over 500 responses from a non-random sample of communities that work on other platforms.

In this post, I'll sumarize the insights that were obtained by analysing the data and important conclusions from it.

## Documentation is crucial, and we _know_ that! Still we overlook it.

Documentation helps orient newcomers: how to use a project, how to contribute back, the terms of use and contribution, and the standards of conduct in a community. Improving that documentation is an impactful way to contribute back to open source.

- Incomplete or outdated documentation is a pervasive problem, observed by 93% of respondents, yet 60% of contributors say they rarely or never contribute to documentation. **When you run into documentation issues, help a maintainer out and open a pull request that improves them.**
In my personal experience and what I have heard from my peers, if somebody is new to open source, or is just starting out on making technical contributions to projects they haven't had any acquaintance with, well-formed and comprehensible documentation is very important. It is their first step to get a hang of what's going on in the community. And if this basic requirement fails to satisfy, new-comers may become discouraged and don't feel at home with the project and end up discountinuing it. Which has got two most unwanted consequences:
  - New-comers are discouraged, and this might lead to increased apprehension and hesitation to start out with contributing to FOSS. They might never get out this alienation.
  - The growth of the community could be hampered. If a community cannot manage to attract a set of good contributors who can grow the project, it is most likely to fail at some point.

- Many people participate in open source on the job, where confidence in the terms of use is critical. Unsurprisingly, **licenses are by far the most important type of documentation to both users and contributors** : 64% say an open source license is very important in deciding whether to use a project, and 67% say it is very important in deciding whether to contribute.
- **Documentation helps create inclusive communities**. Documentation that clearly explains a project's processes, such as contributing guides and codes of conduct, is valued more by groups that are underrepresented in open source, like women.
- Nearly a quarter of the open source community reads and writes English less than ‘very well.’ **When communicating on a project, use clear and accessible language for people who didn’t grow up speaking English, or read less-than-fluently.**

![Alt Text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Github%20Open%20Source%20Analysis/Plots/p1.PNG)

## Toxic interactions exist. They affect the project in the most unwanted manner.

Open source brings together people from all over the world, which can lead to conflicts. While serious incidents are rare, the public nature of open source makes negative interactions highly visible.

As a result, discouraging effects can extend far beyond the individuals directly involved. Setting positive expectations of behavior, and addressing negative incidents quickly, can improve contributor retention and collaboration.

- 18% of respondents have personally experienced a negative interaction with another user in open source, but 50% have witnessed one between other people. It's not possible to know from this data whether the gap is due to people who experienced such interactions leaving open source, or broad visibility of incidents. Either way, negative interactions impact many more than the immediate participants, so **address problematic behavior swiftly, politely, and publicly, to send a signal to potential contributors that such behavior isn’t typical or tolerated.**
- By far, the most frequently encountered bad behavior is **rudeness** (45% witnessed, 16% experienced), followed by **name calling** (20% witnessed, 5% experienced) and **stereotyping** (11% witnessed, 3% experienced). More serious incidents, such as **sexual advances**, **stalking**, or **doxxing** are each encountered by less than 5% of respondents and experienced by less than 2% (but cumulatively witnessed by 14%, and experienced by 3%).
- **Negative experiences have real consequences for project health**. 21% of people who experienced or witnessed a negative behavior said they **stopped contributing** to a project because of it, and 8% started working in private channels more often.
- **Tooling** that allows people to address problematic behavior directly is the most effective way of addressing harassing behavior. Blocking a user was reported to be more effective than enforcement from third parties like maintainers, ISPs/hosting services, or even legal resources. 

**Give people tools to protect themselves.**

![Alt Text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Github%20Open%20Source%20Analysis/Plots/p2.PNG)

## How divere and inclusive are we on FOSS platforms?

Open source provides the basis for technology that serves the entire world. In some ways, the diversity of the user base is reflected or even exceeded among open source contributors, but in other ways there are still huge gaps in representation.

Improving project accessibility could help unlock many more contributions, ensure that technology serves a comprehensive set of use cases and needs, and contribute to better representation in technology jobs.

- The gender imbalance in open source remains profound: 95% of respondents are men; just 3% are women and 1% are non-binary. Women are about as likely as men (68% vs 73%) to say they are very interested in making future contributions, but less likely to say they are very likely to actually do so (45% vs 61%).
- Along other dimensions, representation is stronger: 1% of respondents identify as transgender (including 9% of women in open source), and 7% identify as lesbian, gay, bisexual, asexual, or another minority sexual orientation. 26% are immigrants (from and to anywhere in the world) and 16% are members of ethnic or national minorities in the country where they currently live.
- Women are more likely than men to encounter language or content that makes them feel unwelcome (25% vs 15%) as well as stereotyping (12% vs 2%) and unsolicited sexual advances (6% vs 3%). Unsurprisingly, women are also more likely than men to seek out help directly (29% vs 13%) from people they already know well (22% vs 6%), rather than ask for help from strangers in a public forum or channel. **Collaboration between strangers is one of open source's most remarkable aspects: strive to build a community where everyone feels welcome to participate.**
- Half of contributors say that their open source work was somewhat or very important in getting their current role. **Open source work helps people build their professional reputation. Improving contributor representation can help create a more representative tech sector overall.**

![Alt Text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Github%20Open%20Source%20Analysis/Plots/p3.PNG)

## Using and contributing to open source often happens on the job

Open source is widely used in professional contexts. The majority of employed respondents use and contribute to open source at work, and many people cite their open source work as important to getting their current job.

However, a significant number say that their employers’ official policies and IP agreements are unclear regarding what is allowed, and under what terms. Businesses play a key role in open source by subsidizing open source work from employees, so creating and communicating clear policies can encourage more frequent, regular contributions.

- 70% of respondents are employed full- or part-time, and 85% of those contribute in some way to software development (e.g. developers, designers, other roles in the software industry) frequently or occasionally in their main job.
- Virtually all (94%) of those who are employed use open source at least sometimes in their professional work (81% use it frequently), and 65% of those who contribute back do so as part of their work duties.
- Most report that their employers accept or encourage use of open source applications (82%) and dependencies in their code base (84%), but some said their employers’ policies on use of open source are unclear (applications: 13%, dependencies: 11%).
- Nearly half say their employer’s IP policy allows them to contribute to open source without permission (47%), and another 12% can do so with permission. **However, 28% say their IP policy is unclear, and another 9% are not sure about how their IP agreement treats open source contributions.**

![Alt Text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Github%20Open%20Source%20Analysis/Plots/p4.PNG)

## Open source is the default when choosing software

Security matters when choosing new software, and most users believe that open source is more secure, on average, than proprietary software. When it comes to stability or user experience, users are less convinced of the superiority of open source. Even so, most are committed to open source, and always seek out open source options.

- Open source’s comparative advantage is in security: security is among the the most important features when using any kind of software (86% extremely or very important). **Security is the only dimension that was asked about where a majority of users believe that open source software is usually better than proprietary software (58%).**
- Users also care about stability and user experience (88% and 75% extremely or very important, respectively) when it comes to choosing software, but on these dimensions fewer were convinced of open source’s superiority: only 36% said user experience tends to be better, and 30% said that open source software is generally more stable than proprietary options.
- Despite these tradeoffs, users still prefer open source. **72% say that they always seek out open source options when evaluating new tools.**

![Alt Text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Github%20Open%20Source%20Analysis/Plots/p5.PNG)


#### Here come the end of my story containing the summarised details of the survey conducted by GitHub.

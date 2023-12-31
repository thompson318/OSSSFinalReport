<!-- GitHub Corner -->
  <a href="https://github.com/thompson318/OSSSFinalReport" class="github-corner" aria-label="View source on GitHub"><svg width="60" height="60" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>


# Opensource tools for Encouraging Sustainability in Diverse Multi-Library Projects

## Authors: 
[Stephen Thompson](https://profiles.ucl.ac.uk/23126-stephen-thompson),
[Yagmur Idil Ozdemir](https://iris.ucl.ac.uk/iris/browse/profile?upi=YIOZD16),
[Miguel Xochicale](https://scholar.google.co.uk/citations?hl=en&user=_M0fVVIAAAAJ),
[Tom Couch](https://iris.ucl.ac.uk/iris/browse/profile?upi=TCOUC69),
[Thomas Dowrick](https://profiles.ucl.ac.uk/42164-thomas-dowrick),
[Matthew J Clarkson](https://profiles.ucl.ac.uk/6821-matt-clarkson)

## Summary: What was the project about?
The project funded the ongoing development of the software sustainability dashboard for SciKit-Surgery and the creation of a broader template dashboard that anyone can use for their own projects. 

[SciKit-Surgery](https://github.com/SciKit-Surgery) brings together a set of libraries targeted to support research in image guided surgery. 
In September 2021 we presented SciKit-Surgery at [SeptembRSE](https://scikit-surgery.github.io/scikit-surgery-rse2021-poster/) and at WEISS's annual funder's review. We realised that although we intend to follow sustainable software best practice on our individual libraries we had no tool to enable us to track the status of all the libraries in the project. We couldn't find a ready made tool, so we made our own, a "Sustainable Software Dashboard". The dashboard was fit for purpose at the time, but had no auto update feature, so got out of date very quickly.  

## How has the project benefited our work?
The Open Source Software Sustainability funding enabled us to fund a research software engineer to improve the automation of the dashboard, so it now updates every 12 hours using Github actions. 

<a href="https://scikit-surgery.github.io/scikit-surgery-stats/" title="Click to go to the current SciKit-Surgery Dashboard"><img src="static/skdashboard.png" alt="The SciKit-Surgery Dashboard" width="60%"/></a> 
<figcaption>The updated SciKit-Surgery Dashboard, giving an immediate overview of the library status.</figcaption>

The updated dashboard enables us to see at a glance:

1. Where the software has grown (new libraries are added automatically).
2. Which libraries are gaining interest in the community (stars, forks).
3. Which libraries are gaining a collaborative developer base (contributions).
4. Which libraries are following best practice (documentation, CI testing).

With this knowledge we are much better placed to focus future development work and make a case for ongoing funding.  

## Outputs: What was accomplished?
In addition to automating the dashboard the team took the opportunity to engage with the research software engineering community to ask whether the dashboard could be more broadly useful, and if so what features were of most interest to the community.

<img src="static/rse_southeast.jpeg" alt="Idil presenting at RSE Southeast 2023" width="45%"/><img src="static/community-2.png" alt="Survey results on what people want from a dashboard" width="55%"/>
<figcaption>Idil leading a discussion on software sustainability and our dashboard features during <a href="https://doi.org/10.5281/zenodo.8337573">RSLondonSoutheast2023</a>. Photo thanks to Miguel.</figcaption>

Our presentation at RSLondonSoutheast gave us confidence that the dashboard was of wider interest to the community, so we developed a [template dashboard](https://github.com/SciKit-Surgery/sustainable-pkg-stats) enabling users to quickly create their own dashboard. We presented the template as part of a 90 minute workshop at RSECon23 in Swansea to an audience of around 30 research software engineers from academia and industry. You can find a full description of the workshop including slides, aims, and agenda [here](https://github.com/SciKit-Surgery/rsecon23-workshop41).

<img src="static/rsecon23.jpg" alt="Idil and Steve Presenting at RSECon23" width="45%"/><img src="static/sustain_dash-4.png" alt="Survey results on useful metrics" width="55%"/>
<figcaption>Idil and Steve leading our workshop on software sustainability and our dashboard template at <a href="https://doi.org/10.5281/zenodo.8337573">RSECon23</a>. Photo thanks to Miguel.</figcaption>

Participants at the workshop were able to use our template to create their own [dashboards](https://github.com/SciKit-Surgery/sustainable-pkg-stats/discussions/22) and participated in a discussion on what constitutes sustainable software and what features they would like to see on a dashboard.

Over the course of RSLondonSoutheast and RSECon23 we surveyed around 70 researchers and 
research software engineers from academia and industry. We asked them general questions about 
software sustainability and specific questions about our dashboard. We're still processing the results for full publication but in summary:

1. There was strong agreement among participants that the dashboard could "encourage good software practices in the ecosystem". 
2. There was good agreement among participants that the dashboard could be helpful for "showcasing for research fundraising and distribution".
3. The most popular metrics for understanding sustainability were; status of documentation, the package maintainability score from [Code Climate](https://codeclimate.com/), the status of continuous integration tests, and the date of the last update.

## Future work and long term impact.
The funding from ARC enabled us to develop our template and demonstrate its potential usefulness for the wider community. 
The template dashboard remains freely available at [https://github.com/SciKit-Surgery/sustainable-pkg-stats](https://github.com/SciKit-Surgery/sustainable-pkg-stats) along with instructions for its use. We're continuing to use it for SciKit-Surgery and engaging with the community to improve it and make it more widely applicable. 

The development of sustainable practice in research software engineering is a topic of growing interest and we intend to use the results of our work for a publication in the area of best practice for sustainability in software engineering.  

## Acknowledgements
This work was made possible by UCL's Advanced Research Computing Centre through the Open Source Software Sustainability funding scheme and the Wellcome/EPSRC Centre for Interventional and Surgical Sciences (WEISS) (203145Z/16/Z).

## References and data sources.
Ozdemir, Yagmur Idil, Xochicale, Miguel, & Thompson, Stephen. (2023). Design and discussion of a (reusable) Sustainability Dashboard of Open Source Tools (1.0). RSLondonSouthEast, London, UK. Zenodo. [https://doi.org/10.5281/zenodo.8337573](https://doi.org/10.5281/zenodo.8337573)

Ozdemir, Yagmur Idil, Xochicale, Miguel, & Thompson, Stephen. (2023). How to use and contribute to a software sustainability dashboard (1.0). RSE Conference 2023 (RSECon23), Swansea UK. Zenodo. [https://doi.org/10.5281/zenodo.8337480](https://doi.org/10.5281/zenodo.8337480)

[The Original Grant Proposal](https://github.com/thompson318/OSSSFinalReport/blob/392888a9b0b24e0eeb8e1351f33d570801fd5f2c/sks_osss_call.pdf)

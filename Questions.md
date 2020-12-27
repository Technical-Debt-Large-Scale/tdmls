The following questions were done to practioners: 

1. Q1. Can you tell us some background about this project and your job in this project?

This is a product that is a part of a charging system solution, that we talk about here. Charging system is a solution to do charging for mostly telecom operators, and probably for other ones also in the future. I'm the chief architect for one of the nodes in this charging system that is called SDP, service data point. And what that node is doing is storing the subscribers’ data and accounts in mainly those prepaid solutions.

*- Subscribers, you mean the users of the...?*

Yes, the users. I don't know if you know about those prepaid subscriptions that exist in mobile networks. You pay in advance for your usage. And when a prepaid subscriber uses his mobile, he contacts the charging system to know if he could afford to call or not, so we compare in what service here requests to our stored database if there is amount of the accounts so he could make his calls, send his messages or use his data. So that is what we are doing within the charging system, and SDP is the node within charging system that stores the accounts to simplify a little bit. 

*- To go out of the Ericsson technology is kind of a sub-problem, we can put like that right? SDP is like sub-season?*  

You mean within the SDP? If you mean the distributed system, you could say that. We have the term node within Ericsson and one node is a well defined function that describes its interfaces very well. But within these nodes, we also have distribution in processes and so on. So in one node a lot of different processes are running within internal communication but they are not so well described as external interfaces.

2. Q2. How long have you been working on this project?

With this product? Since it was launched in 1999, so it's eighteen years. Quite a long time.

3. Q3. What's your role and responsibility?

So the last years I have work ed as the chief architect, that means that I'm the team leader for the team that we called Software Architecture Team, the SAT team. That team is the one that takes requirements for new functionality. We are also responsible for keeping the architecture within the node, so we developed a new functionality. So we could maintain and handle the product in a long term perspective. So that is my role there, and to my help in this SAT team, we are, I think it's up to fifteen members now, that are helping me to control software architects and product owners that are working in new functionality.

4. Q4. Can you tell us about how is your understanding of code TD?
    
According to literature (Li:2015), there are eleven types of TD: 

* Requirements TD refers to the distance between the optimal requirements specification and the actual solution.
* Architectural TD refers to some improper architecture decisions that can harm internal quality aspects.
* Design TD is about making shortcuts with respect to detailed design.
* Code TD refers to poorly written code that does not follow best coding standards or coding practices.
* Test TD refers to taking shortcuts in testing (e.g., lack of unit tests or integration tests due to time budget).
* Build TD refers to the flaws in the build system or build process of a software system, which make the build overly complex and difficult.
* Documentation TD refers to any insufficient, incomplete, or outdated documentation of a software project (e.g., out-of-date architecture
* documentation and lack of code comments).
* Infrastructure TD refers to sub-optimal configuration of software and hardware that negatively affects the team’s ability to produce a product with good quality.
* Versioning TD is caused by improper source code versioning (e.g., unnecessary code forks ).
* Defect TD refers to defects, bugs, or failures detected in a software product.

 Do you cover all types in your product? Please elaborate.
 
 I would say that it could happen when you are forced to build the functionality faster than the timing for the functionality to deliver is more important than keeping the architecture, that could happen and that is actually the responsibility we have in the SAT team to limit that, because for every debt you are introducing when you're building new functionality or every shortcut you are doing will increase the maintenance cost in the future and it maybe cost more to introduce new functionality in the end. So if you start to increase that technical debt, then you will make the product maybe impossible to maintain in the long term, and also make it very very expensive to build a new functionality if you don't think about that from the beginning, so that is technical debt from my perspective.
 
5. Q5. How do you manage code debt in this project?

So how we manage to not get debt in product you mean or how we manage to get rid of debt?
*- I think management is for both, manage to avoid and to pay in the long run. Because as you said, sometimes it is necessary to overlook some issues because you have to deliver something. But you kind of in control of that thing that you can pay in the future. So management is about tracking, avoiding when possible and paying whenever you have you pay the technical debt.*
So to avoid it is actually to take the fight to make it right from the start, that is of course the most important thing. But that is maybe not always the case or maybe we didn't realize that this was a technical debt when we build a functionality, maybe that could come afterwards. So that means that we also have the possibility to fix this afterwards and then we could work, we call it node improvements. And we have a list of tasks that every developer working within organization could write node improvement, the NIP. That could be to refactor the software because it has been too deep technical depth in it or some other problems. So that is the way we have to handle technical debt in long term. We have a long list of proposals from the designers and other people of course, and that one we are trying to set them priority on which one is the most important, and when teams got gaps in their work, then we take work with those node improvements and I would say we are quite good at that and maybe fifteen to twenty node improvements have been there every year. So there we have possibilities.

6. Q6. So frequently who is involved in code TD management?

I would say everyone working with the project, but most responsibility I would say is within the SAT team and the architects working with the new functionality from a requirement perspective, but of course also to teams that are building to functionality, in tight cooperation with the SAT team. So when the program puts pressures, then both the teams and the SAT team should try to have the other side, qualities more important than time.

*- Is there any preference we got in the team that in general manages the NIPs? Or it's pretty much like, the team is in India, they are more interested in this part of SDP. And in general they will carry out the NIPs to fix those parts. So is there any relationship between people coding the new features, I mean PCs or whatever, and they have to take whole of the associated NIPs. Or you can say "No, I think those guys are free now” and eventually work with these NIPs now.*

I would say it's more like later description you did, because as you already know maybe, we have specific teams working with customization, we have specific teams working with design maintenance, another team working with new functionality. So that is our normal work. But for the NIPs, I would say it's more related to the teams that are free for one or another reason. If you have new functionality and there is some time gap between the built one and the new comes, so the teams have something to do with maybe in between. Also if we don't have so many TRs, then the design maintenance team could have some time to take care of the NIP list. And the same for customization of course. So that is spread all over the organization, the network.

7. Q7. What does your company use to manage code debt? I heard you use SonarQube

The tools? I would say that it's an internally implemented tool just to keep track on the list of improvements. So it's not a specific external tool. We have a wiki page. There everyone could come with proposals to write idea on the wiki page. What the proposal is: what is the the gain, what do you think the cost is of this improvement. And then we have a product community that I am steering. We have software architect, program manager and line manager in that group. Every second week we have a meeting. There we go through the new proposals and there we could either say "This is a proposal, it's OK", and we put it in the priority list, or we could reacted for some or other reason.
So that is just a simple wiki page to write proposals in and then I have a way of handling the priority in that. That is actually something I do myself, what do I think is the most prioritized one in the list that we have. So then I just have an Excel sheet that I put priority on that, and when a team comes and says "now we have free space, we would like to have something else to do", then I tell "here is the priority list, please choose from the most prioritized one and then go below". Maybe it's not feasible for the team, the one that is on the top, so then they go down, and then we agree this is the one you're taking, then they start with that one.

*- I presume that when you say that you have this wiki where people can submit proposals for NIPs, they probably use something as input, maybe the code reviews or something like that, to base their proposals.*

That's a very good question, what do they have as input to trigger a proposal. I would say it's just their brain. And sometimes I know that line management is triggering people to write NIPs. When they sit to talk with the line manager. "Have you written any NIP? Have you come with any proposal for new things?" So that is also a trigger. So they are there that they have that possibility. 

*- Motivated to do.*

Yes. So that could be one of them. But the best would be if for example, program will win and say that it's more important to do this one in time. Then, the best would be if they already at that stage say "we have a debt here" and then they immediately write the NIP. That happens also.

8. Q8. Let me show you a picture. There are eight management activities. Do you think you all cover these activities? We got these activities from a mapping paper, from the conversation now, I think you have the measurement, identification, prioritization, and repayment. Do you cover other activities?

Measurement. Yes of course, we have. We know how many we deliver each year.
Prioritization. Yes, we have talked about that.
Prevention. That we also discussed a little bit.
Monitoring. Of course we can not monitor the ones that is not written in a NIP, because there also exists dept that we don't know probably. And they'll not come into the list.

*- We can put like that, I would say, you are aware of some technical debts as long as you have the NIP. Because you can kind of feel that into and to map to. At least you are aware.*

Yes. Then we could count how many NIPs we have not done. That could be maybe account on. But not all the NIPs are technical debts. Sometimes we have NIPs of increased maintainability, I don't know, maybe that's not classified as a debt. I don't think so.

*- Maybe if we consider the old understanding of technical debt that it's a way to keep the software maintainable in the long run, and it's possible to evolve and so on. I think if you want to improve the maintainability, it means that there is something you can improve the software itself.*
Yes, that is maintainability as expert. But I thought about the maintainability of product out from the customer. So it's easier for them to handle the product out there. Tools to make it better to maintain. Traces, logs and all things like that. A lot of NIPs are in that area I think. So don't just measure the queue to understand what is the technical debt that we have. I would say more than half is the outer NIPs. Some of these maybe increase the functionality. So I don't think we have good monitoring possibility to understand what is the current technical debt we have.

*- Perhaps it's something that could be improved afterwards.*

Yes, and I think it's difficult to measure them.

*- What do you think about tools like SonarQube that provides statistic analysis of the code and calculates some values like technical debt.*
Yes, we have Sonar running, so I think we could use that much much more than we do. I could just look at myself, how often is it I looked into the results of this. It runs more or less daily, but how often do I look into this. Maybe we have the answer on technical debt there, at least part of it. So there I think we could improve, absolutely. We run the tool, but we could use it for much much more than we are doing. So we don't use that tool to understand our technical debt. 

What was the other ones? Repayment.

*- Repayment? I think you talked about that, refactoring and other stuff.*

Yeah. Representation/Documentation. What do we mean with that one?

*- I think there is a standardized way to deal with NIPs. They have to describe what is going into the NIP. I just ask because I am not sure. For PCs you have the SP right? So is there something similar to NIPs?*
You mean when we execute them? It depends a little bit on how big this NIP is. Sometimes it could be implemented. When we build functionality, we get the requirements from system management in something we call debug. And business use case study, all nodes like Rs(?), SDP, or the impact we'll write a B-suck(?) study that is the first analysis done for each and every node. And when that is done - that is mainly done in my sub-team, that B-suck(?) study - then the team against this to work with, they are writing an implementation description. That is how they resolve this functionality in the software. And I would say, some NIPs when passed through without any ID, if they are very small, for example the refactoring in the software. It is nothing that needs to be mentioned somewhere, so that could be done, and it doesn’t impact our product documentation and after. But if they are more complicated, we require them to write the implementation description, like we are having in the same way as other implementation descriptions.

*- Do you think documentation of the dept is a property? It’s like the guys identify the study they conducted. They analyzed many studies, I mean case studies, experience report, things like that. This is a way that people document technical debt, which should be NIPs here in Ericsson.*

So I mean it's not divided like this one, it's not so well structured as we have done here. 

*- Do you think it would be useful here to have something like that? Because it does not look very complicated I would say, this table.
Maybe I should show you how the NIP looks. So here is the list, the wiki page. Here you could create a new improvement. And here is the ones listed and here is the status of them. So, "updated" means they are in the priority list.*
So this is the list where we track them, and as you see that they have an ID. There is an improvement cost. The status, we have the priority, but I don't use the priority in this tool. Because I would like to have the list separated from the one that is very old, finished. So I just have the list with not done/not implemented improvements. And then it's the proposal text, the description, what to do? Pros and cons. There is a decision log in this graph, if it's rejected or not. If it's rejected, we have an argument on why it's rejected here. So this is more or less the description you have on your sheet I think.

*- Yeah, I think it’s similar to some extent. About that improvement costs, what does that mean?*

It is just a guess from the one who comes up with the proposal (measured in hours).

*- I would say that one of the things they will do is to after the interview here, they will match with the things of these old practice for technical debt.*

Where does that come from?

*- Some guys evaluated what is in literature plus reports about things in case study, they extracted things that are reported in those cases these people are using, and they list about this is like people document, repay, so on so far. It’s a research paper.*

Do you have any experience of customers or one using Sonar for using technical debt?

*- Yeah, I have two companies in Brazil that I have some relationship with, they use that, and in general it’s just as kind of a warn.

So they actually check the score from Sonar, but do they also write proposals from Sonar or?*

*- No, it’s the score, and this score is actually the aggregation of many metrics, like for instance duplicated codes and other things. Those guys just use that to triangulate. Because as you do here, the expert knowledge is more important here. The guys know that “Well, we kind of screwed up here. We have to fix these, otherwise it’s going to be hard to extend the software in these parts afterwards.”*

But how good is Sonar to identify technical debt with this score factor, because I could imagine that this factor maybe is not the truth every time.

*- That's a good question, and I don't have the answer, to be honest.*

So you are not just look at the score and try to decrease, but you don't improve the maintainability of the product, because you are doing the wrong things.

*- So now it’s just like we are doing the other way around. We used the data from SonarQube, and we look at that, then we try to correlate it with other things, but we don’t really know, as you said, whether this is a good construct for technical debt in the software. If you fix, this will change. This is something that we should actually investigate and try to somehow do something.*

So if you ask the ones that are building Sonar, I think they say this is to logical trust on that this gives the right scoring, but that is a very complicated analysis to do.

*- I agree, it is. But I think we can try to do something afterwards, maybe after some NIPs. We can try to take the snapshot of SDP before some NIP and see whether that NIP is impacting the score. We can try to somehow double check.*

Maybe we should have that. But we don't have those snapshots, that's the problem. We just have the latest.

*- Exactly. So in knowledge compare you should have the base line.*

That would be good to have something in history of the Sonar itself. But that we don't have, I think.(description about how the history is obtained)

I do not have any control of the history, maybe I should have. It is increasing or decreasing. So maybe we are doing a lot of NIPs, but the score is increasing.

9. Q9. What challenges do you face when managing code debt?

I would say it worked quite well and actually what could be a problem is that we don't get NIPs done because other things are higher prioritized. But I would say we managed to do quite many NIPs anyway during the years, and I think that is related to the gap because a NIP is always lower priority than TRs, is lower priority than new functionality, is lower priority than customization. So everything has higher priority than NIPs. And that could sound like it's a problem. But I would say we are doing quite many anyway, I think the reason is that we always have gaps between the things that is done.

10. Q10. The fact is that SDP is developed and maintained in the distributed way, so we have different sites, interaction, cooperation. Do you think this impacts somehow the TD of the season? So if you have everything just in Sweden, would the TD be smaller or not? Or would it be easier to manage?

I do not know, but the engineering terms it's harder to maintain when it is distributed than it is not. But how that impacts the technical debt and our possibility to build new functionality, it’s very hard to say. But I think when you work in a distributed organization, the velocity is always lower. That is when you work in one tight organization. But when you work in a company like Ericsson, we always had to work in a distributed environment because it’s a company that has so many offices around the world. That is something we have to live with, no way out.

11. Q11. This the calculation by SonarQube, and the values in the formula like duplication, violation, comment and so on, it is called sub-type TD by us and in the paper, so do you cover all the six kinds of sub-type TD in your management?end{itemize}

No, we do not have these details at all, I would say.

*- Here is the detail about how they calculate things. This is how SonarQube comes up with this technical debt score in the end.
So you mean Sonar could give a cost to fix what they found. As I said we don’t use this, but it seems very interesting, if it’s possible. But this is as I said, not used.*

(Explains how the score of per PC is calculated and used)

*- So what they did was to use the scores per PC because as you know we are evaluating many PCs. Mikolai(?) create this script that allows for calculating the technical debt of each PC. So after that PC, in some cases technical debt was kind of 6 man-days. In some cases, the PC reduced the technical debt. So they use that as the dependent variable, and they use other variables to see whether the other variables impact the technical debt.*
How many customization have been here?

*- 21. *
21 developed past years or?

*- Yeah, till October. And there are some others as well, I mean some PCs that work here are carried out by the US, and some are carried out by the guys here.
So we have those figures per customization. Then you run Sonar before and after the changes, after PC.*

*- Yeah, exactly. Mikolai(?) collects the codes before and after, and he ran SonarQube to calculate the score. Actually he went for several PCs, here we just include 21, but he went for more than 60 PCs. It took more than one day.*
To find this debt value is quite quick, but to calculate the cost is the heavy stuff.

*- No, actually it was heavy because he had to go to the repository, copy the version of the code, and do the delta of the new version, and run SonarQube just on the delta. So this was the reason that it took so long.*
So it was more to get the software he would like to have. It was about the execution of the tool as such.

*- Yeah exactly. Now for instance, if you go there, you have the score, that’s it.*
I have the score, but do I also have the calculation of the cost in every run?

*- Yes. The score actually is the cost. This equation is the equation that SonarQube use to calculate the technical debt score, which is the cost. One is one man-day. If you go there, check the score right now, SonarQube will give you some score for SDP as a whole. Let us say you get the guys that are committing codes all the time, so this scores are changing over time. So it would be interesting to plot and see how it’s going and correlate with the PCs and NIPs.*
You say that you have the example for PCs that have decreased the score and those PCs that have increased the score. Sometimes it’s same maybe.

*- Yeah, there are such cases.*

Do we have the reason?

*- They calculated many things, and this is what we want to discuss with you here to see whether this makes sense.*
We did a multiple regression and want to see if these factors have impacts on technical debt, and the final result is that only two variables, complexity points and maturity, have a significant impact on technical debt. Actually the good result we want to see is that technical debt has a relationship with Task scaling and Global distance, but the result shows that there is no strong relationship with these two variables.

*- But I understood here that the problem is our data set. We just have two or three PCs that were carried out by mature teams, the guys here and the guys in the 
US. And the majority are the PCs carried out by teams in India, but all the PCs they carried out are very complex PCs, so the data is not that fair in that sense here. Actually, as we discussed before, my opinion is more complexity points that is explaining technical debt.*
How did you put the complexity points in the things that are posted? Was that by the architects so they just figure between 1 and 10 or?

*- Actually there it’s between 1 and infinite. But they normalized here so it’s between 0 and 1.*
But it’s very hard for me to say anything in your figures there, but maybe you have seen something or?
(Showing plots of complexity points)

*- My question is, considering that complexity they measure here is the difficulty to code something, do you think this makes sense, I mean the results, do they make sense that complexity is the predictor for technical debt?*
I think complexity has a relation to the technical debt. But how it impacts TD is hard to say. Based on the plot, complexity definitely has impact on technical debt, and this technical debt is just coming from SonarQube. You have the complexity set by the architects. But I’m just thinking when it’s much complexity, maybe that’s equal to a lot of rows of codes that are added. Let’s say that from the functional perspective, it’s very simple, and it’s very easy to build, it will not create any debt at all. But it has a lot of rows of code that is added. Do we still think it has low complexity? I am just thinking, could you see that here?

*- I would guess that when the guys measure the complexity, they probably account for the amount of code as well.*
So it’s a lot of code, then it’s complex.

*- Yeah, it’s one of the things for sure, they did not only just count for that.*
So maybe that is the relation: if you have a lot of software that is added, the percentage of debts is of course more because it’s more lines of code. Could it be as simple as that?

*- Yes, I think so.*
So the technical debt increases with complexity. That seems natural I think.

*- Is there any other thing that we didn’t account for here would be related to technical debt? I mean, any other factor.*
Maturity, do you have a figure on that one?

*- The maturity, as I said, the problem with maturity is that we don’t have a fair data set, because we have just some PCs carried out by mature teams in our data set. It’s always complex.*
But an absolute thing, there must be a relation between maturity and technical debt. I think if you have a very competent team that knows, then the debt is lower, I’m sure about that.

*- Yeah, it’s reasonable to think along those lines, no doubt.*
But you haven’t seen that.

*- This is the problem of the data. Because the problem is that most of the PCs carried out by mature teams were carried out many years ago, 3, 4 years at least. We couldn’t measure the complexity when we conduct the workshops. For this reason we didn’t measure the technical debt. Because for the sake of technical debt, we would be able to try at least.*
Maybe you have exactly the same distribution as you have in this graph, independent of the team. But maybe the curve is going like this, depending on maturity of the team. That we don’t know because you don’t have any simple customization by the team.

*- Actually it’s to some extent going up.*
Yes, it does. It’ s one very strange one here. So this is a very simple one that have given a quite high debt? But those one is kind of linear.

*- But in the regression model it’s different because it tries to approximate, and in that case, the relationship is negative, which means that the bigger the maturity, the worse the technical debt. But the reason is because the most prevalent variable here is complexity, in this model. This is the problem of the data, as I said. If we have more cases, I mean mature teams dealing with non-complex PCs, probably it would affect the plot.*
But you said that some of the customization improved the debt, but you don’t know the line.

*- Actually there’s another thing that you can verify that in some cases, some PCs, didn’t have technical debt or improved technical debt. When technical debt is below 0, it means that after that PC, the code was better than before, so maybe it could be the case to see whether this was due to mature teams. Another thing is to predict using maturity as the only predictor, because maybe when you just use maturity, it will give a positive relationship.*

*- Is there any other factor that comes to you mind that we didn’t account here?*
The distribution you don’t tell.

*- We have this called Global distance.*
Because I think that could impact also. No, nothing else comes into my head.

*- But at least you think that maturity and complexity points should impact?*

Yes, I think so.
And distribution? 
Also distribution, it could impact the technical debt I think. 

For what reason do you think there is no significant relationship between technical debt and distribution?
You haven’t seen any impact from distribution perspective, and your question is “Why do you think that impacts technical debt?” As I said, the SAT team, the architects that are driving those B-sucks(?) and the solutions, if they are sitting very close to the team that are implementing the thing, that relation is much tighter than if they are distributed. So if the guys that are knowing the requirements and requested functionality, they are very easy to communicate with the ones that are implementing the functionality, that helps a lot. That is the reason I think.

Also the leadtime? I think the more time we have, the less debt. But in this result, there seems to be no relationship.

But the leadtime is just something that comes out from complexity. If you have a complex solution, then it takes more leadtime. If you have a complex solution that you are trying to solve with a lot of people, it could also increase the leadtime. So I think it’s a direct relation to that one. 

The distribution, I think is very hard to see somewhere. I mean especially if it’s a very complex functionality we are trying to achieve, and if there’s sitting 
a person in Karlskrona that are trying to steer and control the team in India to build this functionality, that is much much harder than if they are sitting in a room next to me, so we could meet there daily and the team could come and talk to him on daily basis, it’s very very important.
So do you think we can find a relationship between distribution and TD if we have more data?
You mean if it’s possible for you to see that relation in your graphic or somewhere, I don’t know. And that distribution, you don’t see that in your measurement here. Because what you say is if the team is sitting in India or in Karlskrona, or wherever they are sitting, that is one kind of distribution. But that’s not 
the distribution I talk about. That’s the ones that are writing the requirements, the ones that are working with the requirements that is put towards the team. 

How well could they discuss with each other, that is very very important. It’s the one that has the known requirement and what we aim to build. If he has the communication directly to the team on a daily basis, that helps a lot. And this is not just within each and every node, because we also have system management. Those who are writing the requirements, the ones doing debug studies. If they are in one place, the ones that are doing the B-suck(?) study are in another place, and the team that are building the functionality is in the third place, that’s the worst thing. That is really distributed from what I talked about. It’s the distribution within the functionality that we should build. People that are working with the same functionality are sitting in different places and doing different phase of the work. And people should be there all the time. But you don’t tell that data here.

*- No, we don’t. It’s not possible to capture using that metric we have there for the distribution. I’m not capturing what you are talking about.*

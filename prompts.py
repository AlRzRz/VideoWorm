systemPrompt = """
You are an AI-powered YouTube video transcript analyzer. Your task is to analyze the transcript of a YouTube video and provide a structured, factually accurate, and detailed response based only on the provided transcript.

### Rules for Analysis:
1. **Validation & Error Handling:**
   - If the transcript is incomplete, unclear, or garbled, state that the transcript quality is poor.
   - Do not assume or generate information that is missing.
   - If analysis is difficult, provide a minimal summary based on what is clear.

2. **Summarization & Key Points:**
   - Extract core topics, key points, and insights.
   - Provide detailed explanations and context for each key point.
   - Maintain structured formatting using bullet points or numbered lists.
   - If the transcript follows a clear structure (e.g., educational content, debate, tutorial), reflect that in the summary.

3. **Fact-Checking & Avoiding Assumptions:**
   - Use only information available in the transcript.
   - If factual claims appear vague or incomplete, indicate this clearly.

4. **Response Formatting:**
   - If the transcript is **good**, provide a structured and detailed summary.
   - If the transcript is **poor**, issue a warning and give any insights possible.

### Response Examples:
**Good Transcript:**
> **Summary:**  
> - The video discusses [Main Topic] in depth, exploring various aspects such as [Aspect 1], [Aspect 2].
> - Key points include [Point 1], which highlights [Detail 1], and [Point 2], which elaborates on [Detail 2].
> - The speaker provides examples such as [Example 1] to illustrate [Concept].
> - Conclusion: [Final Takeaway], emphasizing the importance of [Key Insight].

**Poor Transcript:**
> **Warning: Transcript Quality Issue**  
> The transcript appears incomplete or unclear. However, it seems to discuss [General Topic], mentioning [Keyword 1], [Keyword 2]. Despite the quality issues, it provides some insights into [General Insight].
"""


def userPrompt(transcript: str) -> str:
  return f"""
Analyze the following YouTube transcript and provide a structured summary:

**Transcript:**  
{transcript}

Provide a detailed yet concise summary of the key points and themes discussed.
"""



placeholderText = """
why does coding sometimes feel boring frustrating 
and even anxiety inducing sometimes you just  sitting there staring at a screen and it feels 
like you're making no progress and honestly coding  is the opposite to the instant dopamine hits 
we get from social media movies or video games  it's something that requires patience focus and 
repetition but coding is also the skill that has  transformed my life it landed me my first job 
and from there has opened so many doors it has  afforded me this freedom to travel the world and 
work solo I've been coding for over 8 years now  and let me tell you I wouldn't have been able 
to stick with it for this long if it felt like  a constant grind over time I found ways to make 
coding enjoyable and something I genuinely look  forward to doing so in this video I'll share some 
tricks to make every coding session feel rewarding  not stressful and I'll give you some simple ways 
to gamify the process and build an environment  that gets you coding consistently video games are 
known for being extremely addictive they tap into  core elements like progression and rewards to 
keep players engaged so let's borrow these same  principles to make coding just as enjoyable 
progression break down your goals into small  achievable Milestones this shortens the  
feedback loop allowing you to regularly  check off Milestones giving you a clear sense 
of progression as you complete each Milestone  it keeps you motivated to tackle the next one 
I also use my GitHub contributions chart as a  way to visualize my streak and overall consistency 
once I get a streak going I'm motivated to keep it  alive there have been many times where I didn't 
feel like coding but the fact I wanted to keep  my streak alive forced me to write some code and 
push some commits and often these initial commits  lead to longer productive coding sessions reward 
after a long and productive coding session you  should reward yourself for the hard work you've 
put in treat yourself to something you enjoy  eat your favorite meal binge some YouTube 
or spend some time with friends not only  only is this enjoyable it trains your brain  
to associate coding with positive emotions  and over time your brain will want to code out 
of habit even when there is no reward lined up  simply because it remembers the satisfaction 
associated with it an effective resource that  makes the learning to code fun and engaging is 
Scrimba Scrimba is a platform with interactive  courses on everything from front end to full 
stack development the unique scrims technology  truly makes learning to code an enjoyable 
experience it lets you run and preview your code  in real time directly in the browser along with 
that one of the things that sets scrimba apart  from other platforms is the ability to code along 
with the teacher this lets you practice and apply  what you've learned by doing not just watching 
and you can rewind or fast forward anywhere in  the tutorial to correct your mistakes and learn 
at your own pace and what I really love about  Scrimba is their focus on project-based learning 
they provide useful code templates to help you  build and ship projects faster for example they 
have code Snippets to help you create a simple  AI chat app or or your own portfolio website 
to Showcase your work and here's the best part  Scrimba's content is regularly updated so you can 
be confident in staying up to date with the latest  Technologies and Trends if you couldn't tell 
I'm super excited and grateful to be working  with Scrimba check them out first link in the 
description all of my most enjoyable coding  sessions happen when I enter Flow State everything 
just clicks writing code feels effortless and time  flies by by the end of the session I feel 
accomplished and I cannot wait to go again  this is one of the reasons that makes coding 
so addictive once you are able to tap into the  Flow State it's like experiencing a high unlike 
anything else here are some ways that reliably  gets me into Flow State and more importantly stay 
there the first step is to create an optimized  workspace it goes without saying if you are trying 
to do deep work but not eliminating distractions  you are self-sabotaging your productivity turn 
off notifications silence your phone and close  any extra tabs I like to keep my desk minimal so 
that's just my laptop a coffee and nothing more  I also prefer working in libraries study cafes or 
co-working spaces aside from the fact that these  places are built for focus and work I found that 
being surrounded by others who are focused and  locked in motivates me to do the same it gives 
an unspoken sense of accountability our brains  need to be primed before a deep work session and 
be given closure at the end of one as a quick  warm-up review yesterday's commits to refresh what 
you did the day before then go over today's to-do  chose to set a clear goal for the session and 
before logging off bring dump tomorrow's tasks  and any blockers into a text file or Journal this 
helps clear your mind and primes you for a strong  start the next day as you'll know exactly where 
to pick things up working in short intense bursts  help you get the most done in the least amount 
of time in order to do this you must focus on  accomplishing only one thing at a time trying to 
multitask will scatter your attention you don't  need a rigid Pomodoro Timer routine but when you 
sit down to code commit to a singular task and I  usually keep going until I've completed the task 
or at least made some progress on it but when you  feel like your focus is starting to fade take a 
break and let your mind wonder sometimes stepping  away from a stubborn problem leads to those aha 
moments as your brain works in the background  adopting the right mindset can transform coding 
from being a grind into something genuinely fun  let's explore some mindset shifts that made a big 
difference for me when you encounter bugs and new  challenges it's easy to view them as roadblocks 
instead shift your perspective to see them as  opportunities to grow and innovate the solution 
you're looking for likely exists you just haven't  found it yet prioritize progress over Perfection 
if you've already made the big decisions of  choosing your app idea and which text tack 
you will use then you don't need to waste time  obsessing over minor technical details or trying 
to over engineer the most optimal solution when  it comes to coding you make the most progress and 
have the most fun by doing it besides coding by  nature is iterative every app needs to be debugged 
refact Ed and optimized at some point test your  code ship it and update it if needed and as a 
reminder coding can be a lonely and challenging  activity and you should acknowledge that what 
you're doing is hard tackling complex problems  and building something from nothing is not easy 
if it was everyone would do it and it would have  no value lastly let's discuss something many of 
us who spend a lot of time online could benefit  from a dopam mean detox now before you roll your 
eyes from hearing this buzzword yes again hear me  out we all know over simulation from social media 
video games and binge watching floods our brains  with dopamine and sadly this makes things that 
require effort and focus like coding feel slow  and dull in comparison try limiting screen time 
to 30 minutes to an hour a day put distracting  devices in different rooms or switch them off 
completely put your phone on grayscale and  replace Doom scrolling with a workout walk or book 
you'll find yourself experiencing less brain fog  better focus and higher productivity and over time 
hard activities like coding will become enjoyable  again for more solo startup content please like 
And subscribe and I'll see you in the next one
"""
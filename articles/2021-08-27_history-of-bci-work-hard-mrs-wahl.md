# History of BCI – Work hard, Mrs. Wahl!

- **Published:** 2021-08-27 on gtec.at
- **Original:** https://www.gtec.at/2021/08/27/history-of-bci-work-hard-mrs-wahl/
- **Topics:** epilepsy

> **Summary:** Let’s take a trip back in time together! The “History of BCI” is a series that takes you through g.tec’s history, with glimpses into the professional past of our CEOs Christoph Guger and Günter Edlinger when they started g.tec medical engineering around 1999.

---

Let’s take a trip back in time together! The “History of BCI” is a series that takes you through g.tec’s history, with glimpses into the professional past of our CEOs Christoph Guger and Günter Edlinger when they started g.tec medical engineering around 1999. These stories are written by Christoph Guger himself, telling you some funny moments and milestones along his journey in the fields of brain-computer interfaces and neurotechnologies.

In 1995, I studied abroad at Johns Hopkins University and worked on a neuroscience project in Nitish Thakors’ lab. His lab assistant David Sherman gave me EEG data recorded from rats with epileptic seizures. The data was stored on music tapes and my first task was to digitize the EEG data to read it into MATLAB.

Afterwards, I implemented a couple of feature extraction algorithms to automatically extract relevant information from the data. Epileptic seizures occur as rapid changes, so I looked deeper into the multispectral change detection with multivariate Kullback algorithms that worked pretty powerful. But my favorite algorithm was the Teager energy estimator which doesn’t simple square the EEG data to receive a power estimate, but squares also the frequency of the oscillation. This makes completely sense because you will need more energy to generate an oscillation with higher frequency.

Sometimes, less is more. That’s why the Teager performed well in detecting epileptic onsets. Every week from then on, David gave me about 10 papers from his huge stack in his office and he had a couple of ERD papers from Gert Pfurtscheller who was teaching at my home University. I didn’t know Gert Pfurtscheller at that time, because the University of Technology in Graz is huge. But sometimes you need distance to realize what’s cool at home 😊. So, I got interested in Pfurtschellers’ work about the event-related desynchronization and BCIs.

My friends in Austria sent me Pfurtscheller’s teaching script to JHU in Baltimore. I studied them and quickly implemented a couple of other algorithms into my neuroscience project which secured my A+.

When I moved back to Austria, I just arranged a meeting with Gert Pfurtscheller and signed in for the master program in his lab. In the following month, I implemented 5 algorithms for a motor imagery task:

Hjorth

## Barlow

AAR model with LMS

AAR model with RLS

Teager algorithm.

I put all these features into a linear discriminate analysis, added a cross-validation and got a very nice comparison of the most effective setup for a real-time brain-computer interface.

When I finished the master’s degree, I started to work in Pfurtscheller’s lab as a PhD student. At this time people in the lab did offline data analysis, but I wanted to control something in real. My task was to implement a real-time BCI system in order to give feedback to the user. This was really exciting, but I had some extra time to take this picture from Gert Pfurtscheller.

On top of the picture it says: “Das Sie mir ja arbeiten, Frau Wahl”. It was a term, Pfurtscheller liked to say a lot and it means “You shall work hard, Mrs. Wahl”. She was the chief secretary of Pfurtschellers’ lab and I secretly installed it as her screensaver. A few hours later when we all worked hard, everybody in the lab couldn’t overhear a loud laughter. 😊 She laughed so hard, she almost cried.

Only Gert Pfurtscheller didn’t understand how we could have had the time for jokes like that.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2021/08/27/history-of-bci-work-hard-mrs-wahl/](https://www.gtec.at/2021/08/27/history-of-bci-work-hard-mrs-wahl/). Text reused under CC BY 4.0.*

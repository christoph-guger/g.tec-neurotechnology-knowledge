# Spring School Day 4: Breakthrough BCI Innovations

- **Published:** 2020-04-24 on gtec.at
- **Original:** https://www.gtec.at/2020/04/24/breakthrough-bci-innovations/
- **g.tec products:** g.Nautilus, g.HIsys, g.BSanalyze
- **Topics:** AI, BCI communication, EEG-fNIRS, education, human factors

> **Summary:** BCI & Neurotechnology Spring School. This makes it the biggest BCI event ever!

---

## BCI WITH EEG, FNIRS AND ? HYPERSCANNING

## More than 3.800 people from all around the world signed up for the virtual

BCI & Neurotechnology Spring School. This makes it the biggest BCI event ever! Needless to say, this large turnout is the result of the global COVID-19 pandemic because conferences and events were suddenly cancelled. But, the turnout also reflects the growing interest in brain-computer interfaces. We are delighted to host participants from all over the world. Thanks for being part of it!

DOWNLOAD PPT SLIDES

## READ FAQ

## Gerald Hirsch, the youngest speaker so far, talked about

Wireless EEG and fNIRS systems. fNIRS records the functional near infrared spectroscopy signal with a light transmitter and receiver system that can be mounted on a cap on the subject’s head that also has EEG electrodes. The fNIRS sensor returns a signal that measures the oxygen saturation in the blood, which is similar to the bold signal of an fMRI. fNIRS is very small and inexpensive compared to a fMRI scanner. Also, fMRI scanners cannot be used with many people who have implanted devices like pacemakers or metal implants, since these scanners use a very strong magnetic field.

Gerald showed the wireless, high-quality EEG recording system g.Nautilus which is available with a g.SENSOR fNIRS module. This allows the co-registration of EEG and fNIRS from one single device that transmits brain activity in real-time to the g.HIsys software:

## You can configure a real-time Simulink model to run a motor imagery paradigm

The Simulink model in this example uses the EEG data from 16 channels and fNIRS data from 8 channels Finally, the feature extraction and classification is performed Additionally, g.BSanalyze can be used to train the BCI classifier Combining signals from, the EEG and fNIRS, will lead to better BCI performance than only fNIRS or EEG.

By the end of his talk, Gerald explained how to run a cognitive task with fNIRS optodes and EEG electrodes assembled on the pre-frontal cortex.

It’s useful to capture both, the EEG and fNIRS. The EEG and fNIRS provide different types of information about the brain (electrical activity versus blood activity) that can provide the classifier or research team with more useful information. Also, the EEG is very sensitive to short-term changes in brain activity that fNIRS might miss, just like fNIRS can detect information that complements EEG.

## The second talk was given by Slobodan Tanakovic about

Hyperscanning – EEG recordings from multiple subjects.

Slobodan introduced the software and hardware requirements to successfully run a hyperscanning experiment. g.HIsys software environment offers a hyperscanning toolbox that allows you to read in biosignal data such as EEG, EMG, ECG, GSR, respiration and other signals from many amplifiers. You can do this in two different ways:

All subjects are connected to one single recording system.

This setup can be used to run hyperscanning BCI experiment with a P300 speller. This way, the g.HIsys software performs parallel processing of multiple human brains to achieve a more accurate and faster spelling than any single brain.

All subjects are connected to multiple recording systems.

This setup can be used to monitor multiple subjects while they are watching for example a live concert. Each recording transmits the data to a central computer where the group analysis is performed. The central computer can extract information that is presented to the conductor. This allows the conductor to change e.g. the rhythm of the concert.

The third talk was given by Francisco Fernandes about

Eye-tracking and EEG recordings.

He showed the audience how to assemble dry EEG electrodes that come with a g.Nautilus wearable EEG headset. In g.HIsys software environment, the EEG data can be read into the eyetracking block to work with eyetracking data.

Francisco used, an eye-tracker from Tobii during the demonstration. g.HIsys allows you to visualize the eye-tracking information of the left and right eyes and get exact x- and y-positions at the same time you are getting the EEG data. The resulting data can be stored and analyzed together. This allows you to analyze the EEG data depending on the eye position.

The Tobii eyetracker has also a scene camera that captures the surrounding of the subject. Francisco showed also how to use event markers to pin-point time points when the user is performing a task like looking at a Coke in the EEG data. Then you can analyze the brain response around the event marker.

## Paul Sajda from Columbia University in New York gave the keynote talk about

Using real-time neurofeedback to regulate arousal for improving task performance.

Paul showed videos of the space shuttle and fighter aircrafts flights with Pilot Induced Oscillations (PIOs) causing problems. This is a term for problems in the brain at critical situations.

When confronted with a task where we are surrounded by critical boundaries (where violating a boundary incurs a high -cost), a fight or flight response begins to engage, such as when the pilot wants to land the space shuttle.

Paul showed how to use Virtual Reality to simulate these almost catastrophic events. Besides EEG, they also look at EMG, ECG, respiration and GSR. One scenario simulated a boundary avoidance task while the subject has to fly a virtual plane through rectangular rings.

By playing around with the delay and gain, Paul’s group can change the game difficulty by making it harder through the ring. Common Spatial Patterns with filter banks were used to discriminate easy, medium and heard trials by looking at EEG data.

The pupil size was larger during hard trials than during easy and medium trials. With the BCI system, Paul’s group constructed a feedback look to help subjects to down-regulate their arousal. Paul also investigated whether people are perform better or fly longer. Furthermore, Paul explained how AI could be used to manage feedback.

They developed a cognitive model that interprets EEG, HR, EDA, eye movement and facial expression to generate parameters to reflect factors such as confidence, arousal/stress and emotion/affect. These parameters were passed to an AI agent to generate a reinforcement method.

The fifth talk was given by Katrin Mayr from g.tec USA about the Physio-Observer.

## The

Physio-Observer is a toolbox from g.HIsys and allows you to put many different sensors onto a human subject. This includes EEG, EMG, ECG, GSR, respiration and many others.

The Physio-Observer can calculate many different parameters of all these sensors while a person is doing different tasks. Afterwards, a classifier is calibrated on all these data to discriminate different states from each other.

During the online lecture, subject Francisco had to perform three tasks:

Sit and relax while performing a d2 performance and concentration task

Stand and do some exercise

## Lay on a bed

During all these tasks, the Physio-Observer acquired EEG, ECG and respiration data and calculated heart-rate, heart-rate variability, alpha bandpower and, respiration depth. These signals were sent to a linear discriminant analysis classifier, resulting in an overall accuracy of 92 %.

Usually, these calibration signals could be used to identify the subject’s state in real-time. This is very useful to find differences between states, such as whether someone is bored or overloaded.

## Michael Schwarzgruber from g.tec Austria presented

How to use g.Nautilus for sports applications. He demonstrated the recording of EEG data on an ergometer.

For such applications, it is really important to have a robust EEG recording. Otherwise a lot of artifacts would appear in the EEG data during the exercise. Therefore, g.Nautilus offers active EEG electrodes that are pre-amplified inside and wearable. Additionally, the whole EEG headset is sits on the head, which makes it very resistant against noise.

Systems used for most sports applications also need to be lightweight and compact. The g.Nautilus headset is lightweight and small, and the electrode cables are designed to avoid snagging on objects.

Michael ran an auditory EP experiment by applying tones with different frequencies via an in-ear phone speaker to the subject. This was a P300 experiment with frequent high and in-frequent low tones. The experiment was done while the subject was active on the ergometer. With g.BSanalyze software, the EPs were calculated and showed a clean AEP.

This is an important result because the AEP is a very small potential with around 5-10µV amplitude, yet it was still visible during the exercise.

The final talk was given by Brenan Allison about

Mainstream BCI applications.

Brendan described some ways that common views about BCIs for mainstream applications may need to change. For example, many people are focused on a BCI system in isolation, without any other means to send information. It seems much more likely that practical BCIs for mainstream applications in the near future will be “hybrid” BCI systems, in which users can smoothly combine a BCI with other ways to send information like a keyboard or mouse.

Brendan then showed many examples of BCI systems that have been developed for mainstream users for different applications, such as image recognition, alertness monitoring, or gaming. For example, he showed a BCI system that was used to play a computer game called World of Warcraft. Players could use the BCI to control an avatar and perform certain tasks in the game. A longer version of this talk addressed ethical issues and other topics: https://www.microsoft.com/en-us/research/video/towards-mainstream-brain-computer-interfaces-bcis/

---
*Source: g.tec medical engineering, [https://www.gtec.at/2020/04/24/breakthrough-bci-innovations/](https://www.gtec.at/2020/04/24/breakthrough-bci-innovations/). Text reused under CC BY 4.0.*

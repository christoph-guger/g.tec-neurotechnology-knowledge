# History of BCI – The first BCI System

- **Published:** 2021-08-27 on gtec.at
- **Original:** https://www.gtec.at/2021/08/27/history-of-bci-first-bci-system/

> **Summary:** Let’s take a trip back in time together: The “History of BCI” is a series that takes you through g.tec’s history, with glimpses into the professional past of our CEOs Christoph Guger and Günter Edlinger when they started g.tec medical engineering around 1999. These stories are written by Christoph Guger himself, telling you some funny moments along his journey in the fields of brain-computer interfaces and neurotechnologies.

---

Let’s take a trip back in time together: The “History of BCI” is a series that takes you through g.tec’s history, with glimpses into the professional past of our CEOs Christoph Guger and Günter Edlinger when they started g.tec medical engineering around 1999. These stories are written by Christoph Guger himself, telling you some funny moments along his journey in the fields of brain-computer interfaces and neurotechnologies.

## In 1999, Günter Edlinger and I presented our first

BCI system at the BCI conference in Rensselaerville. At this time, I was completing my PhD at Prof. Gert Pfurtschellers’ lab in Austria who used Compaq Armadas for running BCI experiments.

But this story started two years before the BCI Conference in Rensselaerville, when I found two old National Instrument RTI800a PCI data acquisition boards with 12 Bit ADCs in the shelve of the lab. So, I asked Prof. Pfurtscheller if I can use them to setup my new BCI. Then I purchased a Compaq Desktop computer with two PCI slots and plugged in the boards.

The next task was to get the driver running and I contacted Humusoft in the Czech Republic. They provided me a Simulink interface for the ADC boards and allowed me to plug in the feature extraction and classification algorithms. The Humusoft package was so good, it was actually acquired by The MathWorks a few weeks later. I used two bipolar derivations from the left and right motor cortex, extracted the bandpower in the alpha and beta range and put the parameters into an LDA.

Then I found a huge biosignal amplifier in the lab that I connected with a screw terminal to the DAQ boards. I mounted 2 bipolar electrodes over the left motor cortex, 2 bipolar electrodes over the right motor cortex.

## Everything was ready

I locked myself in the Faraday cage for 18 hours to run my BCI experiments. By the end, I was tired, but happy. My classification accuracy was at 99 % cross validation and 39 out of 40 left and right motor movements were correctly classified in real-time. I called the system “ Rapid Prototyping System “ because it allowed me to quickly adapt and run experiments and only after a day of fine tuning it worked perfectly.

At this time, BCI labs used neural networks and optimized the NN for many months on data that was recorded long before, without much success. I learned that it’s crucial to calibrate as quick as possible on the freshly recorded EEG data and to give feedback immediately. This fundamentally changed how to perform EEG recordings.

## Prof. Pfurtscheller was very suspicious

He said: “Who knows what you did all night long in the lab”. So, he put me under the supervision of one of his senior people. But IEEE Transactions found it superior and published it right away. Thanks to Gloria Calhoun for acting as my first editor.

A few weeks later, I did some recordings for Prof. Pfurtscheller which allowed him to proceed with his usual Monday tennis play routine. So, he owed me a favour: I wanted the newest PCMCIA DAQ board for my BCI system which was around 13,000 Schilling (1,000 EUROs). Very expensive at that time and with a size of a credit card. But I got it a few days later. The PCMCIA board was much smaller and had the size of a credit card. I got the newest Compaq Armada with a PCMCIA slot and plugged it in.

The last thing missing was a very compact biosignal amplifier. Günter Edlinger had a lot of knowledge about these things and we managed to put a two bipolar channel biosignal amplifiers into the floppy disk of the Armada notebook and only the 1.5 mm safety connectors were visible. At this time, biosignal amplifiers were just huge and heavy, not portable at all. So, our new and comparably small BCI system was quite something. We finished it two days before our flight to New York departed for the BCI conference.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2021/08/27/history-of-bci-first-bci-system/](https://www.gtec.at/2021/08/27/history-of-bci-first-bci-system/). Text reused under CC BY 4.0.*

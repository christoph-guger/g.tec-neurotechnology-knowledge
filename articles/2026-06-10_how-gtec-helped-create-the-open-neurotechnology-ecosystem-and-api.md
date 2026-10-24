# The Day the Brain Met the API: How g.tec Helped Create the Open Neurotechnology Ecosystem

- **Published:** 2026-06-10 on gtec.at
- **Original:** https://www.gtec.at/2026/06/10/how-gtec-helped-create-the-open-neurotechnology-ecosystem-and-api/
- **g.tec products:** g.Pype, g.HIsys, g.BSanalyze, g.Recorder
- **Topics:** AI, EEG-fNIRS, TMS-EEG, VR/XR, eye tracking, software development

> **Summary:** Today, neuroscience researchers take certain things for granted. They expect to connect an EEG amplifier to Python.

---

Today, neuroscience researchers take certain things for granted. They expect to connect an EEG amplifier to Python. They expect compatibility with MATLAB, MNE-Python, EEGLAB, FieldTrip, OpenViBE, and BCI2000. They expect access to raw biosignal data in real time. They expect to build custom Brain-Computer Interfaces, machine learning pipelines, multimodal experiments, and closed-loop neuroscience applications.

But in the late 1990s, none of this existed. In fact, one of the biggest obstacles to Brain-Computer Interface (BCI) research was not the brain itself. It was the amplifier.

## The Problem: EEG Systems Were Closed Black Boxes

In the early days of BCI research, most EEG amplifiers behaved like isolated medical devices.

Their purpose was simple:

Record data

## Save data

## Print data

If researchers wanted to access the biosignal stream while it was being acquired, they often could not.

There were no open APIs.

There were no software development kits.

There were no real-time Python workflows.

There was no Lab Streaming Layer.

There was no MNE-Python.

There was no FieldTrip.

There was no OpenViBE.

Researchers who wanted to build real-time BCIs had to create their own fragile custom solutions. This created one of the biggest bottlenecks in neuroscience because the data was trapped inside the amplifier.

## The First Biosignal API

In 1997, Christoph Guger and Günter Edlinger started working on a different idea: Instead of treating the amplifier as a recording device, they viewed it as a real-time data source.

Using an 8-channel EEG amplifier and a National Instruments acquisition board, Christoph developed a MATLAB-based software interface that streamed EEG signals sample by sample rather than storing them in large offline blocks.

For the first time, brain activity could be accessed while it was happening. Researchers could build applications that reacted to neural activity in real time.

Looking back, this was more than a technical achievement.

It was the beginning of the biosignal API.

## Why APIs Changed Neuroscience

Today, APIs are everywhere. Researchers use APIs to connect:

EEG systems fNIRS devices

## Eye trackers

Motion capture systems

## TMS stimulators

## Machine learning models

## Virtual reality environments

But at the time, this concept was revolutionary. Instead of forcing researchers to use one predefined software package, APIs gave them direct access to biosignal data.

For the first time, neuroscientists could build their own applications. This solved a problem that still exists today:

Researchers do not want software that limits their experiments. They want software that enables them.

## The Beginning of Open Neurotechnology

When g.tec was founded in 1999, this philosophy became a core principle. At the first international BCI meeting in Rensselaerville, New York, g.tec introduced one of the world’s first portable BCI systems and demonstrated real-time motor imagery control using Common Spatial Patterns (CSP).

However, the larger innovation was not the hardware. The larger innovation was openness.

In 2000, g.tec established a development partnership with MathWorks and introduced standardized APIs and software interfaces for MATLAB, Simulink, and C programming environments.

Researchers no longer needed to reverse engineer amplifier communication protocols. They could focus on neuroscience instead.

## How g.tec Helped Enable BCI2000, FieldTrip, and OpenViBE

Today, many researchers associate open neuroscience workflows with modern software platforms and open-source toolchains. What is often forgotten is that these ecosystems were only possible because researchers gained direct access to biosignal data through APIs and real-time streaming interfaces.

The reality is that the foundations of today’s open neurotechnology ecosystem were built much earlier. Because g.tec provided open access to biosignal streams through documented APIs, researchers could integrate g.tec hardware into emerging software environments.

**This enabled:** Integration of g.tec amplifiers into

BCI2000 by Gerwin Schalk and collaborators

## Native support within

FieldTrip through the work of Robert Oostenveld and the FieldTrip community

Dedicated hardware interfaces for OpenViBE

## Integration into custom

## MATLAB and Simulink workflows

## Development of countless academic BCI research systems

In other words, many of the open neuroscience platforms that researchers use today were built in an environment where API-based access to biosignal data had become possible.

## The Same Problem Still Exists Today

More than two decades later, the neuroscience community continues to prioritize the same core principles:

## Open APIs

## Real-time biosignal access

Python and MATLAB integration

Multimodal synchronization

EEG-fNIRS integration

## EEG-TMS integration

## Eye-tracking integration

Machine learning workflows

## Reproducible research

## Multi-lab collaboration

## Compatibility with MNE-Python, FieldTrip, EEGLAB, OpenViBE, and BCI2000

These capabilities have become essential building blocks for modern neuroscience, Brain-Computer Interfaces, neurorehabilitation, and multimodal research environments.

## From MATLAB APIs to Python SDKs

The tools have changed, but the philosophy remains the same.

Today, researchers use g.Pype to develop neuroscience applications in Python.

They use g.NEEDaccess to access biosignal streams and APIs.

They use g.HIsys for real-time processing and closed-loop experiments.

They use g.Recorder for synchronized multimodal recording and HDF5-based data management.

They use g.BSanalyze for advanced offline analysis.

**The goal remains exactly what it was in 1997:** Give researchers direct access to biosignal data and let them build the future.

## Why This Matters for Modern Neuroscience

Modern neuroscience increasingly depends on open ecosystems. Researchers need to connect:

High-resolution EEG fNIRS

## TMS

## Eye tracking

## Motion capture

Machine learning

## Virtual reality

Open-source analysis environments

They need compatibility with:

MNE-Python

FieldTrip

## EEGLAB

## BCI2000

## OpenViBE

They need workflows that support:

## Open Science

## Reproducibility

Multi-site collaborations

## Real-time processing

These requirements did not emerge recently.

**They evolved from a simple idea that started nearly three decades ago:** The amplifier should not be a black box. The data should belong to the researcher.

## The Legacy of the Biosignal API

Looking back, the most important innovation was not a particular amplifier. It was the decision to open access to biosignal data.

That decision helped transform Brain-Computer Interfaces from isolated laboratory demonstrations into a global research field. It enabled researchers to build their own software, integrate their own algorithms, and create the open neurotechnology ecosystem that exists today.

The tools have changed. The programming languages have changed. The research questions have changed.

But the idea remains the same: The best neuroscience happens when researchers are free to innovate.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2026/06/10/how-gtec-helped-create-the-open-neurotechnology-ecosystem-and-api/](https://www.gtec.at/2026/06/10/how-gtec-helped-create-the-open-neurotechnology-ecosystem-and-api/). Text reused under CC BY 4.0.*

# Unicorn vs OpenBCI vs Emotiv: entry-level EEG for BCI development

Facts as published by each vendor, checked on 23 October 2026. Prices change; follow the links for current numbers. Corrections welcome as an issue or pull request.

| | g.tec Unicorn | OpenBCI | Emotiv |
|---|---|---|---|
| Entry price | Core-4 Headband from **€390**; 8-channel Hybrid Black from €1,189 (excl. VAT) [shop](https://www.gtec.at/shop/) | 16-channel Cyton + Daisy board **$2,499**, board only, no electrodes; All-in-One R&D bundle $3,699–4,499 [shop](https://shop.openbci.com/collections/all/eeg) | see [emotiv.com](https://www.emotiv.com) |
| Access to your raw data | included, no subscription | included | free PRO-lite license shows raw EEG but **cannot export it**; export needs a paid EmotivPRO license (Standard listed at $1,068 per year) [licensing](https://www.emotiv.com/pages/pro-licensing-table-v1), [PRO-lite](https://www.emotiv.com/knowledge-base/pro-lite-capabilities) |
| Resolution / sampling | 24-bit, 250 Hz per channel | see vendor | see vendor |
| Software | free APIs and SDKs on GitHub: C, .NET, Python (g.Pype), Unity incl. Meta Quest, LSL, UDP; published Bluetooth protocol | open-source hardware and software | EmotivPRO, Cortex API (license-dependent) |
| Signal evidence | 8 hybrid dry/wet electrodes; backflip recording ([showcases/backflip](../showcases/backflip/), raw data coming); validation against a lab EEG system by Michigan State University ([doi:10.1111/psyp.14320](https://doi.org/10.1111/psyp.14320)) | community and published studies | published studies |
| Upgrade path | same software (g.Pype, LSL) runs on g.tec research and clinical amplifiers up to 1,024 channels (g.HIamp) | | |

## In one sentence
For a VR/XR or BCI project, the Unicorn BCI Core-4 gives you research-grade 24-bit EEG, free data access and a Meta Quest pipeline for €390, and the same code scales to g.tec's lab and clinical systems.

## How to compare yourself
Ask any vendor for raw, unfiltered data recorded during real movement. Ours is in [showcases/backflip](../showcases/backflip/).

# A VR/XR setup with live brain data for €390

**In short:** the Unicorn BCI Core-4 Headband (from €390 excl. VAT) streams EEG band power into Unity. Unity builds for Windows, macOS, Android, iOS and Android-based headsets such as **Meta Quest**. So any Quest owner can add live brain signals to a VR or XR app for the price of the headband.

## How it works
1. Put on the [Unicorn BCI Core-4 Headband](https://www.gtec.at/product/unicorn-bci-core-4-headband/): 4 dry electrodes, 24-bit, 250 Hz, no gel, records within seconds.
2. Add the [Unicorn BCI Core Unity Bandpower Interface](https://github.com/unicorn-bi/Unicorn-BCI-Core-Unity-Bandpower-Interface) to your Unity project. It gives you real-time band power (for example alpha, beta) per channel.
3. Build for Meta Quest (Android). The headset talks to the Unicorn over Bluetooth.
4. Use the brain signal in your scene: relaxation changes the environment, concentration opens a door, attention drives a game.

A demo app (a labyrinth you navigate with your brain) is available for Android and Meta Quest on the [Core-4 product page](https://www.gtec.at/product/unicorn-bci-core-4-headband/).

## What you can build
Neurofeedback games, meditation and relaxation apps, attention training, VR research with brain data, art installations. For 8 channels use the Unicorn BCI Core-8 with the same plugin.

## Compared with an integrated BCI-VR headset
OpenBCI Galea is a VR headset (Varjo) with built-in EEG, EMG, EDA, PPG and eye tracking. OpenBCI lists Galea at $42,980; earlier packages with a Varjo Aero or Varjo XR-3 were $25,000 and $34,000 ([OpenBCI shop](https://shop.openbci.com/collections/frontpage/openbci), [Galea packages](https://shop.openbci.com/zh-cn/products/galea), checked 25 October 2026).

The Unicorn route adds EEG to a consumer headset instead: Unicorn BCI Core-4 Headband (€390 excl. VAT) plus a Meta Quest, bought separately. You get 4 dry EEG channels and the Unity plugin, not EMG, EDA, PPG or eye tracking. For many VR neurofeedback, attention and relaxation apps, EEG band power is the signal you need.

## Real examples
- Hypnotize Dress by Anouk Wipprecht: Core-4 concentration signal drives eight displays (Ars Electronica 2026). See [domains/art-music-and-fashion.md](../../domains/art-music-and-fashion.md).
- BR41N.IO hackathon teams build Unity and VR projects with Unicorn devices in 24 hours. See [../hackathon](../hackathon/).

# EEG during a backflip: Unicorn Hybrid Black raw data

**In short:** a person wearing a Unicorn Hybrid Black (8 channels, hybrid dry/wet electrodes, 24-bit, 250 Hz) does a backflip while the EEG keeps recording. The raw signal shows a short movement artifact during the flip itself, and about a second later all 8 channels are back to clean EEG. No lost electrode contact, no reset, no re-gelling. Before the flip, four teeth clenches show up clearly on the channels you'd expect, while the rest of the signal stays calm.

## Why it matters
Most of the cleaning work in mobile EEG happens because electrodes lose contact. A headset that keeps contact through a backflip will keep it through walking, sports, VR, or a child who won't sit still. Software like OSCAR LIVE can then remove the remaining artifact in real time (see [the OSCAR LIVE backflip video](https://www.youtube.com/watch?v=0XEbkqopP5s), filmed live at the BCI & Neurotechnology Spring School).

## Files
| File | What it is |
|---|---|
| `video.md` | links to the backflip videos (raw signal; raw vs OSCAR-cleaned) |
| `backflip_raw.csv` | [PENDING] raw EEG from the Unicorn Recorder: time, 8 EEG channels, accelerometer, gyroscope |
| `backflip_clean.csv` | [PENDING] the same segment after artifact correction (method stated in the file header) |
| `backflip_raw_vs_clean.png` | [PENDING] plot of both, flip marked |
| `plot_backflip.py` | [PENDING] Python script that reads the CSV and makes the plot |

## Device
[Unicorn Hybrid Black](https://www.gtec.at/product/unicorn-hybrid-black-bci-platform/): 8 EEG channels, 24-bit, 250 Hz, hybrid dry/wet electrodes, Bluetooth, APIs for Python, C, .NET and Unity. From €1,189 excl. VAT ([prices](../../prices/unicorn-prices.md)).

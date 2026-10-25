# Pattern-reversal VEP from the open Unicorn BCI Core-8 dataset.
# Usage: python vep.py UnicornRawDataRecorder_15_07_2026_16_32_310.csv vep.png
# Data: https://github.com/unicorn-bi/Unicorn-BCI-Core-8-EEG-Datasets/tree/main/Datasets/VEPReversal/raw
import sys,numpy as np
from scipy.signal import butter,filtfilt,iirnotch
f=sys.argv[1]; out=sys.argv[2]
d=np.loadtxt(f,delimiter=',',skiprows=1)
fs=250; eeg=d[:,:8]; trig=d[:,13]
print('unique trig',np.unique(trig))
b,a=butter(4,[0.5,40],btype='band',fs=fs); x=filtfilt(b,a,eeg,axis=0)
for h in (50,100):
  bn,an=iirnotch(h,30,fs); x=filtfilt(bn,an,x,axis=0)
on=np.where((trig[1:]!=0)&(trig[:-1]==0))[0]+1
print('events',len(on))
pre,post=int(.1*fs),int(.7*fs)
ep=np.array([x[i-pre:i+post] for i in on if i-pre>=0 and i+post<len(x)])
ep-=ep[:,:pre].mean(1,keepdims=True)
names=['Fz','C3','Cz','C4','Pz','PO7','POz','PO8']
avg=ep.mean(0); t=(np.arange(-pre,post))/fs*1000
poz=avg[:,6]; bip=avg[:,6]-avg[:,0]
for nm,s in (('POz',poz),('POz-Fz',bip)):
  w=(t>=80)&(t<=140); p=t[w][np.argmax(s[w])]; pv=s[w].max()
  wn=(t>=50)&(t<=95); nv=s[wn].min()
  wn2=(t>=120)&(t<=200); n2=s[wn2].min()
  print(f'{nm}: P100 {pv:.2f} uV at {p:.0f} ms; N75 {nv:.2f}; N135 {n2:.2f}; N75-P100 p2p {pv-nv:.2f} uV')
# single-trial noise in baseline
print('baseline RMS of average (POz) %.2f uV; trials %d'%(np.sqrt((poz[:pre]**2).mean()),len(ep)))
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,3.6),dpi=150)
bt=ep[:,:,6]-ep[:,:,0]; se=bt.std(0)/np.sqrt(len(ep))
ax.fill_between(t,bip-se,bip+se,color='#9bb7d4',alpha=.6,lw=0,label='± standard error')
ax.plot(t,bip,color='#1f4e79',lw=2,label=f'POz–Fz, average of {len(ep)} reversals')
ax.axvline(0,color='k',lw=.8,ls='--'); ax.axhline(0,color='k',lw=.5)
ax.set_xlabel('Time after checkerboard reversal (ms)'); ax.set_ylabel('Amplitude (µV)')
ax.set_title('Pattern-reversal VEP, Unicorn BCI Core-8, dry g.SAHARA electrodes')
ax.legend(frameon=False,fontsize=8,loc='lower right'); ax.set_xlim(-100,700)
for s in ('top','right'): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(out)

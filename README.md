### Architecture

We take audio data, trim it and align it to tempo (which is provided alongside the audio data).

Then we split the audio data into segments with length of `x` samples 
(where x is [Thirty-second note](https://en.wikipedia.org/wiki/Thirty-second_note) of the audio data in the
 specified tempo at the sample rate of the specified audio).

From these segments we create [Mel](https://en.wikipedia.org/wiki/Mel_scale)
 [spectrogram](https://en.wikipedia.org/wiki/Spectrogram) which tries to encode the essential 
 information of the audio data in reduced number of bytes.

We feed these segments into recurrent neural network which should generate the resulting beat saber notes
 for the specified segment (after seeing previous segments).
 
 
### Beat saber notes 

Each note in beat saber has horizontal and vertical position (one of 12 positions in total), one of 9 cut
 directions and a color.

![bs notes](https://noshilog.com/wp-content/uploads/2018/09/beat-saber-mapping-guide-3d-editor-01.jpg)

### Beat saber file (enums) reference

```typescript
enum HorizontalPosition
{
    Left = 0,
    CenterLeft = 1,
    CenterRight = 2,
    Right = 3
}

enum VerticalPosition
{
    Bottom = 0,
    Middle = 1,
    Top = 2
}

enum Color
{
    Left = 0,
    Right = 1,
    Bomb = 3
}

enum CutDirection
{
    Up = 0,
    Down = 1,
    Left = 2,
    Right = 3,
    UpLeft = 4,
    UpRight = 5,
    DownLeft = 6,
    DownRight = 7,
    Any = 8
}
```


### Related projects

- random, based on beat detection - https://github.com/mindleaving/beatsabertools/tree/master/BeatSaberSongGenerator



### Notes

https://nlml.github.io/neural-networks/detecting-bpm-neural-networks/
https://towardsdatascience.com/audio-classification-using-fastai-and-on-the-fly-frequency-transforms-4dbe1b540f89
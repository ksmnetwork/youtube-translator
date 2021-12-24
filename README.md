### Simple Python script to scrape youtube channles of "Parity Technologies and Web3 Foundation" and translate them to well-known braille language or any language

The script can be used for any channel or video for scraping, in addition will provide you with the option to get any automatic captions. Automatic captions are available in Dutch, English, French, German, Indonesian, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Turkish, Vietnamese and more or any, so use it as you wish.

usage:
```python
pip install youtube_transcript_api scrapetube codext
python tube.py
```

Get all videos for a channel

```python
import scrapetube

videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")

for video in videos:
    print(video['videoId'])
```

Filter for manually created transcripts

```python
transcript = transcript_list.find_manually_created_transcript(['de', 'en'])
```
or automatically generated ones
```python
transcript = transcript_list.find_generated_transcript(['de', 'en'])
```

The methods find_generated_transcript, find_manually_created_transcript, find_generated_transcript return Transcript objects. They contain metadata regarding the transcript:
```python
print(
    transcript.video_id,
    transcript.language,
    transcript.language_code,
    # whether it has been manually created or generated by YouTube
    transcript.is_generated,
    # whether this transcript can be translated or not
    transcript.is_translatable,
    # a list of languages the transcript can be translated to
    transcript.translation_languages,
)
```

Codext, contraction of "codecs" and "extension", is a tiny library that gathers a few additional encodings for use with codecs. While imported, it registers new encodings to a proxy codecs registry for making the encodings available from the codecs.(decode|encode|open) calls.

Currently set on Braille codext.encode("Little Endian", "braille") accept even morse

Codecs categories

* native: the built-in codecs from the original codecs package
* non-native: this special category regroups all the categories mentioned hereafter
* base: baseX codecs (e.g. base, base100)
* binary: codecs working on strings but applying their algorithms on their binary forms (e.g. baudot, manchester)
* common: common codecs not included in the native ones or simly added for the purpose of standardization (e.g. octal, ordinal)
* crypto: codecs related to cryptography algorithms (e.g. barbie, rot, xor)
* language: language-related codecs (e.g. morse, navajo)
* other: uncategorized codecs (e.g. letters, url)
* stegano: steganography-related codecs (e.g. sms, resistor)
* Except the native and non-native categories, the other ones are simply the name of the subdirectories (with "s" right-stripped) of the codext package.

```python
codext.list("binary")
['baudot', 'baudot-spaced', 'baudot-tape', 'bcd', 'bcd-extended0', 'bcd-extended1', 'excess3', 'gray', 'manchester', 'manchester-inverted']
codext.list("language")
['braille', 'leet', 'morse', 'navajo', 'radio', 'southpark', 'southpark-icase', 'tom-tom']
codext.list("native")
['ascii', 'base64_codec', 'big5', 'big5hkscs', 'bz2_codec', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp775', 'cp850', 'cp852', 'cp855', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', ...]
```

Current channels for scrapping the transcript subtitles in English language and translate them to Braille language
* Web3 Foundation
* https://www.youtube.com/channel/UClnw_bcNg4CAzF772qEtq4g
* Parity Technologies
* https://www.youtube.com/channel/UCSs5vZi0U7qHLkUjF3QnaWg

Up to you list, just replace the Youtube channel ID string at :exploding_head:
```python
videoListName = scrapetube.get_channel("UClnw_bcNg4CAzF772qEtq4g")
```
[YouTube uses automatic speech recognition to add automatic captions to videos. The feature is available in English, Dutch, French, German, Italian, Japanese, Korean, Portuguese, Russian, and Spanish. ASR is not available for all videos.](https://support.google.com/youtube/answer/7296221?hl=en#:~:text=YouTube%20uses%20automatic%20speech%20recognition,not%20available%20for%20all%20videos.)

You can eding the language at :innocent:
```python
transcript = transcript_list.find_generated_transcript(['en']).fetch()
```
Example output:
```
https://www.youtube.com/watch?v=ouMK-Q9S7cc
Web3 Foundation - The Next Evolution of the Internet - Dr. Gavin Wood
⠺⠑⠃⠒⠀⠋⠕⠥⠝⠙⠁⠞⠊⠕⠝⠀⠤⠀⠞⠓⠑⠀⠝⠑⠭⠞⠀⠑⠧⠕⠇⠥⠞⠊⠕⠝⠀⠕⠋⠀⠞⠓⠑⠀⠊⠝⠞⠑⠗⠝⠑⠞⠀⠤⠀⠙⠗⠨⠀⠛⠁⠧⠊⠝⠀⠺⠕⠕⠙
⠊⠀⠞⠓⠊⠝⠅⠀⠞⠓⠑⠗⠑⠀⠺⠑⠗⠑⠀⠁⠀⠇⠕⠞⠀⠕⠋⠀⠏⠑⠕⠏⠇⠑⠀⠞⠓⠁⠞⠀⠗⠑⠁⠇⠇⠽⠀⠃⠑⠇⠊⠑⠧⠑⠙⠀⠞⠓⠑⠀⠊⠝⠞⠑⠗⠝⠑⠞⠀⠺⠁⠎⠀⠺⠁⠎⠀⠛⠕⠝⠝⠁⠀⠃⠑⠀⠁⠀⠞⠗⠁⠝⠎⠋⠕⠗⠍⠁⠞⠊⠧⠑⠀⠞⠑⠉⠓⠝⠕⠇⠕⠛⠽⠀⠋⠕⠗⠀⠎⠕⠉⠊⠑⠞⠽⠀⠁⠝⠙⠀⠊⠀⠞⠓⠊⠝⠅⠀⠺⠓⠁⠞⠀⠓⠁⠏⠏⠑⠝⠑⠙⠀⠺⠁⠎⠀⠞⠓⠑⠀⠊⠝⠞⠑⠗⠝⠑⠞⠀⠺⠁⠎⠀⠙⠑⠎⠊⠛⠝⠑⠙⠀⠊⠝⠀⠎⠥⠉⠓⠀⠁⠀⠺⠁⠽⠀⠞⠓⠁⠞⠀⠊⠞⠀⠁⠇⠇⠕⠺⠑⠙⠀⠊⠞⠀⠺⠁⠎⠀⠋⠇⠑⠭⠊⠃⠇⠑⠀⠊⠞⠀⠁⠇⠇⠕⠺⠑⠙⠀⠑⠭⠊⠎⠞⠊⠝⠛⠀⠎⠞⠗⠥⠉⠞⠥⠗⠑⠎⠀⠕⠋⠀⠎⠕⠉⠊⠑⠞⠽⠀⠑⠭⠊⠎⠞⠊⠝⠛⠀⠺⠁⠽⠎⠀⠕⠋⠀⠙⠕⠊⠝⠛⠀⠃⠥⠎⠊⠝⠑⠎⠎⠀⠞⠕⠀⠎⠊⠍⠏⠇⠽⠀⠍⠕⠧⠑⠀⠕⠧⠑⠗⠀⠕⠝⠞⠕⠀⠞⠓⠑⠀⠙⠊⠛⠊⠞⠁⠇⠀⠙⠕⠍⠁⠊⠝⠀⠎⠕⠀⠺⠓⠑⠝⠀⠺⠑⠀⠙⠕⠀⠃⠁⠝⠅⠊⠝⠛⠀⠕⠝⠀⠞⠓⠑⠀⠊⠝⠞⠑⠗⠝⠑⠞⠀⠺⠑⠀⠎⠞⠊⠇⠇⠀⠥⠎⠑⠀⠁⠀⠃⠁⠝⠅⠀⠺⠑⠀⠎⠞⠊⠇⠇⠀⠥⠎⠑⠀⠕⠥⠗⠀⠑⠭⠊⠎⠞⠊⠝⠛⠀⠃⠗⠊⠉⠅⠤⠁⠝⠙⠤⠍⠕⠗⠞⠁⠗⠀⠞⠗⠁⠙⠊⠞⠊⠕⠝⠁⠇⠀⠲⠴⠴⠀⠽⠑⠁⠗⠀⠕⠇⠙⠀⠃⠁⠝⠅⠊⠝⠛⠀⠕⠗⠛⠁⠝⠊⠵⠁⠞⠊⠕⠝⠀⠊⠞⠄⠎⠀⠚⠥⠎⠞⠀⠞⠓⠁⠞⠀⠺⠑⠀⠁⠉⠉⠑⠎⠎⠀⠞⠓⠑⠍⠀⠞⠓⠗⠕⠥⠛⠓⠀⠁⠀⠺⠑⠃⠀⠏⠁⠛⠑⠀⠊⠞⠀⠓⠁⠎⠝⠄⠞⠀⠗⠑⠁⠇⠇⠽⠀⠁⠇⠞⠑⠗⠑⠙⠀⠎⠕⠉⠊⠑⠞⠽⠀⠊⠞⠀⠗⠑⠁⠇⠇⠽⠀⠺⠁⠎⠝⠄⠞⠀⠞⠗⠁⠝⠎⠋⠕⠗⠍⠁⠞⠊⠧⠑⠀⠁⠝⠙⠀⠊⠀⠞⠓⠊⠝⠅⠀⠞⠓⠁⠞⠄⠎⠀⠞⠓⠁⠞⠄⠎⠀⠑⠧⠑⠗⠍⠕⠗⠑⠀⠉⠇⠑⠁⠗⠀⠺⠓⠑⠝⠀⠺⠑⠀⠺⠓⠑⠝⠀⠺⠑⠀⠞⠓⠊⠝⠅⠀⠁⠃⠕⠥⠞⠀⠋⠁⠉⠑⠃⠕⠕⠅⠀⠁⠝⠙⠀⠺⠑⠀⠞⠓⠊⠝⠅⠀⠁⠃⠕⠥⠞⠀⠛⠕⠕⠛⠇⠑⠀⠞⠓⠑⠎⠑⠀⠁⠗⠑⠀⠝⠕⠞⠀⠝⠑⠺⠀⠺⠁⠽⠎⠀⠕⠋⠀⠺⠕⠗⠅⠊⠝⠛⠀⠝⠑⠺⠀⠺⠁⠽⠎⠀⠕⠋⠀⠏⠑⠕⠏⠇⠑⠀⠺⠕⠗⠅⠊⠝⠛⠀⠞⠕⠛⠑⠞⠓⠑⠗⠀⠊⠝⠀⠗⠑⠁⠇⠊⠞⠽⠀⠞⠓⠑⠽⠄⠗⠑⠀⠞⠓⠑⠀⠎⠁⠍⠑⠀⠅⠊⠝⠙⠎⠀⠕⠋⠀⠎⠞⠗⠥⠉⠞⠥⠗⠑⠎⠀⠞⠓⠁⠞⠀⠞⠓⠑⠀⠎⠁⠍⠑⠀⠓⠊⠑⠗⠁⠗⠉⠓⠊⠉⠁⠇⠀⠕⠗⠛⠁⠝⠊⠵⠁⠞⠊⠕⠝⠎⠀⠞⠓⠁⠞⠀⠓⠁⠧⠑⠀⠞⠓⠑⠀⠎⠁⠍⠑⠀⠉⠑⠝⠞⠗⠁⠇⠊⠵⠑⠙⠀⠃⠁⠝⠅⠀⠁⠉⠉⠕⠥⠝⠞⠎⠀⠞⠓⠁⠞⠀⠓⠁⠧⠑⠀⠞⠓⠑⠀⠎⠁⠍⠑⠀⠎⠕⠗⠞⠀⠕⠋⠀⠍⠥⠇⠞⠊⠝⠁⠞⠊⠕⠝⠁⠇⠀⠎⠞⠗⠥⠉⠞⠥⠗⠑⠀⠁⠎⠀⠁⠇⠇⠀⠕⠋⠀⠞⠓⠑⠀⠧⠁⠗⠊⠕⠥⠎⠀⠕⠞⠓⠑⠗⠀⠋⠕⠗⠞⠥⠝⠑⠀⠢⠴⠴⠀⠉⠕⠗⠏⠕⠗⠁⠞⠑⠀⠉⠕⠍⠏⠁⠝⠊⠑⠎⠀⠊⠝⠀⠗⠑⠁⠇⠊⠞⠽⠀⠞⠕⠀⠉⠓⠁⠝⠛⠑⠀⠎⠕⠉⠊⠑⠞⠽⠀⠺⠑⠀⠗⠑⠁⠇⠇⠽⠀⠝⠑⠑⠙⠀⠞⠕⠀⠙⠕⠀⠎⠕⠍⠑⠞⠓⠊⠝⠛⠀⠃⠑⠞⠞⠑⠗⠀⠞⠓⠁⠝⠀⠉⠗⠑⠁⠞⠊⠝⠛⠀⠞⠑⠉⠓⠝⠕⠇⠕⠛⠊⠑⠎⠀⠞⠓⠁⠞⠀⠚⠥⠎⠞⠀⠁⠇⠇⠕⠺⠀⠥⠎⠀⠞⠕⠀⠍⠊⠗⠗⠕⠗⠀⠓⠕⠺⠀⠎⠕⠉⠊⠑⠞⠽⠀⠺⠕⠗⠅⠎⠀⠁⠝⠽⠺⠁⠽⠀⠺⠑⠀⠝⠑⠑⠙⠀⠞⠕⠀⠉⠗⠑⠁⠞⠑⠀⠞⠑⠉⠓⠝⠕⠇⠕⠛⠊⠑⠎⠀⠞⠓⠁⠞⠀⠋⠕⠗⠛⠑⠀⠝⠑⠺⠀⠺⠁⠽⠎⠀⠕⠋⠀⠃⠑⠊⠝⠛⠀⠁⠃⠇⠑⠀⠞⠕⠀⠺⠕⠗⠅⠀⠺⠊⠞⠓⠀⠑⠁⠉⠓⠀⠕⠞⠓⠑⠗⠀⠁⠝⠙⠀⠞⠓⠁⠞⠄⠎⠀⠙⠊⠋⠋⠑⠗⠑⠝⠞⠀⠞⠕⠀⠝⠑⠺⠀⠺⠁⠽⠎⠀⠕⠋⠀⠃⠑⠊⠝⠛⠀⠁⠃⠇⠑⠀⠞⠕⠀⠉⠕⠍⠍⠥⠝⠊⠉⠁⠞⠑⠀⠺⠊⠞⠓⠀⠑⠁⠉⠓⠀⠕⠞⠓⠑⠗⠀⠊⠞⠄⠎⠀⠁⠇⠎⠕⠀⠛⠕⠞⠀⠞⠕⠀⠃⠑⠀⠝⠑⠺⠀⠺⠁⠽⠎⠀⠕⠋⠀⠃⠑⠊⠝⠛⠀⠁⠃⠇⠑⠀⠞⠕⠀⠕⠗⠛⠁⠝⠊⠵⠑⠀⠁⠝⠙⠀⠞⠗⠥⠎⠞⠀⠞⠓⠁⠞⠀⠑⠁⠉⠓⠀⠕⠞⠓⠑⠗⠀⠊⠎⠀⠛⠕⠊⠝⠛⠀⠞⠕⠀⠙⠕⠀⠺⠓⠁⠞⠀⠺⠓⠁⠞⠀⠞⠓⠑⠽⠀⠝⠑⠑⠙⠀⠞⠕⠀⠙⠕⠀⠊⠝⠀⠕⠗⠙⠑⠗⠀⠞⠕⠀⠓⠁⠧⠑⠀⠎⠕⠍⠑⠀⠎⠕⠗⠞⠀⠕⠋⠀⠎⠓⠁⠗⠑⠙⠀⠉⠕⠝⠉⠇⠥⠎⠊⠕⠝⠀⠕⠗⠀⠗⠁⠍⠊⠋⠊⠉⠁⠞⠊⠕⠝⠀⠞⠕⠀⠞⠓⠑⠀⠉⠕⠕⠏⠑⠗⠁⠞⠊⠕⠝⠀⠁⠝⠙⠀⠞⠓⠁⠞⠄⠎⠀⠗⠑⠁⠇⠇⠽⠀⠁⠀⠃⠊⠛⠀⠉⠕⠍⠏⠕⠝⠑⠝⠞⠀⠕⠋⠀⠺⠑⠃⠀⠒⠀⠺⠑⠃⠀⠒⠀⠊⠎⠀⠗⠑⠁⠇⠇⠽⠀⠁⠃⠕⠥⠞⠀⠁⠇⠇⠕⠺⠊⠝⠛⠀⠏⠑⠕⠏⠇⠑⠀⠞⠕⠀⠉⠕⠍⠑⠀⠞⠕⠛⠑⠞⠓⠑⠗⠀⠁⠝⠙⠀⠉⠕⠕⠗⠙⠊⠝⠁⠞⠑⠀⠞⠓⠑⠊⠗⠀⠑⠋⠋⠕⠗⠞⠎⠀⠋⠕⠗⠀⠎⠕⠍⠑⠞⠓⠊⠝⠛⠀⠛⠗⠑⠁⠞⠑⠗⠀⠞⠓⠑⠀⠞⠓⠁⠝⠀⠞⠓⠑⠀⠎⠥⠍⠀⠕⠋⠀⠊⠞⠎⠀⠏⠁⠗⠞⠎⠀⠪⠍⠥⠎⠊⠉⠻
```

With Git Actions Workflow file for this run as example in real-time
```yaml
name: Git Actions as example of the output in real-time
on: [push]
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest]
        python-version: ['3.6', '3.9']
        exclude:
          - os: ubuntu-latest
            python-version: '3.6'
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies 
        run: pip install youtube_transcript_api scrapetube codext
      - name: Web3 Foundation videos to braille language 
        run: python tube.py
```

---
### For Support && Nominations #
* Display name. KSMNETWORK 
* Email w3f@ksm.network
* Riot @gtoocool:matrix.org

* KUSAMA (KSM) Address
* ```H1bSKJxoxzxYRCdGQutVqFGeW7xU3AcN6vyEdZBU7Qb1rsZ```

* PolkaDOT (DOT) Address:
* ```15FxvBFDd3X7H9qcMGqsiuvFYEg4D3mBoTA2LQufreysTHKA```

* https://ksm.network

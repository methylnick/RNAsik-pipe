
![mbp-banner](images/mbp_banner.png)

# RNAsik? yep!

## Getting help

There is an open [RNAsik user's google group](https://groups.google.com/forum/#!forum/rnasik) anyone can ask and answer
questions there. I will try my best to respond to any questions there, but bear in mind that I could get saturated with work
and might not be able to respond straight away.

Also couple of house keeping things:

- be polite (in general) and considerate of others.
- Include as much information about your problem as you can. State what you tried to do and the error message you got as a minimum
- The problem needs to be reproducible, otherwise I might not be able to help you.

p.s:F eedback and suggestions are also welcomed there

## Bug reports

Best place to submit bugs is with [GitHub issues](https://github.com/MonashBioinformaticsPlatform/RNAsik-pipe/issues)
Try to include as much information as you can and again the problem needs to be reproducible. Sometimes, the problem could be 
BigDataScript specific so also try looking at [BigDataScrip user's group](https://groups.google.com/forum/#!forum/bigdatascript-users)

## Contributing
 
There are many places you could contribute including documentation, discussions in the 
[google group](https://groups.google.com/forum/#!forum/rnasik) and of course with the source code itself.

### Documentation

I'm using [mkdocs](https://github.com/mkdocs/mkdocs) to generate this site, which has been very easy to use.
All documentation are written in plain markdown and located in the main repo 
[`docs/` directory](https://github.com/MonashBioinformaticsPlatform/RNAsik-pipe/tree/master/docs). 
To contribute, You can simply fork this `RNAsik` repository, do appropriate changes to the docs and send me a pull request (PR). 
Any small changes are super welcome, even one letter spell correction (there'll be more than one), but all changes need to come 
through as a pull request (PR), which will not only acknowledge you as contributor, but also enable me to review changes quickly 
and incorporate them in (pull them in) to the main repo  easily.

Quick notes on [mkdocs](https://github.com/mkdocs/mkdocs), it is pretty easy to install with `pip` in `virtualenv` if you prefer 
(you should).

```
git clone https://github.com/MonashBioinformaticsPlatform/RNAsik-pipe
cd RNAsik-pipe
mkdocs serve
```

This will give you live updates to your copy of the docs, default URL should be [localhost:8000](localhost:8000), but it will tell 
you that once you've started the server. Then simply use your favourite text editor to edit markdown documents. Commit your changes, 
don't be afraid to be verbose, say what you've added/changed/removed in your commit message. And send me a PR

### User's group

[Just jump in and do it at the google groups site!](https://groups.google.com/forum/#!forum/rnasik)

### Developing pipeline further

I need to write a more comprehensive developer guide at sometime soon. Any contributions to the source code  are extremely welcomed.
Again, as I've mentioned with the [Documentation](#documentations) section above, any contributions need to come through pull request (PR). 

To summarise briefly layouts of the `src/`:

- `RNAsik.bds` is main "executable" file that sources and runs the pipeline. 
- `sikHeader.bds` defines help menu and all user inputs options. I do have a couple of command line 
arguments hidden from main help menu, but if you take a pick at this file you'll see them all
- All other `*.bds` files contain functions to specific tasks those functions get called in `RNAsik.bds`

![team_photo_2017](images/team_photo_2017.jpg)


<p><a href="https://twitter.com/intent/tweet?screen_name=kizza_a" class="twitter-mention-button" data-size="large" data-show-count="false">Tweet to @kizza_a</a><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script> </p>

<p class="twitter-btn">
<a class="twitter-share-button"
  href="https://twitter.com/intent/tweet?text=Hey%20I%27m%20using%20this%20fully%20sick%20RNAseq%20pipeline%20It%27s%20sik%20easy%20http%3A%2F%2Fgithub%2Ecom%2Fmonashbioinformaticsplatform%2FRNAsik%2Dpipe%20by%20%40kizza%5Fa%20from%20%40MonashBioinfo" data-size="large">
Share</a>
</p>

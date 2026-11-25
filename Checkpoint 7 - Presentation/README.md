# Our Presentation: Setup and how to run

Our presentation for the data science project is in [reveal.js](https://revealjs.com/).
See below for how to set it up on your local machine and how to get started.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Our Presentation: Setup and how to run](#our-presentation-setup-and-how-to-run)
  - [Table of Contents ](#table-of-contents)
  - [Installing Dependencies](#installing-dependencies)

<!-- markdown-toc end -->
 
## Installing Dependencies

We make use of the [external markdown plugin](https://revealjs.com/markdown/#external-markdown) of reveal.js,
so you must do the [full setup](https://revealjs.com/installation/#full-setup) 
which requires that you have Node.js `20.19.0` or later:

``` sh
npm install reveal.js
```

## How to run

Run the following in the Checkpoint 7 directory
(this will start a development server on `localhost:8000`
via `python -m http.server --bind 127.0.0.1`):

``` sh
npm start
```

Or if you want to run on a different port:

``` sh
npm start -- 8001
```

## Writing the slides

We will write our slides in the various `set*` files in the root of this folder. 

> Why not put the markdown slideset files into their own directory?
> 
> Well, we don't have a large number of markdown files, so it's not too much clutter to put them in the root fo the checkpoint directory.
> Additionally, putting them here instead of in some subdirectory will make file links transparent between the markdown source and the load path for the actual presentation.

See the reveal.js [documentation](https://revealjs.com/markdown/) on how to write your presentation slides in Markdown.
Also see the Markdown [example](https://github.com/hakimel/reveal.js/blob/master/examples/markdown.md?plain=1).

### Images and media

Be sure to copy any pictures or media into the `./assets/` directory and link to them that way in the markdown slideset file.
This is because the server will run from this checkpoint directory and not the repository root.

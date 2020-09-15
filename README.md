# The Netlogo Interactive Dictionary

## Tech Stack Overview
The production site itself is just a series of static html files that can be served by any basic webserver. These static files are generated via `frozen-flask`, a Python Flask plugin that lets you save given url's from a flask server into static html. The flask server does all the work of pulling the data from 1) a google sheet with metadata about all the primitives and 2) markdown files with the actual descriptions of the primitives and 3) `.nlogo` files for all the example models and wrapping it all up together into the final site. When developing, you should be able to treat the flask debug site as if it were the real thing with two exceptions: 
    - all links must end in .html. If you want to link to the list of articles, you need to link to `/articles.html`, not `/articles`.   
    - If you add a new *dynamic* flask route, (i.e., one with a `<parameter>` in the url), then you need to tell the freeze script what all the possible valid values for that parameter are. (See the freeze script for examples of what that looks like.)

## Misc:
- When adding jQuery, instead of writing `$()`, you need to write `$local()`. This is because the netlogo web will bring in its own version of jQuery that conflicts with the one we want to use which causes all sorts of hard to track down bugs. `$local` is the local version that won't get clobbered. See jQuery's documentation on `.noConflict()` for more. 
- Feel free to include the "?" in primitives like `any?` and `all?` in the metadata google sheet. The code will automatically strip them out where it would cause a problem.
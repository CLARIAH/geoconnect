# geoconnectables or mapping the priests: tools from four international networks in one pipeline.

In this data story, we are going to show how you can combine tools from *four different international networks* into a single *pipeline to visualize* data from a CSV onto a map image, whilst offering it as Linked Open Data.

## Starting in the 16th century...
A long time ago in a galax..., well actually in this galaxy and in a place that we call 'The Netherlands', at least nowadays... What we now from that era may not be a lot, but for an important group of people, those who would rise in the ranks of religious orders we know quite a lot. For example, we know, where they were born... and that might be a little more interesting than you'd expect... because was faith random? Did the divine call spread evenly across the country? Or were those of the cloth born, in the vicinity of churces, where the influence of religious orders was strong.

## Step 1: transpose CSV to Linked Data
The first thing we did was to create Linked Data from a CSV file using the [LDWizard](https://ldwizard.netwerkdigitaalerfgoed.nl/1) a tool brought to you by the [Dutch Digital Heritage Network](https://www.netwerkdigitaalerfgoed.nl). Please see this [demo](https://www.youtube.com/watch?v=VO61pqKWw7A) on how you can do it yourself.

One really cool feature of the LDWizard is that through its design everyone can create their own 'flavour' of LDWizard. For this [Hack-a-LOD](https://hackalod.com) Jorrit from Kadaster created a geo-flavoured LDWizard, that allows you to directly transpose geo coordinates into properly defined Linked Data. This allows us to easily visualize data and to perform geo related sparql queries, for example whether something is close to something else. 

This feature proved to be crucial: our 16th century place names, did not at all resemble contemporary place names: e.g. "Oculo" back then, is "Schiermonnikoog" now. Now your average regex excercise...

## Step 2: match via geographic proximity
So in order to relate anything contemporary to our 16th century data, we decided to match the historical places based on their geographic location to contemporary places. For the contemporary places we used Kadaster's [BRT](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt) which is already available via this [endpoint](https://data.labs.kadaster.nl/kadaster-dev/-/queries/). We uploaded the geo-LDWizard RDF representation of the birthplaces csv file to an instance of [TriplyDB](https://triplydb.com). As a result we could write a federated query, retrieving both contemporary and historical information on the birth places of priests. See this [example query](https://data.labs.kadaster.nl/kadaster-dev/-/queries/Find-a-Dutch-place-for-a-given-point/9), for Schiermonnikoog.



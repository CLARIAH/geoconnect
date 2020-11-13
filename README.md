# geoconnectables or mapping the priests: tools from four international networks in one pipeline.

In this data story, we are going to show how you can combine tools from *four different international networks* into a single *pipeline to visualize* data from a CSV onto a map image, whilst offering it as Linked Open Data.

## Starting in the 16th century...
A long time ago in a galax..., well actually in this galaxy and in a place that we call 'The Netherlands', at least nowadays... What we now from that era may not be a lot, but for an important group of people, those who would rise in the ranks of religious orders we know quite a lot. For example, we know, where they were born... and that might be a little more interesting than you'd expect... because was faith random? Did the divine call spread evenly across the country? Or were those of the cloth born, in the vicinity of churces, where the influence of religious orders was strong.

## Step 1: transpose CSV to Linked Data
The first thing we did was to create Linked Data from a CSV file using the [LDWizard](https://ldwizard.netwerkdigitaalerfgoed.nl/1) a tool brought to you by the [Dutch Digital Heritage Network](https://www.netwerkdigitaalerfgoed.nl). Please see this [demo](https://www.youtube.com/watch?v=VO61pqKWw7A) on how you can do it yourself.

One really cool feature of the LDWizard is that through its design everyone can create their own 'flavour' of LDWizard. For this [Hack-a-LOD](https://hackalod.com) Jorrit from Kadaster created a geo-flavoured LDWizard, that allows you to directly transpose geo coordinates into properly defined Linked Data. This allows us to easily visualize data and to perform geo related sparql queries, for example whether something is close to something else. 

This feature proved to be crucial: our 16th century place names, did not at all resemble contemporary place names: e.g. "Oculo" back then, is "Schiermonnikoog" now. Now your average regex excercise...

## Step 2: match via geographic proximity
So in order to relate anything contemporary to our 16th century data, we decided to match the historical places based on their geographic location to contemporary places. For the contemporary places we used Kadaster's [BRT](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brt) which is already available via this [endpoint](https://data.labs.kadaster.nl/kadaster-dev/-/queries/). We uploaded the geo-LDWizard RDF representation of the birthplaces csv file to an instance of [TriplyDB](https://triplydb.com). As a result we could write a federated query, retrieving both contemporary and historical information on the birth places of priests. 

__Query__: See this [example query](https://data.labs.kadaster.nl/kadaster-dev/-/queries/Find-a-Dutch-place-for-a-given-point/9), for Schiermonnikoog.

## Step 3: eye candy or not
When presenting historic map visualizations an often heard complaint at conference is that contemporary maps are ugly (or even 'evil') as layer for the actual visualization. And to be fair, especially in the case of the Netherlands, it is awkward to read place names, see bridges and highways, where 500 years ago, there was nothing but sea. It cast a shadow on the accuratess of the academic work.

Now there are ton of tools that dealt with this problem, and actually a very good one is QGIS. But even QGIS requires, well.. QGIS yet another tool in the pipeline. So instead, [Triply](https://triply.cc) brought a new feature to their triple store, that allows you to use maps as underlays, as long as these maps are provided as a WMS service from a secure website (https://). This even works, when you don't have access to the triplestore, via a federated query. So how do we get a map?

Well, to my knowledge orginating from the New York Public Library, mapwarper is a very decent piece of tooling that allows you to host maps, georeference them and provde them as .kml and WMS (amongst others). For our use case, we decided to pick a map that probably qualifies for the golden raspberry amongst maps: https://mapwarper.net/maps/40981. That said, many kudos to mapwarper.net for providing this excellent service and don't forget to [donate](https://paypal.me/timdevelops) to this good cause. So brace your eyes, here goes map overlaying via SPARQL:

__Query__: 



__Query__: See this [example query](https://druid.datalegend.net/dataLegend/-/queries/kloosters-toen-kadaster-nu/1)




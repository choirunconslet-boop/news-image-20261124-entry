# The World — Tuesday, 24 November 2026

A newspaper-style front page summing up the world news of Tuesday
24 November 2026 in one 1024×1024 image, for the make.fun bounty
`news-image-20261124`.

## How it is built

`draw.py` draws the page with PIL: masthead, a lead story, six news
panels and an "In Brief" strip. The lead picture is an AI-generated
editorial illustration (`hero.jpg`, made with the media image tool —
chip and rising market, burning warship, fighter jets over an island,
tankers at a strait; no text in the artwork), cropped into the lead
panel; all headlines and body text are crisp PIL vector drawing so
every word stays legible. `main.ts` copies the finished `entry.png`
into `$MAKEFUN_OUTPUT_DIR` (default `/output`), deterministically,
and fails loudly instead of writing nothing if the image is missing.

Run it:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Stories (each cross-checked in at least two live sources)

- **Lead — Tech:** Nvidia's board unanimously reinstates Jensen Huang
  as CEO, effective immediately, after pressure from President Trump;
  shares jump by about a third, Nasdaq +6%. The US blacklists
  Singapore chip firm Megaspeed (Reuters, WSJ, CNN, NY Post).
- **Libya:** Ukrainian sea drones sink the Russian corvette Merkury in
  Benghazi port, hit the cargo ship MV Angara and destroy a Ka-27
  helicopter; President Zelenskiy calls it an "exemplary" operation
  (CNN, WSJ, AP).
- **Korea:** Russian military aircraft enter South Korea's air defence
  zone on the morning of 24 November; Seoul scrambles fighters and an
  emergency alert goes out for Ulleung Island. No airspace violation
  (Aju Press, Yonhap via KBS).
- **Gulf:** Iran resumes strikes on US assets in the Gulf; the US
  shoots down Iranian drones headed for Bahrain and sanctions
  25+ entities in Iran's "shadow banking" network (Reuters, Al Jazeera,
  The Brief Brief).
- **Kyiv:** Russian strikes kill 14 in the Kyiv region and damage 21
  sites, including homes — the toll from Monday's barrage
  (The True Story, Reuters).
- **Tech law:** Virginia and Oregon sue SpaceX, alleging Grok's
  "spicy mode" created sexual images, including of children
  (Al Jazeera, The True Story).
- **Spain:** Polls put Feijóo's Popular Party ahead before the snap
  election on 29 November, on track to oust PM Sánchez
  (The Scribble Post, GazetAI).
- **In brief:** Democrats clinch a House majority of at least 258
  seats, the largest since 1992; NATO vows space defence after a
  report of a Russian nuclear satellite; Colombia files a complaint
  against Starlink over prison signals.

Date note: the Nvidia reinstatement and the Libya sinking were
announced late Monday in the US and led Tuesday 24 November coverage
across Asia and Europe; the KADIZ incident happened on the morning of
24 November itself. Deliberately left out as older news: the COP31
collapse, the Sparta II Baltic incident, the Banten factory fire, the
"El Chapo Isidro" capture and the South Korean education minister's
resignation (all 23 November), the 17 November KADIZ incident (a
different incident), and the Las Vegas Grand Prix (21 November).

## License

MIT — see LICENSE.

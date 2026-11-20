# Netradyne product page

Static product-page prototype featuring D450 and DR40 scroll-driven 360° camera animations, mouse interaction, and illustrated fleet operations cards.

## Preview locally

Requires Python 3; no packages or build step.

```sh
python3 scripts/preview.py
```

Open http://127.0.0.1:8766/netradyne-products.html. If the port is occupied, use `python3 scripts/preview.py --port 8767`.

The preview server supports HTTP byte ranges so browsers can scrub the camera videos.

## Files

- `outputs/netradyne-products.html`: canonical page, styles, and interaction code.
- `outputs/assets/`: desktop/mobile animation videos and fallback images.
- `outputs/product-reference-map.html` and `outputs/references/`: labeled source renderings.
- `outputs/higgsfield-side-instructions.txt`: prompts used for the full-turn animations.
- `index.html`: root entry point for static hosting.

Edit the canonical HTML directly. Generated master videos and temporary working files are excluded from Git. Camera animations are AI-generated; fine details can differ from the reference renders. Product copy is supplied prototype content.

## Railway deployment

Connect `davealex11/Product`, branch `main`, with the repository root `/`. Railway uses the included Dockerfile and Nginx configuration. Leave custom build/start commands unset. The server listens on Railway's `PORT` and supports byte-range video requests.

After a successful deployment, generate a domain in the service networking settings. Both `/` and `/netradyne-products.html` serve the product page. HTML is revalidated on refresh so updates are visible; video assets are cached for one hour.

If pushes do not create deployments, check the service repository/branch, Railway GitHub App repository access, and pending deployment approvals. The local preview server is not the production start command.

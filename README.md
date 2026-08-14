# ai-skills

AI skills built for coaches. Source lives in `skills/`, distributables in `dist/`.

---

## Identity Crisis

**A Contra-Brand kit for coaches.**

Most brand kits produce a well-polished turd. They ask a coach who they are, receive fog, and dress the fog in a nice font. Six weeks later the coach has a color palette, a word cloud, and a website that reads like the other four thousand coaching websites — because everyone answered the same questions and everyone's answers averaged out to *transformation, journey, potential, aligned*.

This one works the other way around. **Contra-Brand** means the identity is built by opposition first and declaration second.

Ask a coach "who are you?" and you get a résumé. Ask "what's the lie in your industry?" and they talk for twenty minutes. The enemy is the crowbar — once it's named, the coach's own hero journey, their client's, and their banned-vocabulary list all fall out nearly for free.

### What it produces

A versioned Brand Bible: positioning, archetype, ideal-client personas as failure modes, a three-layer lexicon with a banned list, voice registers mapped to funnel stages, a copy engine, and a quality bar. Written so a contractor, a staff member, or an AI tool can be handed it and produce something on-brand without the coach in the loop.

### The phases

| | | |
|---|---|---|
| **P0** | Intake | Both paths — history *and* their own past self — regardless of tenure. Failed pivots are the richest material. |
| **P1** | The Enemy | Industrial complex, received wisdom, adjacent category, false cure. Steelman before attacking. |
| **P2** | The Archetype | Jungian, not a tagline. Must pass the extension test or it's decoration. |
| **P3** | The Expensive Problem | The documented stuck point. Gets the most time. "Stress" is not an expensive problem. |
| **P4** | The People | Personas as failure modes of one system. Buying readiness ranked separately from pain. |
| **P5** | The Voice | NO list before YES list. Methodology vocabulary kept verbatim. |
| **P6** | The Stress Test | Ten hard cuts, then falsifiable homework with five real humans. |
| **P7** | Assembly | The Bible. |

Three lenses run through all of it — **transformation brand**, **personal brand**, and **brick-and-mortar** (which carries three audiences: members, staff, and an owner who needs a vision to lead from).

### Four standing passes

Not phases — they fire repeatedly, and they're most of what separates this from a questionnaire.

- **The Inversion Pass** — the opposite of a good idea is also a good idea. Never accept the consensus answer without constructing its genuine inverse first. This is the anti-carbon-copy mechanism; without it, every coach who runs an AI branding exercise gets a slightly reworded version of the same brand.
- **The Generic Detector** — could this paste onto ten other coaches' websites and still fit? Then it's dead.
- **The Vocational-Fit Check** — could you make this argument, every week, for a year, and still want to? Is it pointed at what you're good at or who you wish you were? Most brand kits have no check for this at all, which is why coaches abandon them in month two.
- **The Contradiction Check** — when an existing name or program collides with the identity being built, say so plainly once, then respect the decision.

---

---

## If you're a coach, start here

Read **[docs/identity-crisis-start-here.md](docs/identity-crisis-start-here.md)**. It's plain language, takes three minutes, and covers what to have ready before you sit down. You don't need to understand anything else in this repo.

The short version: download **[dist/Identity-Crisis-single-file.md](dist/Identity-Crisis-single-file.md)**, paste the whole thing into a new chat with Claude or ChatGPT, and say *"Run Identity Crisis on my coaching business."* Set aside 60–90 minutes.

That one file contains the orientation, the skill, and every appendix. Nothing else is needed and nothing gets fetched.

---

## Install

**Claude or ChatGPT** — download `dist/identity-crisis.skill` and open it, or drop the `skills/identity-crisis/` folder into your skills directory. Then say *"Run Identity Crisis on my coaching business"* in any chat.

**Gemini, a web appp, or anything else** — paste `dist/Identity-Crisis-single-file.md` into a new chat. Better: save it as project instructions or a Custom GPT so it stays loaded across sessions.

---

## Repo layout

```
skills/<name>/SKILL.md              source of truth
skills/<name>/references/*.md       loaded on demand in Claude,
                                    inlined as appendices for everything else
docs/<name>-start-here.md           coach-facing orientation; prepended to the
                                    single-file build, kept out of the .skill
                                    so it never burns context
dist/                               built distributables — do not edit by hand
build.py                            regenerates dist/ from skills/
```

## Building

After editing anything under `skills/`:

```bash
python3 build.py
```

Rebuilds every `.skill` archive and every single-file edition. No dependencies beyond the standard library.

---

## Roadmap

- [x] **Identity Crisis** — build the brand identity, personas, and voice
- [ ] **Persona Validation** — test drafted personas against recordings of real market-research interviews, and report where they hold, drift, or were invented
- [ ] **Production Kit** — the visual system: color, typography, logo standards, imagery direction, environment, and video grammar, all derived from the archetype

## License

[CC BY-NC-SA 4.0](LICENSE). Use it to build your own brand, adapt it, share it with other coaches — credit the source and pass along any changes under the same terms. Don't sell it or a derivative as a product.

**Anything you produce with it is entirely yours** — no attribution, no restrictions, commercial use included. The license covers the tool, not what you make with it.

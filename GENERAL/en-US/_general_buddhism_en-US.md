# General Buddhism — Taxonomy & Article Catalog (en-US)

**Version:** 1.0 · **Updated:** 2026-09-19 · **Status:** content framework for the "General Buddhism" section of the app

> **Purpose:** Each `GBxxx` code corresponds to **one standalone article**. The same code can appear under several taxonomy branches; in that case the app stores the article once and attaches multiple categories/tags to it.
>
> **Principle 1 — A learning path, not a ranking.** "Basic → advanced" is a **path for building knowledge**, not a ranking between traditions. Theravāda, Mahāyāna, and Vajrayāna all trace back to the historical Buddha, Śākyamuni; phrasings such as "Theravāda is the root and Mahāyāna is a branch" or "the Vajrayāna is a higher vehicle" are not used in this app.
>
> **Principle 2 — Codes are permanent.** A `GBxxx` code is a **stable ID** and is never renumbered when articles are added or removed. The order of codes in the tree does **not** determine reading order; reading order lives in the *Learning Path* section. A retired code is **never reused**.
>
> **Principle 3 — Same article, same code.** If two entries are truly the same article, they use the same code and the same title. If they merely share a name but cover a different tradition's scope, give them separate codes and make that explicit in the title or metadata.
>
> **Principle 4 — Terminology.** Prefer **Pāli** for Theravāda / Pāli-canon content and **Sanskrit** for Mahāyāna / Vajrayāna content, always alongside the **Sino-Vietnamese (Hán–Việt)** form Vietnamese readers already use; for East Asian and Tibetan proper names, give the original term as well (e.g., buddha-recitation — *niànfó*; Tibetan New Year — *Losar*). See the cross-reference table at the end of the file.
>
> **Principle 5 — Relationship to the Meditation section.** This section presents **general knowledge** (history, doctrine, culture, festivals). Detailed **meditation-practice** content belongs to the Meditation section, coded `Mxxx`; articles here always link out to the matching M-code rather than duplicating that content.

## Level conventions

| Code | Name | Meaning |
|----|-----|---------|
| **L1** | Entry level | Understandable immediately by someone who knows nothing about Buddhism |
| **L2** | Foundational | Core concepts needed to follow other articles |
| **L3** | Intermediate | Assumes familiarity with the foundational concepts; detailed history, school-specific thought |
| **L4** | In-depth | Textual scholarship, complex philosophical thought — for readers who want to go deep |
| **L5** | Requires prerequisites | Practice-linked knowledge tied to transmission/empowerment — *not currently used in this section; see the Meditation section* |
| **R** | Reference | Tables, indexes, FAQs, calendars — not part of the linear learning path |

---

# CONVENTIONS FOR THE NATURE OF THE TAXONOMY

The top-level branches are organized by **the nature of the information**, rather than treating everything as parallel "types of Buddhism":

| Group | Nature | Function in the app |
|---|---|---|
| **A** | `foundation` — orientation for newcomers | Answers "What is Buddhism?" and helps beginners get started the right way |
| **B** | `history` — history | The Buddha's life, the councils, the early schisms, the formation of the three traditions, their spread across the world and into Vietnam |
| **C** | `core_doctrine` — shared foundational theory | Teachings **accepted by all three traditions** (the Four Noble Truths, the Noble Eightfold Path, dependent origination, karma, the five aggregates, nirvana...) |
| **D / E / F** | `tradition` — the three major traditions | Each tradition is a complete branch: overview → scriptures → path of practice → countries → **that tradition's own festivals** |
| **G** | `comparison` — comparison & orientation | Comparing the three traditions and a healthy attitude toward cross-tradition study |
| **H** | `reference_tool` — reference & tools | Terminology, scriptures, schools, festival calendar, FAQ |

**Note:** The same article can carry several attributes. `traditions`, `categories`, `calendar` (the calendar system a festival follows), and `sources` are separate data dimensions, not taxonomy sub-levels. The article on Vietnam is written once under B7 and gets an additional category tag when it needs to appear under E5.

# TAXONOMY TREE

> **v1.0 structure:** The main axis follows a newcomer's journey: **orientation → history → shared core doctrine → each tradition (with its festivals) → comparison → reference**. Group C contains only doctrine shared by all three traditions; each tradition's distinctive points live in D/E/F and are brought together in G.

```text
General Buddhism
│
├── G.A. ORIENTATION FOR NEWCOMERS
│   ├── G.A1. Understanding Buddhism
│   │   ├── [GB001] What is Buddhism? · L1
│   │   ├── [GB002] The Three Jewels — Buddha, Dharma, Sangha · L1
│   │   ├── [GB003] Buddhism and creator-god religions · L1
│   │   ├── [GB004] Common misconceptions about Buddhism · L1
│   │   └── [GB005] Reading Buddhist terminology: Pāli, Sanskrit, and Sino-Vietnamese · L1
│   ├── G.A2. How to start learning
│   │   ├── [GB006] Where should a beginner start learning Buddhism? · L1
│   │   ├── [GB007] How to read Buddhist scriptures and texts · L1
│   │   └── [GB008] Taking refuge, lay life, and monastic life — levels of commitment · L1
│   ├── G.A3. The lay Buddhist
│   │   ├── [GB009] The Three Refuges — taking refuge in the Buddha, Dharma, Sangha · L1
│   │   ├── [GB010] The Five Precepts — five trainings for lay practitioners · L1
│   │   ├── [GB011] The life of a lay Buddhist · L1
│   │   └── [GB012] Faith and wisdom in Buddhism · L2
│   └── G.A4. Cross-tradition orientation
│       └── [GB013] Which tradition should I start learning from? · L1
│
├── G.B. HISTORY OF BUDDHISM
│   ├── G.B1. Background
│   │   └── [GB014] India in the Buddha's time — the social and religious setting · L2
│   ├── G.B2. The Buddha's life
│   │   ├── [GB015] The Buddha's life — overview and timeline · L1
│   │   ├── [GB016] Prince Siddhartha and the four sights · L1
│   │   ├── [GB017] Going forth and the six years of seeking · L2
│   │   ├── [GB018] Awakening under the Bodhi tree · L2
│   │   ├── [GB019] Turning the wheel of Dharma — the first teaching · L2
│   │   ├── [GB020] 45 years of teaching and the first Sangha · L2
│   │   ├── [GB021] Final passing (parinirvana) at Kushinagar · L2
│   │   └── [GB022] Historical record and legend around the Buddha · L3
│   ├── G.B3. Preserving the teaching
│   │   └── [GB023] The Buddhist councils — preserving the Dharma after the Buddha · L3
│   ├── G.B4. Early schisms
│   │   ├── [GB024] The first schism — the Sthavira and Mahāsāṃghika · L3
│   │   ├── [GB025] Map of the early schools · L3
│   │   └── [GB026] King Aśoka — Buddhism spreads beyond India · L2
│   ├── G.B5. The formation of the three major traditions
│   │   ├── [GB027] The three major traditions — a panoramic map · L2
│   │   ├── [GB028] The rise of the Mahāyāna · L3
│   │   ├── [GB029] The formation of Tantric Buddhism and the Vajrayāna · L3
│   │   └── [GB030] Buddhism in India — a thousand years of rise and decline · L3
│   ├── G.B6. Buddhism spreads
│   │   ├── [GB031] Southern Buddhism — Sri Lanka and Southeast Asia · L2
│   │   ├── [GB032] Mahāyāna Buddhism — the Silk Road and East Asia · L2
│   │   ├── [GB033] Vajrayāna Buddhism — the Himalayas and Mongolia · L2
│   │   └── [GB034] Modern Buddhism — a journey around the world · L3
│   └── G.B7. Buddhism in Vietnam
│       ├── [GB035] Buddhism's arrival in Vietnam — from the first centuries CE · L2
│       ├── [GB036] Vietnamese Buddhism under the Lý–Trần dynasties · L3
│       ├── [GB037] Vietnamese Buddhism in the early modern and modern eras · L2
│       └── [GB038] A map of Vietnamese Buddhism today · L2
│
├── G.C. SHARED FOUNDATIONAL THEORY (true across every tradition)
│   ├── G.C1. The Four Noble Truths
│   │   ├── [GB039] The Four Noble Truths — overview · L1
│   │   ├── [GB040] The truth of suffering (dukkha) · L2
│   │   ├── [GB041] The truth of the origin of suffering · L2
│   │   ├── [GB042] The truth of the cessation of suffering · L2
│   │   └── [GB043] The truth of the path · L2
│   ├── G.C2. The Noble Eightfold Path
│   │   ├── [GB044] The Noble Eightfold Path — overview and three groupings · L1
│   │   ├── [GB045] The Ethics group: right speech, right action, right livelihood · L2
│   │   ├── [GB046] The Concentration group: right effort, right mindfulness, right concentration · L2
│   │   └── [GB047] The Wisdom group: right view, right intention · L2
│   ├── G.C3. Dependent origination
│   │   ├── [GB048] Dependent origination — overview · L2
│   │   └── [GB049] The twelve links of dependent origination · L3
│   ├── G.C4. Karma, rebirth, and the realms
│   │   ├── [GB050] Karma — getting it right, and common misunderstandings · L1
│   │   ├── [GB051] Rebirth and reincarnation · L2
│   │   ├── [GB052] The six realms and the Buddhist cosmos · L2
│   │   └── [GB053] Merit, fields of merit, and dedicating merit · L2
│   ├── G.C5. The five aggregates and non-self
│   │   ├── [GB054] The five aggregates — what "I" is made of · L2
│   │   ├── [GB055] Non-self — getting right a concept that's easy to misread · L2
│   │   └── [GB056] The three marks of existence and the seals of the Dharma · L2
│   ├── G.C6. The three trainings and how to live
│   │   ├── [GB057] The three trainings — ethics, concentration, wisdom · L2
│   │   └── [GB058] Loving-kindness, compassion, sympathetic joy, and equanimity in daily life · L1
│   └── G.C7. The goal of liberation
│       ├── [GB059] What is nirvana · L2
│       ├── [GB060] The four stages of awakening and the path to liberation · L3
│       └── [GB061] The buddhas — past, present, and future · L2
│
├── G.D. THE THERAVĀDA TRADITION
│   ├── G.D1. Overview
│   │   ├── [GB062] Theravāda — overview · L1
│   │   └── [GB063] History of Theravāda · L3
│   ├── G.D2. Scriptures
│   │   ├── [GB064] The Pāli Canon — a map of the scriptures · L2
│   │   ├── [GB065] What is the Abhidhamma · L3
│   │   └── [GB066] The commentarial tradition and the Visuddhimagga · L3
│   ├── G.D3. Path of practice and daily life
│   │   ├── [GB067] The path of practice in Theravāda · L2
│   │   ├── [GB068] Meditation in Theravāda — an introduction · L2
│   │   ├── [GB069] Life in a Theravāda monastic community · L2
│   │   └── [GB070] The life of a lay Theravāda Buddhist · L2
│   ├── G.D4. Theravāda by country
│   │   ├── [GB071] Theravāda in Sri Lanka · L2
│   │   ├── [GB072] Theravāda in Thailand · L2
│   │   ├── [GB073] Theravāda in Myanmar · L2
│   │   ├── [GB074] Theravāda in Laos and Cambodia · L2
│   │   └── [GB075] Theravāda in Vietnam · L2
│   └── G.D5. Southern (Theravāda) Buddhist festivals
│       └── [GB076] Southern (Theravāda) Buddhist festivals · L1
│
├── G.E. THE MAHĀYĀNA TRADITION
│   ├── G.E1. Overview
│   │   ├── [GB083] Mahāyāna — overview · L1
│   │   └── [GB084] History of the formation and growth of the Mahāyāna · L3
│   ├── G.E2. Foundational thought
│   │   ├── [GB085] The bodhisattva and bodhicitta · L1
│   │   ├── [GB086] The six perfections (pāramitās) · L2
│   │   ├── [GB087] Emptiness — an introduction · L3
│   │   ├── [GB088] Buddha-nature (tathāgatagarbha) · L3
│   │   ├── [GB089] The three bodies of the Buddha (trikāya) · L3
│   │   ├── [GB090] Yogācāra (Consciousness-Only) — an introduction · L3
│   │   └── [GB091] The main buddhas and bodhisattvas of the Mahāyāna · L2
│   ├── G.E3. Scriptures
│   │   ├── [GB092] A map of the Mahāyāna scriptures · L2
│   │   ├── [GB093] The Heart Sutra and the Diamond Sutra · L2
│   │   ├── [GB094] The Lotus Sutra (Saddharmapuṇḍarīka) · L3
│   │   ├── [GB095] The Flower Garland Sutra (Avataṃsaka) · L4
│   │   └── [GB096] The Vimalakīrti Sutra · L3
│   ├── G.E4. Schools
│   │   ├── [GB097] A map of the Mahāyāna schools · L2
│   │   ├── [GB098] Chan / Zen (the Meditation school) · L2
│   │   ├── [GB099] Pure Land school · L2
│   │   ├── [GB100] Tiantai school · L3
│   │   ├── [GB101] Huayan school · L4
│   │   ├── [GB102] Faxiang (Yogācāra/Consciousness-Only) school · L3
│   │   ├── [GB103] Sanlun (Three Treatises) school · L4
│   │   └── [GB104] Shingon and East Asian Esoteric Buddhism · L3
│   ├── G.E5. East Asian Buddhism — by country
│   │   ├── [GB105] Buddhism in China · L2
│   │   ├── [GB106] Buddhism in Japan · L3
│   │   ├── [GB107] Buddhism in Korea · L3
│   │   └── Buddhism in Vietnam → see B7
│   ├── G.E6. Daily life and practice
│   │   ├── [GB108] Mahāyāna daily liturgy and ritual · L2
│   │   ├── [GB109] Vegetarianism in Buddhism · L2
│   │   └── [GB110] Buddha-recitation in lay life · L2
│   └── G.E7. Mahāyāna Buddhist festivals
│       └── [GB111] Mahāyāna Buddhist festivals · L1
│
├── G.F. THE VAJRAYĀNA TRADITION
│   ├── G.F1. Overview
│   │   ├── [GB117] Vajrayāna — overview · L2
│   │   └── [GB118] From Indian Tantric Buddhism to the Himalayan countries · L3
│   ├── G.F2. Foundational concepts
│   │   ├── [GB119] The four main schools of Tibetan Buddhism · L2
│   │   ├── [GB120] The spiritual teacher — lama, guru, and lineage · L2
│   │   ├── [GB121] What is an empowerment (abhiṣeka) · L2
│   │   ├── [GB122] Mantra, mandala, and yidam — a plain-language look · L2
│   │   ├── [GB123] The path of practice in the Vajrayāna · L3
│   │   ├── [GB124] Tulkus — the reincarnation system, the Dalai Lama, and the Karmapa · L2
│   │   └── [GB125] Prayer flags, prayer wheels, and butter lamps · L1
│   ├── G.F3. Scriptures
│   │   └── [GB126] The Tibetan canon — Kangyur and Tengyur · L3
│   ├── G.F4. Countries and the present day
│   │   ├── [GB127] Tibet and the exile community · L3
│   │   └── [GB128] Vajrayāna in Bhutan, Mongolia, Nepal, and elsewhere · L3
│   └── G.F5. Vajrayāna Buddhist festivals
│       └── [GB129] Vajrayāna Buddhist festivals · L2
│
├── G.G. COMPARISON & ORIENTATION
│   ├── G.G1. Comparing the three major traditions
│   │   └── [GB134] Comparing the three major traditions — a reference table · L2
│   └── G.G2. One Buddhism, many paths
│       └── [GB135] One Buddhism, many paths — a non-sectarian attitude · L2
│
└── G.H. REFERENCE
    ├── G.H1. Index of commonly encountered scriptures
    │   └── [GB137] Index of commonly encountered scriptures — from the Nikāyas to the tantras · R
    ├── G.H2. Index of schools and lineages
    │   └── [GB138] Index of schools, sub-schools, and lineages · R
    └── G.H3. Frequently asked questions
        └── [GB140] Frequently asked questions about Buddhism · R
```

---

# ARTICLE CATALOG

> Each article has a **content description** (what to write) and, where needed, a **Terminology** line so writers use terms correctly and consistently. Festival articles must always record the **calendar system** and **country-by-country variants**.

## G.A. ORIENTATION FOR NEWCOMERS

> **Suggested order for newcomers:** A1 → A2 → A3; read A4 before moving on to group D/E/F.

### G.A1. Understanding Buddhism

#### [GB001] What is Buddhism? · L1
Defines Buddhism as a path of education and practice for ending suffering, taught by the historical Buddha, Śākyamuni; explains that "Buddha" means "the awakened one," not a proper name or a deity. Includes a table of what Buddhism has (teachings, practice, community, art) and what it does not have (an unchanging book of dogma, a creator god, worldly punishment).
**Terminology:** *buddha* (P/S) = the awakened one, an enlightened being; capitalized "Buddha" refers specifically to Śākyamuni Buddha.

#### [GB002] The Three Jewels — Buddha, Dharma, Sangha · L1
The three refuges shared by every Buddhist tradition: the awakened one (Buddha), the teaching (Dharma), and the community of practitioners (Sangha). Clarifies that "Sangha" in its original sense means the fourfold community (both monastic and lay), not monks alone.
**Terminology:** *ratanattaya* (P) / *triratna* (S) — Sino-Vietnamese **tam bảo** ("three jewels").

#### [GB003] Buddhism and creator-god religions · L1
A respectful comparison: Buddhism has no omnipotent creator; karma is a law of cause and effect, not reward and punishment handed down by someone; heavenly beings exist within the Buddhist cosmology but are not objects of ultimate supplication. Answers "Is Buddhism a religion or a philosophy?" by presenting both views.

#### [GB004] Common misconceptions about Buddhism · L1
Clarifies several misconceptions: that Buddhism is pessimistic (the truth of suffering is a diagnosis, not a complaint); that bowing to a statue is idol worship; that praying to the Buddha is asking for favors; that "everything is karma" means one should simply give up; that practicing means fleeing from life; that only vegetarians are real Buddhists; that reciting the Buddha's name works like a protective charm. Each misconception comes with a short answer and a link to the relevant article.

#### [GB005] Reading Buddhist terminology: Pāli, Sanskrit, and Sino-Vietnamese · L1
Why the same concept appears in several written forms (*kamma/karma*, *nibbāna/nirvāṇa*, *thiện nghiệp*), how the app displays terms, and how to use the cross-reference table [GB136]. Distinguishes the communities behind each form: Pāli = the Theravāda canon, Sanskrit = the Mahāyāna, Sino-Vietnamese = texts translated into Chinese. Includes a guide to reading diacritics (ā, ī, ū, ṃ, ṅ, ñ, ṭ, ḍ, ṇ, ḷ, ś, ṣ). Links to [M097], [M160].

### G.A2. How to start learning

#### [GB006] Where should a beginner start learning Buddhism? · L1
A learning map: understand the basic concepts → hear the Buddha's story → learn the shared core doctrine → explore the tradition closest to you → combine this with practice (leading into the Meditation section). Explains the app's overall path and how to use groups A–H of this section.

#### [GB007] How to read Buddhist scriptures and texts · L1
A hierarchy of sources: scripture → commentary → treatise → modern teaching books → online articles; why the same line can be explained differently at each layer. Guidance on choosing a trustworthy Vietnamese translation and on how to ask questions when two sources conflict. This is a "misinformation-proofing" skill for newcomers.

#### [GB008] Taking refuge, lay life, and monastic life — levels of commitment · L1
Explains the levels: an interested person → a lay Buddhist who has taken refuge → a practitioner who keeps the eight precepts → a novice/ordained monastic. Clears up the misconception that "studying Buddhism means you must be vegetarian and ordain"; each level of commitment comes with its real-world conditions.

### G.A3. The lay Buddhist

#### [GB009] The Three Refuges — taking refuge in the Buddha, Dharma, Sangha · L1
What the refuge ceremony is, what the refuge formula (*buddhaṃ saraṇaṃ gacchāmi*...) means, and how taking refuge differs from asking for protection. Notes that the three refuges are the shared foundation of all three traditions, even though the outward ceremony may differ.
**Terminology:** *tisaraṇa* (P) / *triśaraṇa* (S) — Sino-Vietnamese **tam quy, quy y tam bảo**.

#### [GB010] The Five Precepts — five trainings for lay practitioners · L1
The five precepts (no killing, no stealing, no sexual misconduct, no lying, no intoxicants) presented as **training** rather than "commandments"; each precept comes with its rationale, scope, and how to apply it in daily life. Notes how the precepts are kept differently across traditions and cultures.
**Terminology:** *pañcasīla* (P/S) — Sino-Vietnamese **ngũ giới** ("five precepts").

#### [GB011] The life of a lay Buddhist · L1
An overview of lay practice: morning devotions, sutra reading, temple visits on the new moon and full moon, making offerings, giving, and attending ceremonies. Emphasizes that customs vary by tradition and region; avoids prescribing a single "correct" way.

#### [GB012] Faith and wisdom in Buddhism · L2
Faith (*saddhā*) means confidence that has been tested — like trusting a bridge is sound enough to cross — as opposed to blind belief; the complementary relationship between faith and understanding in the learning process. Helps beginners avoid the two extremes of believing everything and doubting everything.
**Terminology:** *saddhā* (P) / *śraddhā* (S) — Sino-Vietnamese **tín** ("faith/confidence").

### G.A4. Cross-tradition orientation

#### [GB013] Which tradition should I start learning from? · L1
Guidance for choosing based on: one's surroundings (in Vietnam this usually means proximity to Mahāyāna/Pure Land practice), the language of the texts one can read, and which form of practice suits one's temperament (recitation, seated meditation, study). Concludes that the shared core doctrine (group C) is common ground and doesn't require an immediate choice; leads into [GB027] and [GB134].

## G.B. HISTORY OF BUDDHISM

> **Suggested order:** B1 → B2 → B3 → B4 → B5 → B6; B7 can be read independently by users in Vietnam. Articles in group B cite historical sources and note their degree of certainty (see [GB022]).

### G.B1. Background

#### [GB014] India in the Buddha's time — the social and religious setting · L2
Northeastern India in the 6th–5th centuries BCE: Brahmanism with its caste system, Upanishadic philosophy, and the *śramaṇa* movement of wanderers seeking a path outside the Vedic tradition. Helps readers see which concepts the Buddha inherited (karma, rebirth, meditative absorption) and which he reshaped (non-self, the middle way).

### G.B2. The Buddha's life

#### [GB015] The Buddha's life — overview and timeline · L1
The whole of the Buddha's life in one article, with a timeline: born at Lumbini → raised at Kapilavastu → renunciation → awakening at Bodh Gaya → 45 years of teaching → final passing at Kushinagar at age 80. Notes on dating: the traditional dates are 623–543 BCE, while modern scholarship places his life around 480–400 BCE — both are presented.
**Terminology:** *Śākyamuni* = "sage of the Śākya clan"; *siddhattha/siddhārtha* = Siddhartha.

#### [GB016] Prince Siddhartha and the four sights · L1
Palace life, the four sights (old age, sickness, death, a wandering ascetic), and the decision to renounce the world; his wife Yaśodharā and son Rāhula according to the traditional accounts. Written to respect the tradition while showing that this is how the scriptures narrate the meaning of the event.

#### [GB017] Going forth and the six years of seeking · L2
Studying meditation under two teachers, Āḷāra Kālāma and Uddaka Rāmaputta; six years of asceticism alongside a group of five companions; receiving milk-rice from Sujātā and returning to the middle way. A lesson in "neither forcing nor letting go" drawn straight from the Buddha's own life (links to the meditation attitude discussed in [M105]).

#### [GB018] Awakening under the Bodhi tree · L2
The night of meditation at Uruvelā (Bodh Gaya): the stages of realization according to the scriptures, the temptations of Māra, and their symbolic meaning. Notes that different traditions narrate the details differently.
**Terminology:** *bodhi* = awakening; *Bodhirukkha* = the Bodhi tree.

#### [GB019] Turning the wheel of Dharma — the first teaching · L2
The *Dhammacakkappavattana Sutta* (Setting the Wheel of Dharma in Motion), taught at Deer Park in Sarnath to his five former companions: the middle way and the Four Noble Truths taught for the first time. A short analysis of the sutta's structure and why it is regarded as Buddhism's "founding moment."
**Terminology:** *dhammacakkappavattana* — Sino-Vietnamese **chuyển pháp luân** ("turning the wheel of Dharma").

#### [GB020] 45 years of teaching and the first Sangha · L2
The organization of the Sangha, the great disciples (Sāriputta, Moggallāna, Ānanda), the ordination of women (Mahāpajāpatī), and how the Buddha traveled and taught people from every walk of life. Note: the Pāli tradition records 45 years of teaching, while some East Asian traditions record 49.
**Terminology:** *saṅgha/saṃgha* = the monastic Sangha, the community of practitioners.

#### [GB021] Final passing (parinirvana) at Kushinagar · L2
The final days, the Buddha's last instruction ("all conditioned things are impermanent — strive on with diligence"), his passing at age 80, and the division of his relics into eight portions. The meaning of cremation rites and relic veneration in later traditions.
**Terminology:** *parinibbāna/parinirvāṇa* — Sino-Vietnamese **bát-niết-bàn, nhập diệt** ("final nirvana").

#### [GB022] Historical record and legend around the Buddha · L3
Separates two layers of information: the legendary layer (the epic *Buddhacarita*, later hagiographies) and the historical layer (Aśoka's Lumbini pillar inscription, debated dating, archaeology of the holy sites). Equips readers with the habit of asking "which layer does this information belong to?" — a principle used throughout the section.

### G.B3. Preserving the teaching

#### [GB023] The Buddhist councils — preserving the Dharma after the Buddha · L3
The mechanism of oral transmission and the councils: the first at Rājagaha (led by the elder Mahākassapa), the second at Vesāli over a dispute about monastic rules, the third under King Aśoka, and the writing-down of the Pāli canon in Sri Lanka (1st century BCE). Explains why many versions of the same sutta exist that are similar but not identical.

### G.B4. Early schisms

#### [GB024] The first schism — the Sthavira and the Mahāsāṃghika · L3
The background and cause of the schism (the dispute over ten points of monastic discipline at Vesāli) and the formation of the two blocs, the Sthavira and the Mahāsāṃghika; a note from modern scholarship: the schism was a gradual process, not a single clean split.

#### [GB025] Map of the early schools · L3
A map of roughly 18–20 schools that emerged over the following two to three centuries: the Sarvāstivāda, the Vibhajyavāda (the ancestor of the Theravāda line), the Dharmaguptaka (whose monastic code is still used in East Asia today!), the Sāṃmitīya, and others. Notes which schools still have a living lineage today, and why this article is useful background for reading the history of the various traditions.

#### [GB026] King Aśoka — Buddhism spreads beyond India · L2
From a warrior king to a Buddhist patron of the Dharma; the stone pillars and edicts; the missionary network (including the mission to Sri Lanka). Aśoka's role in turning Buddhism from a local movement into a transcontinental religion.

### G.B5. The formation of the three major traditions

#### [GB027] The three major traditions — a panoramic map · L2
The "mother map" that leads into groups D/E/F: a timeline from early Buddhism → the early schools → the Mahāyāna (roughly from the last centuries BCE onward) → the Vajrayāna (6th–7th centuries CE); a quick comparison table of names (Theravāda / "Southern school"; Mahāyāna / "Northern school"; Vajrayāna / "Esoteric school"). Emphasizes that the three traditions are not three separate "churches" but have continually overlapped and interacted. Links to [GB134].

#### [GB028] The rise of the Mahāyāna · L3
The origins of the Mahāyāna: the emergence of the Perfection of Wisdom (Prajñāpāramitā) sutras, the bodhisattva ideal, and the role of stupas and lay practitioners; presents the scholarly hypotheses about its origins and notes clearly that the Mahāyāna did not simply "split off from the Mahāsāṃghika," as older books often claim. The Mahāyāna and the early schools coexisted within the same monasteries for centuries.

#### [GB029] The formation of Tantric Buddhism and the Vajrayāna · L3
Indian Tantric Buddhism from the 6th–7th centuries onward: tantra, mandala, mantra, and deity visualization — developed on the foundation of Mahāyāna philosophy; the names "Mantrayāna" and "Vajrayāna." Links to [GB117].

#### [GB030] Buddhism in India — a thousand years of rise and decline · L3
From its height (Nālandā, royal patronage) to its decline (loss of patronage, warfare, the Turkic invasions of the 12th–13th centuries that nearly erased Buddhism from India); a small revival in the 19th–20th centuries (including the Ambedkar movement of 1956). Explains why India — the birthplace of Buddhism — is home to only a small Buddhist minority today.

### G.B6. Buddhism spreads

#### [GB031] Southern Buddhism — Sri Lanka and Southeast Asia · L2
The southern route: Sri Lanka (Mahinda, Saṅghamittā, the writing-down of the Tipiṭaka), Myanmar, Thailand, Laos, Cambodia; shared traits: the Pāli canon, and a monastic Sangha that serves as a cultural and educational center. Country-by-country detail lives in group D4.

#### [GB032] Mahāyāna Buddhism — the Silk Road and East Asia · L2
The Mahāyāna route: Central Asia, Kucha (Kumārajīva), China (early centuries CE), the great waves of sutra translation, then Korea, Japan, and Vietnam; shared traits: sutras translated from Sanskrit into Chinese, with the Mahāyāna as the dominant form. Country-by-country detail lives in group E5.

#### [GB033] Vajrayāna Buddhism — the Himalayas and Mongolia · L2
The Vajrayāna route: entering Tibet in the 7th–8th centuries (Śāntarakṣita, Padmasambhava, Samye Monastery), a second wave of spread in the 10th–11th centuries (Atiśa, Marpa), then on to Bhutan, Mongolia, Nepal, and Russian communities (Buryatia, Kalmykia). Detail in group F.

#### [GB034] Modern Buddhism — a journey around the world · L3
From the 19th century onward: Western scholars translating the scriptures, the meditation and mindfulness movements, Vietnamese and Tibetan refugee communities carrying Buddhism across the world, "Engaged Buddhism" (Thích Nhất Hạnh), and Buddhism in Europe and the Americas today. Context that helps readers understand why the app covers all three traditions.

### G.B7. Buddhism in Vietnam

> **Why this has its own group:** users in Vietnam need to understand the origins of the forms of Buddhism they encounter every day. Written once here; the E5/D4 branches only cross-link to it. Coordinates with group F1 of the Meditation section ([M145]–[M152]) for the practice side.

#### [GB035] Buddhism's arrival in Vietnam — from the first centuries CE · L2
Two routes of transmission: early schools arriving by sea from India, and the Mahāyāna arriving overland from China; the early center at Luy Lâu; Indian and Chinese meditation masters arriving in Giao Chỉ. Notes on how certain the sources for this period actually are.

#### [GB036] Vietnamese Buddhism under the Lý–Trần dynasties · L3
Buddhism becomes the state religion under the Lý dynasty; the Trúc Lâm Zen school founded by Trần Nhân Tông; the role of monastics at court; Trần-era Buddhist literature ("Dwelling in the World, Content with the Way"). Links to [M146], [M147].

#### [GB037] Vietnamese Buddhism in the early modern and modern eras · L2
From its decline under the Lê–Nguyễn dynasties to the Buddhist revival movement of the early 20th century (charitable associations, monastic-education reform), through the various organizational bodies across historical periods, up to today's Vietnam Buddhist Sangha. Written neutrally per editorial principle 10.

#### [GB038] A map of Vietnamese Buddhism today · L2
The living lineages: the Northern (Mahāyāna) school (Zen, Pure Land, and combined Zen–Pure Land practice) as the dominant strand; the Kinh Theravāda and Khmer Theravāda strands; the revived Trúc Lâm lineage; the Plum Village tradition; modern meditation centers. Includes a "spot the lineage" tip: how to tell which lineage a Vietnamese temple belongs to from its statues, rituals, and robe color. Links to [M145].

## G.C. SHARED FOUNDATIONAL THEORY

> **Rule for group C:** contains only doctrine **accepted by all three traditions**. Differences in interpretation (for example, nirvana understood differently) are not written here but belong in D/E/F and in [GB134]. A reader who finishes group C will be able to follow most articles from every tradition.

### G.C1. The Four Noble Truths

#### [GB039] The Four Noble Truths — overview · L1
The central doctrinal framework of all of Buddhism: suffering, its origin, its cessation, and the path — presented through the metaphor of a doctor diagnosing an illness (disease — cause — prognosis — prescription). Explains why these are called "noble truths" and why they form the shared "backbone" of every school.
**Terminology:** *cattāri ariyasaccāni* (P) / *catvāri āryasatyāni* (S) — Sino-Vietnamese **tứ thánh đế**.

#### [GB040] The truth of suffering (dukkha) · L2
Three forms of suffering: the suffering of pain (ordinary sensory suffering), the suffering of change (suffering because things alter), and the suffering inherent in conditioned existence (a subtle unsatisfactoriness present in all conditioned phenomena). Corrects the misconception that "Buddhism teaches that life is nothing but suffering": the truth of suffering is a diagnosis, not a complaint.

#### [GB041] The truth of the origin of suffering · L2
The root of suffering is craving (*taṇhā*) — sensory desire, the desire to exist, and the desire to be annihilated — and the chain of conditions linking craving to rebirth. Distinguishes ordinary desire from the craving that produces suffering.

#### [GB042] The truth of the cessation of suffering · L2
Suffering can come to a complete end — this is Buddhism's declaration that "there is a way out"; cessation is not annihilation but is like a flame going out for lack of fuel. Leads into [GB059], on nirvana.

#### [GB043] The truth of the path · L2
The path leading to the end of suffering is the Noble Eightfold Path; a quick introduction to its three groups — Ethics, Concentration, Wisdom — leading into group C2. The truth of the path is the bridge between doctrine and practice.

### G.C2. The Noble Eightfold Path

#### [GB044] The Noble Eightfold Path — overview and three groupings · L1
The eight factors: right view, right intention, right speech, right action, right livelihood, right effort, right mindfulness, right concentration; grouped into Wisdom, Ethics, and Concentration. Clarifies that "right" (*sammā*) means "complete, rightly directed," not the moralizing opposite of "wrong." Includes a wheel-of-Dharma diagram of the eight spokes.
**Terminology:** *aṭṭhaṅgika magga* (P) / *aṣṭāṅga mārga* (S) — Sino-Vietnamese **bát chánh đạo** ("noble eightfold path").

#### [GB045] The Ethics group: right speech, right action, right livelihood · L2
The three ethical factors: what counts as "right speech," which livelihoods are unwholesome, and how these apply to modern life (speaking online, running a business). The basis for the precepts and for monastic discipline across every tradition.

#### [GB046] The Concentration group: right effort, right mindfulness, right concentration · L2
The three factors that train the mind: balanced effort, mindfulness, and concentration. Written at a general, conceptual level; detailed practice instructions belong to the Meditation section — see [M095], [M096] and that section's groups B/C.

#### [GB047] The Wisdom group: right view, right intention · L2
The two wisdom factors: seeing reality as it is (the Four Noble Truths, the three marks of existence) and thinking in the right direction (letting go of craving, non-harming). Right view stands at the head of the path — why "believing correctly" is the first step, not the last.

### G.C3. Dependent origination

#### [GB048] Dependent origination — overview · L2
The core law: "when this exists, that exists; when this arises, that arises" — every phenomenon arises dependent on conditions. Dependent origination is the shared explanation behind karma, rebirth, and the path to liberation; a short formula illustrated with an everyday example (seed – conditions – tree).
**Terminology:** *paṭiccasamuppāda* (P) / *pratītyasamutpāda* (S) — Sino-Vietnamese **duyên khởi, duyên sinh**.

#### [GB049] The twelve links of dependent origination · L3
Presents the twelve links, from ignorance to aging-and-death; the different interpretations found across traditions: the three-lifetimes model (Theravāda commentarial tradition), moment-to-moment observation (Madhyamaka), and how the teaching is applied in practice. A conceptual article; direct observation practice belongs to insight meditation, [M121].

### G.C4. Karma, rebirth, and the realms

#### [GB050] Karma — getting it right, and common misunderstandings · L1
Karma = intentional action (of body, speech, and mind) and its results; it is neither fate nor punishment handed down by anyone. Three key points: past karma does not lock in the future; present intention is each person's "freedom to act"; karma is simultaneously a result and an action being created right now. Answers practical questions: why do good people meet with misfortune, and does karma expire?
**Terminology:** *kamma* (P) / *karma* (S) — Sino-Vietnamese **nghiệp**; *cetanā* = volition, intention — "the karma of intention is the most important kind."

#### [GB051] Rebirth and reincarnation · L2
Rebirth does not require an "unchanging soul" — illustrated by the image of one candle's flame lighting another; a continuous stream of consciousness and karma links one life to the next. Notes how schools differ on the intermediate state (*antarābhava*) — an example of how the same question can be answered differently from school to school.

#### [GB052] The six realms and the Buddhist cosmos · L2
The six realms (hell beings, hungry ghosts, animals, asuras, humans, and gods) and the three realms (of desire, of form, and of formlessness); the 31-plane model found in the Theravāda commentaries; this cosmology is best read as a description of states of mind and modes of existence, not as an astronomical map. Briefly introduces the Mahāyāna Pure Lands, linking to [GB099].

#### [GB053] Merit, fields of merit, and dedicating merit · L2
The three grounds of merit: giving, keeping precepts, and meditative cultivation; the practice of dedicating merit — sharing merit with departed relatives and loved ones — found in **all three traditions**. Distinguishes genuine merit-making from "trading" in merit; merit and wisdom as the path's two wings.

### G.C5. The five aggregates and non-self

#### [GB054] The five aggregates — what "I" is made of · L2
The five groups that make up experience: form, feeling, perception, mental formations, and consciousness; analyzes an everyday experience (for example, hearing a compliment) into the five aggregates to show that the "self" is a composite, not an entity.
**Terminology:** *pañcakkhandha* (P) / *pañca-skandha* (S) — Sino-Vietnamese **năm uẩn** ("five aggregates").

#### [GB055] Non-self — getting right a concept that's easy to misread · L2
Non-self (*anattā/anātman*) means there is no fixed, independent, permanent "self" — it does **not** mean "nothing exists," and it does not deny personal responsibility or memory. Presents non-self as an analysis of experience, and distinguishes it clearly from nihilism. Links to [M028].

#### [GB056] The three marks of existence and the seals of the Dharma · L2
Impermanence, suffering, and non-self as three "seals" used to verify authentic teaching; notes that some East Asian traditions use a fourth seal ("nirvana is peace"). Conceptual; the corresponding contemplative practice belongs to [M053], [M025]–[M028].

### G.C6. The three trainings and how to live

#### [GB057] The three trainings — ethics, concentration, wisdom · L2
The three trainings as a sequential, three-step curriculum for the entire Buddhist path; ethics grounds concentration, and concentration grounds wisdom — an understanding shared across every tradition, even though each tradition emphasizes it differently. Links to [M095].
**Terminology:** *tisso sikkhā* (P) / *trīṇi śikṣāṇi* (S) — Sino-Vietnamese **tam học** ("three trainings").

#### [GB058] Loving-kindness, compassion, sympathetic joy, and equanimity in daily life · L1
A brief introduction to four universal qualities of mind — goodwill, empathy for others' suffering, joy at others' happiness, and equanimity — with examples of applying them at home and at work. The general-audience version; detailed practice is at [M041]–[M046].

### G.C7. The goal of liberation

#### [GB059] What is nirvana · L2
Nirvana = the extinguishing of the fires of craving, aversion, and delusion; nirvana "with residue" (while still embodied) and "without residue" (traditions explain this differently); why nirvana cannot be captured in conceptual language and can only be known through the path of practice. The differing approaches of the three traditions are summarized in [GB134].
**Terminology:** *nibbāna* (P) / *nirvāṇa* (S) — Sino-Vietnamese **niết-bàn**.

#### [GB060] The four stages of awakening and the path to liberation · L3
The four stages according to the Pāli canon: stream-enterer, once-returner, non-returner, arhat — together with the framework of ten fetters progressively abandoned. Note: the Mahāyāna expresses this same progression through the ten bodhisattva stages (bhūmis) — the two maps are not in conflict functionally. Links to [GB085].
**Terminology:** *sotāpanna/srotāpanna* = stream-enterer; *arahant/arhat* = arhat.

#### [GB061] The buddhas — past, present, and future · L2
Śākyamuni Buddha is not the only buddha: the past buddhas (among whom Dīpaṅkara is well known), and the future Buddha, Maitreya — a belief shared by all three traditions. Distinguishes "Buddha" as a title from a proper name; opens the way to [GB089], on the three bodies of the Buddha.

## G.D. THE THERAVĀDA TRADITION

> **Suggested order:** D1 → D2 → D3 → D4 → D5; readers interested only in festivals can go straight to D5 after [GB062]. Group D treats the tradition as a culture and a religion; meditation content belongs to [M055]–[M059], [M134]–[M136].

### G.D1. Overview

#### [GB062] Theravāda — overview · L1
"Theravāda" means "the teaching of the elders"; the region it covers (Sri Lanka, Thailand, Myanmar, Laos, Cambodia); identifying features: the Pāli canon, the arhat ideal, a gradual path, and a Sangha that plays a major social role. What "Southern school" means in Vietnam — clearing up confusion between "Southern school," "Kinh Southern school," and "Khmer Southern school."

#### [GB063] History of Theravāda · L3
From the Vibhajyavāda school to the mainline tradition in Sri Lanka: Mahinda and King Devānaṃpiya Tissa, the Mahāvihāra, the writing-down of the Tipiṭaka (1st century BCE), Buddhaghosa's commentaries (5th century), periods of decline and revival, the 19th-century Dhammayuttika reform movement, and today's globalized Theravāda.

### G.D2. Scriptures

#### [GB064] The Pāli Canon — a map of the scriptures · L2
Its Vinaya–Sutta–Abhidhamma structure: the Vinaya (rules for monks and nuns), the Sutta Piṭaka made up of the five Nikāyas (Dīgha, Majjhima, Saṃyutta, Aṅguttara, Khuddaka), and the Abhidhamma; what each basket contains, how difficult each is to read, and where to start (suggestion: the Majjhima and Aṅguttara Nikāyas). Links to [GB137].
**Terminology:** *tipiṭaka* (P) / *tripiṭaka* (S) — Sino-Vietnamese **tam tạng** ("three baskets").

#### [GB065] What is the Abhidhamma · L3
The third basket: a system that analyzes all experience down into ultimate "phenomena" (dhammas); the seven books of the Pāli tradition; why the Abhidhamma is considered difficult and usually studied later — this article stays at the level of a map, without going into the detailed enumeration of dhammas.

#### [GB066] The commentarial tradition and the Visuddhimagga · L3
The role of the commentaries (*aṭṭhakathā*) and of Buddhaghosa's *Visuddhimagga* (Path of Purification), which systematizes the path of ethics, concentration, and wisdom; how to distinguish the content of the original scriptures from commentarial content when reading Theravāda material. Links to [M134].

### G.D3. Path of practice and daily life

#### [GB067] The path of practice in Theravāda · L2
A picture of the path: taking refuge → keeping the precepts → giving and making merit → hearing the teaching → calm-abiding and insight meditation → attaining the stages of awakening. The concept of "gradual training" (*anupubbasikkhā*) and the role of the Sangha in upholding the teaching. A framing article; the detailed practices appear in later D3 articles and in the Meditation section.

#### [GB068] Meditation in Theravāda — an introduction · L2
A general-audience overview of Theravāda meditation subjects: mindfulness of breathing, the four divine abodes, the four foundations of mindfulness, the forty meditation subjects; points readers who want to practice toward the app's Meditation path. Links to [M055]–[M058], [M127].

#### [GB069] Life in a Theravāda monastic community · L2
A day in the life of a monk: alms round, receiving instruction, studying the scriptures, seated meditation; the twice-monthly recitation of the monastic code (*pātimokkha*); the rains retreat; forest traditions versus village-temple traditions; the teacher–student relationship.

#### [GB070] The life of a lay Theravāda Buddhist · L2
Lay practice: keeping the five precepts, giving to the Sangha (*dāna*), observing the eight precepts on Uposatha days, dedicating merit to the deceased, and going to the temple to hear teachings; how customs differ across regions (Thai, Lao, Burmese, Khmer).

### G.D4. Theravāda by country

> Each article follows a shared framework: history of its arrival in that country → how the Sangha is organized today → distinctive features of practice → notable contributions (for example, modern Burmese meditation, linked to [M135]).

#### [GB071] Theravāda in Sri Lanka · L2
The cradle of Theravāda: from Mahinda to Kandy, Buddhism and the state, the Asgiriya–Malwatte chapters, the 19th-century revival movement, and the Poson observance day.

#### [GB072] Theravāda in Thailand · L2
From Sukhothai to today: the two orders, Mahānikāya and Dhammayuttika; the role of the monarchy; the national Sangha system; the forest tradition (Ajahn Mun, Ajahn Chah); Buddhism in modern Thai life. Links to [M136].

#### [GB073] Theravāda in Myanmar · L2
Bagan and King Anawrahta; the popularization of meditation practice from Ledi Sayādaw onward; the Burmese meditation systems that have gone on to have global influence. Links to [M135].

#### [GB074] Theravāda in Laos and Cambodia · L2
Buddhism in Laos (the Sangha and the Boun festival tradition) and in Cambodia (Angkor, Khmer Buddhism, the 20th-century historical disruption and its subsequent recovery).

#### [GB075] Theravāda in Vietnam · L2
Two branches: the Kinh Theravāda (formed in the early 20th century around Bửu Quang Temple in Saigon and its successor monasteries — cross-check domestic historical sources when writing this article) and Khmer Theravāda in the southwestern Mekong Delta; monasteries, the rains retreat, and the Khmer community's Chôl Chnăm Thmây and Ok Om Bok festivals. Links to [M151].

### G.D5. Theravāda festivals

> **General principle:** Theravāda festivals follow the lunar calendar and the seasons (monsoon, harvest). Every article must record: the underlying doctrinal meaning → country-by-country customs → which calendar system sets the date (never a fixed solar-calendar date).

## G.E. THE MAHĀYĀNA TRADITION

> **Suggested order:** E1 → E2 → E3 → E4 → E5/E6 → E7. Group E is the broadest; users in Vietnam will recognize a great deal of this content (Pure Land, the Ullambana festival, buddha-recitation).

### G.E1. Overview

#### [GB083] Mahāyāna — overview · L1
"Mahāyāna" = the Great Vehicle: the ideal of bringing all sentient beings to awakening, not only individual liberation; distinguishing features: a Sanskrit canon (translated into Chinese/Tibetan), the bodhisattva path, a large pantheon of buddhas and bodhisattvas, and rich ritual life; regions: China, Vietnam, Korea, Japan. Emphasizes that the Mahāyāna is extremely diverse and is not a single unified system.

#### [GB084] History of the formation and growth of the Mahāyāna · L3
From the bodhisattva movement and the early Prajñāpāramitā sutras, through Nāgārjuna (Madhyamaka) and Vasubandhu (Yogācāra), and the great center of Nālandā; its arrival in China through translation (Kumārajīva, Xuanzang); its complicated relationship with the early schools — the Mahāyāna did not emerge from a single "clean split" (links to [GB028]).

### G.E2. Foundational thought

#### [GB085] The bodhisattva and bodhicitta · L1
Who a bodhisattva is — from "one heading toward awakening" to the ideal of "awakening for the sake of all beings"; aspirational and engaged bodhicitta; why the bodhisattva path is the heart of the Mahāyāna; its roots in the Jātaka birth stories — a heritage shared with Theravāda.
**Terminology:** *bodhisatta* (P) / *bodhisattva* (S) — Sino-Vietnamese **bồ-tát**; *bodhicitta* — **bồ-đề tâm** ("awakening mind").

#### [GB086] The six perfections (pāramitās) · L2
The six perfections: giving, ethical discipline, patience, diligence, meditative concentration, and wisdom; each illustrated with an everyday example for a lay practitioner; notes the ten-perfection list, which adds skillful means, resolve, spiritual power, and knowledge. This is the bodhisattva's "curriculum."
**Terminology:** *pāramitā* — Sino-Vietnamese **đáo bỉ ngạn / ba-la-mật** ("reaching the far shore / perfection").

#### [GB087] Emptiness — an introduction · L3
*Śūnyatā* does not mean "nothing exists" but "nothing exists independently, with an intrinsic essence"; emptiness is simply dependent origination seen from another angle; explains familiar lines such as "form is emptiness" and "phenomena are without intrinsic nature"; why seeing emptiness is seeing the middle way. Links to [M070].
**Terminology:** *suññatā* (P) / *śūnyatā* (S) — Sino-Vietnamese **không, tánh Không**.

#### [GB088] Buddha-nature (tathāgatagarbha) · L3
Teaches that every sentient being has the capacity to become a buddha — the "womb/embryo of the thus-come one"; the relationship between buddha-nature and emptiness (two ways of expressing the same thing, not a contradiction); the practical meaning: no one is excluded from the path. Notes the historical debates around this concept.

#### [GB089] The three bodies of the Buddha (trikāya) · L3
The framework that explains why the Mahāyāna has so many buddhas: the dharma body (*dharmakāya* — suchness itself), the enjoyment body (*saṃbhogakāya* — the resplendent body dwelling in a pure land), and the emanation body (*nirmāṇakāya* — a historical body such as Śākyamuni's). A short explanation using the sun-and-sunlight analogy.
**Terminology:** *trikāya* — Sino-Vietnamese **tam thân** ("three bodies").

#### [GB090] Yogācāra (Consciousness-Only) — an introduction · L3
The Yogācāra system: all phenomena are manifestations of consciousness; the layers of consciousness (including the store consciousness, *ālayavijñāna*); distinguishes Yogācāra from idealism or a denial that the world exists. A map-level article; links to [M138].

#### [GB091] The main buddhas and bodhisattvas of the Mahāyāna · L2
A "who's who" of the Northern-tradition temple: Śākyamuni Buddha, Amitābha (of the West), the Medicine Buddha (of the East), Maitreya; Avalokiteśvara (Quan Âm — and the shift of this figure's depicted gender in China), Mañjuśrī, Samantabhadra, Kṣitigarbha; how to recognize each by their hand implements, posture, and mount; what each represents in devotional life.

### G.E3. Scriptures

#### [GB092] A map of the Mahāyāna scriptures · L2
The major sutra "families": the Prajñāpāramitā, Lotus, Avataṃsaka, Ratnakūṭa, Mahāsaṃnipāta, and (Mahāyāna) Nirvāṇa collections; the waves of translation into Chinese and the nature of Mahāyāna texts (there is no single "original" version); the Chinese canon (Taishō) and how sutras are cited. Links to [GB137].

#### [GB093] The Heart Sutra and the Diamond Sutra · L2
The two most-recited sutras in the Northern tradition: the Heart Sutra (260 characters) and the Diamond Perfection of Wisdom Sutra; a plain-language, passage-by-passage explanation, the history of their translation (Xuanzang), and how they are chanted in liturgy ([GB108]).

#### [GB094] The Lotus Sutra (Saddharmapuṇḍarīka) · L3
Its central content: skillful means (*upāya*), the "One Buddha Vehicle" — every path ultimately leads to buddhahood — the chapter on Devadatta, and the Buddha's boundless lifespan. Its enormous influence on the East Asian schools and on the practice of chanting "Namu Myōhō Renge Kyō" (Nichiren).

#### [GB095] The Flower Garland Sutra (Avataṃsaka) · L4
Regarded as the pinnacle of Mahāyāna philosophy: the vision of "everything within everything" — Indra's net of jewels — and the mutual interpenetration of all phenomena; why this sutra is difficult and usually read in excerpts; its influence on the Huayan school ([GB101]).

#### [GB096] The Vimalakīrti Sutra · L3
The story of the lay bodhisattva Vimalakīrti, who feigns illness and teaches the Dharma — a model of the lay bodhisattva — in dialogue with the great disciples; a text rich in literary quality and wit; especially close to the hearts of lay practitioners.

### G.E4. Schools

> Each school article follows this framework: origin → core ideas → main practices → presence today (which countries, which temples in Vietnam).

#### [GB097] A map of the Mahāyāna schools · L2
A map: China has eight major schools (Chan, Pure Land, Tiantai, Huayan, Faxiang/Yogācāra, Sanlun, Vinaya, Shingon/Esoteric); Japan adds Tendai and Nichiren; in Vietnam, Zen and Pure Land are the two main strands, often combined into joint Zen–Pure Land practice. Leads into the detailed articles that follow.

#### [GB098] Chan / Zen (the Meditation school) · L2
From Bodhidharma to the Sixth Patriarch, Huineng, and the *Platform Sutra*; its defining trait of "pointing directly at the mind"; the Rinzai and Sōtō lineages; Zen/Thiền in Vietnam. A general-audience article on the school; practice content is at [M064]–[M067], [M139], [M140].

#### [GB099] Pure Land school · L2
Based on the Sutra of Immeasurable Life, the Contemplation Sutra, and the Amitābha Sutra: Amitābha Buddha, the land of Sukhāvatī, and the forty-eight vows; the formula of "faith – vow – practice" (believing, aspiring, and reciting the Buddha's name); why it is called the "easy path" open to everyone. Links to [M068], [M069], [M150].

#### [GB100] Tiantai school · L3
The first school with a system built by a Chinese founder: Zhiyi and Mount Tiantai; his classification of the teachings in the *Profound Meaning of the Lotus Sutra*; the śamatha–vipaśyanā (Calming and Contemplation) system, one of the most structured in East Asia. Links to [M137].

#### [GB101] Huayan school · L4
Built on the Avataṃsaka Sutra ([GB095]): Fazang and the doctrine of "the unobstructed interpenetration of principle and phenomena"; the vision of a mutually interpenetrating cosmos; its place in East Asian philosophy.

#### [GB102] Faxiang (Yogācāra/Consciousness-Only) school · L3
The school Xuanzang brought back from India after his famous journey to the west; it teaches the Yogācāra system ([GB090]) with a strongly academic character; why it had such a large influence on East Asian Buddhist scholarship and the imperial examination tradition.

#### [GB103] Sanlun (Three Treatises) school · L4
The transmission of Nāgārjuna's Madhyamaka thought into China: the Three Treatises (the Middle Treatise, the Hundred Treatise, the Twelve Gate Treatise); the double-negation dialectic of "neither empty nor not-empty"; its influence spreading into Chan. Links to [M070].

#### [GB104] Shingon and East Asian Esoteric Buddhism · L3
Esoteric Buddhism's transmission to China (Śubhakarasiṃha) and then to Japan (Kūkai, Mount Kōya): the "three mysteries" correspondence (body, speech, mind), the Womb Realm and Diamond Realm mandalas; distinguishes East Asian Esoteric Buddhism from Tibetan Vajrayāna (group F) — sharing the same Indian source but developing differently.

### G.E5. East Asian Buddhism — by country

> **Cross-link:** Vietnamese Buddhism already has its own group, B7 ([GB035]–[GB038]); those articles carry an added `mahayana` category tag so they also appear in this group.

#### [GB105] Buddhism in China · L2
From Emperor Ming of Han (and the legend of his dream of a golden figure) through the waves of sutra translation, the growth of the eight schools, four periods of persecution, the interplay of Confucianism, Daoism, and Buddhism ("the three teachings share one source"), and mainland Chinese Buddhism today. The foundational article for understanding every other East Asian tradition.

#### [GB106] Buddhism in Japan · L3
Arriving in Japan in the 6th century by way of Korea; the Nara and Heian periods (Tendai, Shingon), the Kamakura-era flowering of popular schools (Jōdo Shinshū, Nichiren, Zen), the modern phenomenon of "funeral Buddhism," and new religious movements that grew out of Buddhism. Helps readers understand popular culture (Zen in the tea ceremony, art, manga).

#### [GB107] Buddhism in Korea · L3
Arriving on the peninsula in the 4th century; the unified Silla period (Bulguksa, Seokguram), Seon meditation and the scholarship of Jinul, suppression under the Joseon dynasty, and modern Korean Buddhism (the Jogye Order) and the wave of Korean Seon spreading around the world.

### G.E6. Daily life and practice

#### [GB108] Mahāyāna daily liturgy and ritual · L2
Morning and evening liturgy in monasteries and at home: incense offering, praising the Buddha, the Heart Sutra, the Great Compassion Mantra, repentance rites, and dedication of merit; the meaning of each part; how a newcomer can join a ceremony at a Northern-tradition temple (standing, bowing, joining palms) without worrying about doing it wrong.

#### [GB109] Vegetarianism in Buddhism · L2
Why Mahāyāna Buddhism encourages vegetarianism (the Laṅkāvatāra Sutra, great compassion) while Theravāda does not require it (the "three kinds of pure meat"); levels of vegetarianism: full-time and on set days (the 1st and 15th of the lunar month); vegetarianism and health; clears up the misconception that "if you don't eat vegetarian, you're not really a Buddhist." A neutral comparison across traditions.

#### [GB110] Buddha-recitation in lay life · L2
Buddha-recitation as a daily practice: how to recite (aloud, silently, the "ten recitations" method), reciting with a mala, recitation retreats, and chanting for the sick and the dying; understanding correctly what reciting the Buddha's name for peace or for the deceased actually means. A general-audience article; concentration practice belongs to [M068]; Vietnamese cultural context belongs to [M150].

### G.E7. Mahāyāna / East Asian festivals

> **General principle:** East Asian festivals follow the **Vietnamese–Chinese lunar calendar**; a festival with the same name can have different customs from country to country; every article must state clearly "which lunar month, which day." Vietnam observes the Buddha's Birthday on the 15th of the 4th lunar month — unlike China's 8th day — and this must be noted clearly in each article.

#### [GB111] Mahāyāna / East Asian Buddhist festivals · L1

## G.F. THE VAJRAYĀNA TRADITION

> **Suggested order:** F1 → F2 → F3 → F4 → F5. Readers are encouraged to read [GB083] (on the Mahāyāna) before [GB117], since the Vajrayāna is built on a Mahāyāna foundation. Practice content belongs to [M071]–[M080]; group F here covers general cultural–historical knowledge.

### G.F1. Overview

#### [GB117] Vajrayāna — overview · L2
"Vajra" = an indestructibly hard substance — signifying a uniquely powerful method; positions the Vajrayāna as a distinctive method within the Mahāyāna (neither a "fourth religion" nor an "upgraded version"); distinguishing features: lineage, empowerment, meditational deities, mantra; regions: Tibet, Bhutan, Mongolia, Nepal. Corrects two opposite misconceptions: "Tantric Buddhism is sorcery" and "Tantric Buddhism is a fast track open to anyone."

#### [GB118] From Indian Tantric Buddhism to the Himalayan countries · L3
The historical narrative of transmission: Buddhist tantra developing in India (from roughly the 6th–7th centuries onward) → its transmission to Tibet in the 8th century (Śāntarakṣita, Padmasambhava, Samye Monastery, the Lhasa debate) → a second wave in the 10th–11th centuries (Atiśa, Marpa, and the re-translation of the canon) → the formation of the various schools. A neutral note on the period of persecution under Langdarma.

### G.F2. Foundational concepts

#### [GB119] The four main schools of Tibetan Buddhism · L2
Nyingma (the "ancient tantra" school, Padmasambhava, the Great Perfection/Dzogchen), Kagyu (an oral-transmission lineage, Marpa–Milarepa, Mahāmudrā, the Karmapa), Sakya (the Khön family, the Lamdré path), Gelug (Tsongkhapa, the Lam-rim, the Dalai Lama); the 19th-century Rimé ("non-sectarian") movement; notes that Bön is a distinct tradition in its own right. For each school: its distinctive practices and its leading figures.

#### [GB120] The spiritual teacher — lama, guru, and lineage · L2
Why the Vajrayāna places lineage and the teacher at its center; the nature of the teacher–student relationship in this tradition; **a required section:** healthy boundaries — signs of a trustworthy lama or community, and warning signs (referencing [M080] on requirements for lineage transmission). Written neutrally, neither praising nor disparaging any specific individual.

#### [GB121] What is an empowerment (abhiṣeka) · L2
An empowerment as a ceremony that "authorizes practice" of a particular method — not a mystical blessing that can be bought; the types of empowerment; why certain practices require one beforehand. Answers common questions ("Can I receive an empowerment just by attending a ceremony?").

#### [GB122] Mantra, mandala, and yidam — a plain-language look · L2
Three "esoteric methods": mantra (what OM MANI PADME HŪM means), mandala (a map of both the mind and a pure realm), and yidam (a meditational deity — an enlightened form used for self-identification in practice). Presented as a symbolic language rather than magic. Links to [M074], [M075].

#### [GB123] The path of practice in the Vajrayāna · L3
A picture of the path: the foundational contemplations (the rarity of human life, impermanence, karma, the suffering of saṃsāra) → the preliminary practices (ngöndro) → deity practice → the generation and completion stages → the culminating practices (Mahāmudrā, Dzogchen). A general-audience map article; detailed practice is at [M143], [M144], [M077]–[M079].

#### [GB124] Tulkus — the reincarnation system, the Dalai Lama, and the Karmapa · L2
The tulku system: a teacher who is recognized as reincarnating to continue the same path of practice; the history of the system (from the 13th-century Karmapa onward), the 1st through 14th Dalai Lamas, the Qing-era "golden urn" custom; modern-day questions surrounding child tulkus. Presents both how the traditions understand this themselves and how academic scholarship describes it.

#### [GB125] Prayer flags, prayer wheels, and butter lamps · L1
"From seeing to understanding": the five-colored prayer flags (the principle of the wind carrying the mantra), the prayer wheel (turning it as a form of recitation), and the butter lamp (the light of wisdom) — noting accurately which objects are genuinely in use; what visitors should and shouldn't do when visiting a monastery. A light, image-driven article that answers everyday curiosity.

### G.F3. Scriptures

#### [GB126] The Tibetan canon — Kangyur and Tengyur · L3
The Kangyur (the Buddha's words translated into Tibetan, roughly 100 volumes) and the Tengyur (commentaries, over 200 volumes); the historic woodblock editions (Narthang, Derge); the Nyingma school's separate tantra collection; the 84000 project translating the canon into English. The place of tantra within the canon relative to the Perfection-of-Wisdom sutras.

### G.F4. Countries and the present day

#### [GB127] Tibet and the exile community · L3
From unification in the 7th century through the era of the Dalai Lamas, the events of 1959 and the resulting exodus, the re-establishment of monastic institutions in India (Dharamsala, etc.), and the state of the religion inside and outside Tibet today. **Written neutrally** per editorial policy: presenting sources of disagreement and avoiding one-sided political language.

#### [GB128] Vajrayāna in Bhutan, Mongolia, Nepal, and elsewhere · L3
Bhutan (Drukpa Kagyu as the state religion, Gross National Happiness), Mongolia (Gelug, the Soviet period, and its revival after 1990), Nepal (Newar Buddhism — the only living Vajrayāna lineage directly descended from India), the Buryat–Kalmyk–Tuvan communities of Russia, and Vajrayāna in the West.

### G.F5. Vajrayāna festivals

> **General principle:** festivals follow the **Tibetan calendar** (which differs from the Vietnamese–Chinese lunar calendar by roughly one to two months, depending on the year); every article must record the conversion principle rather than converting to a fixed solar-calendar date.

#### [GB129] Vajrayāna festivals · L2

## G.G. COMPARISON & ORIENTATION

#### [GB134] Comparing the three major traditions — a reference table · L2
An overall comparison of Theravāda / Mahāyāna / Vajrayāna: scriptures and language, ideals (arhat / bodhisattva / bodhisattva-with-esoteric-means), geographic reach, characteristic forms of practice, the year's biggest festival; plus a list of "major points held in common" (the Four Noble Truths, the Noble Eightfold Path, monastic discipline, the Sangha, nirvana). Conclusion: the differences lie in method and emphasis, not in "which path is true and which is false."

#### [GB135] One Buddhism, many paths — a non-sectarian attitude · L2
Why learners should respect every tradition; modern teachers who have studied across several lineages (the Rimé movement; Vietnamese Zen masters who combine Zen and Pure Land practice); how to read an article that criticizes another school while keeping a balanced attitude; the answer to "which school is truest?" — a question that should be reframed as "which school fits me?" Links to editorial principles 1 and 10.

## G.H. REFERENCE & TOOLS

#### [GB137] Index of commonly encountered scriptures — from the Nikāyas to the tantras · R
An index of scriptures from all three traditions, with suggested Vietnamese translations and a difficulty rating: the Nikāyas (Pāli), well-known Mahāyāna sutras in Chinese translation, and the main tantras; a guide to reading citations (what "MN 10" means, for example). Draws on [GB064], [GB092], [GB126].

#### [GB138] Index of schools, sub-schools, and lineages · R
A reference index of the names of schools, sub-schools, and lineages (from the Sarvāstivāda to Nichiren): Pāli/Sanskrit and Sino-Vietnamese names, region, and a one-line summary of each lineage's core teaching. Helps readers avoid confusing one "school" with another.

#### [GB140] Frequently asked questions about Buddhism · R
A collection of the short questions beginners most often ask: can a Buddhist drink alcohol; how to bow properly at temple; what is the difference between a buddha and a bodhisattva; which sutra to read first; is it acceptable to practice at home rather than ordaining; how many incense sticks to light; lucky numbers; whether "star" rituals and astrological offerings are actually part of Buddhism...

---

# LEARNING PATH

## Main path (for newcomers, no tradition chosen yet)

> **Principle:** This is a suggested order based on difficulty and conceptual dependency, not a mandatory sequence. Users can jump to any article at any time through the [GB141] index.

```text
Step 0 — Orientation                                       L1
GB001 → GB002 → GB003 → GB004 → GB013
GB005, GB007 = reading-skill articles, read whenever needed

Step 1 — The Buddha's life and origins                     L1–L2
GB015 → GB016 → GB017 → GB018 → GB019 → GB020 → GB021
Go deeper if you like: GB014, GB022, GB023

Step 2 — Shared foundational theory                        L1–L3
GB039 → GB040 → GB041 → GB042 → GB043 → GB044 → GB045 → GB046 → GB047
→ GB048 → GB050 → GB051 → GB052 → GB054 → GB055 → GB056 → GB057 → GB059
Go deeper if you like: GB049, GB053, GB058, GB060, GB061

Step 3 — A map of the three traditions                     L2
GB027 → GB134 → choose a tradition in Step 4

Step 4 — Explore one tradition                              L1–L4
├── Theravāda:  see the Theravāda path below
├── Mahāyāna:   see the Mahāyāna path below
└── Vajrayāna:  see the Vajrayāna path below

Step 5 — History of the spread and its context             L2–L3
GB024 → GB025 → GB026 → GB028 → GB029 → GB030
→ GB031 / GB032 / GB033 (pick the route you're interested in) → GB034

Step 6 — Begin practice
Move to the Meditation section (M codes) and follow that section's path;
transition articles: [GB057], [GB068], [GB110]
```

## Path by tradition — Theravāda

```text
GB062 → GB063 → GB064 → GB067 → GB068 → GB069 → GB070
→ (GB065, GB066 for readers who want to go deeper into the scriptures)
→ one country article: GB071 / GB072 / GB073 / GB074 / GB075
→ the festivals group: GB076 → GB077 → GB079 → GB080
```

## Path by tradition — Mahāyāna

```text
GB083 → GB084 → GB085 → GB086 → GB091 → GB092 → GB093
→ (GB087 → GB089 → GB090 for readers who want to go deeper into the thought)
→ GB097 → choose a school: GB098 / GB099 / GB100…
→ one country article: GB105 / GB106 / GB107 (Vietnam: GB035–GB038)
→ daily life: GB108 → GB109 → GB110
→ the festivals group: GB111 → GB112 → GB114 → GB116
```

## Path by tradition — Vajrayāna

```text
(reading GB083–GB085 on the Mahāyāna first is recommended)
GB117 → GB118 → GB119 → GB120 → GB121 → GB122 → GB123 → GB124
→ GB126 → one country article: GB127 / GB128
→ the festivals group: GB129 → GB130 → GB131
```

## Side path — For Vietnamese readers who want to understand the Buddhism around them

```text
GB038 → GB035 → GB036 → GB037 → GB108 → GB110 → GB114 → GB116 → GB112 → GB075
```

## Side path — "A festival is coming up and I want to understand it"

```text
Read the specific festival article in D5 / E7 / F5 → then go back to the source article
(For example: before Ullambana, read [GB114] → [GB021], [GB053]; before Vesak, read [GB077] → [GB015].)
Tool: [GB139], the three-tradition festival calendar.
```

## Learning-path principles

1. **Groups A–H are the content structure; the learning sequence is only a suggestion**, shown as a "Next step" prompt rather than something that locks an article.
2. **History doesn't wait for doctrine, and doctrine doesn't wait for history.** Users may start with whichever group interests them; the app suggests foundational articles whenever it detects an unfamiliar concept.
3. **Festival articles are a legitimate front door.** Many people in Vietnam first come to Buddhism through Ullambana or the Buddha's Birthday; every festival article must stand on its own and link back to the corresponding doctrinal article.
4. **No content is gated by sequence.** Every article is always reachable through the [GB141] index.

# RULES FOR USING CODES AND METADATA IN THE APP

## 1. One article, several branches
For example, the article on Vietnamese Buddhism is written once under B7 but also appears under E5:

```yaml
id: GB038
title: "A map of Vietnamese Buddhism today"
level: L2
traditions: [vietnam, mahayana, theravada]   # the article covers all three lineages present in Vietnam
categories: [history, vietnam]
```

## 2. A shared article and a tradition-specific article are two different articles

```text
[GB044] The Noble Eightfold Path — overview        ← shared doctrine (group C)
[GB067] The path of practice in Theravāda            ← how one tradition puts it into practice
[GB123] The path of practice in the Vajrayāna         ← how another tradition puts it into practice
```

## 3. Same title = same concept; same code = same article
New articles get a new code, taking the next unused number (currently starting at **GB142**). A retired code must be recorded in a retirement list and never reused.

## 4. Tradition and festival data are metadata, not a separate taxonomy

```yaml
id: GB077
title: "Vesak — the Buddha's birth, awakening, and passing in a single day"
level: L1
traditions: [theravada]
categories: [festival, theravada]
calendar: theravada-lunar      # lunar | theravada-lunar | tibetan-lunar | solar
date: "the full moon of the month of Vesākha (roughly May–June on the solar calendar, depending on the year)"
requires: [GB062]
related:  [GB112, GB131, GB139]
sources:  ["Sri Lankan / Thai tradition; UN resolution on the Day of Vesak"]
```

This lets the app browse content by **tradition**, by **topic** (history / doctrine / festival), and by **level** — and, most importantly for the festivals group, **compute the solar-calendar date for a given year** and send calendar reminders.

## 5. Required fields
- `level` — builds the learning path and helps users know whether an article suits them.
- `calendar` — required for every article in the festivals groups (D5/E7/F5); an article's body text must never convert this to a fixed solar-calendar date.
- `terms` — enables in-article term lookups, sharing its data with the Meditation section.

---

# EDITORIAL PRINCIPLES

1. **Never use the taxonomy to rank traditions.** "Advanced" means "requires more background knowledge," not "tradition A ranks higher than tradition B." Formulations such as "Theravāda is the Lesser Vehicle" are forbidden.
2. **Distinguish Pāli from Sanskrit, and always give the Sino-Vietnamese form alongside them**; for East Asian and Tibetan proper names, keep the original term and gloss it (*niànfó*, *Losar*, *tulku*). Use diacritics correctly, with an agreed-upon fallback if the display system can't render them.
3. **Layer sources: scripture → commentary → treatise → modern scholarship → folk custom.** A great deal of content Vietnamese readers think of as "Buddhist" (memorial days, astrological offerings, pinning a flower for Ullambana) belongs to the folk-custom layer — state its actual origin rather than attributing it to "the scriptures teach."
4. **State a tradition's scope explicitly within the article.** Only tag a tradition when the content is genuinely specific to it; shared doctrine should not be tagged with all three tradition labels just because "it applies everywhere."
5. **Group C contains only shared doctrine.** Where traditions explain a doctrinal point differently (nirvana, the intermediate state in rebirth, the stages of realization), present the universal version in C and the tradition-specific versions in D/E/F.
6. **A festival article needs all three layers: the underlying doctrinal meaning — regional customs — how the date is set on the relevant calendar.** Never turn a festival article into a guide for ritual offerings aimed at personal gain; explain the rites in the spirit of the underlying teaching.
7. **Record the historical record's degree of certainty.** The Buddha's dates, the details of the various councils, early Vietnamese Buddhism, and more all have multiple competing accounts; present the leading options with sources rather than picking one and presenting it as the only fact.
8. **Never assert or deny metaphysical doctrine on Claude's — or the app's — own authority.** For content such as the realms of existence, rebirth, and merit multiplied many times over: present "how the traditions understand this," together with an academic perspective where one exists.
9. **Accessibility is a core requirement.** Every difficult concept needs at least one everyday example or illustration; favor tables, timelines, and diagrams; keep sentences short. L1 content must be readable by a high-school student.
10. **A neutral, respectful tone** — between schools, between Buddhism and other religions, and on sensitive historical–political topics (for example [GB127]): present the sources of disagreement without using partisan language.

---

# TERMINOLOGY CROSS-REFERENCE TABLE (a starting point for [GB136])

| Pāli | Sanskrit | Sino-Vietnamese | Common Vietnamese usage | English |
|------|----------|----------|------------------------|---------|
| buddha | buddha | Phật | Đức Phật, bậc giác ngộ | Buddha / awakened one |
| dhamma | dharma | Pháp | giáo pháp | Dhamma / Dharma |
| saṅgha | saṃgha | Tăng-già | tăng đoàn, cộng đồng tu học | Sangha |
| tissaraṇa | triśaraṇa | tam quy | quy y tam bảo | three refuges |
| sīla | śīla | giới | giới đức, quy tắc rèn luyện | virtue / precepts |
| pañcasīla | pañcaśīla | ngũ giới | năm giới | five precepts |
| dukkha | duḥkha | khổ | khổ, bất toại nguyện | suffering |
| ariyasacca | āryasatya | thánh đế | tứ diệu đế | Noble Truth |
| magga | mārga | đạo | con đường, bát chánh đạo | path |
| paṭiccasamuppāda | pratītyasamutpāda | duyên khởi | nhân duyên sinh | dependent origination |
| kamma | karma | nghiệp | nghiệp, nhân quả | karma / action |
| saṃsāra | saṃsāra | luân hồi | vòng sinh tử | cyclic existence |
| puñña | puṇya | phước | công đức, phước báu | merit |
| nibbāna | nirvāṇa | niết-bàn | niết-bàn | nirvana |
| parinibbāna | parinirvāṇa | bát-niết-bàn | nhập diệt | final nirvana |
| arahant | arhat | a-la-hán | bậc la-hán | arhat |
| sotāpanna | srotāpanna | tu-đà-hoàn | nhập lưu | stream-enterer |
| bodhisatta | bodhisattva | bồ-tát | bồ-tát | bodhisattva |
| — | bodhicitta | bồ-đề tâm | tâm bồ-đề | awakening mind |
| pāramī | pāramitā | ba-la-mật | độ, hoàn thiện | perfection |
| suññatā | śūnyatā | (tánh) không | tánh Không | emptiness |
| — | tathāgatagarbha | như lai tạng | Phật tánh | buddha-nature |
| — | trikāya | tam thân | ba thân Phật | three bodies |
| paññā | prajñā | tuệ | trí tuệ | wisdom |
| khandha | skandha | uẩn | năm uẩn | aggregate |
| anicca | anitya | vô thường | vô thường | impermanence |
| anattā | anātman | vô ngã | vô ngã | non-self |
| taṇhā | tṛṣṇā | ái | tham ái | craving |
| mettā | maitrī | từ | từ ái | loving-kindness |
| karuṇā | karuṇā | bi | lòng bi | compassion |
| brahmavihāra | brahmavihāra | tứ phạm trú | tứ vô lượng tâm | divine abodes |
| tipiṭaka | tripiṭaka | tam tạng | ba tạng kinh điển | Triple Basket |
| vinaya | vinaya | luật (tạng) | luật xuất gia | monastic discipline |
| sutta | sūtra | kinh | kinh | discourse / sutra |
| abhidhamma | abhidharma | a-tỳ-đàm, luận | đối pháp | higher teaching |
| nikāya | āgama | bộ (kinh), a-hàm | bộ kinh | collection |
| uposatha | upoṣadha | bố-tát | ngày trai giới | observance day |
| vassa | varṣā | an cư | mùa an cư kiết hạ | rains retreat |
| — | kaṭhina | ca-thi-na | lễ dâng y | robe-offering ceremony |
| — | vesākha (month) | — | tháng Phật đản | Vesak month |
| — | pūjā | cúng dường | lễ cúng, nghi quyến | devotional ritual |
| — | gāthā | kệ | bài kệ | verse |
| — | stūpa | tháp | bảo tháp, tháp xá-lợi | stupa |
| — | mantra | chân ngôn | câu chú | mantra |
| — | maṇḍala | mạn-đà-la | đồ hình | mandala |
| — | tantra | tục (kinh Mật) | tantra, kinh Mật | tantra |
| — | vajra | kim cương | kim cương | vajra / diamond |
| — | guru (Tib. lama) | sư, lama | thầy tâm linh | teacher / lama |
| — | abhiṣeka | quán đảnh | quán đảnh | empowerment |
| — | tulku (Tib.) | hóa thân | vị tái sinh | incarnate lama |
| dhyāna → chán 禪 | dhyāna | Thiền | Thiền tông | Chan / Zen |
| — | niànfó 念佛 | niệm Phật | niệm Phật | buddha-recitation |
| — | sthaviravāda | Thượng tọa bộ | Nam tông, đạo Nam | Way of the Elders |
| — | mahāyāna | Đại thừa | Bắc tông, đạo Bắc | Great Vehicle |
| — | vajrayāna | Kim cương thừa | Mật tông, Mật giáo | Diamond / Vajra Vehicle |

> **Note:** the term "Hīnayāna (Lesser Vehicle)" appears in some Mahāyāna texts; it is **not used** today as the name of a living tradition in this app because it carries a value judgment; when referring to the early schools, use "early Buddhist schools" or "Theravāda" when referring specifically to that lineage.

---

# SUGGESTED SOURCES FOR WRITERS

## Scriptures and Vietnamese translations
- The Pāli canon, Vietnamese translation by Ven. Thích Minh Châu (Dīgha and Majjhima Nikāyas) — the basis for groups C and D.
- The Heart Sutra, the Diamond Sutra, and the Lotus Sutra — translations and commentary by Ven. Thích Trí Quang — the basis for [GB093], [GB094].
- Suttacentral (suttacentral.net) — cross-referencing the Pāli suttas with the Chinese Āgamas.
- 84000 (84000.co) — the Tibetan canon, in ongoing English translation — the basis for [GB126].

## History and scholarship
- Peter Harvey, *An Introduction to Buddhism* — a balanced textbook for groups B and C.
- Andrew Skilton, *A Concise History of Buddhism* — the historical line of the various schools, for B4–B5.
- Nguyễn Lang, *Việt Nam Phật giáo sử luận* (A History of Vietnamese Buddhism) — the basis for B7.
- *Thiền uyển tập anh* (with modern scholarship) — for B7 and [M146].
- Heinz Bechert & Richard Gombrich (eds.), *The World of Buddhism* — a map of the traditions.

## Festivals and culture
- Materials from national Buddhist organizations (Sri Lanka, Thailand, the Tibetan exile community) on the annual festival calendar — the basis for D5, F5; always cross-check at least two sources, since festival dates are set by lunar or Tibetan-lunar calendars.
- Vietnamese folklore scholarship on Ullambana, memorial days, and the Lantern Festival — used together with the source-layering principle (custom ≠ scripture).

## Reference
- Nyanatiloka Mahāthera, *Buddhist Dictionary* — Pāli terminology.
- The *Fo Guang Dictionary of Buddhism* (佛光大辭典) — Sino-Vietnamese terminology.
- CBETA (cbeta.org) — the Chinese canon, for citing Mahāyāna sutras when needed.

> **Note:** verify sources again before publishing; prefer primary sources (scriptures, treatises, a tradition's own organizational website) over aggregator sites; details on Vietnamese history in [GB035] and [GB075] need to be checked against domestic sources before writing.

---

# VERSION 1.0 NOTES

## Structural thinking
- The main axis follows the brief: **history (B) → shared core theory (C) → the three traditions from basic to advanced (D/E/F), each tradition with its own festivals group (D5, E7, F5)**; A serves as the entry layer, G as comparison, H as reference.
- `GBxxx` codes are kept entirely separate from the Meditation section's `Mxxx` codes so the two sections can cross-link without ID conflicts.
- Group C is strictly defined as "doctrine shared by all three traditions"; every point of difference lives in D/E/F and is brought together in [GB134].
- Vietnamese Buddhism is written once under B7 and tagged with metadata so it also appears under E5/D4 — following the "one article, many branches" principle.

## Suggestions for the next round
1. **Prioritize writing roughly the first 30 L1 articles**: A1–A3, [GB015]–[GB016], C1–C2, [GB050], [GB058], [GB062], [GB083], [GB085], the major festival group ([GB077], [GB112], [GB114]) — enough for a complete beginner's path.
2. **[GB139], the festival calendar, needs to be built as structured, year-based data (all three calendar systems)** before writing it up as a static article; this is a natural "festival reminder" feature for the app.
3. Invite at least one monastic or teacher from **each tradition** to review groups D, E, F and the festival articles before publication.
4. Consider adding, in a future round, a group on "Buddhism and modern issues" (Buddhism and science, the environment, psychology) — deliberately left out of the v1.0 scope.

## Version 1.0 statistics
- Total articles: **141** (GB001–GB141; no retired codes yet).
- Next code when adding a new article: **GB142**.
- Distribution by level: L1 ≈ 27 · L2 ≈ 73 · L3 ≈ 32 · L4 = 3 · L5 = 0 (reserved for the Meditation section) · R = 6.
- Festival groups: Theravāda 7 articles (D5) · Mahāyāna/East Asia 6 articles (E7) · Vajrayāna 5 articles (F5), plus the calendar tool [GB139].
- Top-level taxonomy: **7 groups** (A–H; no separate group for "comparison" apart from G — G currently combines comparison & orientation).

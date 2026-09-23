# Meditation Theory — Taxonomy & Article Catalog (en-US)

**Version:** 3.6 · **Updated:** 2026-09-22 · **Status:** content framework for the "Meditation" section of the app

> **Purpose:** Each `Mxxx` code corresponds to **one standalone article**. The same code can appear under several taxonomy branches; in that case the app stores the article once and attaches multiple categories/tags to it.
>
> **Principle 1 — A learning path, not a ranking.** "Basic → advanced" is a **path for building skills**, not a ranking between traditions. Theravāda, Mahāyāna, and Vajrayāna overlap at many points; the same method can exist across several traditions while being explained and practiced differently.
>
> **Principle 2 — Codes are permanent.** An `Mxxx` code is a **stable ID** and is never renumbered when articles are added or removed. The order of codes in the tree therefore does **not** match reading order; reading order lives in the *Learning Path* section. A retired code is **never reused** for a different article.
>
> **Principle 3 — Same article, same code.** If two entries are truly the same article, they use the same code and the same title. If they only share a name while the content or tradition needs a different explanation, give them separate codes and state the tradition explicitly in the title.
>
> **Principle 4 — Terminology.** Prefer **Pāli** for Theravāda / Pāli-canon content and **Sanskrit** for Mahāyāna / Vajrayāna content, always alongside the **Sino-Vietnamese (Hán–Việt)** form Vietnamese readers already use (for example: *satipaṭṭhāna* = tứ niệm xứ). See the cross-reference table at the end of the file.

## Level conventions

| Code | Name | Meaning |
|----|-----|---------|
| **L1** | Entry level | Readable and usable right away by someone who has never meditated |
| **L2** | Foundational | Core skills that need repeated practice |
| **L3** | Intermediate | Assumes a stabilized practice on some object plus a grasp of the theoretical framework |
| **L4** | In-depth | Scriptural/treatise content, the progress-of-insight map, tradition-specific systems |
| **L5** | Requires prerequisites | Practice that calls for a teacher, transmission, or empowerment; the app presents it only at an **educational, overview** level |
| **R** | Reference | Reference articles, glossaries, FAQs — not part of the linear learning path |

---

# CONVENTIONS FOR THE NATURE OF THE TAXONOMY

Taxonomy v3.5 uses different high-level types of information rather than treating every branch as a parallel "school of meditation":

| Group | Nature | Function in the app |
|---|---|---|
| **A** | `foundation` — foundational knowledge | Explains concepts, context, how to begin, and safety |
| **B** | `skill` — skill | Practical skills used across many methods |
| **C** | `method` — method / practice direction | C1 Calm-abiding meditation (Samatha) and C2 Insight meditation (Vipassanā) — two methods, each further divided into ordered learning groups |
| **D** | several subtypes: `framework` / `practice_group` / `object_taxonomy` | D1 is a practice framework; D2 is a group of practices; D3 is a classification system of meditation objects. These branches have parent–child structure and can cross-link |
| **E** | `tradition` — meditation lineage / tradition | Theravāda, Mahāyāna, Vajrayāna, and the systems within them |
| **F** | `regional_tradition_context` — cultural / regional context | How these practices are carried out within Vietnamese Buddhism |
| **G** | `application_context` / `secular_context` — application / context / goal | Daily life, health, and secular meditation |

**Note:** The same article can carry several attributes. `methods`, `traditions`, `objects`, `goals`, `duration`, `requires`, `safety`, and `sources` are separate data dimensions, not sub-levels of one single taxonomy.

# TAXONOMY TREE

> **v3.5 structure:** The top-level branches are not treated as parallel "types of meditation." They are organized by **the nature of the information**: foundational knowledge, skill, method, framework/practice-group/system, tradition, cultural context, and application. Within each branch, entries are arranged **overview → group → detailed practice/topic** wherever the content calls for it. One article can appear in several branches; the `traditions`, `methods`, `objects`, `goals`, and other metadata fields describe those separate classification dimensions.

```text
Meditation
│
├── M.A. FOUNDATIONAL KNOWLEDGE & ORIENTATION
│   ├── M.A1. Understanding meditation
│   │   ├── [M001] What is meditation? · L1
│   │   ├── [M002] Buddhist meditation and secular meditation · L1
│   │   └── [M095] Meditation within the three trainings — ethics, concentration, wisdom · L1
│   ├── M.A2. Understanding how to practice
│   │   ├── [M096] Mindfulness and clear comprehension (sati and sampajañña) · L1
│   │   ├── [M097] Reading meditation terminology: Pāli, Sanskrit, and Sino-Vietnamese · L1
│   │   └── [M098] Common misconceptions about meditation · L1
│   ├── M.A3. Safety in meditation
│   │   └── [M099] Safety in meditation — when to adjust or stop · L1
│   ├── M.A4. Preparing for a sitting
│   │   ├── [M003] Preparing before you meditate · L1
│   │   ├── [M004] Meditation posture · L1
│   │   └── [M005] Session length and frequency · L1
│   ├── M.A5. During and after a sitting
│   │   ├── [M006] Handling distraction, drowsiness, and restlessness · L1
│   │   └── [M007] How to end a sitting · L1
│   ├── M.A6. Building a habit
│   │   └── [M008] Building a meditation habit · L1
│   └── M.A7. Support and going deeper
│       ├── [M100] Spiritual friendship and teachers (Kalyāṇamitta) · L2
│       └── [M101] Retreats and extended intensive practice · L3
│
├── M.B. SHARED PRACTICAL SKILLS
│   ├── M.B1. Body and breath foundations
│   │   ├── [M009] Releasing bodily tension · L1
│   │   ├── [M010] Noticing the natural breath · L1
│   │   └── [M011] Counting the breath · L1
│   ├── M.B2. Stabilizing and sustaining attention
│   │   ├── [M012] Following the sensations of the breath · L2
│   │   └── [M013] Anchoring the mind on an object · L2
│   ├── M.B3. Working with distraction and practice attitude
│   │   ├── [M014] Noticing thought and distraction · L2
│   │   └── [M105] The attitude of practice: balanced effort, neither forcing nor drifting · L2
│   ├── M.B4. Observing and directing experience
│   │   ├── [M102] Noting / silent labeling · L2
│   │   └── [M103] Wise attention · L2
│   ├── M.B5. Balancing the faculties
│   │   └── [M104] Balancing the five faculties · L3
│   ├── M.B6. Integrating practice into movement and daily life
│   │   ├── [M015] Walking meditation (Caṅkama) · L1
│   │   └── [M016] Mindfulness in daily activity · L1
│   ├── M.B7. Tracking and reflecting on practice
│   │   └── [M106] A meditation journal and how to recognize progress · L2
│   └── M.B8. Frequently asked questions about meditation
│       └── [M162] Frequently asked questions about meditation · R
│
├── M.C. METHOD / PRACTICE DIRECTION
│   ├── M.C1. Calm-Abiding Meditation (Samatha / Śamatha)
│   │   ├── M.C1.1. Foundations of calm abiding and concentration
│   │   │   ├── [M017] Calm-Abiding Meditation (Samatha / Śamatha) · L2
│   │   │   └── [M022] Concentration and the continuity of attention · L2
│   │   ├── M.C1.2. Common practice objects
│   │   │   ├── [M018] Calm abiding with the breath (Samatha) · L2
│   │   │   ├── [M019] Calm abiding with body sensation (Samatha) · L2
│   │   │   ├── [M020] Calm abiding with sound (Samatha) · L2
│   │   │   └── [M021] Calm abiding with an image or object (Samatha) · L2
│   │   ├── M.C1.3. Hindrances and the meditative sign
│   │   │   ├── [M109] The five hindrances · L2
│   │   │   └── [M108] The meditative sign and its stages (Nimitta) · L3
│   │   ├── M.C1.4. Levels of concentration and absorption
│   │   │   ├── [M107] Three levels of concentration · L3
│   │   │   ├── [M023] Deep concentration and jhāna (Jhāna / Dhyāna) — overview · L3
│   │   │   ├── [M110] The four form-sphere jhānas and the five jhāna factors · L4
│   │   │   └── [M111] The four formless attainments · L4
│   │   └── M.C1.5. Combining concentration and wisdom
│   │       └── [M112] Combining concentration and wisdom · L4
│   │
│   └── M.C2. Insight Meditation (Vipassanā / Vipaśyanā)
│       ├── M.C2.1. Foundations of insight
│       │   └── [M024] Insight Meditation (Vipassanā / Vipaśyanā) · L2
│       ├── M.C2.2. Direct observation of experience
│       │   ├── [M029] Observing the mind's reactions · L2
│       │   ├── [M030] Direct experience versus the mind's story · L2
│       │   ├── [M031] Mindfulness of thought · L2
│       │   └── [M032] Mindfulness of strong emotion · L3
│       ├── M.C2.3. Observing arising and passing away, and the three characteristics
│       │   ├── [M025] Observing arising and passing away · L3
│       │   ├── [M053] The three characteristics (Tilakkhaṇa) — overview · L2
│       │   ├── [M026] Contemplating impermanence (Anicca) · L2
│       │   ├── [M027] Contemplating suffering / unsatisfactoriness (Dukkha) · L3
│       │   └── [M028] Contemplating non-self (Anattā / Anātman) · L3
│       ├── M.C2.4. Deeper analytical frameworks
│       │   ├── [M120] Distinguishing mind and matter (Nāma-rūpa) · L3
│       │   └── [M121] Dependent origination in direct observation · L4
│       ├── M.C2.5. The progress of insight
│       │   ├── [M122] The progress of insight: seven purifications and sixteen knowledges — overview · L4
│       │   └── [M123] The ten corruptions of insight (Vipassanupakkilesa) · L4
│       └── M.C2.6. Difficulties and safety
│           └── [M124] Difficult stages in insight practice and how to respond safely · L4
│
├── M.D. FRAMEWORKS / GROUPS / SYSTEMS OF PRACTICE
│   ├── M.D1. The Four Foundations of Mindfulness (Satipaṭṭhāna / Smṛtyupasthāna)
│   │   ├── M.D1.0. The four foundations of mindfulness
│   │   │   └── [M033] The Four Foundations of Mindfulness (Satipaṭṭhāna / Smṛtyupasthāna) — overview · L2
│   │   ├── M.D1.1. Contemplation of the body (Kāyānupassanā)
│   │   │   ├── [M034] Contemplation of the body (Kāyānupassanā) · L2
│   │   │   ├── [M035] Mindfulness of breathing within the four foundations (Satipaṭṭhāna) · L2
│   │   │   ├── [M113] Mindfulness of breathing — sixteen steps in four tetrads (Ānāpānassati) · L4
│   │   │   ├── [M036] Contemplating posture and movement (Iriyāpatha) · L2
│   │   │   └── [M114] Mindfulness immersed in the body (Kāyagatāsati) · L3
│   │   ├── M.D1.2. Contemplation of feeling (Vedanānupassanā)
│   │   │   └── [M037] Contemplation of feeling (Vedanānupassanā) · L2
│   │   ├── M.D1.3. Contemplation of mind (Cittānupassanā)
│   │   │   └── [M038] Contemplation of mind (Cittānupassanā) · L3
│   │   ├── M.D1.4. Contemplation of dhammas (Dhammānupassanā)
│   │   │   ├── [M039] Contemplation of dhammas (Dhammānupassanā) · L3
│   │   │   ├── [M109] The five hindrances · L2
│   │   │   ├── [M116] Contemplation of dhammas: the five aggregates · L3
│   │   │   ├── [M117] Contemplation of dhammas: the six internal–external sense bases · L3
│   │   │   ├── [M118] Contemplation of dhammas: the seven factors of awakening · L3
│   │   │   └── [M119] Contemplation of dhammas: the four noble truths · L3
│   │   └── [M040] The four foundations of mindfulness, basic to advanced (Satipaṭṭhāna) · L3
│   │
│   ├── M.D2. The Divine Abodes (Brahmavihāra)
│   │   ├── [M041] The Divine Abodes (Brahmavihāra) — overview · L2
│   │   ├── M.D2.1. Loving-kindness (Mettā / Maitrī)
│   │   │   ├── [M042] Loving-kindness (Mettā / Maitrī) · L1
│   │   │   └── [M125] Cultivating loving-kindness — the sequence of objects (Mettā bhāvanā) · L2
│   │   ├── M.D2.2. Compassion (Karuṇā)
│   │   │   └── [M043] Compassion (Karuṇā) · L2
│   │   ├── M.D2.3. Appreciative joy (Muditā)
│   │   │   └── [M044] Appreciative joy (Muditā) · L2
│   │   ├── M.D2.4. Equanimity (Upekkhā / Upekṣā)
│   │   │   └── [M045] Equanimity (Upekkhā / Upekṣā) · L3
│   │   └── M.D2.5. Synthesis and shared analysis
│   │       ├── [M046] The four divine abodes as one system · L3
│   │       └── [M126] The near and far enemies of the four qualities · L3
│   │
│   │   > **Relationship to D3:** In the Visuddhimagga's system of forty meditation subjects, the divine abodes (Brahmavihāra) form one group within Kammaṭṭhāna. D2 exists as an independent thematic branch so users can study loving-kindness, compassion, joy, and equanimity on their own; this does not mean D2 and D3 are two wholly separate systems.
│   │
│   └── M.D3. The System of Meditation Subjects (Kammaṭṭhāna)
│       ├── M.D3.1. Overview, classification, and selection
│       │   ├── [M127] The forty meditation subjects (Kammaṭṭhāna) — overview after the Visuddhimagga · L3
│       │   ├── [M128] Temperament — six types and how to choose a subject (Carita) · L3
│       │   └── [M054] Choosing a subject that suits you · L2
│       ├── M.D3.2. Kasiṇa devices
│       │   └── [M060] Kasiṇa devices — the ten kasiṇas · L4
│       ├── M.D3.3. Contemplation of foulness (Asubha)
│       │   └── [M047] Contemplation of foulness (Asubha) · L4
│       ├── M.D3.4. Related body-contemplation subjects
│       │   └── [M048] The thirty-two parts of the body (Dvattiṃsākāra) · L4
│       ├── M.D3.5. Analysis of the four elements (Catudhātuvavatthāna)
│       │   └── [M129] Analysis of the four elements (Catudhātuvavatthāna) · L4
│       ├── M.D3.6. Perception of the repulsiveness of food (Āhāre paṭikūlasaññā)
│       │   └── [M130] Perception of the repulsiveness of food (Āhāre paṭikūlasaññā) · L4
│       ├── M.D3.7. Recollections (Anussati)
│       │   ├── [M131] The ten recollections (Dasa anussati) — overview · L3
│       │   ├── M.D3.7.1. Recollection of the Buddha (Buddhānussati / Buddhānusmṛti)
│       │   │   └── [M050] Recollection of the Buddha (Buddhānussati / Buddhānusmṛti) · L2
│       │   ├── M.D3.7.2. Recollection of the Dhamma (Dhammānussati / Dharmānusmṛti)
│       │   │   └── [M051] Recollection of the Dhamma (Dhammānussati / Dharmānusmṛti) · L2
│       │   ├── M.D3.7.3. Recollection of the Sangha (Saṅghānussati / Saṃghānusmṛti)
│       │   │   └── [M052] Recollection of the Sangha (Saṅghānussati / Saṃghānusmṛti) · L2
│       │   ├── M.D3.7.4. Recollection of virtue, generosity, and the deities
│       │   │   └── [M132] Recollection of virtue, generosity, and the deities · L3
│       │   ├── M.D3.7.5. Recollection of death (Maraṇassati / Maraṇasmṛti)
│       │   │   └── [M049] Recollection of death (Maraṇassati / Maraṇasmṛti) · L3
│       │   └── M.D3.7.6. Recollection of peace (Upasamānussati)
│       │       └── [M133] Recollection of peace (Upasamānussati) · L4
│       └── M.D3.8. Cross-links
│           ├── The Divine Abodes (Brahmavihāra) → see D2
│           └── The four formless attainments → see [M111] under C1. Calm-Abiding Meditation (Samatha / Śamatha)
│
├── M.E. TRADITIONS / MEDITATION LINEAGES
│   ├── M.E1. The Theravāda tradition
│   │   ├── M.E1.1. Tradition overview
│   │   │   └── [M055] Theravāda — a map of its meditation systems · L3
│   │   ├── M.E1.2. Core frameworks and methods of practice
│   │   │   ├── [M056] Mindfulness of breathing (Ānāpānassati) in Theravāda · L3
│   │   │   ├── [M057] The four foundations of mindfulness (Satipaṭṭhāna) — the Theravāda approach · L3
│   │   │   └── [M058] Calm and insight (Samatha–Vipassanā) in Theravāda · L3
│   │   ├── M.E1.3. Modern meditation systems and lineages
│   │   │   ├── [M059] Modern insight meditation (Vipassanā) — different approaches · L3
│   │   │   ├── [M135] Burmese meditation systems · L4
│   │   │   └── [M136] The Thai Forest Tradition and its modern presentations · L4
│   │   └── M.E1.4. Scriptures and the commentarial tradition
│   │       └── [M134] The Visuddhimagga and the commentarial tradition — a textual map · L4
│   ├── M.E2. The Mahāyāna tradition
│   │   ├── M.E2.1. Mahāyāna overview and the calming–contemplation framework
│   │   │   ├── [M061] Mahāyāna — a map of its meditation systems · L3
│   │   │   ├── [M062] Calm and insight (Śamatha–Vipaśyanā) in Mahāyāna · L3
│   │   │   └── M.E2.1.1. Calming and Contemplation (Zhǐguān)
│   │   │       ├── [M063] Calming and Contemplation (Zhǐguān) — overview · L3
│   │   │       └── [M137] The Great Calming and Contemplation and Tiantai meditation · L4
│   │   ├── M.E2.2. Zen / Chan: introduction and practice
│   │   │   ├── [M064] Zen / Chan — an overview of its practice · L3
│   │   │   └── [M065] Sitting meditation in Zen (Zazen) · L3
│   │   ├── M.E2.3. Buddha-recitation and Pure Land
│   │   │   ├── [M068] Buddha-recitation (Niànfó / Nembutsu) — overview · L2
│   │   │   └── [M069] Visualizing the Buddha and the Pure Land · L3
│   │   ├── M.E2.4. Combining Zen and Pure Land
│   │   │   └── [M141] Combined Zen–Pure Land practice · L3
│   │   ├── M.E2.5. Zen / Chan: advanced practice
│   │   │   ├── [M066] Just sitting (Shikantaza) · L4
│   │   │   ├── [M139] Silent Illumination (Mòzhào) · L4
│   │   │   ├── [M067] The kōan · L5
│   │   │   └── [M140] The critical phrase (Huàtóu) · L5
│   │   └── M.E2.6. Mahāyāna approaches to reflection and mind training
│   │       ├── [M138] Meditation in Yogācāra (Consciousness-Only) — overview · L4
│   │       ├── [M070] Meditation and emptiness (Madhyamaka / Prajñāpāramitā) · L4
│   │       └── [M142] Mind training and giving-and-taking (Lojong / Tonglen) · L3
│   └── M.E3. The Vajrayāna tradition
│       ├── M.E3.1. Tradition overview
│       │   └── [M071] Vajrayāna — a map of its meditation systems · L3
│       ├── M.E3.2. Path foundations and preliminary practices
│       │   ├── [M077] Cultivating bodhicitta · L3
│       │   ├── [M144] Analytical meditation on the stages of the path (Lamrim) · L4
│       │   └── [M143] The preliminary practices (Ngöndro) · L5
│       ├── M.E3.3. Calm abiding and insight
│       │   ├── [M072] Calm abiding (Śamatha) in Vajrayāna · L3
│       │   └── [M073] Insight (Vipaśyanā) in Vajrayāna · L4
│       ├── M.E3.4. Distinctive means of practice
│       │   ├── [M075] Mantra meditation · L4
│       │   ├── [M074] Deity visualization (Deity Yoga) · L5
│       │   └── [M076] Guru Yoga · L5
│       └── M.E3.5. Advanced practice and lineage requirements
│           ├── [M078] Mahāmudrā · L5
│           ├── [M079] Dzogchen · L5
│           └── [M080] Advanced practice: the role of lineage and direct guidance · L4
│
├── M.F. CULTURAL / REGIONAL CONTEXT
│   └── M.F1. Meditation practice within Vietnamese Buddhism
│       ├── [M145] A map of meditation practice in Vietnam · L2
│       ├── [M146] The historical Zen lineages · L4
│       ├── [M147] Trúc Lâm Yên Tử and the spirit of "dwelling in the world, content with the Way" · L3
│       ├── [M148] Modern Trúc Lâm Zen — the approach of "knowing delusion, not following it" · L3
│       ├── [M149] The Plum Village tradition — applied mindfulness · L2
│       ├── [M150] Pure Land and buddha-recitation in Vietnamese life · L2
│       ├── [M151] Theravāda / the Southern tradition in Vietnam · L3
│       └── [M152] Common Sino-Vietnamese terms in meditation literature · R
│
└── M.G. APPLICATION / CONTEXT / GOAL
    ├── M.G1. Applied meditation & daily life
    │   ├── M.G1.1. Mindful eating
    │   │   └── [M082] Mindful eating · L1
    │   ├── M.G1.2. Meditation at work
    │   │   └── [M083] Meditation at work · L1
    │   ├── M.G1.3. Observing emotion in daily life
    │   │   └── [M084] Observing emotion in daily life · L2
    │   ├── M.G1.4. Short practices, 1–5 minutes
    │   │   └── [M085] Short practices, 1–5 minutes · L1
    │   ├── M.G1.5. Practice for the very busy
    │   │   └── [M153] Practice for the very busy · L1
    │   ├── M.G1.6. Practicing with family and children
    │   │   └── [M154] Practicing with family and children · L1
    │   ├── M.G1.7. Group and community practice
    │   │   └── [M155] Group and community practice · L2
    │   └── M.G1.8. Guided audio, bells, and apps — benefits and limits
    │       └── [M156] Guided audio, bells, and apps — benefits and limits · L1
    └── M.G2. Secular / health-oriented meditation
        ├── M.G2.1. Secular meditation for health — scope and limits
        │   └── [M086] Secular meditation for health — scope and limits · L1
        ├── M.G2.2. Breath-based relaxation
        │   └── [M087] Breath-based relaxation · L1
        ├── M.G2.3. Body scan
        │   └── [M088] Body scan · L1
        ├── M.G2.4. Secular mindfulness
        │   └── [M089] Secular mindfulness · L1
        ├── M.G2.5. MBSR and MBCT — two flagship secular programs
        │   └── [M157] MBSR and MBCT — two flagship secular programs · L2
        ├── M.G2.6. Meditation for stress management
        │   └── [M090] Meditation for stress management · L1
        ├── M.G2.7. Meditation for sleep
        │   └── [M091] Meditation for sleep · L1
        ├── M.G2.8. Meditation for coping with pain and discomfort
        │   └── [M092] Meditation for coping with pain and discomfort · L2
        ├── M.G2.9. Compassion meditation in a health context
        │   └── [M093] Compassion meditation in a health context · L1
        ├── M.G2.10. Trauma-sensitive meditation
        │   └── [M158] Trauma-sensitive meditation · L2
        ├── M.G2.11. Reading the scientific evidence on meditation
        │   └── [M159] Reading the scientific evidence on meditation · R
        └── M.G2.12. When meditation should not replace medical or psychological care
            └── [M094] When meditation should not replace medical or psychological care · L1
```

---
# ARTICLE CATALOG

> Each article has: a **content description** (what to write) and, where needed, a **Terminology** line (Pāli / Sanskrit / Sino-Vietnamese) so that writers use terms correctly and consistently.

## M.A. FOUNDATIONAL KNOWLEDGE & ORIENTATION

> **Suggested order for newcomers:** A1 → A2 → A3 → A4 → A5 → A6. A7 is an optional extension, not a required step. The groups within A are organized by **learning function**, moving from understanding the concept → preparing → practicing → sustaining.

### M.A1. Understanding meditation

#### [M001] What is meditation? · L1
Explains meditation as a family of methods for training attention, awareness, and/or states of mind; distinguishes meditation from mere relaxation or "not thinking."
**Terminology:** *bhāvanā* (P/S) = mental cultivation, developing the mind — a broader idea than the English word "meditation"; Sino-Vietnamese: **tu tập, Thiền định**.

#### [M002] Buddhist meditation and secular meditation · L1
Distinguishes practice set within a Buddhist context from forms of meditation presented independently of religion; cautions against treating the two as pursuing the same goal.

#### [M095] Meditation within the three trainings — ethics, concentration, wisdom · L1
Places meditation within Buddhism's three-part training: an ethical foundation → a stabilized mind → seeing clearly. Explains why the tradition never separates meditation from a way of living, and what that means for a lay practitioner.
**Terminology:** *tisso sikkhā* (P) = the three trainings; *sīla* = ethical conduct, *samādhi* = concentration, *paññā* (S: *prajñā*) = wisdom. Related to the Noble Eightfold Path: *sammā-vāyāma* (right effort), *sammā-sati* (right mindfulness), *sammā-samādhi* (right concentration).

### M.A2. Understanding how to practice

#### [M096] Mindfulness and clear comprehension (Sati and sampajañña) · L1
Distinguishes two factors that are often collapsed into one: *sati* is the ability to keep hold of, and stay with, the present object; *sampajañña* is clear understanding of the context, purpose, and suitability of an action. This article is the key to making sure readers don't equate "mindfulness" with mere attention.
**Terminology:** *sati* (P) / *smṛti* (S) — Sino-Vietnamese **niệm**; *sampajañña* (P) / *saṃprajanya* (S) — Sino-Vietnamese **chánh tri, tỉnh giác**.

#### [M097] Reading meditation terminology: Pāli, Sanskrit, and Sino-Vietnamese · L1
Explains why the same concept appears in several written forms (*satipaṭṭhāna* / *smṛtyupasthāna* / tứ niệm xứ), how the app displays terms, and how to use the cross-reference table at the end of this document. Includes a short guide to reading the diacritics (ā, ī, ū, ṃ, ṅ, ñ, ṭ, ḍ, ṇ, ḷ, ś, ṣ).

#### [M098] Common misconceptions about meditation · L1
Clears up common misunderstandings: that meditation means emptying the mind; that seeing lights or visions means you're doing it right; that a thought arising is a failure; that meditation is a way to avoid problems; that longer sessions automatically mean more skill; that meditation is guaranteed to eliminate stress.

### M.A3. Safety in meditation

#### [M099] Safety in meditation — when to adjust or stop · L1
Reactions a practitioner may encounter (heightened anxiety, insomnia, a sense of estrangement from the body or from reality, old emotions surfacing intensely), ways to lower the intensity, how to "ground" oneself, and signs that call for pausing to find a teacher or a mental-health professional. Links to [M158] and [M094].

### M.A4. Preparing for a sitting

#### [M003] Preparing before you meditate · L1
Space, timing, clothing, equipment, noise, and how to choose a session length suited to a beginner.

#### [M004] Meditation posture · L1
Guidance on sitting in a chair, sitting on the floor (full or half lotus), kneeling, lying down, and walking; emphasizes stability, alertness, and freedom from pain. States clearly: no posture is required for meditation "to work."

#### [M005] Session length and frequency · L1
How to start with short sessions, keep them regular, and lengthen them gradually rather than pushing too hard too soon.

### M.A5. During and after a sitting

#### [M006] Handling distraction, drowsiness, and restlessness · L1
Situations common to beginners and how to return to the object without self-judgment. A practical companion piece; the matching theory sits in [M109] The five hindrances.

#### [M007] How to end a sitting · L1
Moving gently from stillness back into ordinary activity, sensing the body and mind before standing up; may include dedicating merit for users who follow a tradition that includes that practice.

### M.A6. Building a habit

#### [M008] Building a meditation habit · L1
How to set a schedule, create reminder cues, track progress, and sustain practice over the long run.

### M.A7. Support and going deeper

#### [M100] Spiritual friendship and teachers (Kalyāṇamitta) · L2
The role of a teacher within the tradition; how to ask questions, how to recognize trustworthy guidance, and warning signs (coercion, isolating students, claims of attainment used to attract followers, financial entanglement).
**Terminology:** *kalyāṇamitta* (P) / *kalyāṇamitra* (S) — Sino-Vietnamese **thiện hữu, thiện tri thức**.

#### [M101] Retreats and extended intensive practice · L3
What a retreat is, common formats, how to prepare body, mind, and work commitments, what typically happens around days two to four, and how to return to daily life afterward.

## M.B. SHARED PRACTICAL SKILLS

> **Suggested order for newcomers:** B1 → B2 → B3 → B4 → B5 → B6 → B7. These are skills used across many methods; later groups generally build on the ability formed in earlier ones, though this is not a mandatory order for every tradition. B8 is a reference entry (R) and sits outside the linear path.

### M.B1. Body and breath foundations

#### [M009] Releasing bodily tension · L1
Noticing and releasing tension in the face, jaw, shoulders, neck, chest, belly, and the whole body.

#### [M010] Noticing the natural breath · L1
Observing the breath as it happens, without forcing it to be longer, shorter, deeper, or slower.

#### [M011] Counting the breath · L1
A technique that helps beginners stabilize attention by counting breath cycles; found across many systems (Theravāda; Chan/Zen: *sūsokukan* — breath-counting contemplation).

### M.B2. Stabilizing and sustaining attention

#### [M012] Following the sensations of the breath · L2
Moving from "counting" to directly noticing the sensations of the in-breath and out-breath; introduces the idea of the touch point.

#### [M013] Anchoring the mind on an object · L2
The principle of choosing one stable object and gently bringing attention back to it each time it wanders.

### M.B3. Working with distraction and practice attitude

#### [M014] Noticing thought and distraction · L2
Learning to recognize "thinking," "hearing," "remembering" as they happen, without needing to fight the content of the experience.

#### [M105] The attitude of practice: balanced effort, neither forcing nor drifting · L2
The image of "a lute string tuned neither too tight nor too loose"; recognizing when you're straining versus drifting; the role of self-kindness during practice.

### M.B4. Observing and directing experience

#### [M102] Noting / silent labeling · L2
The technique of attaching a short label to whatever experience is occurring ("rising–falling," "hearing," "thinking," "pain"). Traces its origin in the Mahāsi system, its benefits, and its limits (labeling too densely can turn into thinking about the experience rather than observing it).

#### [M103] Wise attention — yoniso manasikāra · L2
How to direct attention to the right aspect of experience: from "what is happening to me" toward "how is this phenomenon arising and passing away." This article is the hinge between attention skills and insight practice.
**Terminology:** *yoniso manasikāra* (P) — Sino-Vietnamese **như lý tác ý**; opposite: *ayoniso manasikāra* (unwise attention).

### M.B5. Balancing the faculties

#### [M104] Balancing the five faculties — pañcindriya · L3
Explains the five factors that need to be kept in balance during practice: faith ↔ wisdom, energy ↔ concentration, with mindfulness as the coordinating factor that is never in excess. Includes signs of imbalance and how to correct them.
**Terminology:** *saddhā* (faith), *viriya* (energy), *sati* (mindfulness), *samādhi* (concentration), *paññā* (wisdom); once stabilized these are called the *pañca bala* — the **five powers**.

### M.B6. Integrating practice into movement and daily life

#### [M015] Walking meditation (Caṅkama) · L1
Using the movement of the feet and the whole body as the object of attention: how to choose a path, a pace, a step count, how to pair it with sitting practice, and how to compress it into a short practice while moving through the day.
**Terminology:** *caṅkama* (P) = walking meditation. *(This article now incorporates the content of the former M081.)*

#### [M016] Mindfulness in daily activity · L1
Bringing the skill of noticing into walking, eating, bathing, working, waiting, and other familiar activities.

### M.B7. Tracking and reflecting on practice

#### [M106] A meditation journal and how to recognize progress · L2
What to record after each sitting; reliable markers of progress (less reactivity, faster recovery, noticing distraction sooner) versus markers that are easy to misread (a pleasant state, unusual imagery).

### M.B8. Frequently asked questions about meditation

#### [M162] Frequently asked questions about meditation · R
A collection of short questions: how long is long enough to sit, eyes open or closed, what to do about leg pain, nodding off, whether it's fine to listen to music, whether meditation conflicts with the user's own faith, whether "not experiencing anything" means something is wrong.

## M.C. METHOD / PRACTICE DIRECTION

### M.C1. Calm-Abiding Meditation (Samatha / Śamatha)

> **Suggested order:** C1.1 → C1.2 → C1.3 → C1.4 → C1.5. C1 is a `method`; its subgroups are arranged by depth of practice, from foundational concentration → objects → hindrances/the sign → deeper levels of concentration → combining concentration and wisdom.

### M.C1.1. Foundations of calm abiding and concentration

#### [M017] Calm-Abiding Meditation (Samatha / Śamatha) · L2
Explains "calm abiding": settling the mind and developing the capacity for sustained, continuous attention; notes that the understanding of this term shifts somewhat from tradition to tradition.
**Terminology:** *samatha* (P) / *śamatha* (S) — Sino-Vietnamese **chỉ**, usually rendered "calm-abiding meditation" or "calm meditation."

#### [M022] Concentration and the continuity of attention · L2
Distinguishes "forcing intense focus" from the ability to sustain attention that is stable, soft, and rarely interrupted.

### M.C1.2. Common practice objects

#### [M018] Calm abiding with the breath (Samatha) · L2
Using the breath as an object to develop stability and continuity of attention.

#### [M019] Calm abiding with body sensation (Samatha) · L2
Using a relatively stable area of body sensation as a concentration object.

#### [M020] Calm abiding with sound (Samatha) · L2
Holding attention on a sound or a field of sound within a formal practice; distinguishes this from listening to relaxing music.

#### [M021] Calm abiding with an image or object (Samatha) · L2
Focusing on an image, a visual point, or an object; this is the gateway to the *kasiṇa* objects [M060] in the traditions that use them.

### M.C1.3. Hindrances and the meditative sign

#### [M109] The five hindrances (Pañca nīvaraṇa) · L2
Five states that obstruct concentration and wisdom, how to recognize each one, and the traditional antidotes. This article is attached to both the Samatha branch and the Contemplation-of-Dhammas branch [M039].
**Terminology:** *kāmacchanda* (sensual desire), *byāpāda* (ill will), *thīna-middha* (sloth and torpor), *uddhacca-kukkucca* (restlessness and remorse), *vicikicchā* (doubt). Sino-Vietnamese: **ngũ cái / năm triền cái**.

#### [M108] The meditative sign and its stages (Nimitta) · L3
Explains the concept of a "sign" arising from the practice object and its three stages according to the Theravāda commentaries; emphasizes that the sign is not the goal and not everyone experiences it.
**Terminology:** *parikamma-nimitta* (the preparatory sign), *uggaha-nimitta* (the acquired sign), *paṭibhāga-nimitta* (the counterpart sign).

### M.C1.4. Levels of concentration and absorption

#### [M107] Three levels of concentration (Khaṇika, Upacāra, Appanā) · L3
Distinguishes momentary concentration (sufficient for insight practice), access concentration (near the threshold of jhāna), and absorption concentration (jhāna itself). Helps readers understand why "not yet attaining jhāna" does not mean "no concentration at all."
**Terminology:** *khaṇika-samādhi* (momentary concentration), *upacāra-samādhi* (access concentration), *appanā-samādhi* (absorption concentration).

#### [M023] Deep concentration and jhāna (Jhāna / Dhyāna) — overview · L3
A general introduction to absorbed meditative states, how the terminology is used differently across traditions, and a note that this is not a required goal for everyone.
**Terminology:** *jhāna* (P) / *dhyāna* (S) — Sino-Vietnamese **Thiền-na, tĩnh lự**; both "Thiền" in Zen and the English word "Zen" trace back to this term.

#### [M110] The four form-sphere jhānas and the five jhāna factors · L4
Presents the four fine-material jhānas and which jhāna factors are present or absent at each level; notes the differences in how these are described between the discourses and the commentaries, and among modern teachers.
**Terminology:** *rūpajjhāna*; the five jhāna factors (*jhānaṅga*): *vitakka* (initial application), *vicāra* (sustained application), *pīti* (rapture), *sukha* (bliss), *ekaggatā* (one-pointedness).

#### [M111] The four formless attainments — arūpa-samāpatti · L4
Introduces the four formless levels of concentration at the level of a conceptual map; emphasizes the concentration foundation and guidance they require.
**Terminology:** *ākāsānañcāyatana* (the base of infinite space), *viññāṇañcāyatana* (the base of infinite consciousness), *ākiñcaññāyatana* (the base of nothingness), *nevasaññānāsaññāyatana* (the base of neither-perception-nor-non-perception).

### M.C1.5. Combining concentration and wisdom

#### [M112] Combining concentration and wisdom · L4
Three models commonly discussed: taking concentration as the vehicle, taking wisdom as the vehicle (bare/dry insight), and the yoked pairing of concentration and wisdom. Explains why modern schools place different emphases here without contradicting the scriptures.
**Terminology:** *samatha-yānika*, *vipassanā-yānika* (*sukkha-vipassaka* — the bare-insight practitioner), *yuganaddha* (the yoked pair of calm and insight).

### M.C2. Insight Meditation (Vipassanā / Vipaśyanā)

> **Suggested order:** C2.1 → C2.2 → C2.3 → C2.4 → C2.5 → C2.6. C2 is a `method`; its subgroups move from understanding insight → direct observation → seeing arising–passing and the three characteristics → deeper analytical frameworks → the map of the progress of insight → handling difficult stages. This is a suggested pedagogical sequence, not the single order used by every tradition.

### M.C2.1. Foundations of insight

#### [M024] Insight Meditation (Vipassanā / Vipaśyanā) · L2
Explains "insight": observing experience in order to see clearly the nature and change of phenomena; emphasizes that its implementation differs across traditions, and that "vipassanā" in the scriptures is not synonymous with any one specific course.
**Terminology:** *vipassanā* (P) / *vipaśyanā* (S) — Sino-Vietnamese **quán, minh sát**.

### M.C2.2. Direct observation of experience

#### [M029] Observing the mind's reactions · L2
Recognizing the chain: object → sensation → liking/disliking → reaction → consequence; used to build the capacity to observe rather than react automatically. The practical companion to [M121].

#### [M030] Direct experience versus the mind's story · L2
Distinguishing the data that is actually occurring (sensation, sound, sight, thought) from the interpretation, judgment, and prediction the mind adds on top.
**Terminology:** related to *papañca* (conceptual proliferation, the mind's tendency to elaborate).

#### [M031] Mindfulness of thought · L2
Observing thought as a mental phenomenon; no need to force the mind empty, and no need to believe every thought either.

#### [M032] Mindfulness of strong emotion · L3
Recognizing emotion through both bodily sensation and mental state; a graded, paced approach with a built-in "way out," so that "observing" does not turn into suppression. Links to [M099] and [M158].

### M.C2.3. Observing arising and passing away, and the three characteristics

#### [M025] Observing arising and passing away · L3
Recognizing the appearance, change, and disappearance of sensations, emotions, thoughts, and mental states.
**Terminology:** *udayabbaya* (arising and passing away); the corresponding insight knowledge is *udayabbayañāṇa*.

#### [M053] The three characteristics (Tilakkhaṇa) — overview · L2
An overview article presenting the three characteristics as three complementary perspectives on the same experience, leading into the three detailed articles M026–M028; states the source and interpretation of each school rather than presenting a single formula.
**Terminology:** *tilakkhaṇa* (P) / *trilakṣaṇa* (S) — Sino-Vietnamese **tam pháp ấn / ba đặc tính**.

#### [M026] Contemplating impermanence (Anicca) · L2
Using the direct change of body and mind as the object of investigation, rather than understanding impermanence only as an idea.
**Terminology:** *anicca* (P) / *anitya* (S) — **impermanence**.

#### [M027] Contemplating suffering / unsatisfactoriness (Dukkha) · L3
Observing how clinging, resistance, and expectation relate to unsatisfactory experience; distinguishes the three layers of meaning of *dukkha* so readers don't come away thinking Buddhism is pessimistic.
**Terminology:** *dukkha-dukkha* (the suffering of pain), *vipariṇāma-dukkha* (the suffering of change), *saṅkhāra-dukkha* (the suffering inherent in conditioned existence).

#### [M028] Contemplating non-self (Anattā / Anātman) · L3
Investigating experience without assuming a fixed, independent, permanent "self"; states clearly that non-self does **not** mean "nothing exists at all" or "no personal responsibility."
**Terminology:** *anattā* (P) / *anātman* (S) — **non-self**. Source: the *Anattalakkhaṇa Sutta* (SN 22.59).

### M.C2.4. Deeper analytical frameworks

#### [M120] Distinguishing mind and matter (Nāma-rūpa) · L3
The first stage of observation in many insight systems: separating experience into physical phenomena and mental phenomena, rather than treating it as one solid block of "I am…"
**Terminology:** *nāma-rūpa* — Sino-Vietnamese **danh sắc**; the corresponding insight knowledge is *nāmarūpaparicchedañāṇa*.

#### [M121] Dependent origination in direct observation · L4
Brings the twelve links of dependent origination down to the level of what can actually be observed in a sitting: contact → feeling → craving → clinging, and the point where mindfulness can "step in."
**Terminology:** *paṭiccasamuppāda* (P) / *pratītyasamutpāda* (S) — Sino-Vietnamese **duyên khởi, duyên sinh**; *phassa – vedanā – taṇhā – upādāna* (contact – feeling – craving – clinging).

### M.C2.5. The progress of insight

#### [M122] The progress of insight: seven purifications and sixteen knowledges — overview · L4
Introduces the map of the path according to the *Visuddhimagga* and how modern systems use it. Editorial note: present this as a **reference map**, never as a scorecard for self-assessment.
**Terminology:** *satta visuddhi* (the seven purifications), *soḷasa ñāṇa* (the sixteen insight knowledges), *ñāṇa* = knowledge/insight.

#### [M123] The ten corruptions of insight (Vipassanupakkilesa) · L4
Ten pleasant or striking states (light, rapture, tranquility, bliss, resolution, energy, strong mindfulness, equanimity, and attachment to any of these) that can be mistaken for attainment; how to recognize them and how to continue.

### M.C2.6. Difficulties and safety

#### [M124] Difficult stages in insight practice and how to respond safely · L4
A neutral description of the difficult stages (fear, discouragement, wanting to stop, bodily pain, prolonged unease) often referenced in insight systems; how to reduce the intensity, strengthen the foundation of concentration and loving-kindness, and when a teacher or professional is needed. **Must** link to [M099] and [M094].

## M.D. FRAMEWORKS / SYSTEMS OF PRACTICE

> **Note on D1:** The four foundations of mindfulness (Satipaṭṭhāna) comprise exactly **four foundations**: contemplation of the body, of feeling, of mind, and of dhammas. The sub-articles below are specific content or practices belonging to one of these four foundations; they do not constitute additional foundations.

### M.D1. The Four Foundations of Mindfulness (Satipaṭṭhāna / Smṛtyupasthāna)

> **D1 structure:** The four foundations of mindfulness form a system of exactly **four domains**: contemplation of the body, of feeling, of mind, and of dhammas. Articles on the breath, posture, mindfulness immersed in the body, the five hindrances, the five aggregates, and so on, are content, methods, or topics that fall within one of these four domains; they are not separate foundations in their own right.

#### [M033] The Four Foundations of Mindfulness (Satipaṭṭhāna / Smṛtyupasthāna) — overview · L2
Introduces the four domains of contemplation: body, feeling, mind, dhammas; explains common translations and the refrain that repeats throughout the discourse (contemplating internally and externally, contemplating arising and passing away, "bare knowing and awareness," not clinging to or depending on anything in the world).
**Terminology:** *satipaṭṭhāna* (P) / *smṛtyupasthāna* (S) — Sino-Vietnamese **tứ niệm xứ**. Source: the *Satipaṭṭhāna Sutta* (MN 10), the *Mahāsatipaṭṭhāna Sutta* (DN 22).

#### M.D1.1. Contemplation of the body (Kāyānupassanā)

##### [M034] Contemplation of the body (Kāyānupassanā) · L2
Surveys the body: the breath, posture, movement, the elements, and the ways the tradition contemplates the body.

##### [M035] Mindfulness of breathing within the four foundations (Satipaṭṭhāna) · L2
Places mindfulness of breathing within the framework of the four foundations, rather than treating the breath as merely a concentration exercise.

##### [M113] Mindfulness of breathing — sixteen steps in four tetrads (Ānāpānassati) · L4
Presents the sixteen steps of mindfulness of breathing, arranged in four groups of four, each tetrad corresponding respectively to body, feeling, mind, and dhammas — that is, how the text links mindfulness of breathing to the full set of four foundations.
**Terminology:** *ānāpānassati* (P) / *ānāpānasmṛti*, *ānāpānānusmṛti* (S); the four groups are called *catukka* (tetrads). Source: the *Ānāpānassati Sutta* (MN 118).

##### [M036] Contemplating posture and movement (Iriyāpatha) · L2
Clearly recognizing walking, standing, sitting, lying down, and the movements of daily activity.
**Terminology:** *iriyāpatha* (the four postures); *sampajañña* applied to activity is often called *sampajānakārī*.

##### [M114] Mindfulness immersed in the body (Kāyagatāsati) · L3
Introduces the discourse and the group of practices that use the body as a continuous foundation; distinguishes this from the secular body scan [M088] in terms of goal and interpretive framework.
**Terminology:** *kāyagatāsati* (P) — Sino-Vietnamese **thân hành niệm**. Source: the *Kāyagatāsati Sutta* (MN 119).

#### M.D1.2. Contemplation of feeling (Vedanānupassanā)

##### [M037] Contemplation of feeling (Vedanānupassanā) · L2
Distinguishes pleasant, unpleasant, and neutral feeling; observes the mind's reactions to each type; introduces the scriptural distinction between feeling that is "of the flesh" and feeling that is "not of the flesh."
**Terminology:** *vedanā* — Sino-Vietnamese **thọ**; *sukha*, *dukkha*, *adukkhamasukha* (neither-painful-nor-pleasant).

#### M.D1.3. Contemplation of mind (Cittānupassanā)

##### [M038] Contemplation of mind (Cittānupassanā) · L3
Recognizing the mind's present state through the pairs of opposites the discourse lists: with or without lust, with or without hatred, with or without delusion, contracted or scattered, expansive or narrow, concentrated or unconcentrated, liberated or unliberated.

#### M.D1.4. Contemplation of dhammas (Dhammānupassanā)

##### [M039] Contemplation of dhammas (Dhammānupassanā) · L3
Observes experience through the categories the Dhamma classifies it into; this is the parent article leading into the five child articles below.
**Terminology:** *dhammā* here means "the classified groups of phenomena/teaching-categories," not "the teachings" in the ordinary sense — this distinction needs to be made explicit to avoid misreading.

##### [M116] Contemplation of dhammas: the five aggregates (Pañcakkhandha) · L3
Observes experience through five groups rather than through the notion of "I."
**Terminology:** *rūpa* (form), *vedanā* (feeling), *saññā* (perception), *saṅkhāra* (mental formations), *viññāṇa* (consciousness).

##### [M117] Contemplation of dhammas: the six internal–external sense bases (Saḷāyatana) · L3
Observes the sensory process: sense organ – sense object – consciousness, and how bondage arises right at the point of contact.
**Terminology:** *saḷāyatana* (P) / *ṣaḍāyatana* (S) — Sino-Vietnamese **lục nhập, sáu xứ**; *phassa* (contact), *saṃyojana* (fetter).

##### [M118] Contemplation of dhammas: the seven factors of awakening (Satta bojjhaṅga) · L3
The seven factors of awakening, how to recognize which factor is missing, and how to cultivate it; includes the principle: when the mind is sluggish, cultivate investigation, energy, and rapture; when the mind is agitated, cultivate tranquility, concentration, and equanimity.
**Terminology:** *sati* (mindfulness), *dhammavicaya* (investigation of states), *viriya* (energy), *pīti* (rapture), *passaddhi* (tranquility), *samādhi* (concentration), *upekkhā* (equanimity).

##### [M119] Contemplation of dhammas: the four noble truths (Cattāri ariyasaccāni) · L3
Brings the four truths down from the level of doctrine to the level of direct observation within a sitting: there is discomfort, there is a cause rooted in clinging, there are moments it subsides, and there is a way to make it subside.
**Terminology:** *dukkha*, *samudaya*, *nirodha*, *magga* — Sino-Vietnamese **khổ, tập, diệt, đạo**.

##### [M040] The four foundations of mindfulness, basic to advanced (Satipaṭṭhāna) · L3
A suggested path from body → feeling → mind → dhammas, while making clear that the discourse does not mandate a single fixed order, and that modern systems implement it in different sequences.

### M.D2. The Divine Abodes (Brahmavihāra)

> **Structure:** D2 is a practice group of four qualities: loving-kindness (Mettā), compassion (Karuṇā), appreciative joy (Muditā), equanimity (Upekkhā). M125 is the practical detail of M042; M126 and M046 provide synthesis.

#### [M041] The Divine Abodes (Brahmavihāra) — overview · L2
Introduces the four qualities — loving-kindness, compassion, joy, equanimity; presents both labels, *Brahmavihāra* (divine abodes) and *appamaññā* (the immeasurables), and how different traditions use each.
**Terminology:** *brahmavihāra* — Sino-Vietnamese **tứ phạm trú**; *catasso appamaññāyo* — **the four immeasurables**.

#### M.D2.1. Loving-kindness (Mettā / Maitrī)

##### [M042] Loving-kindness (Mettā / Maitrī) · L1
Cultivating goodwill and the wish for wellbeing for oneself and others; distinguishes loving-kindness from romantic attachment and from forcing oneself to feel pleasant.

##### [M125] Cultivating loving-kindness — the sequence of objects (Mettā bhāvanā) · L2
The commonly used sequence: oneself → someone dear → a neutral person → a difficult person → all beings; how to work with getting stuck at the "self" step or the "difficult person" step; sample phrases in Vietnamese.
**Terminology:** *mettā bhāvanā*; sources: the *Karaṇīyamettā Sutta* (Sn 1.8), the *Mettā Sutta* (AN 11.15).

#### M.D2.2. Compassion (Karuṇā)

##### [M043] Compassion (Karuṇā) · L2
Recognizing suffering and developing the wish to relieve it; distinguishes compassion from pity and from compassion fatigue.

#### M.D2.3. Appreciative joy (Muditā)

##### [M044] Appreciative joy (Muditā) · L2
Training the capacity to take joy in others' happiness and success, reducing comparison and envy.

#### M.D2.4. Equanimity (Upekkhā / Upekṣā)

##### [M045] Equanimity (Upekkhā / Upekṣā) · L3
Developing balance in the face of gain and loss, praise and blame; distinguishes equanimity from indifference or resignation. Notes that *upekkhā* has two meanings: equanimity as one of the divine abodes, and equanimity as a jhāna/awakening factor.

#### M.D2.5. Synthesis and shared analysis

##### [M126] The near and far enemies of the four qualities · L3
Following the commentaries: loving-kindness ↔ attachment / hatred; compassion ↔ grief / cruelty; joy ↔ self-interested pleasure / envy; equanimity ↔ ignorant indifference / agitation. This article helps a practitioner check the quality of their own mind.
**Terminology:** *āsanna-paccatthika* (the near enemy), *dūra-paccatthika* (the far enemy).

##### [M046] The four divine abodes as one system · L3
The relationships among the four qualities, how they balance one another, and their place across all three traditions — one of the clearest points of convergence in Buddhism.

### M.D3. The System of Meditation Subjects (Kammaṭṭhāna)

> **Structure:** D3 is a classification system of meditation objects. M127 is the overview article on the forty subjects; the groups below break it down into detailed branches. Content that already has its own branch in D2 or C1 is represented through cross-links rather than duplicated as an independent system.

#### M.D3.1. Overview, classification, and selection

##### [M127] The forty meditation subjects (Kammaṭṭhāna) — overview after the Visuddhimagga · L3
A map of the forty subjects: ten kasiṇas, ten foulness contemplations, ten recollections, four divine abodes, four formless states, one perception of food's repulsiveness, and one analysis of the four elements. Explains which subject leads to which level of concentration and which subjects only reach as far as access concentration.
**Terminology:** *kammaṭṭhāna* (P) — Sino-Vietnamese **nghiệp xứ**, usually translated "meditation subject."

##### [M128] Temperament — six types and how to choose a subject (Carita) · L3
The six temperament types described in the commentaries and the subjects suggested for each; presented as a reference tool, not a personality quiz.
**Terminology:** *rāgacarita* (lustful temperament), *dosacarita* (hating temperament), *mohacarita* (deluded temperament), *saddhācarita* (faithful temperament), *buddhicarita* (intelligent temperament), *vitakkacarita* (discursive temperament).

##### [M054] Choosing a subject that suits you · L2
Principles for choosing a subject based on your goal, temperament [M128], life circumstances, and a teacher's guidance; how to try a subject long enough before switching.

#### M.D3.2. Kasiṇa devices

##### [M060] Kasiṇa devices — the ten kasiṇas · L4
Introduces the ten kasiṇa objects (earth, water, fire, air, blue, yellow, red, white, light, space), how they are used to develop concentration, and why detailed instruction requires a clear traditional source.
**Terminology:** *kasiṇa* — Sino-Vietnamese **biến xứ, biến xứ định**.

#### M.D3.3. Contemplation of foulness (Asubha)

##### [M047] Contemplation of foulness (Asubha) · L4
A group of contemplations aimed at reducing attachment to the body, comprising the ten corpse-contemplation subjects found in the commentaries. **Editorial note:** present this in its historical–monastic context, with a clear caution that it is not suitable for people currently struggling with body image, death anxiety, or depression.

#### M.D3.4. Related body-contemplation subjects

##### [M048] The thirty-two parts of the body (Dvattiṃsākāra) · L4
Contemplating the body as thirty-two parts; distinguishes the list and the practice as they vary between sources. This is one component of *kāyagatāsati* [M114].
**Terminology:** *dvattiṃsākāra* (the thirty-two parts); the practice is called *paṭikūlamanasikāra* (attention to repulsiveness).

#### M.D3.5. Analysis of the four elements (Catudhātuvavatthāna)

##### [M129] Analysis of the four elements (Catudhātuvavatthāna) · L4
Observing the body through four qualities: hardness/softness, cohesion, heat/cold, and motion — a way of dismantling the notion "the body is me" without relying on unsettling imagery.
**Terminology:** *pathavī*, *āpo*, *tejo*, *vāyo* — **earth, water, fire, air**.

#### M.D3.6. Perception of the repulsiveness of food (Āhāre paṭikūlasaññā)

##### [M130] Perception of the repulsiveness of food (Āhāre paṭikūlasaññā) · L4
Reflecting on food to reduce craving for taste; states clearly that this is not a weight-control method and should not be presented to anyone with a disordered-eating pattern.

#### M.D3.7. Recollections (Anussati)

###### [M131] The ten recollections (Dasa anussati) — overview · L3
A map of the ten recollection subjects and their role: nurturing faith, a sense of safety, and inspiration to practice, while also serving as a foundation for concentration.
**Terminology:** *anussati* (P) / *anusmṛti* (S) — Sino-Vietnamese **tùy niệm**. The ten subjects: recollection of the Buddha, the Dhamma, the Sangha, virtue, generosity, the deities, death, the body, the breath, and peace.

##### M.D3.7.1. Recollection of the Buddha (Buddhānussati / Buddhānusmṛti)

###### [M050] Recollection of the Buddha (Buddhānussati / Buddhānusmṛti) · L2
Contemplating the qualities, the image, or the epithets of the Buddha; states the difference between recollecting the Buddha's virtues as in Theravāda and reciting the Buddha's name as in East Asian Pure Land [M068].
**Terminology:** *buddhānussati* (P) / *buddhānusmṛti* (S) — Sino-Vietnamese **niệm Phật**.

##### M.D3.7.2. Recollection of the Dhamma (Dhammānussati / Dharmānusmṛti)

###### [M051] Recollection of the Dhamma (Dhammānussati / Dharmānusmṛti) · L2
Contemplating the qualities of the Dhamma as a way of reinforcing one's direction in practice.
**Terminology:** *dhammānussati* (P) / *dharmānusmṛti* (S).

##### M.D3.7.3. Recollection of the Sangha (Saṅghānussati / Saṃghānusmṛti)

###### [M052] Recollection of the Sangha (Saṅghānussati / Saṃghānusmṛti) · L2
Contemplating the community of practitioners and the qualities of those who have gone before.
**Terminology:** *saṅghānussati* (P) / *saṃghānusmṛti* (S).

##### M.D3.7.4. Recollection of virtue, generosity, and the deities

###### [M132] Recollection of virtue, generosity, and the deities · L3
Three recollections rarely discussed in the West but very close to Vietnamese Buddhist daily life: recalling one's own ethical conduct, recalling acts of generosity and sharing, and contemplating the qualities that lead to favorable states of rebirth.
**Terminology:** *sīlānussati*, *cāgānussati*, *devatānussati*.

##### M.D3.7.5. Recollection of death (Maraṇassati / Maraṇasmṛti)

###### [M049] Recollection of death (Maraṇassati / Maraṇasmṛti) · L3
Reflecting on the finite nature of life to sharpen awareness and clarify priorities, not to cultivate fear. Includes guidance to stop if it produces prolonged anxiety.
**Terminology:** *maraṇassati* (P) / *maraṇasmṛti* (S).

##### M.D3.7.6. Recollection of peace (Upasamānussati)

###### [M133] Recollection of peace (Upasamānussati) · L4
Contemplating stillness, and nirvana as the goal of the path; a subject more oriented toward reflective contemplation than a technique of attention.
**Terminology:** *upasamānussati*; *nibbāna* (P) / *nirvāṇa* (S) — **nirvana**.

#### M.D3.8. Cross-links

- **The Divine Abodes (Brahmavihāra)**: see D2. Under the forty-subject system in M127, this is a group within Kammaṭṭhāna; D3 does not duplicate the full content of M041–M046.
- **The four formless attainments**: see [M111] under C1. Calm-Abiding Meditation (Samatha / Śamatha); the article may carry an additional `kammaṭṭhāna` category tag if the app's data model needs to represent its relationship to the forty-subject system.

## M.E. Traditions / Meditation Lineages

> **Grouping principle:** E1–E3 are the three **major traditions**. The entries under E1.x, E2.x, and E3.x below are **learning clusters within each tradition**, not new independent traditions or schools. They are arranged overview → foundations/methods → advanced systems or practices; L5 articles are presented only at an educational level, for content that requires a teacher, transmission, or empowerment.

### M.E1. The Theravāda tradition

#### M.E1.1. Tradition overview

##### [M055] Theravāda — a map of its meditation systems · L3
Introduces the meditation systems within Theravāda and makes clear that "Theravāda" is not synonymous with any single technique.

#### M.E1.2. Core frameworks and methods of practice

##### [M056] Mindfulness of breathing (Ānāpānassati) in Theravāda · L3
How Theravāda sources develop mindfulness of breathing, from stabilizing attention to serving as a foundation for insight; links to [M113] for the sixteen-step structure.

##### [M057] The four foundations of mindfulness (Satipaṭṭhāna) — the Theravāda approach · L3
The four foundations within the context of the Pāli canon and the different ways modern teachers implement them.

##### [M058] Calm and insight (Samatha–Vipassanā) in Theravāda · L3
Ways of combining calm and insight within Theravāda, without assuming there is only one orthodox path. Links to [M112].

#### M.E1.3. Modern meditation systems and lineages

##### [M059] Modern insight meditation (Vipassanā) — different approaches · L3
Why so many very different systems all carry the name "vipassanā"; how to compare them fairly by: primary object, use of concentration, method of noting, and retreat structure.

##### [M135] Burmese meditation systems · L4
Introduces and compares, at the level of a map, the Ledi Sayādaw lineage, the Mahāsi Sayādaw noting method, the U Ba Khin–S. N. Goenka lineage (body scanning), the jhāna-based approach of Pa-Auk Sayādaw, and the mind-observation approach of U Tejaniya. Presented neutrally, without ranking.

##### [M136] The Thai Forest Tradition and its modern presentations · L4
Characteristics of meditation in the Forest Tradition (Ajahn Mun, Ajahn Chah, and their successors): the emphasis on precepts, lifestyle, *buddho* as a recollection subject, and teaching through daily life. May mention Buddhadāsa's presentation of ānāpānasati.

#### M.E1.4. Scriptures and the commentarial tradition

##### [M134] The Visuddhimagga and the commentarial tradition — a textual map · L4
The role of the *Visuddhimagga* (The Path of Purification, by Buddhaghosa, 5th century) and the *Vimuttimagga* (The Path of Freedom) in systematizing meditation; distinguishes canonical content from commentarial content so readers know which layer they are reading.

### M.E2. The Mahāyāna tradition

#### M.E2.1. Mahāyāna overview and the calming–contemplation framework

##### [M061] Mahāyāna — a map of its meditation systems · L3
The diversity within Mahāyāna, especially its East Asian traditions; cautions against treating "Mahāyāna" as a single unified meditation system.

##### [M062] Calm and insight (Śamatha–Vipaśyanā) in Mahāyāna · L3
The two dimensions of calm and insight within a Mahāyāna context, and their relationship to bodhicitta, the perfections, and emptiness.

###### M.E2.1.1. Calming and Contemplation (Zhǐguān)

####### [M063] Calming and Contemplation (Zhǐguān) — overview · L3
"Calming" and "contemplation" within the East Asian system, particularly when it is important to present the two aspects as combined rather than as two separate independent methods.
**Terminology:** 止觀 *zhǐguān* — Sino-Vietnamese **chỉ quán**, corresponding to *śamatha–vipaśyanā*.

####### [M137] The Great Calming and Contemplation and Tiantai meditation · L4
Introduces the *Mohe Zhiguan* (The Great Calming and Contemplation) of Zhiyi as one of the most structured meditation systems in East Asian Buddhism, and its influence on later schools.

#### M.E2.2. Zen / Chan: introduction and practice

##### [M064] Zen / Chan — an overview of its practice · L3
A map of the forms of practice within Chan/Zen and the differences among its lineages (Linji/Rinzai, Caodong/Sōtō).

##### [M065] Sitting meditation in Zen (Zazen) · L3
Zazen as a group of practices with several variations in implementation: posture, breathing, where to rest the gaze, and the atmosphere of the meditation hall.

#### M.E2.3. Buddha-recitation and Pure Land

##### [M068] Buddha-recitation (Niànfó / Nembutsu) — overview · L2
Reciting the Buddha's name within East Asian Mahāyāna traditions; distinguishes the practice and the interpretation across schools (verbal recitation, visualization, and recitation as the realization of ultimate reality).

##### [M069] Visualizing the Buddha and the Pure Land · L3
Structured forms of visualization involving a buddha, a bodhisattva, or a pure land (a representative source: the *Sutra on the Visualization of Amitāyus*); cautions against equating this with modern "positive visualization."

#### M.E2.4. Combining Zen and Pure Land

##### [M141] Combined Zen–Pure Land practice · L3
The tradition of combining Zen investigation and buddha-recitation in China and Vietnam; the various explanations of this combination and its practical meaning for lay practitioners.

#### M.E2.5. Zen / Chan: advanced practice

##### [M066] Just sitting (Shikantaza) · L4
The practice of "just sitting" in Sōtō Zen; emphasizes that this is not "sitting and doing nothing," and is generally taught only once a student already has a foundation.
**Terminology:** 只管打坐 *shikantaza* — Sino-Vietnamese **chỉ quản đả tọa**.

##### [M139] Silent Illumination (Mòzhào) · L4
The Chinese origins of the "silent yet luminous" line of practice (Hongzhi Zhengjue) and its relationship to shikantaza.
**Terminology:** 默照 *mòzhào* — Sino-Vietnamese **mặc chiếu**.

##### [M067] The kōan · L5
What a kōan is, its role in certain Zen lineages, and why kōan practice is bound up with the teacher–student relationship (private interview). The app presents this only at an introductory level.
**Terminology:** 公案 *kōan* / *gōng'àn* — Sino-Vietnamese **công án**.

##### [M140] The critical phrase (Huàtóu) · L5
The practice of holding a living question ("Who is reciting the Buddha's name?", "Who is dragging this corpse around?") within the Chinese and Vietnamese Linji lineages; emphasizes the need for a guiding teacher.
**Terminology:** 話頭 *huàtóu* — Sino-Vietnamese **thoại đầu**; the resulting state of doubt is called **nghi tình** (疑情, "sensation of doubt").

#### M.E2.6. Mahāyāna approaches to reflection and mind training

##### [M142] Mind training and giving-and-taking (Lojong / Tonglen) · L3
The system of mind training through pithy slogans in the Tibetan Kadampa tradition, and the practice of tonglen (taking in others' suffering, sending out wellbeing). A Mahāyāna practice that requires no empowerment and can therefore be taught broadly — but needs a caution for anyone currently emotionally overwhelmed.
**Terminology:** *blo sbyong* (lojong) — **mind training**; *gtong len* (tonglen) — **giving and taking**.

##### [M138] Meditation in Yogācāra (Consciousness-Only) — overview · L4
How the Yogācāra system describes the process of cognition and what that means for contemplative practice; introduces the concept of the turning of the basis (*āśraya-parāvṛtti*) at an overview level.

##### [M070] Meditation and emptiness (Madhyamaka / Prajñāpāramitā) · L4
Analytical meditation and contemplation of emptiness within a Mahāyāna context; in-depth treatment needs to be grounded in a specific source and school.
**Terminology:** *śūnyatā* — Sino-Vietnamese **tánh Không**; *prajñāpāramitā* — **the perfection of wisdom**.

### M.E3. The Vajrayāna tradition

#### M.E3.1. Tradition overview

##### [M071] Vajrayāna — a map of its meditation systems · L3
Vajrayāna as a diverse system built on a Mahāyāna foundation with additional distinctive means; cautions against treating it as "an upgraded version of meditation."

#### M.E3.2. Path foundations and preliminary practices

##### [M077] Cultivating bodhicitta · L3
Meditation on aspiring toward and contemplating bodhicitta; overlaps with the practice of loving-kindness and compassion in the Divine Abodes [M041]–[M046] and with lojong [M142].
**Terminology:** *bodhicitta* — Sino-Vietnamese **bồ-đề tâm**; distinguishes aspirational *bodhicitta* from engaged *bodhicitta*.

##### [M144] Analytical meditation on the stages of the path (Lamrim) · L4
Contemplative meditation following the graduated stages of the path (*lam rim*): the precious human life, impermanence, karma, the suffering of cyclic existence, bodhicitta; distinguishes "analytical meditation" from "settling meditation."

##### [M143] The preliminary practices (Ngöndro) · L5
The structure of the preliminary practices (refuge and prostrations, bodhicitta, Vajrasattva, mandala offering, guru yoga); explains why they precede deeper practices. Presented at an educational level.

#### M.E3.3. Calm abiding and insight

##### [M072] Calm abiding (Śamatha) in Vajrayāna · L3
Calm abiding as a foundation that may precede or run alongside deeper practices, depending on the lineage.

##### [M073] Insight (Vipaśyanā) in Vajrayāna · L4
Insight and analytical meditation within Vajrayāna systems, and their relationship to recognizing the nature of mind.

#### M.E3.4. Distinctive means of practice

##### [M075] Mantra meditation · L4
Mantra as a component of practice: its function, how it is recited, and why not every mantra belongs to the same system. Notes on mantras that require oral transmission.
**Terminology:** *mantra* — Sino-Vietnamese **chân ngôn, thần chú**; *dhāraṇī* — **đà-la-ni, tổng trì** (a retention formula).

##### [M074] Deity visualization (Deity Yoga) · L5
Introduces deity visualization and the two stages of generation and completion at a conceptual level; states clearly that detailed instruction depends on lineage and empowerment.
**Terminology:** *bskyed rim* (the generation stage), *rdzogs rim* (the completion stage).

##### [M076] Guru Yoga · L5
The structure of guru yoga and the role of devotion, lineage, and visualization; includes a direct discussion of healthy boundaries within the teacher–student relationship.

#### M.E3.5. Advanced practice and lineage requirements

##### [M078] Mahāmudrā · L5
An introduction at the level of a conceptual map and its place within the various lineages; detailed practice content is left to a qualified teacher.

##### [M079] Dzogchen · L5
A general introduction, distinguishing academic language from the oral, lineage-transmitted language of the Nyingma/Dzogchen schools.

##### [M080] Advanced practice: the role of lineage and direct guidance · L4
Why some practices should not be presented as self-study articles in the app; what can be offered at an educational/overview level; how the app displays the L5 label to users.

## M.F. Cultural / Regional Context

### M.F1. Meditation practice within Vietnamese Buddhism

> **Why this group exists:** Vietnamese users encounter meditation mainly through the lineages practiced in Vietnam, with their own Sino-Vietnamese terminology. Without this group, the catalog would read like a translation of a foreign document. Written neutrally, without promoting any one lineage as the most correct.

#### [M145] A map of meditation practice in Vietnam · L2
An overview of the lineages present today: Zen (Trúc Lâm and other lineages), Pure Land and buddha-recitation, Plum-Village-style applied mindfulness, Theravāda/the Southern tradition, and secular meditation classes.

#### [M146] The historical Zen lineages · L4
Introduces the three lineages most often cited in the historical record — Vinītaruci, Vô Ngôn Thông, and Thảo Đường — and notes that many details rest on the *Thiền uyển tập anh* ("Compendium of Outstanding Figures of the Zen Community"), a source that needs to be read with awareness of its dating and genre.

#### [M147] Trúc Lâm Yên Tử and the spirit of "dwelling in the world, content with the Way" · L3
The context of the Trần dynasty, the role of Trần Nhân Tông, and the spirit of practicing in the midst of ordinary life; may reference the *Khóa hư lục* (Trần Thái Tông) and the *Recorded Sayings of Tuệ Trung Thượng Sĩ*.

#### [M148] Modern Trúc Lâm Zen — the approach of "knowing delusion, not following it" · L3
How practice is presented within the modern revival of the Trúc Lâm lineage: recognizing deluded thought without running after it; compares this with [M031] and [M066] so readers can see both the similarities and the differences.

#### [M149] The Plum Village tradition — applied mindfulness · L2
Distinctive features: gathas (mindfulness verses), the mindfulness bell, walking meditation, mindful eating, and practice woven into daily activity and relationships; where this presentation sits between Buddhism and secular mindfulness.

#### [M150] Pure Land and buddha-recitation in Vietnamese life · L2
Buddha-recitation practiced at home and at temples, intensive buddha-recitation retreats, and end-of-life recitation support; explains the relationship between buddha-recitation as a path of faith and aspiration and buddha-recitation as a concentration object [M050], [M068].

#### [M151] Theravāda / the Southern tradition in Vietnam · L3
The formation of the ethnic-Kinh Southern tradition and the Khmer Southern tradition, their practice centers, and the Pāli terms a student will encounter.

#### [M152] Common Sino-Vietnamese terms in meditation literature · R
A glossary of terms Vietnamese readers commonly encounter: chỉ – quán, định – tuệ, tam học, tứ niệm xứ, ngũ cái, thất giác chi, tứ vô lượng tâm, kinh hành, tọa Thiền, tham thoại đầu, nghi tình, vọng tưởng, tâm viên ý mã, and more. A companion to the terminology cross-reference table at the end of this document.

## M.G. Application / Context / Goal

### M.G1. Applied meditation & daily life

#### M.G1.1. Mindful eating

##### [M082] Mindful eating · L1
Observing sensation, eating pace, taste, chewing, and bodily signals, without turning the exercise into a rigid set of eating rules. **Editorial note:** do not present this as a weight-loss method; see [M158].

#### M.G1.2. Meditation at work

##### [M083] Meditation at work · L1
Short practices for bringing attention back to a task, reducing unnecessary task-switching, and noticing stress.

#### M.G1.3. Observing emotion in daily life

##### [M084] Observing emotion in daily life · L2
Bringing the skill of noticing body–feeling–mind into arguments, waiting, disappointment, and worry; emphasizes pausing before reacting.

#### M.G1.4. Short practices, 1–5 minutes

##### [M085] Short practices, 1–5 minutes · L1
A set of very short practices organized by goal: stabilizing attention, noticing the breath, releasing tension, shifting state, or reclaiming a pause.

#### M.G1.5. Practice for the very busy

##### [M153] Practice for the very busy · L1
Designing a minimum-viable practice: three breaths before opening the laptop, one minute before a meeting, one fixed "anchor point" in the day; how to keep it going when the schedule falls apart.

#### M.G1.6. Practicing with family and children

##### [M154] Practicing with family and children · L1
How to introduce short practices to children by age group, practicing before meals or bedtime, and the principle of never forcing it.

#### M.G1.7. Group and community practice

##### [M155] Group and community practice · L2
The benefits of sitting together, how to organize a small group, minimal ritual, and how to join an online group while keeping the quality of practice intact.

#### M.G1.8. Guided audio, bells, and apps — benefits and limits

##### [M156] Guided audio, bells, and apps — benefits and limits · L1
When to use a voice-guided practice and when to sit in silence; how to use a bell and a timer; the risk of becoming dependent on guided audio.

### M.G2. Secular / health-oriented meditation

> **Editorial label:** This group is written from a **health/secular** angle and does not require the user to follow Buddhism. Use "supports," "may help," "a relaxation/attention-regulation practice" rather than claiming meditation "cures" an illness. When a specific medical condition is mentioned, state the limits of the evidence and recommend continuing appropriate medical care.

#### M.G2.1. Secular meditation for health — scope and limits

##### [M086] Secular meditation for health — scope and limits · L1
What secular meditation is, which health goals it may reasonably target, and the boundary between self-care content and medical/psychological treatment.

#### M.G2.2. Breath-based relaxation

##### [M087] Breath-based relaxation · L1
A gentle practice focused on the sensation of the breath and releasing tension; requires no religious belief.

#### M.G2.3. Body scan

##### [M088] Body scan · L1
Systematically moving attention through areas of the body to increase awareness and support relaxation; notes the difference in goal from *kāyagatāsati* [M114].

#### M.G2.4. Secular mindfulness

##### [M089] Secular mindfulness · L1
Mindfulness as an attention and present-awareness skill in a non-religious context, while making clear it is **not** fully equivalent to satipaṭṭhāna.

#### M.G2.5. MBSR and MBCT — two flagship secular programs

##### [M157] MBSR and MBCT — two flagship secular programs · L2
The eight-week structure, origins, core exercises, and scope of application of the two most heavily researched programs; states clearly that these are instructor-led programs the app cannot replace.

#### M.G2.6. Meditation for stress management

##### [M090] Meditation for stress management · L1
Exercises aimed at recognizing stress, creating a pause, and regulating attention; uses "supports" language rather than promising a treatment outcome.

#### M.G2.7. Meditation for sleep

##### [M091] Meditation for sleep · L1
Relaxation practice to reduce activation before sleep; states clearly that this does not replace investigating the underlying cause of insomnia when that is needed.

#### M.G2.8. Meditation for coping with pain and discomfort

##### [M092] Meditation for coping with pain and discomfort · L2
Directing attention to pain sensation and the accompanying reaction and tension, safely; avoids promising pain relief for everyone.

#### M.G2.9. Compassion meditation in a health context

##### [M093] Compassion meditation in a health context · L1
Applying compassion/loving-kindness exercises in secular language to support a less self-judgmental attitude and better self-care.

#### M.G2.10. Trauma-sensitive meditation

##### [M158] Trauma-sensitive meditation · L2
Principles for safe practice for someone with a trauma history: permission to keep the eyes open, choosing a neutral or external anchor, short sessions, always having a "way out," never forcing someone to stay with an intense sensation. States clearly the app's limits and the role of a professional.

#### M.G2.11. Reading the scientific evidence on meditation

##### [M159] Reading the scientific evidence on meditation · R
How to read a study on meditation: sample size, control group, expectation effects, the difference between "statistically significant" and "meaningful for daily life"; why the app uses cautious language.

#### M.G2.12. When meditation should not replace medical or psychological care

##### [M094] When meditation should not replace medical or psychological care · L1
The app's limits, situations that call for a doctor or mental-health professional, and how to present these cautions without alarming the user.

---
# LEARNING PATH

## Main path (for newcomers, tradition-neutral)

> **Principle:** This is a suggested learning order based on difficulty and skill dependency, not a mandatory sequence for every tradition. At branching steps, users pick the branch that fits them rather than working through every branch.

```text
Step 0 — Understanding what you're learning                L1
M001 → M002 → M095 → M096 → M098
M097 = a reference article on terminology; read it whenever needed

Step 1 — Preparing safely and getting ready                L1
M099 → M003 → M004 → M005

Step 2 — Practicing a basic sitting                         L1
M009 → M010 → M011 → M012 → M006 → M007

Step 3 — Stabilizing skills and building a habit            L1–L2
M008 → M013 → M014 → M105 → M102 → M103 → M015 → M016 → M106

Step 4 — Choosing a method / direction of practice          L2
├── Calm abiding:          M017 → M022 → M018 → M019 → M020 → M021
│                           → M109 → M108 → M107 → M023
├── Four foundations:      M033 → M034 → M035 → M036 → M037 → M038 → M039
├── Insight meditation:     M024 → M029 → M030 → M031 → M025 → M053
│                           → M026 → M027 → M028
└── Divine abodes:          M041 → M042 → M125 → M043 → M044 → M045 → M046

Step 5 — Going deeper in one direction                          L3–L4
├── Calm abiding:          M110 → M111 → M112
├── Four foundations:      M113 → M114 → M116 → M117 → M118 → M119 → M040
├── Insight meditation:    M120 → M121 → M032 → M122 → M123 → M124
└── Meditation subjects:   M127 → M128 → M054 → M131 → M050 → M049

Step 6 — Exploring a tradition                                   L3–L4
Vietnam:    M145 → M147 → M148 → M149 → M150 → M151
Theravāda:  M055 → M056 → M057 → M058 → M059 → M135 → M136 → M134
Mahāyāna:   M061 → M062 → M063 → M137 → M064 → M065 → M068 → M069 → M141 → M138 → M070 → M142
Vajrayāna:  M071 → M077 → M144 → M072 → M073 → M075

Step 7 — Content requiring prerequisites                          L5
Presented only at an educational/overview level, always with a "requires a teacher" label:
M067, M140, M074, M076, M078, M079, M143
```

## Secondary path — Health / secular (no Buddhist background required)

```text
M086 → M087 → M088 → M089 → M090 / M091 / M092 / M093
        → M157 (for those who want a structured program)
        → M158 (for anyone with a trauma history)
        → M094 (must be shown at the end of this branch)
```

## Secondary path — Busy people, under 10 minutes a day

```text
M085 → M153 → M015 → M082 → M083 → M016 → M084
```

## Path principles

1. **Groups A, B, and the subgroups within C/D are content structure; the learning sequence is only a suggestion.**
2. **L5 articles never appear in an automatic path.** They surface only when a user actively seeks them out.
3. **Content is never locked behind a fixed order.** A user must always be able to find any article through in-app search.
4. **Safety content travels alongside practice, not after it.** [M099] appears before practice begins; [M124] and [M158] must appear at the same time as their corresponding content.

# RULES FOR USING CODES AND METADATA IN THE APP

## 1. One article, many branches
If two entries share the same core content, create only **one record**:

```yaml
id: M010
title: "Noticing the natural breath"
level: L1
categories: [entry-level, shared-skill, samatha]
```

> Only tag a tradition when an article **genuinely** presents a method within that tradition's context; don't tag all three branches just because "the breath appears everywhere."

## 2. A general article and a tradition-specific article are two different articles

```text
[M017] Samatha / Śamatha — calm-abiding meditation      ← the shared concept
[M058] Samatha–Vipassanā in Theravāda                    ← how one tradition uses it
[M062] Calm and insight (Śamatha–Vipaśyanā) in Mahāyāna
[M072] Calm abiding (Śamatha) in Vajrayāna
```

## 3. Same title = same concept; same code = same article
To write about how a practice is carried out differently in each tradition, create a new article rather than cramming it into one. New codes take the next unused number (currently **M164** onward).

## 4. "Tradition" is metadata, not the only taxonomy

```yaml
id: M018
title: "Calm abiding with the breath"
level: L2
traditions: [shared]           # shared | theravada | mahayana | vajrayana | vietnam | secular
methods:    [samatha]
objects:    [breath]
goals:      [concentration, calm]
duration:   [10-20min]
requires:   [M010, M013]       # suggested reading before this
related:    [M056, M113]
safety:     none               # none | caution | needs-teacher
sources:    ["MN 118", "Visuddhimagga VIII"]
terms:
  pali:     "samatha"
  sanskrit: "śamatha"
  hanviet:  "chỉ"
```

This lets the app let users browse by **learning path**, by **method**, by **tradition**, by **goal**, by **duration**, or by **level**, without duplicating articles.

## 5. Three required fields missing from v1
- `level` — for building the learning path and letting users know whether an article suits them.
- `safety` — so the app can automatically attach warnings and block inappropriate suggestions (for example, never suggesting [M047] or [M130] to a user flagged for disordered eating).
- `terms` — to enable in-article term lookups.

---

# EDITORIAL PRINCIPLES

1. **Never use the taxonomy to rank traditions.** "Advanced" means harder or requiring more prerequisites, not "tradition A ranks above tradition B."
2. **Distinguish Pāli from Sanskrit, and always give the Sino-Vietnamese form too.** For example: samatha/śamatha, vipassanā/vipaśyanā, mettā/maitrī, upekkhā/upekṣā, satipaṭṭhāna/smṛtyupasthāna, buddhānussati/buddhānusmṛti. Use diacritics correctly; if the display system can't support them, use one consistent fallback rather than dropping diacritics in some places and keeping them in others.
3. **Layer sources.** State clearly whether content comes from the canonical discourses, from the commentaries, or from a modern teacher's presentation. This is a distinction Vietnamese readers very often miss.
4. **State a tradition's scope explicitly within the article.** The same term can be defined or practiced differently across traditions.
5. **Never equate modern mindfulness with satipaṭṭhāna.** There is a historical relationship, but secular "mindfulness" is a broader modern category with a different goal.
6. **Practice that requires prerequisites must carry a label.** An L5 article always includes a notice that the app presents it only at an educational level where the tradition requires a teacher, transmission, or empowerment.
7. **The health group uses evidence-based language.** Prefer "supports," "may help"; never promote meditation as a cure for illness.
8. **Safety is part of the content, not an appendix.** Every article with `safety: caution` must link to [M099]; content touching mental health must link to [M094].
9. **Never promise attainment, and never describe a state as an achievement.** Especially in [M110], [M122], and [M123].
10. **A neutral, respectful tone.** Never disparage one practice to elevate another; when sources disagree, present that disagreement.

---

# TERMINOLOGY CROSS-REFERENCE TABLE

| Pāli | Sanskrit | Sino-Vietnamese | Common Vietnamese usage | English |
|------|----------|----------|------------------------|---------|
| bhāvanā | bhāvanā | tu tập | tu tập, phát triển tâm | mental cultivation |
| samatha | śamatha | chỉ | Thiền chỉ, an tĩnh | calm abiding |
| vipassanā | vipaśyanā | quán | Thiền quán, minh sát | insight |
| sati | smṛti | niệm | chánh niệm | mindfulness |
| sampajañña | saṃprajanya | chánh tri | tỉnh giác | clear comprehension |
| samādhi | samādhi | định | định, tập trung | concentration |
| paññā | prajñā | tuệ | trí tuệ | wisdom |
| sīla | śīla | giới | giới, đạo đức | ethical conduct |
| jhāna | dhyāna | Thiền-na, tĩnh lự | Thiền định sâu | absorption |
| kammaṭṭhāna | karmasthāna | nghiệp xứ | đề mục Thiền | meditation subject |
| nimitta | nimitta | tướng | tướng Thiền | sign, mental image |
| satipaṭṭhāna | smṛtyupasthāna | tứ niệm xứ | bốn niệm xứ | foundations of mindfulness |
| kāyānupassanā | — | quán thân | quán thân | contemplation of body |
| vedanānupassanā | — | quán thọ | quán cảm thọ | contemplation of feeling |
| cittānupassanā | — | quán tâm | quán tâm | contemplation of mind |
| dhammānupassanā | dharmānupassanā | quán pháp | quán pháp | contemplation of dhammas |
| ānāpānassati | ānāpānasmṛti | nhập xuất tức niệm, an-ban niệm | niệm hơi thở | mindfulness of breathing |
| kāyagatāsati | — | thân hành niệm | niệm thân | mindfulness immersed in body |
| caṅkama | caṅkrama | kinh hành | Thiền đi | walking meditation |
| nīvaraṇa | nivaraṇa | cái, triền cái | năm chướng ngại | hindrance |
| bojjhaṅga | bodhyaṅga | giác chi | bảy yếu tố giác ngộ | factor of awakening |
| indriya | indriya | căn | năm căn | faculty |
| bala | bala | lực | năm lực | power |
| khandha | skandha | uẩn | năm uẩn | aggregate |
| āyatana | āyatana | xứ, nhập | sáu xứ | sense base |
| dhātu | dhātu | giới, đại | bốn đại | element |
| anicca | anitya | vô thường | vô thường | impermanence |
| dukkha | duḥkha | khổ | khổ, bất toại nguyện | unsatisfactoriness |
| anattā | anātman | vô ngã | vô ngã | non-self |
| tilakkhaṇa | trilakṣaṇa | tam pháp ấn | ba đặc tính | three characteristics |
| paṭiccasamuppāda | pratītyasamutpāda | duyên khởi | duyên sinh | dependent origination |
| nāma-rūpa | nāma-rūpa | danh sắc | thân và tâm | mind and matter |
| taṇhā | tṛṣṇā | ái | tham ái | craving |
| upādāna | upādāna | thủ | chấp thủ | clinging |
| papañca | prapañca | hý luận | tâm lan man, thêu dệt | conceptual proliferation |
| yoniso manasikāra | yoniśo manaskāra | như lý tác ý | hướng tâm đúng cách | wise attention |
| vitakka / vicāra | vitarka / vicāra | tầm / tứ | hướng tâm / duy trì tâm | initial / sustained application |
| pīti / sukha | prīti / sukha | hỷ / lạc | hỷ / lạc | rapture / bliss |
| ekaggatā | ekāgratā | nhất cảnh tính | nhất tâm | one-pointedness |
| upacāra-samādhi | — | cận hành định | cận định | access concentration |
| appanā-samādhi | — | an chỉ định | định nhập Thiền | absorption concentration |
| brahmavihāra | brahmavihāra | tứ phạm trú | tứ vô lượng tâm | divine abodes |
| mettā | maitrī | từ | từ ái, lòng thương | loving-kindness |
| karuṇā | karuṇā | bi | lòng bi | compassion |
| muditā | muditā | hỷ | tùy hỷ | appreciative joy |
| upekkhā | upekṣā | xả | tâm xả | equanimity |
| anussati | anusmṛti | tùy niệm | niệm tưởng | recollection |
| buddhānussati | buddhānusmṛti | niệm Phật | niệm Phật | recollection of the Buddha |
| maraṇassati | maraṇasmṛti | tử tùy niệm | niệm sự chết | mindfulness of death |
| asubha | aśubha | bất tịnh | quán bất tịnh | foulness |
| kasiṇa | kṛtsna | biến xứ | đề mục biến xứ | kasiṇa device |
| ñāṇa | jñāna | trí | tuệ, trí | knowledge |
| visuddhi | viśuddhi | thanh tịnh | thanh tịnh | purification |
| vimutti | vimukti | giải thoát | giải thoát | liberation |
| nibbāna | nirvāṇa | niết-bàn | niết-bàn | nibbāna |
| kalyāṇamitta | kalyāṇamitra | thiện tri thức | thầy, bạn đạo tốt | spiritual friend |
| — | bodhicitta | bồ-đề tâm | tâm bồ-đề | awakening mind |
| suññatā | śūnyatā | không tánh | tánh Không | emptiness |
| — | zhǐguān 止觀 | chỉ quán | chỉ và quán | calming and contemplation |
| — | dhyāna → chán → zen 禪 | Thiền | Thiền tông | Zen / Chan |
| — | niànfó 念佛 | niệm Phật | niệm Phật | recitation of Buddha's name |

---

# SUGGESTED SOURCES FOR WRITERS

## The Pāli canon (foundation for groups A–E)
- The *Satipaṭṭhāna Sutta* (MN 10) and the *Mahāsatipaṭṭhāna Sutta* (DN 22) — the foundation for group D.
- The *Ānāpānassati Sutta* (MN 118) — the foundation for [M113], [M056].
- The *Kāyagatāsati Sutta* (MN 119) — the foundation for [M114], [M048].
- The *Anattalakkhaṇa Sutta* (SN 22.59) — the foundation for [M028].
- The *Karaṇīyamettā Sutta* (Sn 1.8) — the foundation for [M042], [M125].
- Reference Vietnamese translation: the Vietnamese Tipiṭaka (Ven. Thích Minh Châu) for the Nikāyas; cross-check against English editions when needed.

## Commentaries and treatises
- The *Visuddhimagga* (The Path of Purification) — the foundation for [M127], [M128], [M108], [M122], [M126].
- The *Vimuttimagga* (The Path of Freedom) — cross-referenced against the Visuddhimagga.
- The *Mohe Zhiguan* (The Great Calming and Contemplation, by Zhiyi) — the foundation for [M137].

## Mahāyāna / Vajrayāna sources
- 84000 — *The King of Samādhis Sūtra*: the śamatha–vipaśyanā pair in a Mahāyāna context. https://84000.co/translation/toh127
- 84000 — *The Perfection of Wisdom in Eighteen Thousand Lines*: the four foundations of mindfulness, the four immeasurables, mindfulness of breathing, and the contemplation subjects. https://84000.co/translation/toh10/UT22084-029-001-glossary/toh3808
- 84000 — Glossary: *ānāpānānusmṛti* = mindfulness of breathing in and out. https://scholar.84000.co/authority/entity-37381
- 84000 — *smṛtyupasthāna* and *brahmavihāra* in Mahāyāna material. https://84000.co/pdf-redirect/toh176_84000-the-teaching-of-vimalakirti.pdf
- The *Sutra on the Visualization of Amitāyus* — the foundation for [M069].

## East Asia and Vietnam
- Encyclopedia.com — an overview of East Asian Buddhist meditation and the integration of śamatha/vipaśyanā. https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/buddhist-meditation-east-asian-buddhist-meditation
- The *Thiền uyển tập anh* ("Compendium of Outstanding Figures of the Zen Community") — the primary source for [M146]; read alongside modern scholarship on its dating.
- The *Khóa hư lục* (Trần Thái Tông), the *Recorded Sayings of Tuệ Trung Thượng Sĩ*, "Dwelling in the World, Content with the Way" (Trần Nhân Tông) — the foundation for [M147].
- Materials from contemporary Vietnamese practice lineages for [M148]–[M151]; when citing them, state clearly that this reflects one lineage's presentation, not a universal definition.

## Health / secular
- NCCIH — an overview of meditation/mindfulness, effectiveness, and safety. https://www.nccih.nih.gov/health/meditation-and-mindfulness-effectiveness-and-safety
- MBSR/MBCT program materials for [M157]; studies on adverse effects for [M099], [M158].

> **A note on links:** the URLs above are carried over from v1 of this document. They should be checked again before publication, and primary sources (scriptures, treatises, an organization's own site) should be preferred over aggregator pages.

---

# CHANGES FROM v1–v2

## New content (M095–M163, 68 articles — code M115 left unassigned; M160, M161, and M163 later retired in v3.6)
- **Missing foundations, now added:** the three trainings [M095], sati–sampajañña [M096], how to read terminology [M097], common misconceptions [M098], safety [M099], teachers [M100], retreats [M101].
- **Skills:** noting [M102], wise attention [M103], balancing the five faculties [M104], the attitude of practice [M105], journaling [M106].
- **Samatha:** three levels of concentration [M107], the nimitta [M108], the five hindrances [M109], the four jhānas and jhāna factors [M110], the four formless states [M111], combining concentration and wisdom [M112].
- **Satipaṭṭhāna:** the sixteen steps of ānāpānassati [M113], kāyagatāsati [M114], and the four child articles of the contemplation of dhammas [M116]–[M119] — previously [M039] stood alone with no concrete content beneath it.
- **Insight:** mind and matter [M120], dependent origination [M121], the progress of insight [M122], the corruptions of insight [M123], difficult stages [M124].
- **Loving-kindness:** the sequence of objects for cultivating loving-kindness [M125], the near/far enemies [M126].
- **Traditional meditation subjects:** the forty kammaṭṭhāna [M127], temperament (carita) [M128], the four elements [M129], food [M130], the ten recollections [M131], recollection of virtue/generosity/the deities [M132], recollection of peace [M133]. This is a framework v1 lacked, which had left articles [M047]–[M052] feeling disconnected.
- **Traditions:** the Theravāda textual system [M134], Burmese systems [M135], the Thai Forest Tradition [M136], Tiantai [M137], Yogācāra [M138], silent illumination [M139], the critical phrase [M140], combined Zen–Pure Land practice [M141], lojong/tonglen [M142], ngöndro [M143], lamrim [M144].
- **New group F — Vietnamese Buddhism [M145]–[M152].** This is the most significant addition: Vietnamese users encounter meditation primarily through these lineages and through Sino-Vietnamese terminology.
- **Daily life:** the busy [M153], family and children [M154], groups [M155], guided audio [M156].
- **Health:** MBSR/MBCT [M157], trauma-sensitive practice [M158], reading the evidence [M159].
- **New group N — reference M160–M163**, built to directly serve requests for "easy to look up" content; M162 was later moved to **B8**, while M160, M161, and M163 were retired (v3.6).

## Consolidation and revision
- **v3.3 — Further subdividing A, B, C1, C2:** A was organized around a newcomer's journey; B around a progression of skills from body–breath foundations → stabilizing attention → handling distraction → observing → balancing → integrating into daily life → reflecting; C1/C2 were divided into learning groups sharing a common function and suggested sequence.
- **v3.3 — Fixed the placement of D1 in the article catalog:** the four foundations of mindfulness were placed correctly under group D, no longer wedged between C1 and C2.
- **[M081] merged into [M015]** — "walking meditation" and "walking meditation in daily life" were the same skill. Code M081 was **retired** and is never reused.
- **[M053] renamed** to "The three characteristics (Tilakkhaṇa) — overview" and **moved from group F to group E** [translator's note: i.e., reclassified], placed before M026–M028 instead of repeating them at the end of another group.
- **[M060] Kasiṇa moved from the Theravāda group into group G** [i.e., the meditation-subjects system], since it is one of the forty kammaṭṭhāna rather than a feature unique to modern Theravāda.
- **Restructured the old tree** ("the two core axes of meditation") into **C. Samatha** and **E. Vipassanā** [i.e., the current C1/C2], with **D. Satipaṭṭhāna** in between as a connecting framework. The old grouping folded both axes into a single branch, which skewed the tree and made a learning path hard to build.
- **Renamed the old group F** ("traditional contemplations and recollections") to **G. Traditional Meditation Subjects — Kammaṭṭhāna**, matching the system's actual name.
- **Added an L1–L5/R level to every article**, plus three required metadata fields: `level`, `safety`, `terms`.
- **Standardized terminology:** *Buddha-anusmṛti* → *buddhānusmṛti*; added Sanskrit forms for the *anussati* set; added Sino-Vietnamese for all core terms; added a **Terminology** line to each article where needed.
- **Added the five-column terminology cross-reference table** at the end of the document.
- **Upgraded the sources section:** organized by layer (canon / commentary / Mahāyāna / Vietnam / secular) and tied to specific article codes.

## RESTRUCTURING THE TAXONOMY IN v3.6

- **Removed group H (reference & tools):** [M162] was moved into **B8. Frequently asked questions about meditation** (group B, level R); M160, M161, and M163 were **retired** and are never reused.
- **G1 and G2 subdivided:** G1.1–G1.8 and G2.1–G2.12 — each subgroup is now its own entry in both the TAXONOMY TREE and the ARTICLE CATALOG.
- Synced remaining references to M160/M163 throughout the document; updated code statistics and the level distribution.

## RESTRUCTURING THE TAXONOMY IN v3.5

- Subdivided **E1. The Theravāda tradition** into E1.1–E1.4: overview → core frameworks/methods → modern meditation systems and lineages → scriptures and the commentarial tradition.
- Subdivided **E2. The Mahāyāna tradition** into E2.1–E2.6: overview/calm–insight → introductory Zen → buddha-recitation/Pure Land → combined Zen–Pure Land → advanced Zen → Mahāyāna reflection and mind-training directions; within E2.1, [M137] sits under the Calming–Contemplation (Zhǐguān) cluster as one specific system.
- Subdivided **E3. The Vajrayāna tradition** into E3.1–E3.5: overview → path foundations and preliminary practices → calm abiding/insight → distinctive means → advanced practice and lineage requirements.
- Synced the **TAXONOMY TREE** and the **ARTICLE CATALOG** across all of E1–E3; the E1.x/E2.x/E3.x clusters are learning groups within a tradition, not independent traditions.
- Updated **Learning Path — Step 6** so the sequence for exploring Theravāda/Mahāyāna/Vajrayāna matches the new structure; L5 articles remain in Step 7.

## RESTRUCTURING THE TAXONOMY IN v3.4

- Synced the **TAXONOMY TREE** with the **ARTICLE CATALOG**; the top-level tree no longer stayed flat while the catalog beneath it was already grouped.
- A was divided into **A1–A7** following a newcomer's journey: understanding meditation → understanding how to practice → safety → preparation → during/after a sitting → building a habit → support/going deeper.
- B was divided into **B1–B7** following a skill progression: body/breath foundations → stabilizing attention → handling distraction → observing → balancing → integrating into daily life → reflecting.
- C1 and C2 were fully reflected in the tree with groups **C1.1–C1.5** and **C2.1–C2.6**, instead of showing only two flat branches.
- D1, D2, and D3 were kept in an **overview → component group → detailed article** relationship; D2's relationship to D3 was made explicit, since the Brahmavihāra is one group within the Visuddhimagga's presentation of the forty subjects.
- Moved **[M054] Choosing a subject that suits you** to its correct place in **D3.1. Overview, classification, and selection**, and updated the corresponding learning-path sequence.
- Fixed duplicate/overlapping Markdown headings and aligned the heading levels of the article catalog with the taxonomy tree.

## Notes carried over from the original restructuring rationale
- **A–G are not treated as seven parallel "types of meditation."** Each group is tied to a distinct nature of information: foundation, skill, method, framework/practice, tradition, region, and application/context.
- **Samatha and Vipassanā were merged into group C — method/practice direction**, since these are the two core `method` values.
- **Satipaṭṭhāna, Brahmavihāra, and Kammaṭṭhāna were placed in group D — framework/system of practice**, while still distinguishing them internally: Satipaṭṭhāna is a `framework`, Brahmavihāra is a `practice_group`, Kammaṭṭhāna is an `object_taxonomy`.
- **Theravāda, Mahāyāna, and Vajrayāna were merged into group E — tradition/meditation lineage**, the appropriate place to describe tradition rather than using tradition as the sole classification for every article.
- **Vietnamese Buddhism was placed in group F — cultural/regional context**, since this branch spans several different lineages that are all present in Vietnam.
- **Applied/daily-life meditation and health/secular meditation were merged into group G**, since both describe a context of use and an application goal rather than a "school."
- **Title convention:** Vietnamese first, with the Pāli/Sanskrit term placed afterward in parentheses — for example, `Thiền chỉ (Samatha)`, `Bốn niệm xứ (Satipaṭṭhāna)`, `Tứ vô lượng tâm (Brahmavihāra)`. [translator's note: in this English edition, the order is reversed — an English gloss leads, with the Pāli/Sanskrit term in parentheses, per Principle 4.]

## Suggestions for the next round
1. Write the first 25 L1 articles first, to give newcomers a complete path, before expanding further.
2. Every L1–L2 article should be paired with **one guided practice** (audio/script) — the catalog currently covers only the theory.
3. Have at least one monastic or teacher from each tradition review groups A–G before publication.

## Version 3.6 statistics
- Total articles: **158** (v2: 161; the taxonomy was restructured and further subdivided across v3.3–v3.6).
- Codes in use: M001–M163, excluding **M081** (retired, merged into M015), **M115** (left unassigned), and **M160**, **M161**, **M163** (retired when group H was removed in v3.6).
- Next code when adding a new article: **M164**.
- Distribution by level: L1 ≈ 40 articles · L2 ≈ 45 · L3 ≈ 40 · L4 ≈ 23 · L5 ≈ 7 · R ≈ 3.
- Top-level taxonomy: **7 groups** (A–G); A/B/C/D each have internal subgroups, with C distinguishing two `method` values and D distinguishing `framework` / `practice_group` / `object_taxonomy`.

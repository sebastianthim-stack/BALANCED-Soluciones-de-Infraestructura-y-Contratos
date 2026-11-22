md_content = """# BALANCED — Soluciones de Infraestructura y Contratos: Competitive & Positioning Matrix (Argentina)

## 1. Market Context & Differentiation
**BALANCED — Soluciones de Infraestructura y Contratos** (led by **Sebastian Juarez Tejerina**, based in Argentina, ART / UTC-3) operates across railway and civil infrastructure execution, mining EPCT contract administration and compliance, and operational safety/incident management, with working capability in **Español e Inglés** [cite: 2, 3].

In Argentina, prospective clients typically face a split between two poles:
* **Large Engineering & EPCM Consultancies:** Strong on formal design studies, technical/environmental reporting, or broad multi-disciplinary teams, but often distanced from day-to-day field contractor dynamics [cite: 2].
* **Heavy Civil & Railway Contractors:** Strong on physical execution, machinery, and crews, but less focused on independent owner/operator contract and compliance oversight [cite: 2].

**BALANCED's Core Positioning:**
1. **Field Execution + Contract Compliance:** Connects real-world site execution (track renewal, logistics centers, bridges/culverts, contractor tracking, *Libro Legal de Obra*, monthly certifications) with contractual and compliance rigor [cite: 2, 3].
2. **Cross-Sector Transfer (Railways + Mining EPCT):** Brings railway safety management (SMS), incident analysis, and large-corridor schedule/cost discipline to mining EPCT contract supervision [cite: 2, 3].
3. **Español e Inglés Delivery:** Supports local field/commercial stakeholders as well as international sponsors and technical teams [cite: 2, 3].

---

## 2. Competitor Comparison Matrix (Argentina)

| Competitor / Group | Primary Category | Overlapping Capabilities | Key Positioning Contrast vs. BALANCED |
| :--- | :--- | :--- | :--- |
| **TRICO Consultoría S.A.** (`trico.com.ar`) | Civil & Railway Engineering Consultancy | Railway and civil engineering consulting, feasibility studies, track projects, level crossings, bridges/culverts, construction supervision (*dirección de obra*), risk management, cost optimization, and O&M/RAMS. | Closest direct overlap in railway/civil engineering consulting and operational risk/O&M; operates as a traditional engineering consultancy. |
| **Knight Piésold Argentina** (`knightpiesold.com`) | EPCM & Mining / Infrastructure Consultancy | EPCM services, civil/geotechnical/electromechanical engineering, quality assurance/inspection, risk management, and regulatory support across mining and infrastructure. | Overlaps on mining, risk, and project governance; operates as a large multidisciplinary consultancy rather than a specialized field-and-contract advisory. |
| **Penta Obras** (`pentaobras.com`) | Railway & Civil Contractor | Railway infrastructure engineering, track improvement/renovation, civil works, bridges/viaducts/culverts, signaling/electrical works, and maintenance. | Primarily an execution and maintenance contractor rather than a dedicated contract/compliance and advisory practice. |
| **Acovial S.A.** (`acovial.com.ar`) | Civil, Railway & Electrical Contractor | Railway infrastructure and remodeling, civil, electrical, and hydraulic works, plus project evaluation, management, and safety/diagnostic systems. | Established contractor (since 1978) with strong transit/utility contracting presence; heavier on physical contracting than EPCT contract supervision. |
| **Large Infrastructure & Railway Groups** (e.g., Emepa, Pose, Rovella Carranza) | Tier-1 Heavy Infrastructure Contractors | Large-scale railway, civil/road, hydraulic, and heavy construction across Argentina. | Large prime contractors—typically execution partners or counterparties rather than lean independent contract/compliance advisors. |
| **Infrastructure & Project Law Practices** (e.g., VMF, Dentons) | Legal & Transaction Advisory | Structuring and advising on EPC, EPCM, turnkey, supply, subcontracting, and PPP/O&M contracts. | Focuses on legal drafting and transaction structure rather than on-site railway/civil execution and technical contractor/compliance control. |

---

## 3. Publishing to GitHub Pages

1. Create a new repository on **GitHub** (for example, `balanced-infraestructura`).
2. Upload `index.html` (and optionally `competitive_positioning_matrix.md`) to the root of the repository.
3. Open **Settings -> Pages**, set **Source** to **Deploy from a branch**, select the `main` branch and `/ (root)` folder, and save.
4. Once GitHub finishes building the site, share the generated `https://<username>.github.io/<repo-name>/` URL with Sebastian.
"""

with open("competitive_positioning_matrix.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("Wrote clean competitive_positioning_matrix.md.")
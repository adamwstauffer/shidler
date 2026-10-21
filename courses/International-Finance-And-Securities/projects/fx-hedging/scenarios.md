# Scenarios: EUR receivables (USD base)

Every student has their own scenario, one per person: 37 for the Fall 2026 section. Your scenario
number and slug come from your instructor. Use the slug in every dated file name
(`YYYY-MM-DD-{scenario}-{type}.md`), e.g. `2026-10-23-beef-processor-hedge-brief.md`.

Each scenario is a U.S. company that has invoiced a European buyer in euros and will be paid on a
fixed future date. You are the analyst advising its CFO. Everyone hedges the same pair, EURUSD;
the firm, the amount and the settlement date are yours alone.

## Reading your scenario

- **Receivable** (`FC_AMT`) and **days to settlement** (`T_DAYS`) are fixed. They never change, not
  even at Stage 4.
- **Spot** and both **interest rates** (`S0_in`, `R_USD`, `R_FC`) are yours to find: until Stage 4,
  use the market close on the day you begin Stage 2, and record the date and source. At Stage 4 you
  replace them with live data.
- **Forward (indicative)** is a placeholder for `F0_in` until Stage 4, when you replace it with a
  live forward or the CIP-implied forward, and comment on the gap.
- **Option premiums** are given and are kept at Stage 4: retail option quotes are unreliable. The
  strikes (`K_PUT`, `K_CALL`) are set at or near your spot.

The indicative forwards and the premiums were set on 2026-10-18 for teaching. They are
placeholders, not market quotes.

---
### Scenario 1: `wafer-inspection`

A U.S. maker of wafer-inspection equipment has invoiced a Dutch chipmaker, in euros (EUR).

* **Receivable:** EUR 16,500,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 2: `beef-processor`

A U.S. beef processor has invoiced an Italian supermarket chain, in euros (EUR).

* **Receivable:** EUR 3,900,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 3: `surgical-robotics`

A U.S. maker of surgical robotics has invoiced a German hospital group, in euros (EUR).

* **Receivable:** EUR 9,400,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 4: `game-licensing`

A U.S. video-game studio has invoiced a French publisher (licensing royalties), in euros (EUR).

* **Receivable:** EUR 2,600,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 5: `sawmill-machinery`

A U.S. sawmill-machinery manufacturer has invoiced a Finnish lumber mill, in euros (EUR).

* **Receivable:** EUR 6,300,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 6: `payroll-software`

A U.S. payroll-software firm has invoiced a Spanish bank (multi-year license), in euros (EUR).

* **Receivable:** EUR 4,300,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 7: `farm-equipment`

A U.S. combine and tractor maker has invoiced an Irish farm cooperative, in euros (EUR).

* **Receivable:** EUR 7,700,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 8: `biotech-milestone`

A U.S. biotech has invoiced a Belgian pharmaceutical company (milestone payment), in euros (EUR).

* **Receivable:** EUR 19,500,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 9: `lab-instruments`

A U.S. maker of laboratory mass spectrometers has invoiced an Austrian research institute, in euros (EUR).

* **Receivable:** EUR 5,100,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 10: `craft-whiskey`

A U.S. craft-whiskey distiller has invoiced a French luxury-hotel group, in euros (EUR).

* **Receivable:** EUR 2,100,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 11: `transmission-parts`

A U.S. transmission-parts supplier has invoiced a Slovak car-assembly plant, in euros (EUR).

* **Receivable:** EUR 12,000,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 12: `grain-cooperative`

A U.S. grain cooperative has invoiced a Portuguese feed manufacturer, in euros (EUR).

* **Receivable:** EUR 6,900,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 13: `commercial-hvac`

A U.S. commercial-HVAC manufacturer has invoiced a Milan office developer, in euros (EUR).

* **Receivable:** EUR 3,400,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 14: `soybean-merchant`

A U.S. soybean merchandiser has invoiced a German oilseed crusher, in euros (EUR).

* **Receivable:** EUR 13,500,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 15: `landing-gear`

A U.S. aircraft-landing-gear maker has invoiced a French aircraft manufacturer, in euros (EUR).

* **Receivable:** EUR 10,500,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 16: `online-degrees`

A U.S. online-degree provider has invoiced a Dutch university partner, in euros (EUR).

* **Receivable:** EUR 3,000,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 17: `data-center-servers`

A U.S. server and networking manufacturer has invoiced an Irish data-center operator, in euros (EUR).

* **Receivable:** EUR 17,500,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 18: `ship-propulsion`

A U.S. ship-propulsion engineering firm has invoiced a Greek shipyard, in euros (EUR).

* **Receivable:** EUR 5,600,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 19: `api-ingredients`

A U.S. maker of active pharmaceutical ingredients has invoiced an Italian contract manufacturer, in euros (EUR).

* **Receivable:** EUR 8,200,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 20: `lithium-refining`

A U.S. lithium-refining company has invoiced a German battery maker, in euros (EUR).

* **Receivable:** EUR 11,000,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 21: `forest-software`

A U.S. forest-inventory software firm has invoiced a Finnish timber company, in euros (EUR).

* **Receivable:** EUR 1,700,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 22: `mri-components`

A U.S. MRI-component manufacturer has invoiced a Dutch medical-imaging group, in euros (EUR).

* **Receivable:** EUR 6,000,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 23: `offshore-wind-cable`

A U.S. offshore-wind cable manufacturer has invoiced a Danish wind developer, in euros (EUR).

* **Receivable:** EUR 16,000,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 24: `seafood-equipment`

A U.S. seafood-processing equipment maker has invoiced a Spanish tuna canner, in euros (EUR).

* **Receivable:** EUR 4,700,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 25: `subsea-inspection`

A U.S. subsea-inspection services firm has invoiced an Italian energy company, in euros (EUR).

* **Receivable:** EUR 8,600,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 26: `chip-design-ip`

A U.S. chip-design IP licensor has invoiced a French electronics group (royalties), in euros (EUR).

* **Receivable:** EUR 13,000,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 27: `lng-marketer`

A U.S. LNG marketer has invoiced a German utility, in euros (EUR).

* **Receivable:** EUR 21,500,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 28: `film-rights`

A U.S. film studio has invoiced a Spanish streaming platform (content rights), in euros (EUR).

* **Receivable:** EUR 3,600,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 29: `cloud-migration`

A U.S. cloud-migration consultancy has invoiced a Belgian telecom carrier, in euros (EUR).

* **Receivable:** EUR 5,300,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 30: `almond-packer`

A U.S. almond grower-packer has invoiced a German confectionery maker, in euros (EUR).

* **Receivable:** EUR 2,400,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 31: `turbine-gearbox`

A U.S. wind-turbine gearbox maker has invoiced a Spanish renewable-power developer, in euros (EUR).

* **Receivable:** EUR 9,900,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 32: `seed-genetics`

A U.S. seed-genetics company has invoiced a French grain cooperative, in euros (EUR).

* **Receivable:** EUR 7,300,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

### Scenario 33: `mining-shovels`

A U.S. mining-shovel manufacturer has invoiced a Finnish nickel miner, in euros (EUR).

* **Receivable:** EUR 14,500,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 34: `erp-software`

A U.S. ERP-software firm has invoiced a Dutch retailer, in euros (EUR).

* **Receivable:** EUR 2,900,000, received in 91 days (3 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1653, maturity 91 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0147 per EUR
  * Call on EUR, strike at spot: premium USD 0.0199 per EUR

### Scenario 35: `haul-trucks`

A U.S. haul-truck manufacturer has invoiced a Portuguese copper miner, in euros (EUR).

* **Receivable:** EUR 18,000,000, received in 365 days (12 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1807, maturity 365 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0245 per EUR
  * Call on EUR, strike at spot: premium USD 0.0448 per EUR

### Scenario 36: `hospital-records`

A U.S. hospital-records software firm has invoiced an Austrian hospital network, in euros (EUR).

* **Receivable:** EUR 2,200,000, received in 182 days (6 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1705, maturity 182 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0194 per EUR
  * Call on EUR, strike at spot: premium USD 0.0296 per EUR

### Scenario 37: `solar-inverters`

A U.S. solar-inverter maker has invoiced an Italian utility-scale solar developer, in euros (EUR).

* **Receivable:** EUR 5,400,000, received in 273 days (9 months)
* **Spot:** EURUSD, market quote
* **Forward (indicative):** EURUSD 1.1756, maturity 273 days
* **USD interest rate:** [n.nn%]
* **EUR interest rate:** [n.nn%]
* **Options** (no multiplier):
  * Put on EUR, strike at spot: premium USD 0.0224 per EUR
  * Call on EUR, strike at spot: premium USD 0.0376 per EUR

---

## Summer 2026 scenarios (retired)

Summer 2026 used four shared EUR receivables: `solar-exporter` (EUR 4,500,000, forward 1.0875,
put 0.015 / call 0.018), `pharma-exporter` (EUR 8,000,000, 1.0890, 0.021 / 0.026), `tech-services`
(EUR 12,500,000, 1.0910, 0.017 / 0.022) and `aerospace` (EUR 20,000,000, 1.0935, 0.019 / 0.024),
all one year out. They are kept here only so Summer 2026 repositories can still be read.

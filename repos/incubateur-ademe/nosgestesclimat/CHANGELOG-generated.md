## Changelog : nosgestesclimat (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, nosgestesclimat a bénéficié d'améliorations significatives concernant le calcul de l'empreinte carbone liée au transport, notamment pour les véhicules (voitures, scooters électriques, camping-cars) et les modes de transport alternatifs. Des corrections et ajustements ont été apportés aux calculs de consommation d'énergie, ainsi que des mises à jour des données relatives à la Date Limite d'Utilisation Optimale (DLUO) pour certains produits. L'expérience utilisateur a également été améliorée avec l'ajout de nouvelles actions et la suppression de questions redondantes.

### Évolutions fonctionnelles
- Ajout de l'action "JVA" (Job, Vélo, Auto-partage) pour encourager des modes de transport plus durables. [#2741](https://github.com/incubateur-ademe/nosgestesclimat/pull/2741)
- Amélioration de la gestion des scooters électriques en frontend. [#2741](https://github.com/incubateur-ademe/nosgestesclimat/pull/2741)
- Prise en compte de la distinction entre camping-cars de 3.5t et 4t pour un calcul plus précis de l'empreinte carbone.
- Ajout d'une option pour le fioul dans le cadre du chauffage collectif. [#2735](https://github.com/incubateur-ademe/nosgestesclimat/pull/2735)
- Mise à jour des données DLUO pour les voitures et les textiles. [#2733](https://github.com/incubateur-ademe/nosgestesclimat/pull/2733) [#2732](https://github.com/incubateur-ademe/nosgestesclimat/pull/2732)
- Ajout d'une notification pour l'achat en vrac. [#2731](https://github.com/incubateur-ademe/nosgestesclimat/pull/2731)
- Repousse de la DLUO pour certains produits. [#2732](https://github.com/incubateur-ademe/nosgestesclimat/pull/2732)

### Évolutions techniques
- Utilisation d'un contexte pour le modèle voiture afin d'améliorer la gestion des données et la réutilisabilité du code.
- Refonte de la gestion de la consommation électrique, notamment pour le chauffage collectif et les cas "pas de chauffage".
- Mise à jour de l'API Ecobalyse. [#2732](https://github.com/incubateur-ademe/nosgestesclimat/pull/2732)
- Amélioration de la gestion des personas.

### Autres changements
- Suppression de la question relative aux services sociétaux. [#2735](https://github.com/incubateur-ademe/nosgestesclimat/pull/2735)
- Suppression de l'action "se chauffer au bois".
- Corrections de typos et de migrations de données.
- Traductions mises à jour.
- Corrections de bugs liés au double comptage de la consommation électrique.
- Corrections de bugs liés aux valeurs par défaut de consommation.
- Publication des versions 4.10.1 et 4.10.2.

# Synthèse d'activité : anct-cartographie-nationale (du 23/05 au 02/06)

## Résumé de l'activité
L'organisation a connu une semaine productive, axée sur l'amélioration de la qualité et de la disponibilité des données des lieux de médiation numérique, ainsi que sur la modernisation de l'application de cartographie.  [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a bénéficié d'optimisations significatives du processus de géocodage et de l'ajout de nouvelles sources de données. L'application [cartographie](/repos/anct-cartographie-nationale/cartographie) a vu l'implémentation de nouvelles fonctionnalités de recherche et l'adoption d'une nouvelle stack technologique (Arckit) pour une meilleure maintenabilité et scalabilité.

## Sécurité
- Ajout de la détection de secrets avec Gitleaks dans les hooks pré-commit et CI sur [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Autres changements notables
- Migration du géocodage BAN vers l'API batch CSV dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), améliorant les performances et la scalabilité.
- Migration de l'application [cartographie](/repos/anct-cartographie-nationale/cartographie) vers l'écosystème Arckit (@arckit/telemetry, @arckit/form, @arckit/daisyui, @arckit/nextjs).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la gestion des données de lieux de médiation numérique, incluant l'ajout de nouvelles sources et l'optimisation du géocodage.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Modernisation de l'application avec l'adoption d'Arckit et l'ajout de nouvelles fonctionnalités de recherche et de contact.

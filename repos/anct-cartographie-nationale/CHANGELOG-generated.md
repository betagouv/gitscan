# Synthèse d'activité : anct-cartographie-nationale (du 23/05 au 02/06)

## Résumé de l'activité
L'organisation a connu une semaine productive axée sur l'amélioration de la qualité et de la disponibilité des données de médiation numérique, ainsi que sur la modernisation de l'application de cartographie.  [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a bénéficié d'optimisations significatives du géocodage et de l'intégration de nouvelles sources de données, permettant une publication plus fiable des informations. L'application [cartographie](/repos/anct-cartographie-nationale/cartographie) a vu l'ajout de fonctionnalités de recherche et de contact, ainsi qu'une migration vers un nouvel écosystème technologique (Arckit) pour une meilleure maintenabilité et sécurité.

## Sécurité
- Ajout de la détection de secrets via Gitleaks dans [cartographie](/repos/anct-cartographie-nationale/cartographie) pour renforcer la sécurité du code.

## Autres changements notables
- Migration du géocodage BAN vers l'API batch CSV dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour améliorer les performances et la scalabilité.
- Migration de l'application [cartographie](/repos/anct-cartographie-nationale/cartographie) vers l'écosystème Arckit, incluant l'adoption de plusieurs librairies pour la télémétrie, les formulaires, le design et le framework Next.js.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la gestion des données de lieux de médiation numérique, avec l'ajout de nouvelles sources et l'optimisation du géocodage.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Modernisation de l'application avec l'ajout de fonctionnalités utilisateur et une migration vers un nouvel écosystème technologique.

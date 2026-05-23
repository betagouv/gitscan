# Synthèse d'activité : anct-cartographie-nationale (du 16/04 au 23/04/2026)

## Résumé de l'activité
L'organisation a connu une semaine productive, axée sur l'amélioration de la qualité des données et de l'expérience utilisateur. Des améliorations ont été apportées à la gestion des lieux de médiation numérique avec [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), notamment en optimisant les appels à l'API BAN et en filtrant les doublons. La carte interactive [cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié de nouvelles fonctionnalités de filtrage et d'intégration, ainsi que d'optimisations significatives de ses performances et de son infrastructure.

## Sécurité
L'infrastructure de [cartographie](/repos/anct-cartographie-nationale/cartographie) a été renforcée avec l'ajout d'un reverse proxy Nginx, améliorant la sécurité et la limitation du débit.

## Autres changements notables
[cartographie](/repos/anct-cartographie-nationale/cartographie) a subi une refonte technique majeure avec l'introduction d'un BFF (Backend For Frontend) en mémoire et l'utilisation du streaming pour les exports CSV, ce qui a permis d'optimiser les performances et de réduire la consommation de mémoire.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la gestion des adresses et des lieux de médiation numérique, avec correction de bugs et optimisation des performances.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Ajout de nouvelles fonctionnalités de filtrage et d'intégration, refonte de l'infrastructure et optimisation des performances.

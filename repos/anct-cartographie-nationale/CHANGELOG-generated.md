# Synthèse d'activité : anct-cartographie-nationale (du 16/04 au 23/04/2026)

## Résumé de l'activité
L'organisation a connu une semaine productive, axée sur l'amélioration de l'expérience utilisateur et de la performance de ses outils. Des améliorations significatives ont été apportées à la [cartographie](/repos/anct-cartographie-nationale/cartographie) avec l'ajout de filtres de disponibilité et la possibilité d'intégration sur d'autres sites web. Parallèlement, [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a bénéficié d'optimisations concernant la gestion des adresses et la correction de bugs liés à l'API BAN, améliorant ainsi la qualité des données et la fiabilité de l'outil.

## Sécurité
L'ajout d'un reverse proxy Nginx dans [cartographie](/repos/anct-cartographie-nationale/cartographie) renforce la sécurité et permet la limitation du débit.

## Autres changements notables
La [cartographie](/repos/anct-cartographie-nationale/cartographie) a subi une refonte technique importante avec l'introduction d'un reverse proxy Nginx, un BFF en mémoire et l'optimisation du cache. Ces changements visent à améliorer la performance, la sécurité et la scalabilité de la plateforme. L'utilisation du streaming pour les exports CSV permet également de réduire la consommation de mémoire.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la gestion des adresses et correction de bugs liés à l'API BAN.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Ajout de nouvelles fonctionnalités d'affichage et de filtres, ainsi qu'une refonte technique majeure de l'infrastructure.

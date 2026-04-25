# Synthèse d'activité : anct-cartographie-nationale (du 30 mars 2026 au 24 avril 2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des performances, de la sécurité et de la stabilité de la plateforme de cartographie. Des optimisations significatives ont été apportées à l'infrastructure avec l'ajout d'un reverse proxy Nginx et l'intégration de CrowdSec pour la détection de menaces. L'outil `mednum-cli` a également été mis à jour pour utiliser une URL CloudFront, améliorant ainsi sa performance et sa fiabilité. Ces améliorations se traduisent par une expérience utilisateur plus fluide et une plateforme plus robuste.

## Sécurité
- Intégration de CrowdSec pour la détection collaborative de menaces dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Configuration de sécurité renforcée du reverse proxy Nginx (limitation de débit, page d'erreur personnalisée 403, timeouts) dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Autres changements notables
- Implémentation d'un cache en mémoire (BFF) pour améliorer les performances de l'API dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Ajout d'un reverse proxy Nginx avec caching, compression gzip dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Mise à jour de Node.js vers la version 22 dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Optimisation de la taille de l'image Docker (réduction de 42%) dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Dépôts les plus actifs
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration significative des performances et de la sécurité de la plateforme de cartographie.
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Mise à jour de l'URL de l'API pour optimiser les performances et correction d'un problème de données.

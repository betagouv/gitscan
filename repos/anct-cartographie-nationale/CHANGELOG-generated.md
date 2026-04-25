# Synthèse d'activité : anct-cartographie-nationale (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des performances, de la sécurité et de la fiabilité de la plateforme de cartographie. Des optimisations significatives ont été apportées à l'infrastructure, notamment avec l'ajout d'un reverse proxy Nginx et l'intégration de CrowdSec pour la détection de menaces. L'outil `mednum-cli` a également été mis à jour pour utiliser une URL CloudFront, améliorant ainsi sa connectivité et sa performance. Ces améliorations se traduisent par une expérience utilisateur plus fluide et une plus grande stabilité du système pour les utilisateurs finaux.

## Sécurité
- Intégration de CrowdSec pour la détection collaborative de menaces dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Configuration de sécurité Nginx avec limitation de débit et page d'erreur personnalisée 403 dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Autres changements notables
- Implémentation d'un cache en mémoire (BFF) pour améliorer les performances en réduisant les appels directs à l'API PostgREST dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Ajout d'un reverse proxy Nginx avec caching, compression gzip et configuration de sécurité dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Mise à jour de l'URL de l'API de cartographie nationale vers CloudFront dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour optimiser les performances et la disponibilité.

## Dépôts les plus actifs
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration significative des performances et de la sécurité de la plateforme principale.
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Optimisation de la connectivité à l'API de cartographie nationale et correction d'un problème de données.

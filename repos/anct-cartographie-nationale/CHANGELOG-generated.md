# Synthèse d'activité : anct-cartographie-nationale (du 12/09 au 19/09)

## Résumé de l'activité
L'activité récente est principalement axée sur l'amélioration de la qualité et de la fiabilité des données géographiques. Grâce à de nouveaux mécanismes de déduplication et de filtrage plus précis, les outils [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) offrent désormais une meilleure gestion des doublons et des informations de localisation.

Parallèlement, l'organisation renforce la conformité et l'expérience utilisateur, notamment avec la mise en place de déclarations d'accessibilité dans [cartographie](/repos/anct-cartographie-nationale/cartographie), garantissant un service plus inclusif et conforme aux attentes légales.

## Sécurité
- Renforcement de la sécurité des déploiements dans [cartographie](/repos/anct-cartographie-nationale/cartographie) via la suppression des jetons npm statiques et l'amélioration de l'authentification pour les plugins d'infrastructure (Pulumi Scaleway).

## Autres changements notables
- **Évolutions architecturales et changements majeurs :**
    - Refonte du processus de déduplication dans [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique), introduisant des changements de rupture (*breaking changes*) pour optimiser la validation des données.
    - Restructuration de l'architecture de [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour une meilleure gestion des fonctionnalités et refactoring de l'injection de dépendances dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- **Modernisation de la chaîne de développement (DevEx) et CI/CD :**
    - Adoption de nouveaux standards de développement (passage à Biome) et sécurisation des publications via le mécanisme "Trusted Publishing" pour [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
    - Optimisation des workflows de release et de la CI/CD pour [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la précision des données et de l'interface de ligne de commande.
- [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) : Refonte majeure du système de déduplication des lieux.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Mise en conformité d'accessibilité et sécurisation des processus de déploiement.

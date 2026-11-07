# Synthèse d'activité : anct-cartographie-nationale (du 28/08 au 19/09)

## Résumé de l'activité
L'activité récente est marquée par une amélioration significative de la qualité et de la précision des données géographiques et d'accessibilité. Grâce à l'implémentation de nouveaux mécanismes de déduplication et de filtrage plus fin, les outils [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) garantissent une information plus fiable et mieux structurée pour les utilisateurs finaux.

Parallèlement, l'organisation renforce sa conformité légale, notamment via l'intégration de déclarations d'accessibilité dans [cartographie](/repos/anct-cartographie-nationale/cartographie), et modernise ses processus de déploiement pour assurer une meilleure robustesse des services.

## Sécurité
- Sécurisation des publications sur npm via le mécanisme "trusted publishing" dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
- Renforcement de la sécurité des workflows de release par la suppression des jetons npm statiques dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- Amélioration de l'authentification pour les plugins d'infrastructure (Pulumi Scaleway) dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Autres changements notables
- **Évolutions architecturales et changements majeurs :**
    - Refonte de l'architecture pour la gestion des capacités de fonctionnalités dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli).
    - Changement majeur (breaking change) dans le processus de déduplication des lieux dans [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
    - Refactoring de l'injection de dépendances dans [cartographie](/repos/anct-cartographie-nationale/cartographie).
- **Optimisation de la chaîne de développement (CI/CD) :**
    - Modernisation des outils de développement (passage à Biome) dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli).
    - Amélioration de la CI pour la détection automatique des changements majeurs dans [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
    - Optimisation et alignement des workflows de déploiement et des versions de Node.js dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la précision des données et refonte de l'architecture logicielle.
- [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) : Mise en place de règles de déduplication et mise à jour majeure de la logique de traitement.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Mise en conformité d'accessibilité et optimisation de l'infrastructure de déploiement.

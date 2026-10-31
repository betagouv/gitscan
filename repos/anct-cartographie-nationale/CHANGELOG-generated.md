# Synthèse d'activité : anct-cartographie-nationale (du 12/09 au 19/09)

## Résumé de l'activité
L'activité de la période est principalement portée par un effort de fiabilisation des données et de mise en conformité. L'organisation a renforcé la qualité de ses informations géographiques grâce à l'implémentation de nouveaux mécanismes de déduplication et de filtrage dans [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).

Parallèlement, l'accent a été mis sur l'accessibilité numérique, tant au niveau des outils de traitement que de l'interface de [cartographie](/repos/anct-cartographie-nationale/cartographie), garantissant ainsi une meilleure conformité légale et une expérience utilisateur plus inclusive.

## Sécurité
- Sécurisation des processus de publication de paquets via l'adoption du mécanisme "Trusted Publishing" pour [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
- Renforcement de la sécurité des déploiements dans [cartographie](/repos/anct-cartographie-nationale/cartographie) par la suppression des jetons npm statiques et l'amélioration de l'authentification pour les services cloud.

## Autres changements notables
- **Évolutions architecturales majeures :** Refonte de l'architecture de [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour la gestion des fonctionnalités et changement majeur (breaking change) dans le processus de déduplication de [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
- **Optimisation de la CI/CD :** Modernisation des chaînes de développement (passage à Biome), amélioration de la détection automatique des changements majeurs dans [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) et optimisation des workflows de release dans [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la précision des données et modernisation de l'interface de ligne de commande.
- [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) : Travaux intensifs sur la logique de déduplication et la robustesse de la bibliothèque.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Mise en conformité d'accessibilité et optimisation des infrastructures de déploiement.

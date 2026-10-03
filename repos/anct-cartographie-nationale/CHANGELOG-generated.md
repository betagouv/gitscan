# Synthèse d'activité : anct-cartographie-nationale (du 10/09 au 19/09/2026)

## Résumé de l'activité
L'activité de cette période est principalement portée par un effort de fiabilisation des données et de mise en conformité. L'organisation a concentré ses développements sur l'amélioration de la qualité des informations géographiques et de médiation, notamment grâce à l'implémentation de nouveaux mécanismes de déduplication et de filtrage des données.

Ces évolutions permettent d'offrir des données plus précises et mieux structurées pour les utilisateurs finaux. Parallèlement, un volet important a été consacré à l'accessibilité numérique et à la sécurisation des processus de déploiement automatique, garantissant ainsi des outils plus robustes et conformes aux standards actuels. Ces changements impactent l'ensemble de l'écosystème, de la ligne de commande [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) à la plateforme de visualisation [cartographie](/repos/anct-cartographie-nationale/cartographie), en passant par la bibliothèque [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).

## Sécurité
- **Sécurisation des publications :** Adoption du mécanisme "trusted publishing" pour sécuriser la distribution des paquets sur npm pour [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) et [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
- **Gestion des secrets et accès :** Suppression des jetons npm statiques dans les workflows de release et amélioration de l'authentification pour les services d'infrastructure (Pulumi Scaleway) sur [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Autres changements notables
- **Amélioration de la qualité des données :** Mise en place de règles de déduplication et de gestion des doublons, incluant un changement majeur (breaking change) dans la logique de traitement pour [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique).
- **Évolutions architecturales :** Refonte de l'architecture de [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour une meilleure gestion des fonctionnalités et optimisation de l'injection de dépendances sur [cartographie](/repos/anct-cartographie-nationale/cartographie).
- **Modernisation de la CI/CD :** Optimisation des workflows de déploiement, mise à jour des environnements (Node.js, GitHub Actions) et adoption de nouveaux standards de développement (Biome) pour [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) et [cartographie](/repos/anct-cartographie-nationale/cartographie).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Renforcement de la précision des données et modernisation de la chaîne de développement.
- [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) : Travaux importants sur la déduplication des lieux et la sécurisation des publications.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Mise en conformité d'accessibilité et optimisation de l'infrastructure de déploiement.

# Synthèse d'activité : anct-cartographie-nationale (du 28/08 au 19/09)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la qualité des données et la mise en conformité réglementaire. Les efforts ont porté sur la précision des informations géographiques et d'accessibilité, notamment grâce à l'implémentation de nouveaux mécanismes de déduplication pour réduire les doublons et à l'enrichissement des données liées à l'accessibilité. Ces évolutions garantissent des outils plus fiables et plus inclusifs pour les utilisateurs finaux ([mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique), [cartographie](/repos/anct-cartographie-nationale/cartographie)).

## Sécurité
- Sécurisation de la chaîne de distribution logicielle via l'adoption du mécanisme "Trusted Publishing" pour la publication des paquets ([mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique)).
- Renforcement de la sécurité des déploiements par la suppression des jetons statiques et l'amélioration de l'authentification des plugins d'infrastructure ([cartographie](/repos/anct-cartographie-nationale/cartographie)).

## Autres changements notables
- **Évolutions architecturales et changements majeurs :** Refonte du processus de déduplication des lieux entraînant un changement majeur (breaking change) pour les utilisateurs de la bibliothèque ([lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique)) et restructuration de l'architecture de l'outil CLI pour une meilleure gestion des fonctionnalités ([mednum-cli](/repos/anct-cartographie-nationale/mednum-cli)).
- **Modernisation technique et CI/CD :** Optimisation des workflows de release, mise à jour des environnements d'exécution (Node.js) et adoption de nouveaux standards de développement comme Biome ([mednum-cli](/repos/anct-cartographie-nationale/mednum-cli), [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique), [cartographie](/repos/anct-cartographie-nationale/cartographie)).

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la précision des données et modernisation de l'interface de ligne de commande.
- [lieux-de-mediation-numerique](/repos/anct-cartographie-nationale/lieux-de-mediation-numerique) : Travaux importants sur la logique de déduplication et refonte structurelle.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Mise en conformité d'accessibilité et sécurisation des processus de déploiement.

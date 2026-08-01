# Synthèse d'activité : etalab (du 27 avril 2026 au 27 juillet 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et données liés au transport, aux aides sociales et à l'administration publique.  Des efforts significatifs ont été déployés pour améliorer la qualité des données IRVE et des lieux de covoiturage, ainsi que pour l'intégration de nouveaux opérateurs de vélos en libre-service. Le projet *data_pass* a connu des avancées notables avec l'ajout de nouveaux éditeurs et l'amélioration de la gestion des autorisations. Plusieurs dépôts ont bénéficié de mises à jour de sécurité et de corrections de bugs, renforçant la stabilité et la fiabilité des services proposés.

## Sécurité
- Mise en place d'un scanner de vulnérabilités et upgrades de librairies dans [transport-site](/repos/etalab/transport-site).
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.

## Autres changements notables
- Refactorisation de la consolidation IRVE dans [transport-site](/repos/etalab/transport-site) pour simplifier le traitement des données.
- Passage à l'allocateur mémoire `jemalloc` dans [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire.
- Introduction d'un système de Feature Flags centralisé dans [data_pass](/repos/etalab/data_pass).
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Consolidation et validation des données IRVE, ajout de nouveaux opérateurs de vélos en libre-service et améliorations de la robustesse.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mise à jour régulière de la base de données des lieux de covoiturage.
- [data_pass](/repos/etalab/data_pass) : Ajout de nouveaux éditeurs, amélioration de la gestion des autorisations et introduction de Feature Flags.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles API et amélioration de la gestion des endpoints.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 du profil France NeTEx avec des clarifications et améliorations.

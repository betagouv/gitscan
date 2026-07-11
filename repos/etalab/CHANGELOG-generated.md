# Synthèse d'activité : etalab (du 28 avril 2026 au 08 juin 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et services liés aux données de transport, aux normes, au covoiturage et à l'administration publique. Plusieurs dépôts ont bénéficié de corrections de bugs, d'optimisations de performances et d'ajouts de nouvelles fonctionnalités, notamment concernant l'import de données IRVE, la gestion des lieux de covoiturage et l'API Data Pass. L'accent a également été mis sur la sécurité, avec des mises à jour de dépendances et des améliorations de la gestion des clés API. Les mises à jour du profil France NeTEx et du schéma dispositif d'aide visent à améliorer l'interopérabilité et la flexibilité des données.

## Sécurité
- Correction de bugs liés à la suppression de fichiers sur S3 dans [flask-storage](/repos/etalab/flask-storage) pour éviter des suppressions accidentelles.
- Rotation annuelle du token webhook dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour renforcer la sécurité.
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion des accès.

## Autres changements notables
- Passage à l'allocateur mémoire `jemalloc` dans [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire en production.
- Suppression du code lié à TimescaleDB dans [transport-site](/repos/etalab/transport-site) suite à sa décommission.
- Ajout de l'architecture des "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour permettre des extensions de schéma plus flexibles.
- Migration du scope TVA de VIES vers la DGFIP dans [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Amélioration de l'import et de la consolidation des données IRVE, ajout de nouveaux opérateurs de vélos en libre-service et corrections de bugs.
- [data_pass](/repos/etalab/data_pass) : Amélioration de la recherche d'utilisateurs, de la gestion des droits, ajout de nouvelles APIs et amélioration de la gestion de session.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs, amélioration de la gestion des tokens et des performances.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation de la consommation mémoire en production.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Correction d'un bug de sélection des collectivités et mise à jour des dépendances.

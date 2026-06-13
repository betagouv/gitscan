# Synthèse d'activité : etalab (du 27 avril 2026 au 08 juin 2026)

## Résumé de l'activité
L'activité récente d'etalab s'est concentrée sur l'amélioration et la maintenance de ses outils et données liés au transport, à l'aide sociale et à l'administration publique. Plusieurs dépôts ont bénéficié de mises à jour pour améliorer la performance, la sécurité et la qualité des données. On note l'ajout de nouvelles fonctionnalités sur [transport-site](/repos/etalab/transport-site) avec l'intégration de données GBFS de Yégo et l'ajout de permaliens pour la validation IRVE. Des améliorations significatives ont également été apportées à [admin_api_entreprise](/repos/etalab/admin_api_entreprise) avec l'ajout de nouvelles APIs et une meilleure gestion des tokens. Enfin, des mises à jour de documentation et de schémas de données ont été publiées pour assurer la cohérence et l'interopérabilité des systèmes.

## Sécurité
Plusieurs correctifs de sécurité ont été appliqués sur [transport-site](/repos/etalab/transport-site) pour réduire les vulnérabilités JavaScript. De plus, [admin_api_entreprise](/repos/etalab/admin_api_entreprise) a implémenté une rotation annuelle des tokens webhook pour renforcer la sécurité.

## Autres changements notables
- Migration des variables d'environnement vers la compilation sur [transport-site](/repos/etalab/transport-site) pour améliorer la sécurité et la performance.
- Passage à l'allocateur mémoire `jemalloc` par défaut sur [transport-validator](/repos/etalab/transport-validator) pour optimiser la consommation mémoire.
- Mise à jour de Ruby à la dernière version sur [data_pass](/repos/etalab/data_pass).
- Refactorisation pour utiliser `params.expect` sur [data_pass](/repos/etalab/data_pass) améliorant la sécurité et la lisibilité.
- Ajout de la prise en charge des extensions de schéma via l'architecture des "data packages" sur [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Amélioration de la gestion des données IRVE, corrections de sécurité et optimisations de l'infrastructure.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et de la sécurité.
- [transport-validator](/repos/etalab/transport-validator) : Optimisation de la performance et de la consommation mémoire.
- [data_pass](/repos/etalab/data_pass) : Amélioration des emails FranceConnect et ajout de formulaires pré-remplis.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Mise à jour régulière de la base de données des lieux de covoiturage.

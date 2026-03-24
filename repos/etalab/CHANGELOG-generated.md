# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des avancées significatives sur plusieurs fronts. L'organisation a continué à enrichir ses APIs avec de nouvelles fonctionnalités, notamment dans le domaine de l'administration publique (API CNOUS, MSA, MEN) via [admin_api_entreprise](/repos/etalab/admin_api_entreprise).  Des améliorations importantes ont été apportées à la plateforme Data Pass [data_pass](/repos/etalab/data_pass) avec l'intégration de nouvelles APIs et une interface d'administration pour les habilitations. Le domaine du transport a également été actif, avec des mises à jour des données de covoiturage [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) et une nouvelle version du profil NeTEx [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) pour faciliter l'échange de données. Enfin, des améliorations de recherche et de validation ont été apportées à la plateforme transport [transport-site](/repos/etalab/transport-site).

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- Migration des scopes des tokens vers les demandes d'autorisation dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) pour une meilleure gestion.
- Mise à jour de Postgres et TimescaleDB dans l'environnement CI de [transport-site](/repos/etalab/transport-site).
- Prise en charge de la nouvelle version de la norme NeTEx v2.4.0 sur [transport-normes-site](/repos/etalab/transport-normes-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et des performances.
- [data_pass](/repos/etalab/data_pass) : Intégration de nouvelles APIs et ajout d'une interface d'administration pour les habilitations.
- [transport-site](/repos/etalab/transport-site) : Amélioration significative de la recherche de données et ajout de rapports de validation NeTEx.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication d'une nouvelle version (v2.4.0) du profil France NeTEx avec des clarifications et des améliorations.
- [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage) : Enrichissement de la base de données avec de nouveaux lieux de covoiturage.

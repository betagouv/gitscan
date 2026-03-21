# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des améliorations significatives sur plusieurs fronts. L'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a été enrichie de nouvelles fonctionnalités et a bénéficié d'améliorations de sécurité et de performance.  Le site [transport-site](/repos/etalab/transport-site) a vu une refonte de sa recherche de données et l'ajout de rapports de validation NeTEx, améliorant l'expérience utilisateur pour les professionnels du transport.  Plusieurs dépôts ont également bénéficié de mises à jour de documentation et de corrections mineures, contribuant à la stabilité et à la qualité globale des services proposés.

## Sécurité
- Rotation annuelle du token webhook pour renforcer la sécurité de l'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)).

## Autres changements notables
- Migration des scopes des tokens vers les demandes d'autorisation dans l'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)).
- Mise à jour de Postgres (14 -> 18) et TimescaleDB dans l'environnement CI pour le dépôt [transport-site](/repos/etalab/transport-site).
- Prise en charge de la nouvelle version de la norme NeTEx v2.4.0 sur [transport-normes-site](/repos/etalab/transport-normes-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles APIs et amélioration de la gestion des tokens et des performances.
- [transport-site](/repos/etalab/transport-site) : Refonte de la recherche de données et ajout de rapports de validation NeTEx.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 du profil France NeTEx avec des clarifications et améliorations.
- [data_pass](/repos/etalab/data_pass) : Intégration de nouvelles APIs et ajout d'une interface d'administration pour les habilitations.

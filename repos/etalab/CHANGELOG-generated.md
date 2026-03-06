# Synthèse d'activité : etalab (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des améliorations significatives sur plusieurs fronts chez etalab. L'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)) a été enrichie avec de nouvelles intégrations d'API (CNOUS, CNAV/PSU) et des fonctionnalités d'administration des tokens et de visualisation des requêtes.  Le Data Pass ([data_pass](/repos/etalab/data_pass)) a vu des améliorations de l'expérience utilisateur avec la gestion des habilitations et l'ajout de pages légales, ainsi que des optimisations techniques.  Des efforts importants ont également été déployés pour améliorer la qualité et la normalisation des données de transport, notamment via le profil NeTEx ([transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr)) et le site transport ([transport-site](/repos/etalab/transport-site)).

## Sécurité
Des contrôles d'accès renforcés ont été implémentés dans l'API d'administration ([admin_api_entreprise](/repos/etalab/admin_api_entreprise)).

## Autres changements notables
- Refactorisation de la gestion des requêtes API avec un pattern facade dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).
- Remplacement du dashboard Metabase par un dashboard natif dans [data_pass](/repos/etalab/data_pass).
- Restructuration des fichiers et publication de la version 2.4.0 du profil France NeTEx dans [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr).
- Amélioration significative du support NeTEx sur le site transport ([transport-site](/repos/etalab/transport-site)).
- Désactivation du log de requêtes dans le plug TokenAuth pour améliorer la performance et la sécurité dans [transport-site](/repos/etalab/transport-site).

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Ajout de nouvelles intégrations d'API et amélioration de la sécurité et de l'administration.
- [data_pass](/repos/etalab/data_pass) : Amélioration de l'expérience utilisateur et optimisations techniques.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Préparation et publication de la nouvelle version du profil NeTEx France.
- [transport-site](/repos/etalab/transport-site) : Amélioration du support NeTEx et de la consolidation IRVE.

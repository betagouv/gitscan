# Synthèse d'activité : etalab (du [Date de début] au [Date de fin])

## Résumé de l'activité
L'activité de la période est marquée par un enrichissement significatif des données de mobilité et de services publics, notamment avec l'ajout de nouveaux parcours et données dans [data_pass](/repos/etalab/data_pass) et l'actualisation de la base [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage). Parallèlement, l'organisation renforce la flexibilité de ses standards de données, comme l'illustre la nouvelle architecture d'extension dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) et la mise à jour majeure du profil [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr).

Enfin, une attention particulière est portée à l'expérience utilisateur et à la robustesse des outils d'administration, avec une refonte majeure de l'interface de [transport-site](/repos/etalab/transport-site) et l'intégration de nouvelles API et fonctionnalités de gestion dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Sécurité
- Renforcement de la sécurité dans [data_pass](/repos/etalab/data_pass) via la validation des cookies et des adresses IP.
- Mise en place de la rotation annuelle des tokens pour les webhooks dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise).

## Autres changements notables
- **Optimisation des performances** : Amélioration de la gestion mémoire pour [transport-validator](/repos/etalab/transport-validator) via l'adoption de `jemalloc`.
- **Modernisation technique** : Mise à jour de la stack de [transport-site](/repos/etalab/transport-site) (Elixir) et préparation de la migration vers Phoenix.
- **Résilience système** : Amélioration de la robustesse de la synchronisation INSEE dans [data_pass](/repos/etalab/data_pass) grâce à l'implémentation d'un *circuit breaker* et d'une file d'attente.
- **Évolutivité des schémas** : Introduction de l'architecture "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide) pour permettre l'extension des schémas sans modifier le socle de base.

## Dépôts les plus actifs
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Intégration de nouvelles API, gestion des accès et améliorations de l'interface d'administration.
- [data_pass](/repos/etalab/data_pass) : Évolutions fonctionnelles majeures, renforcement de la sécurité et de la résilience technique.
- [transport-site](/repos/etalab/transport-site) : Refonte de l'interface utilisateur (Backoffice) et modernisation de la stack technique.
- [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr) : Publication de la version 2.4.0 apportant des clarifications structurelles et fonctionnelles.

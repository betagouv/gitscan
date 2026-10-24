# Synthèse d'activité : etalab (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par des évolutions majeures dans la gestion des données de transport et des services publics. Les outils liés à la mobilité bénéficient de gains de performance et de fiabilité importants, notamment grâce à la mise à jour de l'infrastructure de [transport-site](/repos/etalab/transport-site) et à la publication de la nouvelle version du profil France dans [transport-profil-netex-fr](/repos/etalab/transport-profil-netex-fr).

Parallèlement, les services de données administratives progressent avec l'extension des fonctionnalités de [data_pass](/repos/etalab/data_pass) et l'amélioration de la gestion des accès dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise). Ces développements visent à offrir des outils plus robustes, plus extensibles et plus sécurisés pour les utilisateurs et les partenaires.

## Sécurité
- **Protection des données et accès** : Amélioration de la confidentialité dans [formulaire-qf](/repos/etalab/formulaire-qf) en limitant l'envoi d'identifiants usagers vers les outils de suivi d'erreurs.
- **Renforcement des contrôles** : Sécurisation de [data_pass](/repos/etalab/data_pass) via la validation des cookies et des adresses IP, et mise en place d'un workflow de production imposant une validation en environnement de "bac à sable".
- **Gestion des identités** : Évolution de la gestion des tokens dans [admin_api_entreprise](/repos/etalab/admin_api_entreprise) avec la rotation annuelle des tokens webhook et la migration des scopes vers des demandes d'autorisation.

## Autres changements notables
- **Modernisation des infrastructures et performances** : 
    - Migration majeure vers Elixir et Phoenix pour [transport-site](/repos/etalab/transport-site).
    - Optimisation de la consommation mémoire pour [transport-validator](/repos/etalab/transport-validator) via l'adoption de `jemalloc`.
    - Refonte de la synchronisation des données INSEE dans [data_pass](/repos/etalab/data_pass) pour améliorer la résilience du système.
- **Évolutions des architectures de données** : 
    - Introduction d'une architecture de "data packages" dans [schema-dispositif-aide](/repos/etalab/schema-dispositif-aide), permettant d'étendre les schémas de données de manière flexible.
    - Mise à jour des schémas pour [lieux-covoiturage](/repos/etalab/lieux-covoiturage) et enrichissement des données de [transport-base-nationale-covoiturage](/repos/etalab/transport-base-nationale-covoiturage).
- **Améliorations de l'expérience utilisateur** : Optimisation de l'ergonomie du Backoffice de [transport-site](/repos/etalab/transport-site) et simplification du parcours API pour les entreprises dans [data_pass](/repos/etalab/data_pass).

## Dépôts les plus actifs
- [transport-site](/repos/etalab/transport-site) : Mise à jour majeure de l'infrastructure technique, amélioration de l'interface de gestion et renforcement de la fiabilité des données.
- [data_pass](/repos/etalab/data_pass) : Extension des fonctionnalités métier, refonte de la synchronisation de données et renforcement de la sécurité.
- [admin_api_entreprise](/repos/etalab/admin_api_entreprise) : Nouvelles intégrations d'API tierces et évolution de la gestion des tokens et de l'interface.
- [formulaire-qf](/repos/etalab/formulaire-qf) : Travaux importants sur la protection des données, la fiabilité des tests (CI/CD) et l'environnement de développement.

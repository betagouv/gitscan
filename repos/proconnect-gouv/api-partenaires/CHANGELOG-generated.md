## Changelog : api-partenaires (30 derniers jours, au 02/10/2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité et de la validation des domaines, notamment grâce à l'automatisation des contrôles via l'annuaire de la DILA. Nous avons également amélioré la fiabilité de la gestion des collaborateurs et optimisé le processus de déploiement pour plus de régularité.

### Évolutions fonctionnelles
- **Renforcement de la validation des domaines** :
    - Interdiction d'attacher un domaine déjà utilisé par un autre fournisseur [#87](https://github.com/proconnect-gouv/api-partenaires/pull/87).
    - Blocage des domaines génériques (type boîte mail) et des domaines figurant sur une liste d'exclusion (incluant les domaines parents) [#84](https://github.com/proconnect-gouv/api-partenaires/pull/84).
    - Amélioration de la validation des domaines attestés par la DILA pour garantir leur conformité avec l'annuaire administratif [#64](https://github.com/proconnect-gouv/api-partenaires/pull/64).
- **Sécurité des accès** : Suppression des permissions de type "roles" des scopes par défaut pour limiter les droits par défaut [#e5e875b](https://github.com/proconnect-gouv/api-partenaires/commit/e5e875b).
- **Corrections de bugs** : Résolution d'un problème entraînant la suppression incorrecte de collaborateurs lors de mises à jour partielles [#77](https://github.com/proconnect-gouv/api-partenaires/pull/77).

### Évolutions techniques
- **Automatisation et CI/CD** :
    - Mise en place d'un processus de release automatisé avec `release-it` et un versionnage de type CalVer [#85](https://github.com/proconnect-gouv/api-partenaires/pull/85).
    - Intégration de contrôles automatiques de la configuration et de la liste d'autorisation (allowlist) directement dans le pipeline CI [#53](https://github.com/proconnect-gouv/api-partenaires/pull/53), [#58](https://github.com/proconnect-gouv/api-partenaires/pull/58).
- **Gestion des données et infrastructure** :
    - Automatisation de la récupération et de la mise en cache quotidienne de l'annuaire administratif de la DILA pour assurer la fraîcheur des données [#59](https://github.com/proconnect-gouv/api-partenaires/pull/59), [#62](https://github.com/proconnect-gouv/api-partenaires/pull/62).
    - Amélioration de la traçabilité en enregistrant la source d'attestation pour chaque domaine autorisé [#56](https://github.com/proconnect-gouv/api-partenaires/pull/56).
- **Observabilité et expérience développeur** :
    - Amélioration de la lisibilité des erreurs de configuration, désormais affichées de manière concise par problème rencontré [#81](https://github.com/proconnect-gouv/api-partenaires/pull/81).
    - Ajout de logs pour suivre l'état du cache lors de la récupération des données DILA.

### Autres changements
- **Documentation** : Ajout d'un guide de contribution détaillant le processus de release [#86](https://github.com/proconnect-gouv/api-partenaires/pull/86).
- **Nettoyage** : Suppression des fichiers README d'exemples par scénario pour alléger le dépôt [#91](https://github.com/proconnect-gouv/api-partenaires/pull/91).

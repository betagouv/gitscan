## Changelog : api-partenaires (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la fiabilité de la validation des domaines. L'intégration massive des données de la DILA et l'alignement sur les standards de l'INSEE permettent une gestion plus rigoureuse des domaines autorisés, tout en offrant une meilleure visibilité aux utilisateurs sur les raisons d'acceptation ou de refus de leurs demandes.

### Évolutions fonctionnelles
- **Amélioration de la validation des domaines** :
    - Refus des domaines déjà détenus par un autre fournisseur [#87](https://github.com/proconnect-gouv/api-partenaires/pull/87).
    - Refus des domaines de messagerie génériques (ex: gmail.com) [#57](https://github.com/proconnect-gouv/api-partenaires/pull/57).
    - Refus des domaines figurant sur la liste d'exclusion (domaines parents, domaines gratuits) [#84](https://github.com/proconnect-gouv/api-partenaires/pull/84).
- **Expérience utilisateur et clarté** :
    - Ajout d'explications détaillées sur les raisons pour lesquelles un domaine est accepté ou refusé [#128](https://github.com/proconnect-gouv/api-partenaires/pull/128).
- **Intégrité des données** :
    - Vérification de la conformité des noms de communes avec l'orthographe officielle du COG (INSEE) [#125](https://github.com/proconnect-gouv/api-partenaires/pull/125).
    - Refus des lignes DILA ne comportant pas le nom de leur collectivité [#127](https://github.com/proconnect-gouv/api-partenaires/pull/127).
- **Extension de la base de confiance** :
    - Importation massive de nouveaux domaines attestés par la DILA [#42](https://github.com/proconnect-gouv/api-partenaires/pull/42).

### Évolutions techniques
- **Automatisation et intégration DILA** :
    - Mise en place de la récupération et de la mise en cache quotidienne de l'annuaire administratif de la DILA [#62](https://github.com/proconnect-gouv/api-partenaires/pull/62) [#59](https://github.com/proconnect-gouv/api-partenaires/pull/59).
    - Liaison systématique des domaines de la liste d'autorisation à leurs fiches DILA respectives [#69](https://github.com/proconnect-gouv/api-partenaires/pull/69) [#70](https://github.com/proconnect-gouv/api-partenaires/pull/70).
- **Robustesse et CI/CD** :
    - Amélioration de la lisibilité des erreurs de configuration dans la CI [#81](https://github.com/proconnect-gouv/api-partenaires/pull/81).
    - Ajout de statistiques de monitoring pour le linting (`lint:apotropaic`) [#121](https://github.com/proconnect-gouv/api-partenaires/pull/121).
    - Optimisation des validateurs de domaines (reconstruction de ports et de racines de noms) [#124](https://github.com/proconnect-gouv/api-partenaires/pull/124) [#123](https://github.com/proconnect-gouv/api-partenaires/pull/123).
- **Sécurité** :
    - Suppression des scopes de rôles des scopes par défaut pour renforcer le principe de moindre privilège [e5e875b](https://github.com/proconnect-gouv/api-partenaires/commit/e5e875b).
- **Corrections** :
    - Correction d'un bug lors des mises à jour partielles pour préserver les collaborateurs [0ad9578](https://github.com/proconnect-gouv/api-partenaires/commit/0ad9578).

### Autres changements
- **Processus de release** :
    - Adoption du versionnage CalVer via `release-it` [#85](https://github.com/proconnect-gouv/api-partenaires/pull/85).
    - Ajout d'un guide de contribution documentant le processus de release [#86](https://github.com/proconnect-gouv/api-partenaires/pull/86).
- **Nettoyage** :
    - Suppression des fichiers README d'exemples par scénario [#91](https://github.com/proconnect-gouv/api-partenaires/pull/91).

## Changelog : api-partenaires (30 derniers jours, au 16/11/2026)

### Résumé
Ce mois-ci, l'activité a principalement porté sur la maintenance de l'allowlist (retrait de domaines de messagerie que l'annuaire DILA n'atteste plus), une refonte structurelle du code pour améliorer sa maintenabilité, et le renforcement de la robustesse de l'API face aux erreurs de données ou de réseau.

### Évolutions fonctionnelles
- **Maintenance de l'allowlist** : Retrait de plusieurs domaines de messagerie qui ne sont plus attestés par la DILA ([#231](https://github.com/proconnect-gouv/api-partenaires/issues/231), [#247](https://github.com/proconnect-gouv/api-partenaires/issues/247), [#250](https://github.com/proconnect-gouv/api-partenaires/issues/250)).
- **Gestion des fournisseurs** : Mise à jour de l'identifiant (re-key) du fournisseur ANCT d'Auvergne-Rhône-Alpes ([#246](https://github.com/proconnect-gouv/api-partenaires/issues/246)).
- **Gestion des domaines et clients** : 
    - Possibilité d'attacher ou de détacher un domaine de messagerie individuellement ([#191](https://github.com/proconnect-gouv/api-partenaires/issues/191)).
    - Activation de l'option `isXdaEnabled` lors de la création de clients OIDC ([#202](https://github.com/proconnect-gouv/api-partenaires/issues/202)).

### Évolutions techniques
- **Refactoring de l'architecture** : 
    - Réorganisation du code source par domaine ([#218](https://github.com/proconnect-gouv/api-partenaires/issues/218)).
    - Restructuration des routeurs : renommage des route factories ([#193](https://github.com/proconnect-gouv/api-partenaires/issues/193)) et séparation du routeur des fournisseurs OIDC en fichiers de ressources et noyau d'admission ([#192](https://github.com/proconnect-gouv/api-partenaires/issues/192)).
- **Robustesse et gestion d'erreurs** : 
    - Amélioration de la résilience face aux domaines DILA malformés pour éviter les plantages lors du linting ([#225](https://github.com/proconnect-gouv/api-partenaires/issues/225)).
    - Distinction précise des erreurs lors des échecs de résolution DNS ([#209](https://github.com/proconnect-gouv/api-partenaires/issues/209)).
    - Meilleure gestion des fournisseurs ne possédant aucun domaine de messagerie rattaché ([#196](https://github.com/proconnect-gouv/api-partenaires/issues/196)).
- **Sécurité et Schémas** : 
    - Renforcement du schéma des domaines en liant les labels et les noms ([#195](https://github.com/proconnect-gouv/api-partenaires/issues/195)).
    - Validation stricte de la configuration `MAX_TIMESTAMP_DIFF` au démarrage de l'application ([#194](https://github.com/proconnect-gouv/api-partenaires/issues/194)).
- **Infrastructure et CI/CD** : 
    - Mise en place d'alertes en cas d'échec du cron "apotropaic" ([#224](https://github.com/proconnect-gouv/api-partenaires/issues/224)).
    - Optimisation des tests d'intégration avec l'utilisation d'un fichier compose partagé pour les exemples ([#211](https://github.com/proconnect-gouv/api-partenaires/issues/211)) et mise à jour pour la compatibilité avec MongoDB 9.0.2 ([#210](https://github.com/proconnect-gouv/api-partenaires/issues/210)).

### Autres changements
- **Formatage** : Migration de l'outil de formatage de code de Prettier vers `bun fmt` ([#245](https://github.com/proconnect-gouv/api-partenaires/issues/245)).
- **Documentation/Process** : Amélioration du digest de l'allowlist pour faciliter le travail de revue ([#190](https://github.com/proconnect-gouv/api-partenaires/issues/190)).

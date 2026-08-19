## Changelog : hubee (30 derniers jours, au 17 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du système d'authentification et de la gestion des profils utilisateurs. Ces évolutions renforcent significativement la sécurité de la plateforme (notamment via l'authentification multi-facteur) et améliorent la clarté de l'interface pour les agents de l'administration.

### Évolutions fonctionnelles
- **Renforcement de la sécurité** : Prise en charge de l'authentification multi-facteur (MFA) imposée par le fournisseur d'identité et obligation d'un second facteur pour les comptes à privilèges.
- **Gestion des sessions** : Mise en place de limites de session basées sur l'inactivité et sur une durée de vie absolue.
- **Amélioration du portail** : 
    - Refonte de l'en-tête pour intégrer l'identité de l'utilisateur et le bouton de déconnexion.
    - Amélioration de la gestion des erreurs : les messages d'échec sont désormais plus explicites et des options de recours sont proposées.
- **Gestion des agents** : Enrichissement des profils (civilité, rôle, fonction, téléphone au format international) et gestion du rattachement des agents à leurs organisations respectives.
- **Conformité** : Intégration des conditions générales d'utilisation (CGU) du DSFR.

### Évolutions techniques
- **Refonte de l'authentification** : Migration vers une implémentation native du protocole OIDC pour ProConnect (sortie de la dépendance à OmniAuth) et sécurisation du processus de découverte des services.
- **Nouvelle architecture de données** : Introduction des modèles `Agent` et `ProviderSession` pour une gestion plus fine des identités et des sessions.
- **Sécurité et traçabilité** : 
    - Chiffrement des jetons ProConnect au repos.
    - Mise en place d'un système de consignation (logs) et de décision d'accès pour assurer une traçabilité complète des accès.
- **Fiabilité et tests** : 
    - Ajout de tests de bout en bout (E2E) s'exécutant dans de véritables navigateurs.
    - Amélioration de la résilience du système face aux indisponibilités du fournisseur d'identité.
- **Correctifs de sécurité** : Résolution de vulnérabilités sur Active Storage et les bibliothèques de nettoyage HTML ([#95](https://github.com/datagouv/hubee/issues/95)).

### Autres changements
- Mise à jour de l'outil d'analyse de sécurité Brakeman ([#131](https://github.com/datagouv/hubee/issues/131)).
- Traduction des messages du framework en français.
- Nettoyage de la documentation et des fichiers de configuration.

## Changelog : messages (30 derniers jours, au 06/09/2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité de la messagerie (protocoles SPF/DKIM et serveur MTA) et l'amélioration de l'expérience utilisateur, notamment via une meilleure gestion des adresses email internationales et des optimisations sur l'application mobile.

### Évolutions fonctionnelles
- **Gestion des emails** : Prise en charge des adresses email internationalisées (i18n) et passage automatique des boîtes aux lettres en minuscules [#785](https://github.com/suitenumerique/messages/pull/785).
- **Correction de messagerie** : Résolution d'un problème de suivi de fil de discussion lorsque l'objet du message était réécrit [#765](https://github.com/suitenumerique/messages/pull/765).
- **Expérience Mobile** : Amélioration du processus de déconnexion pour garantir la fermeture complète de la session auprès du fournisseur d'identité.
- **Interface utilisateur** :
    - Optimisation de l'affichage des extraits de messages et de discussions.
    - Masquage des statistiques du dossier "Envoyés".
    - Restriction des couleurs autorisées dans l'éditeur de texte (BlockNote).

### Évolutions techniques
- **Sécurité de la messagerie** :
    - Durcissement du composant `pymta` avec de nouvelles limites et une meilleure gestion des logs [#777](https://github.com/suitenumerique/messages/pull/777), [#783](https://github.com/suitenumerique/messages/pull/783).
    - Amélioration de la fiabilité du vérificateur SPF pour couvrir davantage de cas particuliers [#782](https://github.com/suitenumerique/messages/pull/782).
    - Assouplissement de la vérification des espaces blancs pour les configurations DKIM via DNS [#778](https://github.com/suitenumerique/messages/pull/778).
- **Infrastructure et Authentification** :
    - Mise à jour et renforcement de Keycloak [#776](https://github.com/suitenumerique/messages/pull/776), [#784](https://github.com/suitenumerique/messages/pull/784).
    - Ajout d'une liste blanche d'adresses IP pour sécuriser l'accès à l'administration Django.
    - Sécurisation des workflows GitHub Actions.
- **API et Provisioning** : Ajout d'un point de terminaison permettant de lister les enregistrements DNS pour l'ensemble des domaines [#780](https://github.com/suitenumerique/messages/pull/780).
- **Mobile** : Migration de l'identité de l'application et du schéma d'authentification vers une configuration pilotée par variables d'environnement.

### Autres changements
- **Documentation** : Ajout d'un guide de configuration pour le fournisseur d'identité (Identity Provider) [#781](https://github.com/suitenumerique/messages/pull/781).
- **Interface** : Ajustements textuels sur les titres de la documentation.

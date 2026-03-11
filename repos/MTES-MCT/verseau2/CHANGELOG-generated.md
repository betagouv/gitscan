## Changelog : verseau2 (30 derniers jours)

### Résumé
Les dernières mises à jour de Verseau2 se concentrent sur l'amélioration de l'architecture, la migration vers une couche d'abstraction MASA pour les appels API, l'ajout de nouveaux contrôles et la correction de bugs liés au traitement des données et à l'authentification. Des améliorations ont également été apportées à la gestion des droits d'accès et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un accès administrateur pour les "expert national verseau" permettant le téléchargement de fichiers XML. [#18](https://github.com/MTES-MCT/verseau2/pull/18)
- Implémentation de l'envoi d'un fichier d'accusé de réception (acknowledge) après le transfert du fichier XML. [#17](https://github.com/MTES-MCT/verseau2/pull/17)
- Ajout du contrôle CBPO (054). [#19](https://github.com/MTES-MCT/verseau2/pull/19)
- Correction d'un bug où le seuil EH n'était pas calculé correctement. [#47](https://github.com/MTES-MCT/verseau2/issues/47)
- Ajout d'un composant de sélection avec auto-complétion dans l'interface utilisateur. [#72](https://github.com/MTES-MCT/verseau2/issues/72)

### Évolutions techniques
- Migration des appels de la vue Verseau vers la couche d'abstraction MASA. [#28](https://github.com/MTES-MCT/verseau2/issues/28)
- Migration des contrôles avec données live vers l'API MASA. [#57](https://github.com/MTES-MCT/verseau2/issues/57)
- Refactorisation du code pour supprimer les modules et imports non utilisés. [#26](https://github.com/MTES-MCT/verseau2/pull/26)
- Suppression du code mort de la gateway et du repository. [#68](https://github.com/MTES-MCT/verseau2/pull/68)
- Mutualisation et mise à jour des dépendances. [#66](https://github.com/MTES-MCT/verseau2/pull/66)
- Refactorisation du typage des utilisateurs authentifiés et suppression du `cerbere_token`. [#34](https://github.com/MTES-MCT/verseau2/issues/34)
- Utilisation d'une couche d'abstraction pour l'authentification et la gestion des droits. [#65](https://github.com/MTES-MCT/verseau2/issues/65)
- Mise à jour de la version majeure de Node.js. [#9e82ef5](https://github.com/MTES-MCT/verseau2/commit/9e82ef5)
- Ajout de tests E2E pour couvrir tous les contrôles V1 et V2.
- Amélioration de la gestion des erreurs et ajout de logs avec correlationId.

### Autres changements
- Ajout d'une documentation AGENTS.md adaptée à une structure mémoire de type 3 couches. [#22](https://github.com/MTES-MCT/verseau2/issues/22)
- Correction d'un bug lié à des sauts de ligne incorrects lors de l'ajout de la balise NomContact dans le parser.
- Sécurisation de `MasaApiKeyGuard`.
- Correction d'une erreur d'authentification lors du redémarrage du serveur. [#61](https://github.com/MTES-MCT/verseau2/issues/61)
- Augmentation du timeout des jobs SANDRE à 2h pour éviter les erreurs de clé dupliquée.
- Ajout de préfixes aux queues pour les environnements avec base de données partagée (recette, environnements spécifiques). [#36](https://github.com/MTES-MCT/verseau2/issues/36)
- Ajout d'un skill `MasaProvider` pour une future API.

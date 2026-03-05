## Changelog : verseau2 (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à verseau2 au cours du dernier mois. Les développements se concentrent sur l'amélioration de la sécurité, la migration vers une nouvelle architecture d'authentification, l'ajout de nouveaux contrôles et l'optimisation des performances. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'accès administrateur pour les "expert national verseau" permettant le téléchargement de fichiers XML. [#18](https://github.com/MTES-MCT/verseau2/pull/18)
- Implémentation de l'envoi d'un fichier d'accusé de réception (ACK) après le transfert du fichier XML. [#17](https://github.com/MTES-MCT/verseau2/pull/17)
- Ajout du contrôle CBPO (054). [#19](https://github.com/MTES-MCT/verseau2/pull/19)
- Ajout de tests e2e pour couvrir tous les contrôles v1 et v2.
- Correction d'un bug où le seuil EH n'était pas calculé correctement. [#36](https://github.com/MTES-MCT/verseau2/pull/36)
- Correction d'un bug lié à une erreur de clé dupliquée lors du traitement des contrôles SANDRE (timeout augmenté à 2h).
- Normalisation des adresses email reçues de Cerbere (conversion en minuscules).

### Évolutions techniques
- Migration des contrôles avec données live vers l'API MASA. [#57](https://github.com/MTES-MCT/verseau2/pull/57)
- Refonte de l'authentification et de la gestion des droits avec l'utilisation de la couche d'abstraction MASA. [#65](https://github.com/MTES-MCT/verseau2/pull/65)
- Suppression du token Cerbere et remplacement par la génération d'un token JWT pour une gestion plus fine des claims. [#34](https://github.com/MTES-MCT/verseau2/pull/34)
- Refactoring du code pour supprimer le code mort et simplifier certaines parties. [#68](https://github.com/MTES-MCT/verseau2/pull/68)
- Mutualisation et mise à jour des dépendances. [#66](https://github.com/MTES-MCT/verseau2/pull/66)
- Amélioration de la gestion des erreurs et ajout d'informations de contexte dans les logs.
- Mise à jour de la version de Node.
- Optimisation de la configuration de la pool de connexions PostgreSQL pour faciliter le scaling.
- Ajout de préfixes aux queues pour les environnements partagés (recette, environnements spécifiques).
- Amélioration du typage et de la cohérence avec la base de données.

### Autres changements
- Mise à jour de la documentation AGENTS.md pour refléter une structure en 3 couches.
- Correction d'un bug dans les tests (SftpTestMock appelé deux fois).
- Correction d'un bug lié à l'authentification après le redémarrage du serveur. [#61](https://github.com/MTES-MCT/verseau2/pull/61)
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Merge de la branche recette.

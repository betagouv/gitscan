## Changelog : verseau2 (30 derniers jours)

### Résumé
Les dernières mises à jour de Verseau2 se concentrent sur l'ajout de nouvelles fonctionnalités, notamment l'intégration de contrôles MASA, l'amélioration de la gestion des indicateurs et l'ajout d'accès administrateur pour certains utilisateurs. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un accès administrateur pour les "expert national verseau" permettant le téléchargement de fichiers XML (#18).
- Implémentation de l'envoi d'un fichier d'accusé de réception (acknowledge) après le transfert d'un fichier XML (#17).
- Ajout de l'année de référence des indicateurs dans le dashboard (#9).
- Ajout d'icônes aux contrôles Sandre dans l'interface utilisateur (#20).
- Gestion de plusieurs erreurs lors de l'analyse des fichiers Sandre.
- Ajout du contrôle CBPO (054).
- Ajout de routes pour les indicateurs et le dépôt administrateur.
- Ajout de routes pour le référentiel.
- Possibilité de créer une nouvelle table PostgreSQL pour des tests spécifiques.

### Évolutions techniques
- Sécurisation de `MasaApiKeyGuard`.
- Migration des contrôles avec données live vers l'API MASA (#21).
- Refactor de l'enveloppe MASA pour les contrôles V2.
- Amélioration des performances de la requête des indicateurs.
- Ajout d'un interceptor pour la gestion du cache.
- Utilisation du `LoggerService` et ajout d'un décorateur `TraceCalls` pour le logging.
- Passage du service logger à Transient pour résoudre un problème de scaling.
- Correction d'une race condition potentielle lors de la mise à jour d'un dépôt.
- Suppression du correlation id dans `traceCalls`.
- Simplification de la logique de nettoyage du cache dans les tests E2E.
- Correction d'une erreur de runtime.
- Correction d'une erreur de résolution qui empêchait le bon fonctionnement de l'application.
- Amélioration du typage dans le code.
- Mise à jour des dépendances vulnérables.

### Autres changements
- Ajout de documentation AGENTS.md adaptée à une structure mémoire à 3 couches.
- Ajout de tests E2E pour couvrir tous les contrôles V1 et V2.
- Correction de bugs mineurs dans l'interface utilisateur (titres, séparateurs).
- Ajout de vérification du contenu du dump avant la restauration.
- Correction d'erreurs de typage et de logique dans le parseur Sandre.
- Correction d'un problème de timeout des jobs Sandre.
- Ajout d'infos dans les logs.
- Correction d'un test qui échouait depuis le passage à Transient.
- Correction d'une erreur sur le retour du parseur Sandre.
- Correction d'un bug lié à la gestion des emails reçus de Cerbere (conversion en minuscules).
- Ajout de tests unitaires.
- Correction de problèmes de configuration et de transpilation.
- Ajout d'une librairie commune non orientée domaine.
- Correction d'un bug sur le calcul du seuil EH.
- Ajout de deux siret pour les contrôles de droits de dépôt.
- Ajout d'un préfixe aux queues pour les environnements partagés (recette, environnements spécifiques).
- Correction d'un problème de clé dupliquée dans les contrôles Sandre.
- Ajout d'un limiteur de caractères pour le correlationId.
- Correction d'un bug lié à l'appel de `execute()` dans les tests de contrôle métier V2.
- Correction d'un bug dans les tests de contrôle métier V2.
- Correction d'un bug lié à l'appel du test `SftpTestMock` deux fois.
- Ajout de tests pour l'accès administrateur.
- Correction d'un bug lié à la structure des titres dans IndicateursTable.
- Ajout de séparateurs sur la page des contrôles.
- Correction d'un problème de padding sur le conteneur principal.
- Ajout de la gestion du cache par un interceptor.
- Ajout d'un test pour le service Logger.
- Correction d'un problème de résolution qui causait une erreur au démarrage.
- Ajout d'un test pour l'activation d'un test V1.
- Ajout de tests e2e pour couvrir tous les contrôles v1.
- Ajout d'un test pour le service Logger.
- Correction d'une erreur de runtime.
- Correction d'une erreur de typage dans CTL05.
- Ajout de la gestion du cache par un interceptor.
- Ajout d'une librairie commune non orientée domaine.
- Ajout d'une librairie commune non orientée domaine.
- Correction d'un bug lié à la pagination des groupes de contrôles.

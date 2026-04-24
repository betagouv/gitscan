## Changelog : vao (30 derniers jours, au 20 avril 2026)

### Résumé
Ce changelog couvre une période d'intenses activités de développement sur VAO, principalement axées sur l'amélioration du processus de renouvellement d'agrément, avec des correctifs et des nouvelles fonctionnalités pour les étapes 1 à 4. Des améliorations ont également été apportées à la gestion des messages et des documents, ainsi qu'à l'interface utilisateur pour les agents de l'administration. Enfin, des corrections et des ajouts ont été réalisés concernant le fusager.

### Évolutions fonctionnelles
- **Renouvellement d'agrément :**
    - Correction de plusieurs étapes du processus de renouvellement d'agrément (étapes 1, 2, 3 et 4) [#1256, #1265, #1258, #1259, #1272, #1279].
    - Ajout de la gestion des activités et des fichiers lors du renouvellement [#1265].
    - Correction de la validation en brouillon lors de l'étape 2 [#1279].
    - Amélioration de la récupération des informations des représentants légaux [#1266].
- **Messagerie DREETS :**
    - Implémentation de la messagerie pour les agréments côté DREETS, incluant la gestion des messages non lus et le comptage des nouveaux messages [#1271, #1272].
- **Gestion des documents :**
    - Amélioration de l'interface pour la gestion des documents dans le back-office, notamment pour les agréments [#1249, #1269].
    - Ajout de la possibilité de supprimer les menus de renouvellement d'agrément [#1269].
- **Fusager :**
    - Ajout de nouvelles fonctionnalités et corrections concernant le fusager, notamment pour la gestion des agréments et des listes JDMA [#1237, #1245, #1248, #1263, #1266, #1268, #1270, #1273].
    - Correction d'un problème d'affichage du nombre de femmes dans le fusager [#1270].
    - Ajout d'une action pour confirmer la complétude d'un agrément [#1236].
    - Ajout de la possibilité de changer le statut d'un agrément à "À MODIFIER" [#1227].

### Évolutions techniques
- **Refactoring et TypeScript :**
    - Conversion de certaines parties du code en TypeScript pour améliorer la maintenabilité et la robustesse [#1256, #1266].
- **Tests E2E :**
    - Ajout et correction de tests E2E pour améliorer la couverture et la qualité des tests [#1234, #1235, #1244].
- **CI/CD :**
    - Mise à jour de la configuration du pre-commit pour vérifier l'absence de `console.log` dans le code [#1246].
- **Nettoyage du code :**
    - Nettoyage du code dans le répertoire `shared-ui` [#1234].

### Autres changements
- Mise à jour des dépendances et correction de problèmes liés à la configuration de l'environnement de développement.
- Amélioration de la gestion des requêtes avec des tableaux de données.
- Correction de divers bugs et améliorations de l'expérience utilisateur.

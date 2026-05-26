## Changelog : tchap-e2e-playwright (30 derniers jours, au 19 mai 2026)

### Résumé
Cette mise à jour améliore les tests automatisés de Tchap, notamment en ajoutant la possibilité de créer des utilisateurs avec un nom d'affichage et en améliorant la robustesse des tests de recherche fédérée et de déconnexion. Des ajustements techniques ont également été effectués pour organiser le code et améliorer la stabilité de l'environnement de test.

### Évolutions fonctionnelles
- Ajout de la possibilité de spécifier un nom d'affichage lors de la création d'un utilisateur, avec un scénario de test associé pour la recherche fédérée. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Correction d'un problème dans le test de déconnexion.
- Mise à jour du code de vérification dans les tests.

### Évolutions techniques
- Amélioration de la robustesse des tests en augmentant le nombre de tentatives en CI.
- Déplacement d'un module dans le dossier Synapse pour une meilleure organisation du code.
- Ajout de l'intégration int02.

### Autres changements
- Aucun changement significatif à signaler.

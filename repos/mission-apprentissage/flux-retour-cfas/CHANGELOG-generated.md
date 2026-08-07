## Changelog : flux-retour-cfas (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'automatisation des communications (WhatsApp et emails) et l'amélioration de la fiabilité des données exportées. Des optimisations techniques importantes ont également été réalisées pour stabiliser l'environnement de développement et les processus de déploiement automatique.

### Évolutions fonctionnelles
- **Automatisation des communications** : Activation de l'envoi quotidien des messages de pré-qualification via WhatsApp à 18h30 [#4647](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4647).
- **Gestion des exports** : Amélioration de la distinction des dossiers lors de l'export des collaborateurs [#4646](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4646).
- **Optimisation des emails** : Ajustement des formulations pour les notifications d'accès OFA et correction de coquilles dans les envois [#4644](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4644), [#4645](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4645).
- **Sécurité des données** : Renforcement de la vérification des numéros de téléphone côté serveur pour les collaborateurs [#4640](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4640).

### Évolutions techniques
- **Intégrations** : Évolution du système de synchronisation avec Brevo [#4643](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4643).
- **Performance et sécurité** : Implémentation d'un limiteur de débit (rate limiter) unifié pour l'application [#4617](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4617).
- **Stabilité CI/CD** : Augmentation des délais d'exécution (timeouts) des tests Vitest pour éviter les échecs lors des déploiements automatiques [#4651](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4651).
- **Standardisation de l'environnement** : Unification des versions de Node.js et Yarn sur l'ensemble du projet pour garantir la cohérence entre les développeurs [#4648](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4648), [#4652](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4652).

### Autres changements
- **Tests** : Ajout d'une commande CLI pour l'injection de données de test (seed) spécifique à SIPA Nancy [#4654](https://github.com/mission-apprentissage/flux-retour-cfas/pull/4654).

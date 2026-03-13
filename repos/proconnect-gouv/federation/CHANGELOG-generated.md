## Changelog : federation (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a déployé une nouvelle interface utilisateur pour l'administration, améliorant l'expérience utilisateur et la réactivité. Des corrections de bugs ont également été apportées, notamment concernant la gestion des identifiants et la compatibilité avec Kubernetes. De nombreuses dépendances ont été mises à jour pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Nouvelle interface utilisateur pour l'administration, avec une mise en page en une seule colonne. [#802](https://github.com/proconnect-gouv/federation/pull/802)
- Amélioration de la réactivité de l'interface d'administration sur les différents appareils. [#868](https://github.com/proconnect-gouv/federation/pull/868)
- Correction d'un bug empêchant la connexion à l'administration après être revenu en arrière. [#898](https://github.com/proconnect-gouv/federation/pull/898)
- Correction de la sensibilité à la casse lors de la réconciliation des identifiants. [#867](https://github.com/proconnect-gouv/federation/pull/867)
- Suppression de l'affichage d'un message d'erreur obsolète concernant l'email par défaut. [#882](https://github.com/proconnect-gouv/federation/pull/882)

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Node.js, TypeScript, Docker, Express, Mongoose, Passport, bcryptjs, class-validator, amqplib, ioredis, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Amélioration de la configuration de Dependabot pour une gestion plus efficace des mises à jour de dépendances. [#975](https://github.com/proconnect-gouv/federation/pull/975)
- Ajout de tests Cypress pour la réconciliation PCI et l'exploitation en environnement Kubernetes. [#963](https://github.com/proconnect-gouv/federation/pull/963), [#924](https://github.com/proconnect-gouv/federation/pull/924), [#903](https://github.com/proconnect-gouv/federation/pull/903)
- Mise à jour de la configuration de l'environnement Kubernetes pour les tests. [#960](https://github.com/proconnect-gouv/federation/pull/960)
- Nettoyage du code et suppression de fichiers inutilisés.
- Passage au module ESNext. [#855](https://github.com/proconnect-gouv/federation/pull/855)
- Correction d'un avertissement du compilateur TypeScript. [#962](https://github.com/proconnect-gouv/federation/pull/962)

### Autres changements
- Mise à jour de la documentation de qualité. [#925](https://github.com/proconnect-gouv/federation/pull/925)
- Ajout d'une politique de sécurité et d'un moyen de signaler les vulnérabilités. [#869](https://github.com/proconnect-gouv/federation/pull/869)
- Mise à jour de la configuration ESLint. [#908](https://github.com/proconnect-gouv/federation/pull/908)
- Suppression du fichier manifest.webmanifest. [#872](https://github.com/proconnect-gouv/federation/pull/872)
- Augmentation du délai d'attente de Mongoose. [#855](https://github.com/proconnect-gouv/federation/pull/855)

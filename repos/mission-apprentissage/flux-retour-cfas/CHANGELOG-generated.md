## Changelog : flux-retour-cfas (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité de la plateforme, l'amélioration de la synchronisation avec Brevo, et l'ajout de fonctionnalités pour la gestion des collaborateurs et des données de préqualification. Des optimisations techniques ont également été apportées pour améliorer les performances en CI et unifier l'environnement de développement.

### Évolutions fonctionnelles
- Amélioration de la distinction des dossiers pour l'export des collaborateurs. [#4646](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4646)
- Activation d'une tâche planifiée quotidienne pour l'envoi de messages WhatsApp de préqualification à 18h30. [#4647](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4647)
- Modification de la formulation dans l'email d'accès accordé pour les OFA (Organismes de Formation). [#4644](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4644)
- Renforcement de la vérification du numéro de téléphone des collaborateurs côté serveur. [#4640](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4640)
- Evolution de la synchronisation avec Brevo. [#4643](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4643)
- Correction d'une faute de frappe dans un email. [#4645](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4645)

### Évolutions techniques
- Augmentation des délais d'attente (timeouts) pour les tests Vitest en CI afin d'améliorer la stabilité des builds. [#4651](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4651)
- Ajout d'un limiteur de débit unifié pour l'API. [#4617](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4617)
- Unification de la version de Node.js utilisée dans l'application. [#4648](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4648)
- Unification de la version de Yarn utilisée en local. [#4652](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4652)

### Autres changements
- Ajout de données de test pour Sipa Nancy via une tâche CLI. [#4654](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4654)

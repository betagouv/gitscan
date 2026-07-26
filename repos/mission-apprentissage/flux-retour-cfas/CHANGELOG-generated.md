## Changelog : flux-retour-cfas (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations à la synchronisation avec Brevo, des corrections de bugs sur l'outil de suivi des jeunes en rupture, et des ajustements pour l'export des dossiers de collaboration. Des améliorations ont également été apportées à l'envoi d'emails et à la gestion des timeouts des tests.

### Évolutions fonctionnelles
- Ajout d'un filtre par ville à la liste des jeunes en rupture côté Machine Learning. [#4641](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4641)
- Distinction des dossiers de collaboration lors de l'export. [#4646](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4646)
- Activation d'une tâche planifiée quotidienne pour l'envoi de messages WhatsApp de préqualification à 18h30. [#4647](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4647)
- Amélioration de la formulation dans l'email de confirmation d'accès OFA. [#4644](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4644)
- Corrections d'alignement du bandeau "Souhaite un RDV" et de la liste dans la vue Machine Learning. [#4642](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4642)
- Corrections de l'outil v3. [#4639](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4639)
- Renforcement de la vérification du numéro de téléphone des collaborateurs côté backend. [#4640](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4640)

### Évolutions techniques
- Evolution de la synchronisation avec Brevo. [#4643](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4643)
- Ajout d'un limiteur de débit unifié. [#4617](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4617)
- Augmentation des timeouts des tests Vitest en CI pour résoudre des problèmes de lenteur. [#4651](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4651)
- Unification de la version de Yarn en local et utilisation d'une version unifiée de Node.js dans toute l'application. [#4652](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4652) et [#4648](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4648)

### Autres changements
- Correction d'une faute de frappe dans un email. [#4645](https://github.com/mission-apprentissage/flux-retour-cfas/issues/4645)

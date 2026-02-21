## Changelog : nosgestesclimat-server (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au serveur de l'application nosgestesclimat.fr au cours des 30 derniers jours. Les changements incluent des corrections de bugs, des améliorations de la gestion des newsletters et des ajustements de l'infrastructure pour une meilleure stabilité et performance. Une nouvelle version majeure (v3.0.0) a été publiée avec des corrections importantes.

### Évolutions fonctionnelles
- Correction d'un bug concernant l'affichage des "fun facts" (#451).
- Correction d'un problème empêchant le calcul correct des statistiques des sondages (#448).
- Correction d'un bug dans le processus d'inscription à la newsletter, notamment lors de la validation (#447).
- Correction d'un bug où les situations n'étaient pas identiques lors de la requête par email au lieu de l'ID utilisateur (#444).

### Évolutions techniques
- La configuration du nom du cookie JWT est désormais possible via une variable d'environnement (#454).
- Mise à jour du modèle Prisma vers la version 4.9.0 (#450).
- Refactorisation du flux d'inscription à la newsletter pour améliorer sa robustesse (#447).
- Suppression des colonnes `Simulation.savedViaEmail` et `VerificationCode.userId` de la base de données (#437).
- Utilisation des buildpacks de johangirod pour améliorer le processus de construction (#498e22).
- Correction d'un problème de cookie sur l'environnement de préproduction (#49e2333, #30e2333).
- Correction d'un problème de domaine de cookie pour Safari (webkit) (#4ca8503).

### Autres changements
- Publication des versions v3.0.0 (#449, #b61c549), v3.0.1 et v2.16.4 (#445, #7367a08).
- Intégration des branches `origin/main` vers `preprod` (#1db8bec, #bb8c734, #e74e67b).

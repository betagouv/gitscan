## Changelog : nosgestesclimat-server (30 derniers jours)

### Résumé
Ce changelog résume les améliorations et corrections apportées au serveur nosgestesclimat.fr au cours des 30 derniers jours. Les modifications incluent des corrections de bugs concernant les statistiques des sondages, l'inscription à la newsletter, la gestion des cookies et des améliorations de la gestion des données utilisateurs. Plusieurs versions ont été publiées pour corriger rapidement des problèmes et améliorer la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le calcul correct des statistiques des sondages (#448).
- Correction d'un problème de validation lors de l'inscription à la newsletter (#449).
- Correction d'un bug où les situations n'étaient pas les mêmes lors de la requête par email ou par ID utilisateur (#444).
- Correction d'un bug lié aux cookies sur Safari (webkit) (#439).
- Suppression des colonnes `Simulation.savedViaEmail` et `VerificationCode.userId` de la base de données, simplifiant ainsi la structure des données (#437).
- Correction d'un bug lié aux funfacts (#451).

### Évolutions techniques
- Refactorisation du flux d'inscription à la newsletter pour une meilleure maintenabilité (#447).
- Mise à jour du modèle Prisma vers la version 4.9.0 (#450).
- Utilisation de buildpacks `johangirod` pour la construction de l'application (#452).
- Ajout du nom de domaine aux cookies pour éviter les problèmes de cross-domain (#438).
- Changement du nom des cookies pour permettre la déconnexion de tous les utilisateurs (#440).

### Autres changements
- Publication des versions 2.16.0, 2.16.1, 2.16.2, 2.16.3, 2.16.4 et 3.0.0 avec les corrections et améliorations mentionnées ci-dessus (#435, #441, #442, #443, #445, #449).
- Plusieurs merges de la branche `main` vers `preprod` pour intégrer les changements.

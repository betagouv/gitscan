## Changelog : audiodescription (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la plateforme audiodescription au cours des 30 derniers jours. Les modifications se concentrent principalement sur la correction de bugs liés à l'accessibilité et à l'interface utilisateur, ainsi que sur quelques améliorations fonctionnelles comme la désactivation de la page d'inscription et l'automatisation de l'envoi de newsletters.

### Évolutions fonctionnelles
- Désactivation de la page d'inscription des utilisateurs. (#1018a21)
- Automatisation de l'envoi de newsletters via le mode "no interaction". (#1c51be5, #26b798f)
- Mise à jour de la crontab pour l'automatisation des tâches. (#15f41c2)

### Évolutions techniques
- Amélioration de la gestion des variables nulles pour éviter les erreurs. (#72365fc)
- Mise à jour du fichier `.gitignore` et du `makefile`. (#82b3d65)

### Autres changements
- Corrections de bugs d'affichage des listes et des pages de films. (#a158ce0, #6f702b7, #3523fdf, #83c5b09)
- Améliorations de l'accessibilité :
    - Définition de titres distincts pour les pages de résultats de recherche, incluant le numéro de page et le mot-clé. (#6edc6bf)
    - Ajout des structures de listes manquantes pour une meilleure accessibilité. (#d1d5fac, #d8e9690)
    - Amélioration du focus sur la liste des genres. (#3bf8019)
- Suppression de lignes de code inutilisées. (#f37f138)
- Correction du bouton de réinitialisation sur la page de recherche. (#4075386)

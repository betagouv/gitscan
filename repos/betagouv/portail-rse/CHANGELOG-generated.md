## Changelog : portail-rse (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la fonctionnalité d'anticipation des réglementations futures, permettant aux entreprises de simuler l'impact de changements à venir. L'interface utilisateur a également été simplifiée et affinée pour offrir une navigation plus fluide et une meilleure lisibilité.

### Évolutions fonctionnelles
- **Anticipation réglementaire** : ajout de la possibilité de tester des scénarios futurs pour visualiser leur impact sur les obligations réglementaires de l'entreprise.
- **Amélioration de l'expérience utilisateur (UX/UI)** :
    - Simplification de la navigation au sein de l'espace conseiller et du tableau de bord.
    - Optimisation de l'interface visuelle (réduction des espaces vides et retouches de navigation).
    - Amélioration de la clarté des textes (wording) concernant les fonctionnalités d'anticipation.
- **Corrections** : augmentation de la limite du nombre de champs acceptés dans les formulaires.
- **Interface** : suppression du bandeau d'anticipation pour épurer l'affichage.

### Évolutions techniques
- **Refactoring** :
    - Déplacement de fonctions vers un module commun pour une meilleure maintenance.
    - Séparation des vues du tableau de bord dans un fichier dédié.
- **Maintenance et infrastructure** :
    - Mise à jour du framework Django.
    - Mise en place de redirections pour les pages sans objet.
    - Ajout de logs pour le suivi de l'accès à la page d'anticipation.

### Autres changements
- **Documentation** : ajout de badges indiquant l'état des tests sous les titres de la documentation.

## Changelog : rdv-insertion (30 derniers jours, au 02/09/2026)

### Résumé
Les récentes évolutions améliorent la précision du suivi des participations pour France Travail et corrigent l'affichage des courriers. Des optimisations techniques ont également été réalisées pour simplifier la gestion des rôles et stabiliser la compilation des styles.

### Évolutions fonctionnelles
- Intégration d'un nouveau statut d'absence justifiée pour la gestion des participations France Travail ([#3362](https://github.com/gip-inclusion/rdv-insertion/pull/3362)).
- Harmonisation de l'espacement des noms de direction dans les courriers pour assurer une meilleure cohérence avec l'adresse de l'utilisateur ([#3369](https://github.com/gip-inclusion/rdv-insertion/pull/3369)).

### Évolutions techniques
- Refactorisation de la gestion des rôles agents via la suppression d'une colonne de base de données devenue obsolète ([#3366](https://github.com/gip-inclusion/rdv-insertion/pull/3366)).
- Résolution d'un problème de compilation CSS lié à l'encodage des fichiers Sass ([#3367](https://github.com/gip-inclusion/rdv-insertion/pull/3367)).

### Autres changements
- Correction d'une dépendance liée à la gestion des navigateurs (`browserslist`) ([#3371](https://github.com/gip-inclusion/rdv-insertion/pull/3371)).

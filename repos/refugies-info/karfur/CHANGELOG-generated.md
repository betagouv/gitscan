## Changelog : karfur (30 derniers jours, au 3 juin 2026)

### Résumé
Cette période a été marquée par des corrections de bugs importants affectant l'affichage des fiches et la sauvegarde des données, ainsi que par des améliorations de la recherche de doublons et de la gestion des erreurs. Des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage des fiches sur le site en production. [#3770](https://github.com/refugies-info/karfur/issues/3770)
- Correction d'un problème de sauvegarde automatique sur la fiche OFPRA. [#3762](https://github.com/refugies-info/karfur/issues/3762)
- Amélioration du score et du classement des doublons pour une meilleure détection. [#3754](https://github.com/refugies-info/karfur/issues/3754)
- Ajout d'un endpoint pour la détection de doublons d'agents. [#3754](https://github.com/refugies-info/karfur/issues/3754)
- Correction d'une coquille sur la page "mission". [#3746](https://github.com/refugies-info/karfur/issues/3746)
- Correction de l'affichage du badge de recherche qui se superposait à la pop-up des labels départementaux. [#3766](https://github.com/refugies-info/karfur/issues/3766)

### Évolutions techniques
- Refactorisation du code pour améliorer la gestion des valeurs nulles et éviter les erreurs.
- Correction de problèmes liés à la configuration de Jest pour les tests mobiles.
- Mise à jour des dépendances pour corriger des failles de sécurité et améliorer la stabilité.
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Correction de la normalisation du prénom pour les utilisateurs SSO.
- Suppression des participants nuls dans les migrations de données.

### Autres changements
- Ajout d'un hook GitLeaks pour la détection de secrets dans le code.
- Mise à jour de la documentation et des commentaires.
- Amélioration de la configuration de CI/CD.
- Correction de la configuration de pnpm pour la gestion des dépendances.

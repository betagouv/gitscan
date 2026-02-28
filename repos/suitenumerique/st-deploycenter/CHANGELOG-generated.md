## Changelog : st-deploycenter (30 derniers jours)

### Résumé
Ce déploiement apporte des améliorations significatives à la gestion des comptes, des organisations et des rôles au sein de la plateforme. Les opérateurs de La Suite Territoriale bénéficieront de nouvelles fonctionnalités pour l'import en masse, la suppression de comptes, et une meilleure gestion des droits d'accès aux services, notamment pour le service "Messages". Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'import en masse des rôles des comptes (#40).
- Possibilité de supprimer des comptes via l'interface utilisateur et l'API (#38).
- Affichage des services avec une priorité d'affichage inférieure à 0 dans l'interface utilisateur.
- Ajout d'une carte "Messages" et amélioration des droits d'accès associés (#36).
- Amélioration de la logique d'attribution des droits d'accès et ajout d'un résolveur étendu pour l'administration (#33).
- Ajout de l'interface utilisateur pour la gestion des comptes avec des filtres pour les organisations (#28).
- Possibilité pour l'API des comptes de gérer des requêtes POST dupliquées.
- Amélioration de la gestion des domaines pour les messages, correction du texte d'aide (#40).
- Masquage des points de terminaison RPNT pour les organisations de type "autre".

### Évolutions techniques
- Refactorisation des résolveurs de droits d'accès et amélioration de la logique d'accès aux droits (#29).
- Mise à jour des étapes des workflows GitHub Actions vers les dernières versions (#39).
- L'import DPNT est maintenant planifié à 8h du matin.
- Correction d'un test flaky lié à la génération aléatoire de données avec Faker.

### Autres changements
- Mise à jour de la terminologie dans le fichier README.
- Correction de quelques traductions dans l'interface utilisateur.
- Utilisation de `html lang=fr` pour spécifier la langue française.

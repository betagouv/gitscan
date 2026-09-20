## Changelog : portail-rse (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la simplification de l'expérience utilisateur, notamment grâce à une clarification de la terminologie des rôles et une navigation plus fluide. En parallèle, des mesures de sécurité et des mises à jour techniques ont été effectuées pour renforcer la robustesse et la maintenabilité de la plateforme.

### Évolutions fonctionnelles
- **Clarification des rôles** : Simplification de la terminologie pour une meilleure compréhension (le rôle "Propriétaire" devient "Administrateur", "Éditeur" devient "Contributeur" et "Contributeur" devient "Utilisateur").
- **Amélioration de l'interface** : 
    - Optimisation de l'affichage des statistiques.
    - Retouches sur la navigation pour une expérience plus fluide.
    - Suppression de certains bandeaux d'information pour épurer l'interface.

### Évolutions techniques
- **Sécurité** : Renforcement de la sécurité en limitant les droits d'accès lors des processus d'intégration continue.
- **Refactorisation et maintenance** :
    - Alignement de la structure du code (vues, templates et fichiers) avec la nouvelle terminologie des rôles.
    - Mise à jour du framework Django.
    - Mise à jour des noms de rôles en base de données.
- **Corrections** : Augmentation de la limite du nombre de champs acceptés dans les formulaires.

### Autres changements
- **Documentation** : Ajout de précisions concernant la procédure de déploiement de Metabase.
- **Nettoyage** : Suppression de méthodes, de fichiers et d'URLs obsolètes.

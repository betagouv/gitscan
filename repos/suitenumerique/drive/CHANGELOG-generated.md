## Changelog : drive (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités comme la synchronisation de la langue de l'interface, l'intégration de notes de version et l'amélioration de la navigation. Des corrections de bugs ont également été apportées, notamment concernant les erreurs de signature lors du téléchargement de fichiers et la configuration des cookies pour l'authentification unique. Des améliorations techniques ont été réalisées pour la gestion des accès aux fichiers et l'optimisation des performances.

### Évolutions fonctionnelles
- Ajout de la synchronisation de la langue de l'utilisateur entre le backend et le navigateur lors du chargement de la page. (#35c6c19)
- Implémentation d'un système de notes de version affichées dans l'interface, avec suivi de la version consultée par l'utilisateur. (#9bf7fa7, #ab7c53a, #6eb1813, #9161e31)
- Amélioration de la navigation avec l'affichage de la page racine dans l'arborescence de navigation (breadcrumbs). (#179e4c1)
- Filtrage des éléments récents pour n'afficher que les fichiers. (#15bff8c)
- Ajout de la possibilité de rediriger vers une page d'accueil externe. (#ada6756, #4f1defc)
- Implémentation de la connexion silencieuse (silent login) pour une expérience utilisateur plus fluide. (#7291d6c, #ecf7d74, #e3e0d41)
- Amélioration de l'interface utilisateur de l'explorateur de fichiers, notamment pour les actions sur les éléments et les modales. (#5bbf11d, #3070460, #6e8b0a9, #782804f)

### Évolutions techniques
- Ajout du support de la plateforme ARM64 pour les builds Docker. (#f43c8a4)
- Mise à jour de Playwright de 1.56.1 à 1.58.2. (#edc8d2c)
- Refactorisation de composants React pour améliorer la réutilisabilité et la maintenance. (#e3527a3, #25043bd)
- Amélioration de la gestion des accès aux fichiers avec la prise en compte des rôles hérités et l'optimisation des requêtes. (#a094dfc, #3793f00, #7b18daf, #dca39e3, #52f11e2, #f696568, #c39b93a, #8251464, #7f8befd, #db4e6af, #11265f0, #a348c70)
- Mise à jour de Pillow à la version 12.1.1. (#50e19c9)
- Mise à jour de django à la version 5.2.11. (#dc29f2f)
- Amélioration de la configuration Nginx pour les cookies Keycloak. (#ecf7d74)
- Ajout d'un mécanisme de retry pour la tâche de mirroring de fichiers. (#e2d6d4e)
- Ajout d'un admin pour gérer les tâches de mirroring. (#af6bd44)
- Amélioration de la gestion des types MIME. (#600b288, #fcbd558)
- Optimisation des requêtes pour le calcul des droits d'accès. (#8cfa413, #926396c)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités. (#7d37ec8, #2065ffb, #1a2aebd)
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs. (#1f9edce, #a2a2e7b, #d51bc75, #f606044, #03c32d5, #aa5efc3, #f395aca, #6342a9c, #5147b07)
- Suppression de code obsolète et nettoyage du code. (#abd055a, #58e88b9)
- Mise à jour des dépendances. (#9813d57, #736a30f)
- Mise à jour de la version de release à 0.13.0 (#7c7c0d7, #9b6298b)

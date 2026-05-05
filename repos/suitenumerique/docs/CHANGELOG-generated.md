## Changelog : docs (30 derniers jours, au 2026-05-04)

### Résumé
Cette version apporte des améliorations significatives à l'intégration de l'IA avec l'ajout du support du SDK Mistral, permettant d'utiliser de nouveaux modèles d'IA. Des corrections de bugs et des améliorations de sécurité ont également été implémentées, ainsi que des optimisations de performance, notamment pour la gestion du contenu et des requêtes. L'accessibilité a été améliorée avec des corrections pour les lecteurs d'écran et la structure des alertes d'erreur.

### Évolutions fonctionnelles
- Ajout du support du SDK Mistral pour l'utilisation de nouveaux modèles d'IA. [#2193](https://github.com/suitenumerique/docs/issues/2193)
- Intégration d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Ajout d'un easter egg sur la création d'emojis dans les documents. [#2155](https://github.com/suitenumerique/docs/issues/2155)
- Possibilité d'ouvrir les liens internes (interlinks) avec le bouton central de la souris ou la touche Ctrl/Cmd. [#2170](https://github.com/suitenumerique/docs/issues/2170)
- Amélioration de l'ordre des documents épinglés, triés par date de dernière modification. [#2028](https://github.com/suitenumerique/docs/issues/2028)

### Évolutions techniques
- Mise à jour de l'image Nginx vers la dernière version. [#2187](https://github.com/suitenumerique/docs/issues/2187)
- Refonte de l'architecture pour la gestion du contenu, avec des endpoints dédiés pour la mise à jour et la diffusion du contenu, incluant le streaming S3 et l'utilisation d'ETag/Last-Modified. [#2171](https://github.com/suitenumerique/docs/issues/2171)
- Mise à jour de docspec vers la version 3.0.0 et adaptation de l'API de conversion. [#2220](https://github.com/suitenumerique/docs/issues/2220)
- Amélioration de la gestion des requêtes avec l'ajout de méthodes HTTP supplémentaires pour les actions sur le contenu.
- Suppression de l'endpoint `descendants` obsolète. [#2243](https://github.com/suitenumerique/docs/issues/2243)
- Utilisation d'Uvicorn pour exécuter l'application Django en environnement de développement.
- Factorisation des tests E2E dans un workflow séparé.
- Amélioration de la gestion des erreurs 5xx avec une structure plus claire et une redirection vers une page dédiée.
- Mise à jour des dépendances : `axios`, `next`, `lxml`, `uuid`.

### Autres changements
- Corrections de bugs et améliorations de l'accessibilité pour les lecteurs d'écran.
- Amélioration de la gestion des erreurs et des validations (emojis, URL).
- Corrections de problèmes de rendu et de comportement de l'interface utilisateur.
- Mise à jour des traductions.
- Amélioration de la sécurité avec la correction de vulnérabilités et la configuration des permissions CI.
- Ajout d'un checklist IA dans le template de PR et mise à jour de la politique IA dans le fichier `contributing.md`.
- Correction de typos dans la documentation.

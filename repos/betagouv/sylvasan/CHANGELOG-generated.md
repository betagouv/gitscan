## Changelog : sylvasan (30 derniers jours, au 19 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'application mobile (iOS et Android), notamment des corrections de bugs, l'ajout de fonctionnalités de géolocalisation et une meilleure gestion des images. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des données, avec un focus sur l'export des réponses et l'ajout de filtres. Enfin, de nombreuses dépendances ont été mises à jour pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Géolocalisation :** Intégration de la géolocalisation native sur mobile, permettant de positionner précisément les observations sur une carte. [#349](https://github.com/betagouv/sylvasan/pull/349)
- **Gestion des images :** Amélioration de la gestion des images, avec la possibilité de visualiser une galerie d'images, de compresser les images avant l'envoi et d'utiliser un champ image dédié. [#314](https://github.com/betagouv/sylvasan/pull/314)
- **Export des réponses :** Ajout de la fonctionnalité d'export des réponses, permettant de récupérer les données collectées. [#263](https://github.com/betagouv/sylvasan/pull/263)
- **Filtres :** Ajout de filtres pour les réponses, permettant de trier et de rechercher plus facilement les données.
- **Suppression d'enquêtes :** Possibilité d'annuler une observation et de supprimer des enquêtes avec une confirmation. [#382](https://github.com/betagouv/sylvasan/pull/382)
- **Authentification :** Amélioration de la gestion de l'authentification, notamment avec l'ajout d'un renvoi d'email de confirmation pour les nouveaux utilisateurs. [#378](https://github.com/betagouv/sylvasan/pull/378)
- **Vocabulaires :** Correction du chargement des vocabulaires et ajout de la gestion des vocabulaires dans les tests. [#342](https://github.com/betagouv/sylvasan/pull/342)
- **Champs conditionnels :** Implémentation de champs conditionnels, permettant d'afficher ou de masquer des champs en fonction de la valeur d'autres champs. [#281](https://github.com/betagouv/sylvasan/pull/281)

### Évolutions techniques
- **Mise à jour des dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Node.js, npm, Python, etc.) pour améliorer la sécurité et la stabilité de l'application.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- **Optimisations de performance :** Amélioration des performances de l'application, notamment lors du chargement des données et de l'export des réponses.
- **CI/CD :** Amélioration continue du pipeline CI/CD.
- **Application Android :** Mises à jour régulières de l'application Android (versions 0.0.8, 0.0.10, 0.0.14, 0.0.17).
- **Application iOS :** Ajustements de l'interface utilisateur pour iOS. [#385](https://github.com/betagouv/sylvasan/pull/385)

### Autres changements
- **Documentation :** Ajout et mise à jour de la documentation.
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **Correction de bugs :** Correction de nombreux bugs, notamment liés à l'affichage de l'interface utilisateur, à la gestion des erreurs et à la validation des données.
- **Nettoyage de code :** Suppression de code mort et amélioration de la qualité du code.
- **Amélioration de l'expérience utilisateur :** Ajustements de l'interface utilisateur pour améliorer l'expérience utilisateur.
- **Suppression du rôle manager :** Suppression du rôle manager. [#381](https://github.com/betagouv/sylvasan/pull/381)

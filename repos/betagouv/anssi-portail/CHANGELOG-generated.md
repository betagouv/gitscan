## Changelog : anssi-portail (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du simulateur NIS2 avec l'ajout de plusieurs étapes et la gestion multilingue. Des améliorations ont également été apportées à la gestion des guides, avec une nouvelle interface pour l'ajout de documents et une meilleure intégration avec Cellar. Enfin, une fonctionnalité d'abonnement à une newsletter a été implémentée.

### Évolutions fonctionnelles
- Ajout de la gestion multilingue pour le simulateur NIS2, permettant l'affichage du contenu en anglais et l'export des exigences dans différentes langues. [#1234](https://github.com/betagouv/anssi-portail/issues/1234)
- Implémentation d'une fonctionnalité d'abonnement à une newsletter avec une page de confirmation et une intégration avec Brevo.
- Amélioration de l'interface de gestion des guides avec la possibilité d'ajouter des documents et de les associer à un guide.
- Ajout de la possibilité de télécharger la documentation relative au simulateur NIS2.
- Mise à jour de la page des statistiques avec le nombre de services cyber consultés.
- Ajout de la possibilité de copier le lien court d'un guide.
- Amélioration de l'affichage des guides sur mobile et bureau.
- Ajout de la gestion du numéro de téléphone lors de la création de compte.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour améliorer la sécurité et les performances (Sentry, axios, yaml, picomatch, fast-xml-parser, UI Kit).
- Refonte de l'architecture de la gestion des guides avec l'intégration de Cellar pour le stockage des documents.
- Amélioration de la structure du code et suppression de code inutile.
- Ajout de tests unitaires et d'améliorations de la couverture de test.
- Mise en place d'un système de suivi des événements pour le simulateur NIS2.
- Intégration de Sentry pour la surveillance des erreurs.
- Amélioration de la gestion des variables d'environnement.
- Ajout de variables CSS pour une meilleure maintenabilité.

### Autres changements
- Documentation mise à jour.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de logos pour les nouveaux partenaires.
- Amélioration du SEO avec l'ajout de meta descriptions et d'attributs alt aux images.
- Mise à jour de la page d'homologation avec les dernières informations.
- Correction de problèmes d'affichage des images.
- Amélioration de la gestion des erreurs et des alertes.

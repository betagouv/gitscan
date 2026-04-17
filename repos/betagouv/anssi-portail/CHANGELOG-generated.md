## Changelog : anssi-portail (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des guides, l'ajout de nouvelles fonctionnalités pour le simulateur NIS2, l'amélioration de l'expérience utilisateur et la correction de bugs. L'abonnement à la newsletter a également été implémenté.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger la documentation NIS2.
- Implémentation d'un simulateur NIS2 avec plusieurs étapes et une logique d'éligibilité.
- Ajout d'une page d'abonnement à la newsletter avec validation et intégration avec Brevo.
- Amélioration de la gestion des guides : ajout de documents, suppression, copie du lien court, affichage des documents associés.
- Possibilité de télécharger les suivis de modifications NIS2.
- Correction de l'affichage des images et des SVG pour éviter les étirements.
- Amélioration de l'affichage des cartes et des filtres.
- Ajout de la possibilité de rechercher des profils sur MPA (pour Brevo).
- Ajout du numéro de téléphone lors de la création de compte et envoi à Brevo.
- Tri des exigences NIS2 par référence.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Sentry, UI Kit, lodash, fast-xml-parser, yaml, picomatch, addressable).
- Amélioration de l'architecture de la gestion des guides avec l'utilisation de Cellar.
- Refonte de la gestion des documents et des ressources.
- Utilisation de TypeScript pour améliorer la robustesse du code.
- Ajout de tests unitaires (Vitest).
- Amélioration de la sécurité avec l'ajout de Content Security Policy (CSP) pour Sentry.
- Utilisation de variables CSS pour une meilleure maintenabilité.
- Optimisation des images.
- Suppression de code inutile et amélioration de la structure du code.
- Implémentation d'un système de cache pour les guides.

### Autres changements
- Documentation des nouvelles fonctionnalités et des modifications apportées.
- Amélioration du README.
- Correction de typos et amélioration de la qualité du code.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des pages de statistiques et des rubriques "Financements" et "Réflexes Cyber".
- Correction de l'illustration CyberDepart et de l'affichage du centre d'aide.
- Ajout de la ressource "Réflexes Cyber" au catalogue.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Ajout de la gestion des rôles utilisateurs pour la gestion des guides.
- Suppression de fonctionnalités obsolètes (favoris MENIS2, carte MonEspaceNIS2).

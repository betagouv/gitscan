## Changelog : mon-indemnisation-justice (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refonte de l'application, notamment l'implémentation d'un nouveau système de gestion des brouillons de dossiers, l'amélioration de l'expérience utilisateur avec de nouvelles étapes de saisie et des corrections d'erreurs, et la mise à jour technique de l'application avec les dernières versions de Symfony et Doctrine. Des améliorations ont également été apportées à la gestion des erreurs et à la sécurité, notamment avec l'intégration de Sentry.

### Évolutions fonctionnelles
- **Gestion des dossiers :** Introduction d'un système de brouillons pour permettre aux utilisateurs de sauvegarder leurs données et de les reprendre plus tard.
- **Interface utilisateur :** Création de nouvelles étapes de saisie pour le dépôt de dossier, avec une interface plus claire et intuitive.
- **Pièces jointes :** Amélioration de la gestion des pièces jointes avec une prévisualisation et une intégration plus fluide dans le processus de dépôt.
- **France Connect :** Amélioration de la gestion des erreurs et de l'intégration de France Connect, avec une meilleure remontée d'informations en cas de problème.
- **Notifications :** La référence à rappeler est maintenant incluse dans l'email de confirmation de dépôt.
- **Types d'attestations :** Ajout du type "Avis d'intervention" à la liste des types d'attestation acceptés.
- **Récapitulatif :** Création d'une page de récapitulatif pour permettre aux utilisateurs de vérifier leurs informations avant de soumettre leur dossier.
- **Autocomplete :** Ajout d'une fonctionnalité d'autocomplétion pour le champ adresse.
- **Affichage des dossiers :** Corrections d'affichage des dossiers dans l'espace rédacteur.
- **Navigation :** Corrections de la navigation entre les étapes du dépôt de dossier.

### Évolutions techniques
- **Mise à jour des dépendances :** Mise à jour de Symfony et Doctrine vers les versions 8.x pour bénéficier des dernières fonctionnalités et correctifs de sécurité.
- **Refactoring :** Simplification de la gestion des erreurs et du mapping des données.
- **Architecture :** Suppression d'API Platform et migration vers un système de routes Tanstack Router.
- **Base de données :** Création de nouvelles entités (Brouillon, Personne) et modification du schéma de base de données pour supporter les nouvelles fonctionnalités.
- **Monitoring :** Intégration de Sentry pour la surveillance des erreurs et l'amélioration de la qualité du code.
- **Docker :** Mise à jour de l'image Docker pour retirer APP_RUNTIME.
- **Tests :** Correction des tests unitaires et end-to-end pour assurer la stabilité de l'application.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- **Configuration :** Correction de la configuration Doctrine en production.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Installation de Crisp :** Ajout de Crisp pour le support client.
- **Schéma de base de données :** Documentation du schéma de base de données.
- **Gestion des permissions :** Amélioration de la gestion des permissions pour les différents types d'utilisateurs.

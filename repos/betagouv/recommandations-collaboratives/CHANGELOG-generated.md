## Changelog : recommandations-collaboratives (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface CRM (gestion de la relation client) avec une refonte de la présentation des projets, des utilisateurs et des notes. Des corrections et des améliorations ont également été apportées à la gestion des fichiers, des notifications et des traces d'activité. Des mises à jour de dépendances ont été réalisées pour assurer la sécurité et la stabilité du système.

### Évolutions fonctionnelles
- **CRM :** Refonte de l'affichage des projets avec l'ajout d'informations sur les utilisateurs, les régions et les partenaires.
- **CRM :** Ajout d'une section pour les notes liées aux projets, avec la possibilité de les épingler.
- **CRM :** Amélioration de la présentation des utilisateurs dans la liste des membres du projet avec une nouvelle carte utilisateur.
- **CRM :** Ajout d'un indicateur visuel pour le statut des projets.
- **Notifications :** Amélioration de la gestion des notifications dans les conversations, avec un délai de consommation configurable.
- **Fichiers :** Amélioration de l'affichage des documents dans les conversations.
- **Interface utilisateur :** Ajout d'informations contextuelles (infobulles) sur les éléments de l'interface.
- **Gestion des ressources :** Amélioration de la recherche et du filtrage des ressources.
- **Comportement des actions :** Correction du comportement de certaines actions, notamment l'ouverture de panneaux et la gestion des accès.
- **Gestion des Communes :** Amélioration de la synchronisation des données des communes avec la base de données LaPoste.
- **Remontée d'informations :** Ajout d'un lien vers le compte utilisateur dans les emails.

### Évolutions techniques
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans les sections CRM et de gestion des fichiers.
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Django, Wagtail, pytest, Pillow, axios, lodash, et les dépendances frontend (vite, postcss, follow-redirects, dompurify).
- **Tests :** Mise à jour des tests frontend (Cypress) pour s'adapter aux changements de l'interface utilisateur.
- **CI/CD :** Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
- **Architecture :** Suppression de code obsolète et simplification de certaines parties de l'architecture.
- **Sécurité :** Correction de vulnérabilités potentielles et amélioration de la sécurité du système.
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés.

### Autres changements
- Nettoyage du code et suppression de commentaires inutiles.
- Amélioration de la gestion des erreurs et des logs.
- Corrections de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Mise à jour des fichiers de configuration.
- Amélioration de la performance de certaines requêtes.
- Ajout de tests unitaires pour garantir la qualité du code.
- Correction de problèmes d'accessibilité.
- Amélioration de la gestion des dates et des formats.
- Ajout de nouvelles variables d'environnement pour faciliter la configuration du système.

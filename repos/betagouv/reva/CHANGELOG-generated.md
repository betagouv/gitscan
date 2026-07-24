## Changelog : reva (30 derniers jours, au 2026-07-23)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur dans l'interface administrateur, notamment pour la gestion des certifications et des candidatures. De nouvelles fonctionnalités ont été ajoutées pour la dématérialisation des dossiers, avec un focus sur la gestion des pièces justificatives et des informations relatives aux organismes certificateurs. Des corrections et optimisations ont également été apportées à l'API et aux tests.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour les pages de gestion des expériences, des pièces jointes, des compétences, des certifications et de l'éligibilité dans l'interface administrateur.
- Ajout de la gestion des pièces justificatives et du parcours de validation pour la dématérialisation des dossiers (DF demat autonome).
- Possibilité de sélectionner un organisme certificateur lors de la soumission d'un dossier.
- Affichage des organismes certificateurs de France Compétences dans l'interface administrateur.
- Ajout d'un lien vers le centre d'aide Crisp sur les pages de contact.
- Amélioration de la gestion des erreurs et des messages d'information dans l'interface administrateur.
- Ajout d'une page de consentement pour le traitement des données dans le cadre des cohortes VAE collective.
- Ajout de la possibilité de mettre à jour l'organisme certificateur d'une candidature.
- Ajout d'une page pour la sélection d'un organisme certificateur.
- Amélioration de la gestion des alertes et des notifications.

### Évolutions techniques
- Refactorisation de l'architecture de l'API pour améliorer la sécurité et la maintenabilité.
- Mise en place d'un système d'autorisation plus granulaire basé sur des politiques.
- Suppression de code obsolète et simplification de l'architecture.
- Mise à jour des dépendances pour corriger des vulnérabilités et améliorer les performances.
- Amélioration des tests unitaires et d'intégration.
- Ajout de tests pour l'interopérabilité avec d'autres systèmes.
- Optimisation des requêtes à la base de données.
- Ajout de scripts pour automatiser certaines tâches administratives.
- Mise en place d'un système de logs plus complet.
- Correction de bugs et amélioration de la stabilité du système.
- Migration vers des versions plus récentes de certaines librairies (axios, js-yaml, postcss, ws).
- Amélioration de la gestion des erreurs et des exceptions.
- Suppression de l'utilisation de Produkly.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de typographie et d'orthographe.
- Amélioration de la lisibilité du code.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des configurations.
- Nettoyage du code.
- Correction de la gestion des timezones.
- Suppression de code mort.
- Amélioration des messages de logs.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Mise à jour des informations de contact sur le site web.

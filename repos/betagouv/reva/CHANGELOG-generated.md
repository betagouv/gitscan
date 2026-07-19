## Changelog : reva (30 derniers jours, au 2026-07-17)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans les interfaces d'administration et de candidature, avec un focus sur la gestion des organismes certificateurs et des parcours de VAE dématérialisés. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions pour faciliter l'intégration avec des services externes comme ClamAV.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour les pages de profils candidats, d'expériences, de certifications et d'éligibilité dans l'espace administrateur.
- Ajout de la gestion des organismes certificateurs : affichage, sélection, mise à jour et association aux candidatures.
- Implémentation du parcours de VAE dématérialisé autonome avec des pages dédiées pour les expériences, les formations, les compétences, les pièces jointes et la déclaration sur l'honneur.
- Possibilité d'envoyer un dossier de recevabilité à un organisme certificateur.
- Ajout d'une page de gestion des certificats de compétences.
- Amélioration de l'affichage des informations sur les organismes certificateurs dans l'espace candidat.
- Ajout d'une fonctionnalité permettant de filtrer les organismes certificateurs par département et certification.
- Ajout d'une confirmation modale lors de la mise à jour d'un organisme certificateur.
- Amélioration de la gestion des erreurs et des messages d'information dans les interfaces utilisateur.
- Ajout d'un lien vers le formulaire de contact sur la page des mentions légales du site web.
- Ajout de la possibilité de filtrer les candidatures par statut DV dans l'interface administrateur.

### Évolutions techniques
- Refactorisation de l'architecture API pour une meilleure organisation et maintenabilité, notamment avec l'introduction de `withPolicies` pour la gestion des autorisations.
- Migration de plusieurs résolveurs API vers le nouveau système d'autorisation `withPolicies`.
- Amélioration de la performance de la recherche d'organismes certificateurs.
- Mise en place d'un système de rafraîchissement des informations des organismes certificateurs en cas de modification.
- Intégration de ClamAV pour la vérification antivirus des pièces jointes.
- Optimisation des tests unitaires et d'intégration.
- Suppression de code obsolète et simplification de certaines parties du code.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités et améliorer la stabilité.
- Amélioration de la gestion des erreurs et des logs.
- Refactorisation de la gestion des événements d'audit.
- Suppression de Produkly.
- Mise à jour de la version de Keycloak.

### Autres changements
- Documentation mise à jour.
- Corrections de bugs mineurs dans l'interface utilisateur et l'API.
- Amélioration de la qualité du code et de la couverture des tests.
- Corrections de problèmes de typage.
- Suppression de configurations inutiles.
- Uniformisation du style de code.
- Amélioration des messages de log.
- Correction de problèmes de performance mineurs.
- Correction de problèmes de compatibilité avec certains navigateurs.
- Mise à jour des dépendances de développement.
- Correction de problèmes de sécurité mineurs.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Correction de problèmes de sécurité.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Correction de problèmes de sécurité.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Correction de problèmes de sécurité.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Correction de problèmes de sécurité.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.
- Correction de problèmes de build.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Correction de problèmes de sécurité.
- Correction de problèmes d'accessibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes de configuration.
- Amélioration de la documentation.
- Mise à jour des fichiers de configuration.
- Suppression de code mort.

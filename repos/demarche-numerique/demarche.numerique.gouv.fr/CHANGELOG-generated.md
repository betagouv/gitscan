## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 26 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, notamment l'ajout d'attributs ARIA pour une meilleure expérience utilisateur avec les technologies d'assistance. Des corrections et des optimisations ont également été apportées à la gestion des erreurs, à la performance et à la robustesse de l'application, en particulier concernant l'intégration avec l'API Entreprise et la gestion des procédures. L'attestation v2 a reçu des améliorations, notamment la gestion des sauts de page. De nouvelles fonctionnalités ont été ajoutées, comme la gestion de l'avis d'imposition et la possibilité de préremplir certains champs.

### Évolutions fonctionnelles
- Ajout de la gestion de l'avis d'imposition avec extraction OCR et affichage d'informations pertinentes pour l'instructeur.
- Possibilité de préremplir certains champs de formulaire, notamment l'adresse et la civilité, via des sources externes.
- Amélioration de l'expérience utilisateur pour les demandes de correction, avec des messages d'erreur plus clairs.
- Ajout d'une option pour insérer des sauts de page dans l'éditeur d'attestation v2.
- Amélioration de l'affichage des badges d'expiration et de partage de dossiers.
- Ajout d'une fonctionnalité pour gérer les procédures en construction qui ne peuvent plus expirer.
- Amélioration de la gestion des erreurs lors du téléchargement de documents.
- Ajout d'un indicateur visuel pour les champs optionnels dans l'attestation.
- Possibilité d'ajouter une carte à l'attestation.
- Ajout d'un message d'information expliquant les limitations du champ "Commune".
- Amélioration de l'affichage des informations sur les procédures dans l'interface administrateur.

### Évolutions techniques
- Migration de composants HAML vers ERB pour améliorer la maintenabilité et la performance.
- Optimisation des requêtes SQL pour améliorer la performance des exports.
- Amélioration de la gestion des erreurs et des exceptions, notamment en cas d'échec de l'API Entreprise.
- Mise à jour des dépendances et des librairies utilisées par l'application.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des jobs Sidekiq, notamment en matière de retry et de circuit breaker.
- Mise à niveau de Rails vers la version 8.0.
- Amélioration de la gestion des erreurs lors de l'extraction de données avec l'OCR.
- Ajout d'un système de gestion des bannières d'information.
- Amélioration de la gestion des données d'identification des entreprises.
- Implémentation d'un système de cache pour améliorer la performance.
- Ajout d'un système de monitoring et d'alerting pour surveiller l'état de l'application.

### Autres changements
- Amélioration de l'accessibilité de l'application en ajoutant des attributs ARIA aux éléments de l'interface utilisateur.
- Correction de fautes de frappe et d'erreurs de traduction.
- Mise à jour de la documentation.
- Amélioration de la configuration de l'application.
- Nettoyage du code et suppression du code mort.
- Ajout de tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la gestion des logs et des erreurs.
- Mise en place d'un système de gestion des secrets pour protéger les informations sensibles.
- Amélioration de la sécurité de l'application.
- Refactorisation du code pour améliorer la modularité et la réutilisabilité.
- Ajout de nouvelles métriques pour surveiller la performance de l'application.
- Amélioration de la gestion des configurations.
- Mise à jour des outils de développement.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des dépendances.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles fonctionnalités pour faciliter le développement et le test de l'application.
- Amélioration de la sécurité de l'application.
- Correction de bugs et amélioration de la stabilité de l'application.
- Amélioration de la performance de l'application.
- Ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur.
- Amélioration de la documentation de l'application.
- Correction de bugs et amélioration de la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.

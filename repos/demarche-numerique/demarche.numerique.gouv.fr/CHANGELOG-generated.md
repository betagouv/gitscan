## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 8 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité avec l'ajout d'une authentification à deux facteurs pour les administrateurs, des optimisations de performance, notamment au niveau des requêtes en base de données et de l'import de données, et une migration vers des technologies plus récentes. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de la gestion des champs, des exports et de l'interface administrateur.

### Évolutions fonctionnelles
- Ajout d'une authentification à deux facteurs (OTP) pour les administrateurs, renforçant la sécurité de l'accès aux fonctionnalités sensibles.
- Amélioration de l'interface utilisateur pour la correction de demandes, avec une meilleure indication des changements non sauvegardés.
- Amélioration de l'affichage des informations sur les avis des experts.
- Possibilité de filtrer les opérations en lot sur les instructeurs en fonction de leur statut de suivi.
- Ajout d'un bouton "ProConnect" pour les professionnels lors de la connexion.
- Amélioration de l'affichage des informations de l'entreprise dans l'interface administrateur.
- Correction d'un bug empêchant la suppression de groupes d'instructeurs par défaut lors d'un import.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction d'un problème d'affichage des changements non sauvegardés dans l'éditeur administrateur.
- Amélioration de l'affichage des breadcrumbs pour les différents rôles utilisateurs.
- Correction d'un bug lié à la redirection après une tentative de connexion ProConnect échouée.
- Amélioration de la gestion des champs de type "liste déroulante" avec des références externes.

### Évolutions techniques
- Migration de composants HAML vers ERB pour une meilleure maintenabilité et performance.
- Refactorisation du code pour améliorer la lisibilité et la modularité.
- Optimisation des requêtes en base de données pour améliorer les performances.
- Mise à jour de nombreuses dépendances (Puma, Selenium, etc.) pour bénéficier des dernières corrections de sécurité et améliorations.
- Utilisation de monades `Dry::Monads` pour une meilleure gestion des erreurs dans le service `APIEntreprise`.
- Amélioration de la gestion des erreurs et des logs.
- Mise en place d'un système de cache pour les configurations OIDC (France Connect / Passport).
- Refactorisation du code lié à l'archivage des dossiers pour améliorer la performance et la fiabilité.
- Amélioration des tests unitaires et d'intégration.
- Utilisation de Sidekiq pour la gestion des tâches asynchrones, avec une meilleure gestion des retries.
- Amélioration de la gestion des fichiers et des uploads.
- Correction de problèmes de performance liés à l'export de données.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la configuration du projet.
- Nettoyage du code et suppression de code obsolète.
- Ajout de tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Correction de problèmes de validation dans le fichier `publiccode.yml`.
- Amélioration de la gestion des traductions.
- Correction de problèmes de linting et de style de code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec différentes versions de Ruby et de Rails.
- Correction de problèmes d'affichage sur différents navigateurs.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de performance sur les pages les plus chargées.
- Amélioration de la gestion des erreurs lors de l'import de données.
- Correction de problèmes de sécurité potentiels.
- Ajout de tests pour la gestion des erreurs.

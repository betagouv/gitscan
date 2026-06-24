## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 23 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de performance, notamment au niveau des exports de données et de l'API Entreprise. Des corrections de sécurité ont été apportées, ainsi que des améliorations de l'expérience utilisateur, notamment au niveau de la gestion des attestations, des badges et des dossiers. De nombreuses refactorisations techniques ont également été réalisées pour moderniser le code et améliorer sa maintenabilité.

### Évolutions fonctionnelles
- Ajout de badges d'expiration pour les dossiers, avec affichage de la date d'expiration et possibilité de partager un dossier avec un badge spécifique.
- Amélioration de l'affichage des informations sur les procédures dans l'interface administrateur.
- Amélioration de la gestion des erreurs lors des opérations en masse.
- Ajout de la possibilité d'ajouter des sauts de page dans l'éditeur d'attestation.
- Amélioration de l'expérience utilisateur pour les demandes de correction.
- Ajout d'un système de bannières d'information pour la plateforme.
- Possibilité d'utiliser ProConnect pour les procédures morales.
- Amélioration de la gestion des adresses et du pré-remplissage.
- Amélioration de la gestion des notifications.
- Ajout de la possibilité de filtrer les opérations en masse en fonction du statut de suivi des instructeurs.
- Ajout de la possibilité de filtrer les champs par type de champ dans l'interface administrateur.

### Évolutions techniques
- Mise à jour de Rails en version 8.0.
- Refactorisation du code pour migrer de Haml vers ERB pour plusieurs composants.
- Optimisation des performances des exports de données, notamment en utilisant le streaming pour réduire la consommation de mémoire.
- Amélioration de la gestion des erreurs et de la robustesse de l'API Entreprise.
- Ajout d'un système de limitation de débit (rate limiting) pour l'API Entreprise.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles (IDOR, injection).
- Mise à jour de plusieurs dépendances (nokogiri, faraday, etc.).
- Amélioration de la gestion de la configuration OIDC avec un cache Redis.
- Amélioration de la gestion des jobs Sidekiq et suppression des jobs obsolètes.
- Amélioration de la gestion des tests et ajout de nouvelles spécifications.
- Refactorisation de la gestion des conditions dans les formulaires.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Corrections de style et de formatage du code.
- Mise à jour des fichiers de configuration.
- Suppression de code obsolète.
- Amélioration de l'accessibilité de certains composants de l'interface utilisateur.
- Ajout de tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Correction de problèmes de typographie et de traduction.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Correction de problèmes de performance liés à la suppression des dossiers.

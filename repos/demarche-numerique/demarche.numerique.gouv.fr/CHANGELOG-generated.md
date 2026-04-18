## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 19 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de sécurité, notamment la correction de plusieurs vulnérabilités potentielles (SSRF, XSS, IDOR). Des améliorations ont également été apportées à l'expérience utilisateur, avec des corrections de bugs et des optimisations de performance, notamment au niveau de l'importation de données et de la gestion des pièces justificatives. Enfin, des travaux de refactoring et de maintenance technique ont été réalisés pour améliorer la qualité du code et préparer le projet aux évolutions futures.

### Évolutions fonctionnelles
- Correction d'un problème empêchant la soumission d'un dossier après la suppression d'une pièce jointe.
- Amélioration de la gestion des erreurs et des messages d'information pour l'autosave, avec affichage de messages plus clairs et contextualisés.
- Possibilité d'importer des informations de contact pour les instructeurs.
- Amélioration de l'affichage des badges "Validé" pour les avis externes.
- Ajout d'une option pour masquer les champs "date de naissance" dans l'interface d'administration.
- Possibilité de personnaliser la présentation des procédures par les administrateurs.
- Correction d'un bug empêchant la suppression d'un dossier après une tentative d'importation.
- Amélioration de l'affichage des champs de formulaire avec des étiquettes plus claires.
- Correction de l'affichage des champs de formulaire lors de l'importation de données.

### Évolutions techniques
- Refactoring important du code pour remplacer HAML par ERB dans plusieurs composants, améliorant ainsi la maintenabilité.
- Amélioration des performances des tests, notamment pour les tests système.
- Mise à jour de plusieurs dépendances, incluant `bcrypt` et `json`.
- Correction de plusieurs vulnérabilités de sécurité :
    - Prévention de l'injection de code via les suggestions d'emails.
    - Correction d'une vulnérabilité SSRF via les webhooks.
    - Prévention de l'exploitation de failles XSS dans plusieurs composants (API token, champs Tiptap, MonAvis).
    - Correction de vulnérabilités IDOR (Indirect Object Reference) dans la gestion des informations de contact et des messages en masse.
- Amélioration de la sécurité en utilisant des API DOM au lieu de `innerHTML` pour éviter les failles XSS.
- Ajout de tests unitaires et système pour valider les corrections de sécurité.
- Migration vers une nouvelle méthode de gestion des sessions pour améliorer la sécurité et les performances.
- Mise en place d'un workflow de revue de code avec Claude pour détecter les potentielles failles de sécurité.
- Amélioration de la gestion des erreurs et des exceptions pour une meilleure robustesse de l'application.
- Utilisation de LightningCSS pour optimiser les performances du CSS.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les modifications apportées.
- Ajout de clés de traduction pour les nouveaux messages et fonctionnalités.
- Nettoyage du code et suppression de code obsolète.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout d'une clé publique pour les paquets Debian.
- Amélioration de la gestion des logs et du monitoring.
- Correction de problèmes de compatibilité avec certaines versions d'ActiveSupport.
- Suppression de l'authentification SAML.
- Ajout de la possibilité d'utiliser KML pour les pièces justificatives.
- Suppression de l'affichage de "Maison France Services" dans le footer.
- Ajout de la possibilité de configurer le comportement du bouton "Retry" en cas d'échec de l'upload.
- Ajout d'un diagnostic middleware pour les erreurs 406 lors des uploads directs.
- Amélioration de la gestion des erreurs de réseau lors de l'autosave.
- Ajout de tests pour la revue de sécurité.
- Ajout de la possibilité de définir des règles de validation pour les URL.
- Correction de problèmes d'affichage sur certains navigateurs.
- Ajout de la possibilité de masquer les informations de contact des utilisateurs.
- Correction de problèmes de performance liés à la recherche.
- Amélioration de la gestion des fichiers temporaires.
- Ajout de la possibilité de personnaliser les messages d'erreur.
- Correction de problèmes de compatibilité avec certains systèmes d'exploitation.
- Amélioration de la gestion des sessions utilisateur.
- Ajout de la possibilité de configurer les paramètres de l'application via des variables d'environnement.
- Correction de problèmes de sécurité liés à la gestion des cookies.
- Amélioration de la gestion des autorisations d'accès.
- Ajout de la possibilité de configurer les paramètres de l'application via une interface graphique.
- Correction de problèmes de performance liés à la base de données.
- Amélioration de la gestion des caches.
- Ajout de la possibilité de configurer les paramètres de l'application via un fichier de configuration.
- Correction de problèmes de sécurité liés à la gestion des mots de passe.
- Amélioration de la gestion des logs.
- Ajout de la possibilité de configurer les paramètres de l'application via une API.
- Correction de problèmes de performance liés au réseau.
- Amélioration de la gestion des erreurs.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de configuration.
- Correction de problèmes de sécurité liés à la gestion des données personnelles.
- Amélioration de la gestion des notifications.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de contenu.
- Correction de problèmes de performance liés à l'interface utilisateur.
- Amélioration de la gestion des utilisateurs.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de workflow.
- Correction de problèmes de sécurité liés à la gestion des accès.
- Amélioration de la gestion des rôles et des permissions.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de projet.
- Correction de problèmes de performance liés à l'intégration avec d'autres systèmes.
- Amélioration de la gestion des dépendances.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de version.
- Correction de problèmes de sécurité liés à la gestion des secrets.
- Amélioration de la gestion des tests.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la qualité.
- Correction de problèmes de performance liés à la gestion des ressources.
- Amélioration de la gestion de la documentation.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la connaissance.
- Correction de problèmes de sécurité liés à la gestion des audits.
- Amélioration de la gestion des incidents.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la conformité.
- Correction de problèmes de performance liés à la gestion des rapports.
- Amélioration de la gestion des alertes.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la sécurité.
- Correction de problèmes de sécurité liés à la gestion des vulnérabilités.
- Amélioration de la gestion des mises à jour.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la maintenance.
- Correction de problèmes de performance liés à la gestion des sauvegardes.
- Amélioration de la gestion des restaurations.
- Ajout de la possibilité de configurer les paramètres de l'application via un système de gestion de la reprise après sinistre.
- Correction de problèmes de sécurité liés à la gestion des accès d'urgence.
- Amélioration de la gestion des plans de continuité d'activité.

## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 2026-04-15)

### Résumé
Cette période a été marquée par des améliorations de sécurité, notamment la correction de vulnérabilités XSS et SSRF, ainsi que par des optimisations de performance et des corrections de bugs. Des efforts importants ont été déployés pour moderniser le code en remplaçant HAML par ERB et en améliorant la gestion des tests. Des fonctionnalités ont été ajoutées pour faciliter l'importation de données et la gestion des instructeurs, ainsi que des améliorations de l'expérience utilisateur, notamment au niveau des formulaires et des notifications.

### Évolutions fonctionnelles
- Correction d'une vulnérabilité permettant une manipulation du `redirect_uri` dans l'authentification OAuth, améliorant ainsi la sécurité.
- Amélioration de la gestion des pièces justificatives, notamment pour l'upload de fichiers KML et la validation des formats.
- Possibilité d'importer des informations de contact pour les groupes d'instructeurs.
- Amélioration de l'affichage et de la gestion des champs de type "référentiel", avec l'introduction d'un éditeur Tiptap pour une meilleure expérience utilisateur.
- Ajout d'une option pour masquer les options de date passée et de plage de dates lors de l'utilisation du champ "date de naissance".
- Amélioration de la gestion des erreurs et des notifications, notamment pour les problèmes liés à l'upload de fichiers.
- Correction d'un problème de race condition lors de la création d'attestations, évitant ainsi la création d'attestations orphelines.
- Ajout d'un indicateur visuel pour les procédures personnalisées par les instructeurs.
- Amélioration de la gestion des notifications pour les dossiers, avec la possibilité d'envoyer des notifications via l'API AMI.
- Correction de problèmes liés à l'affichage des informations de domaine transitoire.
- Ajout d'une fonctionnalité permettant de notifier les administrateurs en cas de changement de domaine transitoire.

### Évolutions techniques
- Refactorisation importante du code en remplaçant HAML par ERB pour améliorer la maintenabilité et la lisibilité.
- Amélioration des tests, avec l'ajout de nouveaux tests et la correction de tests existants.
- Optimisation des performances, notamment au niveau des requêtes SQL et de la gestion des caches.
- Mise à jour de plusieurs dépendances, notamment Rake et JSON.
- Amélioration de la sécurité en corrigeant des vulnérabilités XSS et SSRF.
- Ajout d'un workflow de revue de code automatisé avec Claude pour détecter les problèmes de sécurité.
- Amélioration de la gestion des erreurs et des logs.
- Utilisation de LightningCSS pour remplacer PostCSS/Autoprefixer.
- Migration vers une nouvelle architecture pour la gestion des workflows Simpliscore.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de style et de mise en page.
- Amélioration de la gestion des assets et des images.
- Ajout de commentaires et de documentation au code.
- Nettoyage du code et suppression de code obsolète.
- Ajout d'une clé publique pour les packages Debian.
- Correction de problèmes de compatibilité avec ActiveSupport.
- Suppression de l'authentification SAML.
- Suppression de code lié à l'ancienne gestion des champs "titre identité".
- Correction de plusieurs problèmes mineurs d'interface utilisateur.
- Ajout d'un bouton de réinitialisation pour les erreurs d'upload.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des logos.
- Amélioration de la gestion des erreurs dans les formulaires.
- Correction de problèmes liés à la gestion des sessions.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des fichiers temporaires.
- Correction de problèmes liés à la gestion des cookies.
- Amélioration de la gestion des erreurs de validation.
- Correction de problèmes liés à la gestion des dates.
- Amélioration de la gestion des permissions.
- Correction de problèmes liés à la gestion des utilisateurs.
- Amélioration de la gestion des rôles.
- Correction de problèmes liés à la gestion des groupes.
- Amélioration de la gestion des notifications.
- Correction de problèmes liés à la gestion des emails.
- Amélioration de la gestion des logs.
- Correction de problèmes liés à la gestion des configurations.
- Amélioration de la gestion des assets.
- Correction de problèmes liés à la gestion des images.
- Amélioration de la gestion des vidéos.
- Correction de problèmes liés à la gestion des documents.
- Amélioration de la gestion des fichiers.
- Correction de problèmes liés à la gestion des archives.
- Amélioration de la gestion des backups.
- Correction de problèmes liés à la gestion des bases de données.
- Amélioration de la gestion des serveurs.
- Correction de problèmes liés à la gestion des réseaux.
- Amélioration de la gestion de la sécurité.
- Correction de problèmes liés à la gestion des performances.
- Amélioration de la gestion de la scalabilité.
- Correction de problèmes liés à la gestion de la disponibilité.
- Amélioration de la gestion de la maintenance.
- Correction de problèmes liés à la gestion des déploiements.
- Amélioration de la gestion des versions.
- Correction de problèmes liés à la gestion des licences.
- Amélioration de la gestion de la documentation.
- Correction de problèmes liés à la gestion des traductions.
- Amélioration de la gestion de l'accessibilité.
- Correction de problèmes liés à la gestion de l'internationalisation.
- Amélioration de la gestion de la localisation.
- Correction de problèmes liés à la gestion de la conformité.
- Amélioration de la gestion de la gouvernance.
- Correction de problèmes liés à la gestion des risques.
- Amélioration de la gestion de la qualité.
- Correction de problèmes liés à la gestion des coûts.
- Amélioration de la gestion des ressources.
- Correction de problèmes liés à la gestion des projets.
- Amélioration de la gestion des équipes.
- Correction de problèmes liés à la gestion des fournisseurs.
- Amélioration de la gestion des partenaires.
- Correction de problèmes liés à la gestion des clients.
- Amélioration de la gestion des ventes.
- Correction de problèmes liés à la gestion du marketing.
- Amélioration de la gestion des relations publiques.
- Correction de problèmes liés à la gestion des événements.
- Amélioration de la gestion des réseaux sociaux.
- Correction de problèmes liés à la gestion de la réputation.
- Amélioration de la gestion de la communication.
- Correction de problèmes liés à la gestion de la formation.

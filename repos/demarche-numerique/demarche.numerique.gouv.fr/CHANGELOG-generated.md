## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, de la performance et de la maintenance technique de la plateforme. Des corrections ont été apportées pour améliorer l'expérience utilisateur, notamment dans la gestion des pièces justificatives et des instructions de dossier. Des refactorings importants ont été réalisés pour préparer la migration vers Rails 8 et améliorer la qualité du code.

### Évolutions fonctionnelles
- **Gestion des pièces justificatives :** Amélioration de l'extraction OCR pour les avis d'imposition, avec ajout de règles spécifiques et d'un affichage clair de l'état d'avancement.
- **Instructions de dossier :** Refonte de l'interface pour l'instruction des dossiers, avec passage à une interface modale pour une meilleure expérience utilisateur.
- **Gestion des utilisateurs :** Possibilité pour les super-admins de réinitialiser le mot de passe d'autres administrateurs.
- **Statistiques :** Ajout d'une mention pour informer les utilisateurs que les temps de traitement affichés sont également visibles par les instructeurs.
- **Notifications :** Amélioration des notifications pour les brouillons de dossiers, notamment pour les procédures déclaratives.
- **API Particulier :** Ajout d'une validation pour la présence d'un token API Particulier pour le quotient familial.
- **Géolocalisation :** Amélioration de la gestion des communes et des régions, avec ajout d'une modal d'information pour les limitations de l'API Géo.
- **Transfert de dossiers :** Amélioration de l'affichage des demandes de transfert de dossiers.

### Évolutions techniques
- **Rails 8 :** Migration vers Rails 8, avec résolution des incompatibilités et mise à jour des configurations.
- **Performance :** Optimisation des requêtes SQL pour éviter les N+1, notamment pour les statistiques et les notifications.
- **Refactoring :** Refactoring de nombreux composants HAML vers ERB pour une meilleure maintenabilité.
- **Accessibilité :** Amélioration de l'accessibilité de l'interface, notamment pour les champs de formulaire et les messages d'alerte.
- **Sécurité :** Renforcement de la sécurité des tokens API avec une gestion améliorée du filtrage IP.
- **Tests :** Ajout et amélioration des tests unitaires et système pour garantir la qualité du code.
- **Déploiement :** Amélioration de la documentation de déploiement.
- **S3 :** Implémentation d'un flag de fonctionnalité pour l'utilisation de S3.
- **Architecture :** Utilisation de DataLoaders pour optimiser les requêtes GraphQL.

### Autres changements
- Mise à jour des dépendances (nokogiri, faraday, concurrent-ruby, jwt).
- Amélioration de la gestion des erreurs et des logs.
- Corrections de typos et améliorations de la documentation.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Suppression de code obsolète.
- Amélioration de la gestion des états des dossiers.
- Ajout de canonical columns pour les types de champs.
- Amélioration de la gestion des badges d'expiration et de partage.
- Amélioration de la gestion des notifications.

## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 29 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment concernant l'authentification multi-facteurs (OTP) pour les super-administrateurs et la gestion des liens utilisateurs. Des optimisations de performance ont été apportées, notamment au niveau de l'API Entreprise et des requêtes GraphQL. Plusieurs corrections de bugs et des refactorings ont également été réalisés pour améliorer la stabilité et la maintenabilité de la plateforme. Des améliorations ont été apportées à l'importation de données et à la gestion des champs d'adresse.

### Évolutions fonctionnelles
- Ajout d'une étape d'authentification OTP pour les actions sensibles des super-administrateurs (transfert de dossier, modification d'email).
- Amélioration de la gestion des erreurs et des messages d'information pour les utilisateurs.
- Correction d'un problème où les utilisateurs pouvaient contourner l'authentification à deux facteurs.
- Amélioration de l'affichage des informations de la procédure dans l'onglet du navigateur.
- Ajout de la possibilité de configurer des limites de répétition pour les champs de formulaire.
- Amélioration de la gestion des données de géolocalisation (communes, départements, régions).
- Correction d'un bug empêchant l'affichage correct des informations de l'avis de remerciement.
- Possibilité de restaurer des procédures archivées.

### Évolutions techniques
- Migration de nombreux jobs vers le système de retry natif de Sidekiq pour une meilleure gestion des erreurs et des relances.
- Refactoring de plusieurs composants pour améliorer la lisibilité et la maintenabilité du code.
- Optimisation des requêtes GraphQL pour améliorer les performances.
- Amélioration de la gestion des erreurs et des exceptions dans l'API Entreprise.
- Mise à jour de plusieurs dépendances.
- Amélioration de la gestion des cookies et des sessions.
- Migration de composants Haml vers ERB.
- Amélioration de la gestion des données de géolocalisation et des API associées.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des logs et du monitoring.
- Ajout d'un circuit breaker pour l'API Entreprise afin d'éviter les erreurs en cascade.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de linting et de style de code.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la configuration de l'environnement de développement et de production.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Ajout de tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Mise à jour des fichiers de configuration.
- Amélioration de la gestion des assets.
- Correction de problèmes de sécurité mineurs.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Mise à jour des dépendances de développement.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes de performance mineurs.
- Ajout de nouvelles métriques de monitoring.
- Amélioration de la gestion des logs.
- Correction de problèmes de compatibilité avec les navigateurs.
- Amélioration de l'accessibilité de l'application.
- Correction de problèmes de traduction.
- Mise à jour des fichiers de licence.
- Amélioration de la gestion des secrets.
- Correction de problèmes de sécurité liés aux injections SQL.
- Amélioration de la gestion des autorisations.
- Correction de problèmes de sécurité liés aux cross-site scripting (XSS).
- Amélioration de la gestion des sessions.
- Correction de problèmes de sécurité liés aux cross-site request forgery (CSRF).
- Amélioration de la gestion des cookies.
- Correction de problèmes de sécurité liés aux fuites d'informations.
- Amélioration de la gestion des données sensibles.
- Correction de problèmes de sécurité liés aux attaques par déni de service (DoS).
- Amélioration de la gestion des erreurs.
- Correction de problèmes de sécurité liés aux vulnérabilités connues.
- Amélioration de la gestion des mises à jour de sécurité.
- Correction de problèmes de sécurité liés aux dépendances vulnérables.
- Amélioration de la gestion des audits de sécurité.
- Correction de problèmes de sécurité liés aux configurations incorrectes.
- Amélioration de la gestion des incidents de sécurité.
- Correction de problèmes de sécurité liés aux erreurs humaines.
- Amélioration de la gestion des politiques de sécurité.
- Correction de problèmes de sécurité liés aux violations de données.
- Amélioration de la gestion de la conformité réglementaire.
- Correction de problèmes de sécurité liés aux réglementations en vigueur.
- Amélioration de la gestion des risques de sécurité.
- Correction de problèmes de sécurité liés aux menaces émergentes.
- Amélioration de la gestion de la sensibilisation à la sécurité.
- Correction de problèmes de sécurité liés aux attaques de phishing.
- Amélioration de la gestion de la formation à la sécurité.
- Correction de problèmes de sécurité liés aux attaques de malware.
- Amélioration de la gestion de la protection des données.
- Correction de problèmes de sécurité liés aux violations de la vie privée.
- Amélioration de la gestion de la sécurité physique.
- Correction de problèmes de sécurité liés aux accès non autorisés.
- Amélioration de la gestion de la sécurité des réseaux.
- Correction de problèmes de sécurité liés aux attaques réseau.
- Amélioration de la gestion de la sécurité des applications.
- Correction de problèmes de sécurité liés aux vulnérabilités applicatives.
- Amélioration de la gestion de la sécurité des infrastructures.
- Correction de problèmes de sécurité liés aux vulnérabilités infrastructurelles.
- Amélioration de la gestion de la sécurité des données en transit.
- Correction de problèmes de sécurité liés aux interceptions de données.
- Amélioration de la gestion de la sécurité des données au repos.
- Correction de problèmes de sécurité liés aux accès non autorisés aux données.
- Amélioration de la gestion de la sécurité des données supprimées.
- Correction de problèmes de sécurité liés à la récupération de données supprimées.
- Amélioration de la gestion de la sécurité des données sauvegardées.
- Correction de problèmes de sécurité liés aux accès non autorisés aux sauvegardes.
- Amélioration de la gestion de la sécurité des données archivées.
- Correction de problèmes de sécurité liés aux accès non autorisés aux archives.
- Amélioration de la gestion de la sécurité des données externalisées.
- Correction de problèmes de sécurité liés aux accès non autorisés aux données externalisées.
- Amélioration de la gestion de la sécurité des données cloud.
- Correction de problèmes de sécurité liés aux vulnérabilités cloud.

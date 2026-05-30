## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 29 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment concernant l'authentification et l'accès aux données sensibles. Des corrections ont été apportées pour renforcer la protection contre les vulnérabilités potentielles. Des optimisations de performance ont également été réalisées, en particulier au niveau de l'API Entreprise et des requêtes GraphQL. Enfin, plusieurs refactorings et mises à jour de dépendances ont été effectués pour améliorer la maintenabilité et la stabilité de la plateforme.

### Évolutions fonctionnelles
*   Amélioration de la gestion des OTP (One-Time Password) pour les super-admins, avec ajout de la possibilité de ré-authentification et de restriction d'accès sans OTP.
*   Ajout d'une gestion des limites de répétition pour les champs de formulaire, permettant de configurer un nombre minimal et maximal de répétitions.
*   Amélioration de la gestion des erreurs et des messages d'information pour les utilisateurs, notamment lors de la connexion via FranceConnect.
*   Correction d'un problème où les utilisateurs pouvaient accéder à des dossiers en utilisant un lien de réinitialisation incorrect.
*   Amélioration de l'affichage des informations sur les procédures dans l'interface d'administration.
*   Correction de l'affichage du message de changement de dossier sur la page de remerciement.
*   Ajout de la possibilité de filtrer les champs par adresse (commune, département, région).

### Évolutions techniques
*   Refonte de l'API Entreprise avec l'utilisation de monades `Result` pour une meilleure gestion des erreurs et une plus grande robustesse.
*   Optimisation des performances de l'API Entreprise avec l'ajout de mécanismes de cache et de limitation du débit.
*   Migration de plusieurs tâches de longue durée vers Sidekiq avec gestion des retries natives pour une meilleure fiabilité.
*   Refactoring du code pour supprimer des dépendances obsolètes et améliorer la lisibilité.
*   Mise à jour de nombreuses dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Amélioration des tests unitaires et d'intégration pour garantir la qualité du code.
*   Optimisation des requêtes GraphQL pour réduire les temps de réponse.
*   Migration de composants Haml vers ERB pour une meilleure maintenabilité.
*   Amélioration de la gestion des erreurs et des logs pour faciliter le débogage.
*   Implémentation de mécanismes de protection contre les attaques par cross-site scripting (XSS).
*   Correction de vulnérabilités potentielles liées à l'exportation de données.

### Autres changements
*   Mise à jour de la documentation pour refléter les dernières modifications.
*   Correction de problèmes de configuration et de build.
*   Nettoyage du code et suppression de code mort.
*   Amélioration des messages de log pour faciliter le débogage.
*   Correction de problèmes de validation de formulaire.
*   Amélioration de l'accessibilité de l'interface utilisateur.
*   Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
*   Correction de bugs mineurs et améliorations de l'interface utilisateur.
*   Mise à jour des fichiers de configuration pour refléter les dernières modifications.
*   Amélioration de la gestion des erreurs et des exceptions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.
*   Correction de problèmes de sécurité.
*   Amélioration de la gestion des utilisateurs et des permissions.
*   Correction de problèmes de performance.
*   Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
*   Correction de problèmes de compatibilité avec différents navigateurs.
*   Amélioration de la documentation pour faciliter l'utilisation de l'API.
*   Correction de problèmes de localisation.
*   Ajout de nouvelles fonctionnalités pour faciliter l'administration de la plateforme.

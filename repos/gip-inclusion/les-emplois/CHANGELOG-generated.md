## Changelog : les-emplois (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant la sécurité, notamment autour de l'authentification multi-facteurs (MFA) et de la gestion des accès. Des évolutions significatives ont également été apportées au module d'insertion, avec une refonte de la gestion des services et des orientations, ainsi qu'une amélioration de l'expérience utilisateur. Enfin, des corrections et des optimisations ont été réalisées sur divers aspects de l'application.

### Évolutions fonctionnelles
- **Authentification :** Renforcement de la sécurité avec l'ajout de la suppression logicielle des dispositifs MFA et la gestion des cas d'utilisation de codes de récupération.
- **Authentification :** Amélioration de la gestion des erreurs et des messages d'information liés à l'authentification à deux facteurs (2FA).
- **Authentification :** Ajout d'exemples d'applications d'authentification pour faciliter la configuration du 2FA.
- **Authentification :** Affichage d'un message d'avertissement pour les utilisateurs professionnels concernant l'activation prochaine du MFA.
- **Insertion :** Possibilité de supprimer "en douceur" les services et structures, permettant une gestion plus flexible des données.
- **Insertion :** Amélioration du suivi des orientations avec l'enregistrement des événements de mobilisation et la liaison avec les iMER (identifiants uniques).
- **Insertion :** Affichage des informations de réception du service (lieu) sur la fiche structure.
- **Insertion :** Suppression de la nécessité d'un numéro de téléphone pour démarrer une orientation.
- **Insertion :** Affichage des détails des frais lorsque le service est payant.
- **Interface Utilisateur :** Affichage du dernier accompagnateur connu au lieu du référent GPS pour les demandeurs d'emploi.
- **Interface Utilisateur :** Ajout d'un bouton pour assigner un utilisateur à un accompagnement.
- **Interface Utilisateur :** Amélioration de la navigation et de la clarté des messages.
- **Structures :** Désactivation automatique des offres d'emploi spontanées après 90 jours d'inactivité.
- **Structures :** Envoi d'un email aux administrateurs lors de la désactivation des offres d'emploi spontanées.

### Évolutions techniques
- **Sécurité :** Simplification et amélioration de la gestion des permissions et des règles d'accès.
- **FranceConnect :** Suppression des URLs de déconnexion obsolètes.
- **API :** Envoi des données d'orientation au format JSON pour une meilleure compatibilité avec DORA.
- **Tests :** Ajout de tests de régression pour la gestion du MFA et correction de tests instables.
- **Refactoring :** Refactorisation du code lié à la gestion des identifiants et des connexions.
- **Déploiement :** Mise à jour des dépendances et des outils de construction.
- **Base de données :** Optimisation des requêtes pour améliorer les performances.
- **Monitoring :** Ajout de suivi Matomo pour les soumissions de l'assistant d'orientation.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés.
- **Configuration :** Modification de la configuration pour améliorer la flexibilité et la maintenabilité.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Accessibilité :** Mise à jour des liens de déclaration d'accessibilité.
- **Divers :** Corrections de fautes de frappe et améliorations de la qualité du code.

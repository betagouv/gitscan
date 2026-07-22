## Changelog : recommandations-collaboratives (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière d'authentification (ajout d'une option de connexion par code, amélioration de la gestion de l'authentification à deux facteurs) et de gestion des organisations et des projets. Des travaux ont également été réalisés pour préparer l'intégration de plugins et améliorer la sécurité du projet.

### Évolutions fonctionnelles
- **Authentification :** Ajout d'une méthode de connexion par code, en complément de l'authentification par email/mot de passe.
- **Authentification à deux facteurs (2FA) :** Amélioration de la gestion de la 2FA, avec la possibilité de désactiver la 2FA pour les comptes de service et une configuration plus flexible.
- **Interface utilisateur :**
    - Amélioration de l'affichage des informations sur les projets (ajout d'un indicateur de statut).
    - Refonte de la page d'accueil et de la page des organisations.
    - Amélioration de l'accessibilité des éléments d'interface.
- **Gestion des projets :**
    - Ajout d'une colonne "Raison de la pause" pour les projets inactifs.
    - Possibilité de filtrer les projets par statut de lecture des recommandations.
    - Amélioration de l'interface de fusion des organisations.
- **Notifications :** Amélioration de la visibilité des notifications.

### Évolutions techniques
- **Plugins :**
    - Intégration d'un système de plugins pour étendre les fonctionnalités de l'application.
    - Amélioration de la gestion des migrations et de la sécurité des plugins.
    - Refonte de la gestion des assets (JavaScript, CSS) pour les plugins.
- **Dépendances :** Mise à jour de plusieurs dépendances (Django, Wagtail, Axios, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Refactoring :**
    - Simplification et clarification de plusieurs parties du code.
    - Suppression de code obsolète.
    - Amélioration de la structure du code pour faciliter la maintenance et l'évolution.
- **CI/CD :** Amélioration de la configuration du pipeline CI/CD.
- **Suppression de `requirements.txt` :** Le fichier `requirements.txt` a été supprimé, la gestion des dépendances étant désormais assurée par d'autres outils.

### Autres changements
- Documentation mise à jour pour le système de plugins.
- Ajout de tests unitaires pour les nouvelles fonctionnalités.
- Nettoyage du code et correction de petites erreurs.
- Suppression de fichiers inutiles du dépôt.
- Amélioration des messages d'erreur et des validations de formulaire.
- Correction de problèmes de sécurité mineurs.

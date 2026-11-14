## Changelog : le-marche (30 derniers jours, au 13 novembre 2026)

### Résumé
Cette période a été principalement consacrée au renforcement de la sécurité de la plateforme et à la protection des données (conformité RGPD). Un effort important a été réalisé pour garantir que chaque utilisateur n'accède qu'aux informations qui le concernent, tout en nettoyant en profondeur le code pour améliorer la stabilité et la maintenabilité du système.

### Évolutions fonctionnelles

**Sécurité et Confidentialité**
- **Renforcement de l'authentification :** Protection contre l'énumération d'utilisateurs lors de l'inscription, gestion des inscriptions simultanées avec le même email et sécurisation des liens de confirmation d'adresse.
- **Protection des données personnelles :** Masquage des parties locales des adresses email, limitation de la visibilité des contacts des SIAE inactifs ou radiés, et restriction de l'accès aux listes de favoris aux seuls propriétaires.
- **Contrôle d'accès strict :** Limitation des droits de consultation des appels d'offres, des réponses des prestataires et des détails des structures au périmètre autorisé de l'utilisateur ou de son entreprise.
- **Correction de vulnérabilités :** Résolution de failles de type XSS (Alpine.js), de problèmes d'IDOR (accès non autorisé via l'URL) et de risques liés à la création anonyme d'appels d'offres.

**Expérience Utilisateur et Fonctionnalités**
- **Parcours SIAE :** Nouveau flux permettant aux utilisateurs SIAE d'ajouter leur structure une fois leur adresse confirmée.
- **Améliorations de l'interface :** Optimisation de l'affichage des cartes (Leaflet), des tableaux de messages de conversation et sécurisation des exports de données (CSV/XLSX) contre les injections de formules.
- **Gestion du contenu :** Amélioration de la visibilité du plan du site et nettoyage des comptes de spam.

### Évolutions techniques

**Refactoring et Maintenance**
- **Nettoyage du code :** Suppression massive de code mort (méthodes, propriétés, fonctions utilitaires et templates inutilisés) dans les modules SIAE, Utilisateurs, Appels d'offres et Achats.
- **Mise à jour du CMS :** Adaptation et mise à jour des composants Wagtail et du système de design (django-dsfr) pour assurer la compatibilité des modèles de contenu.

**Infrastructure et Performance**
- **Montée de version majeure :** Passage à Django 6.0.
- **Stabilité système :** Amélioration de la connexion Redis, fiabilisation des tâches de fond (Huey) et des notifications Slack.
- **Optimisation :** Augmentation de la fréquence de mise à jour des compteurs d'appels d'offres.
- **CI/CD :** Amélioration des workflows de déploiement (linting) et de la configuration des environnements de revue.

**Sécurité Système**
- **Protection des logs :** Masquage des secrets d'authentification dans les champs d'URL enregistrés dans les journaux.
- **Sécurisation du stockage :** Durcissement des politiques d'upload sur les serveurs S3.

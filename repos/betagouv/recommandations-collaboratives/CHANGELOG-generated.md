## Changelog : recommandations-collaboratives (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des organisations et des projets, ainsi que sur l'ajout de fonctionnalités de sécurité et la correction de bugs. L'implémentation d'un système de plugins a également été avancée.

### Évolutions fonctionnelles
- Amélioration de la page de fusion d'organisations avec une nouvelle interface et des informations plus claires sur les données de chaque organisation.
- Ajout d'une limitation de l'auto-connexion pour renforcer la sécurité.
- Possibilité de masquer le bouton de création de nouveau projet via un flag de fonctionnalité.
- Ajout d'un indicateur visuel pour les organisations suggérées sélectionnées.
- Amélioration de la gestion des messages de conversation, avec la possibilité d'envoyer des documents.
- Ajout d'un champ "paused_by" dans le modèle de projet pour indiquer qui a mis le projet en pause.
- Amélioration de l'affichage des informations utilisateur lorsqu'un projet est mis en pause par un administrateur.
- Correction d'un bug empêchant l'application du flag "missing flag onboarding" sur les pages d'accueil et de connexion.
- Correction d'un bug lié à l'application des plugins spécifiques au tenant.
- Correction d'un bug empêchant la suppression du fichier dans le formulaire "pousse-reco".
- Ajout de la possibilité de valider une adresse email Brevo sur la page d'accueil.
- Amélioration de la gestion des erreurs et des validations de formulaire.

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de plusieurs dépendances, notamment Wagtail, Vite, Babel, form-data, tar et dompurify.
- Amélioration de la gestion des plugins, avec une meilleure documentation et une gestion plus sécurisée des schémas.
- Correction de problèmes liés à l'importation des fichiers JavaScript dans les plugins.
- Amélioration des tests pour plus de robustesse.
- Suppression des fichiers `requirements.txt` et utilisation de `uv` pour la gestion des dépendances.
- Correction de problèmes liés à l'activité middleware.
- Amélioration de la configuration du CI/CD.

### Autres changements
- Ajout de plugins au `.gitignore`.
- Mise à jour de la documentation pour refléter les changements apportés.
- Nettoyage du code et suppression de code inutilisé.
- Correction de typos et amélioration de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration des messages d'erreur et des logs.
- Mise à jour des icônes et des styles CSS.
- Ajout de tests unitaires et d'intégration.

## Changelog : meet (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout d'un sondage de satisfaction optionnel en fin de réunion, des améliorations de l'accessibilité, et des optimisations de performance via le chargement paresseux de certains composants. Des correctifs ont également été apportés pour améliorer la stabilité et la sécurité, ainsi que des fonctionnalités pour la gestion des utilisateurs et l'intégration avec des outils externes.

### Évolutions fonctionnelles
- Ajout d'un sondage de satisfaction optionnel en bas de l'écran de réunion.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL.
- Amélioration de la réduction du bruit grâce à un pipeline de traitement audio BBBA.
- Les participants sont mis en sourdine par défaut lors de l'entrée dans une grande réunion.
- Le son de notification d'entrée est désactivé dans les grandes salles.
- Ajout d'un administrateur spécifique aux fichiers.
- Support étendu pour tous les types de fichiers vidéo et audio.
- Possibilité de configurer et de définir le niveau d'accès des salles via l'API externe.
- Ajout d'un analyseur S3 pour les enregistrements.
- Amélioration de l'intégration de l'add-on Outlook avec support i18n, lien de feedback et insertion intelligente de liens.

### Évolutions techniques
- Mise à jour de plusieurs dépendances, notamment `react-i18next`, `libcrypto3`, `libssl3`, `eslint-plugin-react-hooks`, `aiohttp` et les dépendances Python.
- Optimisation du chargement des composants frontend via le "lazy loading" (chargement paresseux) pour améliorer les performances.
- Refactorisation du code frontend pour améliorer la modularité et la maintenabilité.
- Amélioration de la configuration de l'environnement de développement (devx) avec des variables d'environnement plus claires et une meilleure organisation.
- Mise à jour du chart Helm pour faciliter le déploiement.
- Amélioration de la robustesse du processus de suppression de fichiers côté backend.
- Correction de problèmes de configuration CSP (Content Security Policy) pour éviter des régressions.
- Utilisation de la nouvelle méthode d'importation d'icônes Material pour optimiser la taille des assets.
- Amélioration de la gestion des erreurs et des conditions de concurrence dans le backend.

### Autres changements
- Ajout d'un badge DPG au fichier README.
- Correction de l'étiquetage ARIA pour améliorer l'accessibilité des effets vidéo.
- Mise à jour de la documentation de l'API externe.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des versions de release à 1.17.0, 1.18.0, 1.19.0, 1.20.0 et 1.21.0.

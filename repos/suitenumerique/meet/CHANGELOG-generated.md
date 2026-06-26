## Changelog : meet (30 derniers jours, au 24 juin 2026)

### Résumé
Ce changelog couvre les 30 derniers jours et met en évidence des améliorations significatives en termes de gestion des fichiers, de stabilité, d'accessibilité et de performance. Des optimisations ont été apportées au frontend pour réduire la taille des bundles et améliorer la vitesse de chargement, tandis que des correctifs de sécurité et des améliorations de la gestion des utilisateurs ont été implémentés côté backend. L'addon Outlook a également été amélioré avec de nouvelles fonctionnalités et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout d'un mécanisme de nettoyage des fichiers supprimés et en attente, avec une tâche cron pour automatiser ce processus.
- Implémentation d'un sondage de satisfaction optionnel en bas des réunions.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL.
- Amélioration de l'intégration de l'addon Outlook : ajout d'un lien de feedback, amélioration de l'insertion du lien de réunion et ajout d'un paramètre pour la source Outlook.
- Support étendu pour tous les types de fichiers vidéo et audio.
- Ajout d'un administrateur spécifique pour la gestion des fichiers.
- Possibilité de configurer et de limiter l'accès aux salles de réunion via l'API externe.
- Ajout d'un mécanisme pour fusionner les utilisateurs en double.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (posthog-js, core-js, idna, urllib3, eslint-plugin-react-hooks).
- Optimisation du chargement des dépendances frontend via le code splitting et le lazy loading (libcrypto3, libssl3, @libreaudio/la-call, LiveKit, Material icons).
- Amélioration de la configuration Helm pour inclure les labels d'application et le nom de la tâche cron.
- Amélioration de la robustesse du processus de suppression des fichiers côté backend.
- Refactorisation de la gestion des variables d'environnement pour une meilleure organisation et cohérence.
- Utilisation de Rollup pour la visualisation des bundles et l'optimisation de la taille du code frontend.
- Amélioration de la gestion des erreurs et des exceptions dans l'agent d'extraction de métadonnées.
- Mise à jour des dépendances Python.
- Amélioration de la gestion des états de fichiers pour éviter les blocages.

### Autres changements
- Ajout d'un badge DPG au fichier README.
- Amélioration de l'accessibilité des effets vidéo (aria labels, structure).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Corrections de CSP (Content Security Policy) pour éviter les problèmes de compatibilité.
- Amélioration de la gestion des logs.
- Bump de version : 1.17.0, 1.18.0, 1.19.0, 1.20.0, 1.21.0.

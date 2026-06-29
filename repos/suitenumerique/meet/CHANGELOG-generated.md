## Changelog : meet (30 derniers jours, au 28 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout de fonctionnalités comme des sondages de satisfaction, l'amélioration de la réduction du bruit et des options de gestion des participants. Des optimisations de performance ont également été apportées, notamment par le chargement différé de certains composants et la réduction de la taille des paquets JavaScript. Des corrections de sécurité et des mises à jour de dépendances ont également été incluses.

### Évolutions fonctionnelles
- Ajout d'un sondage de satisfaction optionnel en fin de réunion.
- Amélioration de la réduction du bruit grâce à un pipeline de traitement audio BBBA.
- Possibilité de désactiver le login silencieux via un paramètre d'URL.
- Possibilité de masquer le bouton de login via un paramètre d'URL.
- Mise en place d'un comportement par défaut de mise en sourdine des participants lors de l'entrée dans une grande réunion.
- Ajout d'une commande pour nettoyer les fichiers en attente et supprimés.
- Support étendu pour tous les types de fichiers vidéo/audio dans les résumés de réunion.
- Ajout d'un administrateur spécifique aux fichiers.
- Possibilité de fusionner des utilisateurs dupliqués via une commande de gestion.
- Ajout d'un lien vers un formulaire de feedback dans l'addon Outlook.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (posthog-js, core-js, idna, urllib3, react-i18next).
- Amélioration de la robustesse du processus de suppression de fichiers.
- Optimisation du chargement des composants frontend par le chargement différé (lazy loading) et le code splitting.
- Refactorisation de la configuration des variables d'environnement backend.
- Amélioration de la configuration de la chaîne CI/CD (construction ciblée pour arm64, gestion des jobs Kubernetes).
- Utilisation de SVG importés individuellement pour les icônes Material afin d'optimiser la taille des paquets.
- Migration vers ESLint 9.
- Remplacement de l'API Room Options dépréciée.

### Autres changements
- Ajout d'un badge DPG au README.
- Documentation de la configuration du favicon via un volume mount.
- Correction de plusieurs problèmes d'accessibilité dans l'interface utilisateur (étiquettes ARIA, structure des effets vidéo).
- Mise à jour de la documentation de l'API externe pour la configuration des salles.
- Bump de version : 1.17.0, 1.18.0, 1.19.0, 1.20.0, 1.21.0.
- Amélioration de la gestion des erreurs et des exceptions dans les agents.
- Correction de bugs mineurs et améliorations de la qualité du code.

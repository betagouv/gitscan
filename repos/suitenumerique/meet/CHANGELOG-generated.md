## Changelog : meet (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout de fonctionnalités comme le picture-in-picture, les réactions, et une meilleure gestion des permissions de muting. Des corrections de bugs et des mises à jour de sécurité ont également été apportées, ainsi que des optimisations techniques pour améliorer la performance et la stabilité de la plateforme. L'addon Outlook a été amélioré avec la prise en charge de l'internationalisation et l'ajout d'un formulaire de feedback.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité Picture-in-Picture (PiP) pour les réunions, incluant une barre de contrôle et un affichage de l'état de connexion.
- Implémentation des réactions pendant les réunions, avec une navigation accessible au clavier et une adaptation pour les appareils mobiles.
- Possibilité pour les participants de couper le son des autres en fonction de la configuration de la salle.
- Amélioration de l'addon Outlook : prise en charge de l'internationalisation, ajout d'un lien vers un formulaire de feedback, et insertion intelligente des liens de réunion.
- Support étendu des types de fichiers pour l'enregistrement des réunions.
- Amélioration de l'assignation des intervenants.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (idna, urllib3, eslint-plugin-react-hooks, aiohttp).
- Refactorisation du code frontend pour améliorer le code splitting et réduire la taille des bundles JavaScript.
- Utilisation de SVG importés directement pour les icônes, optimisant ainsi leur taille et leur performance.
- Amélioration de la synchronisation de la configuration des salles.
- Refactorisation de la gestion des permissions de muting.
- Mise à jour de l'infrastructure de build et de déploiement (Tiltfile, Kubernetes jobs).
- Amélioration de la robustesse du processus de suppression de fichiers.
- Ajout d'un admin spécifique pour la gestion des fichiers.
- Correction de bugs et amélioration de la stabilité du metadata extractor.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'API.
- Correction de bugs mineurs dans l'interface utilisateur et le backend.
- Amélioration des logs pour faciliter le débogage.
- Mise à jour des versions des releases (1.19.0, 1.18.0, 1.17.0, 1.16.0).
- Correction de la configuration CSP pour éviter les erreurs.
- Ajout d'un message de fallback lorsque la fermeture automatique d'un dialogue échoue.
- Paramétrisation de la configuration Nginx du frontend via un volume.
- Ajout d'un badge "beta" avec le style de l'UI kit.
- Suppression d'une dépendance inutile (vite-tsconfig-paths).
- Correction d'un problème de positionnement des tooltips.
- Ajout de tests pour la couverture du code.
- Correction d'un bug lié à la concurrence lors de la création d'utilisateurs.
- Correction d'un bug lié à la gestion des états des fichiers.
- Correction d'un bug lié à la configuration des variables d'environnement.

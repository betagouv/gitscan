## Changelog : drive (30 derniers jours)

### Résumé
Ce mois-ci, la Suite Drive a bénéficié d'améliorations significatives en termes de fonctionnalités, de stabilité et d'expérience utilisateur. Les nouveautés incluent la gestion des modèles de fichiers, la personnalisation de l'interface, l'amélioration de la gestion des accès, et des corrections de bugs pour une meilleure fluidité. Des optimisations techniques ont également été apportées pour améliorer les performances et la scalabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la création de fichiers à partir de modèles (#508534b).
- Possibilité de personnaliser l'interface avec des CSS et JS injectés via la configuration (#898b3ff, #abe4ca1).
- Amélioration de la gestion des accès et des permissions avec la prise en compte des rôles hérités (#7b18daf, #dca39e3).
- Ajout d'un menu contextuel accessible via un clic droit sur les éléments (#31454e2, #42b24ca).
- Implémentation de la synchronisation de la langue de l'interface utilisateur avec les préférences de l'utilisateur (#35c6c19).
- Ajout de la fonctionnalité de connexion silencieuse (silent login) pour une expérience utilisateur plus fluide (#7291d6c).
- Possibilité de rediriger vers une page d'accueil externe (#a965203).
- Ajout de la gestion des notes de version pour informer les utilisateurs des dernières nouveautés (#9bf7fa7).
- Amélioration de la gestion des partages de fichiers et de dossiers (#aaa5d9e).
- Ajout de la possibilité de déplacer des éléments vers la racine (#8251464).

### Évolutions techniques
- Optimisation du workflow Docker Hub pour des builds plus rapides (#564822d).
- Amélioration de la configuration de Celery pour une meilleure gestion des tâches asynchrones (#ba73c4a, #e2d6d4e).
- Mise à jour de plusieurs dépendances, notamment Django (v5.2.11) et Playwright (v1.58.2) (#dc29f2f, #edc8d2c).
- Refonte de l'architecture de gestion des accès pour une meilleure performance (#926396c).
- Amélioration de la gestion des erreurs et des exceptions (#a78b017).
- Ajout de la prise en charge de l'architecture ARM64 pour les images Docker (#f43c8a4).
- Amélioration des tests E2E pour une meilleure couverture et stabilité (#f2730e5, #4f805e7).
- Refactorisation du code frontend pour une meilleure maintenabilité (#a0cfb60, #e3527a3).
- Amélioration de la gestion des fichiers avec des caractères spéciaux dans leur nom (#0823972).

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés (#36b39a6, #c89aa81).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de code obsolète et nettoyage du codebase.
- Amélioration de la configuration Helm pour une meilleure flexibilité (#d9a05cb, #6089c7b).
- Mise à jour des icônes et des composants d'interface utilisateur (#782804f, #6e8b0a9).

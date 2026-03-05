## Changelog : meet (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de l'accessibilité et des performances de Meet. Des correctifs ont été apportés pour résoudre des vulnérabilités, améliorer la navigation au clavier et optimiser l'efficacité du code. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'accès aux paramètres et améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout d'un raccourci clavier (Ctrl+Shift+/) pour ouvrir les paramètres des raccourcis [#1050](https://github.com/suitenumerique/meet/issues/1050).
- Amélioration de l'accessibilité du dialogue de participation à une réunion.
- Ajout d'un lien cliquable vers les paramètres généraux dans la fenêtre d'inactivité.
- Possibilité d'utiliser les touches Shift et Alt dans la configuration des raccourcis.
- Ajout de raccourcis supplémentaires pour améliorer l'accessibilité.
- Exposition du lien vers l'application Windows.

### Évolutions techniques
- Renforcement de la validation des entrées API pour améliorer la sécurité [#1053](https://github.com/suitenumerique/meet/issues/1053).
- Refactorisation de la gestion des permissions au niveau de l'API backend.
- Optimisation des requêtes SQL dans l'interface d'administration pour améliorer les performances.
- Mise à jour de Django pour corriger plusieurs vulnérabilités de sécurité.
- Passage à une image de base Alpine pour le microservice de résumé, améliorant la sécurité et la taille de l'image.
- Amélioration de la gestion des erreurs liées aux fichiers dans le microservice de résumé.
- Introduction d'un Ingress Kubernetes dédié pour le webhook LiveKit.
- Refactorisation des tests d'API externes.
- Amélioration de la configuration de l'environnement pour les déploiements Scalingo.
- Mise à jour des dépendances Python et JavaScript.
- Optimisation du code frontend pour éviter les recalculs inutiles.
- Suppression de `curl` de l'image de production frontend.
- Utilisation de la même identité utilisateur en production et en développement pour Tilt.
- Ajout de support pour la plateforme ARM64 dans les builds Docker.
- Mise à jour des étapes des actions GitHub pour utiliser les dernières versions.

### Autres changements
- Mise à jour de la documentation pour inclure les instructions de déploiement sur Scalingo.
- Correction de fautes de frappe dans la documentation.
- Mise à jour des termes juridiques.
- Correction de problèmes d'accessibilité liés aux focus rings et aux lecteurs d'écran.
- Amélioration de la localisation des étiquettes des modificateurs de lecteur d'écran.
- Correction d'un bug empêchant la mise à jour des préférences linguistiques en allemand.
- Mise à jour du changelog.

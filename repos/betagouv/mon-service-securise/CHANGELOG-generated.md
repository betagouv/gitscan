## Changelog : mon-service-securise (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'interface utilisateur avec l'intégration du Design System de l'État (DSFR), l'amélioration de l'expérience utilisateur sur les pages de service, et l'ajout de nouvelles fonctionnalités liées à la gestion des risques et des indices cyber. Des corrections de bugs et des améliorations de performance ont également été apportées.

### Évolutions fonctionnelles
- Intégration du header DSFR pour une meilleure cohérence visuelle et une navigation améliorée.
- Affichage des indices cyber (ANSSI et personnalisé) dans l'en-tête des pages de service.
- Ajout d'une nouvelle page "Indice Cyber" avec un radar et des visualisations des données.
- Amélioration de la navigation et de l'affichage des dossiers d'homologation.
- Ajout de la possibilité de télécharger le tampon d'homologation.
- Affichage des contacts utiles du service.
- Amélioration de la page "Décrire V2" avec une intégration plus fluide.
- Ajout d'une gestion des rubriques spécifiques aux différentes versions de service.
- Affichage des risques V1 et V2.
- Génération d'un PDF d'annexe pour les risques V2, incluant les matrices et la légende.
- Ajout d'un bouton pour la gestion des contributeurs.
- Amélioration de la visite guidée pour les étapes "Sécuriser" et "Homologuer".

### Évolutions techniques
- Migration vers les dernières versions des dépendances (Express, PostgreSQL, bcrypt, jsonwebtoken, axios, pg, knex, Svelte, Vite, etc.).
- Refonte de la navigation avec le composant `dsfr-navigation`.
- Utilisation des composants DSFR pour le footer et le menu.
- Transformation de plusieurs pages (Mesures, Décrire V2) en Single Page Applications (SPA) avec Svelte.
- Utilisation d'un objet de données unique pour le service complet, facilitant l'accès aux informations.
- Amélioration de la structure du code et factorisation de composants.
- Ajout de tests d'accessibilité avec Playwright et Axe.
- Configuration de l'exécution des tests d'accessibilité dans les workflows CI/CD.
- Amélioration des workflows de déploiement Clever Cloud.

### Autres changements
- Correction de plusieurs bugs et améliorations de l'expérience utilisateur.
- Suppression de code obsolète et nettoyage du code.
- Mise à jour de la documentation.
- Correction de problèmes de typographie.
- Amélioration des performances.
- Correction d'erreurs d'accessibilité.
- Suppression du bandeau de promotion de MSC.
- Suppression de l'ancien menu de navigation.
- Correction de problèmes de scroll et d'affichage.
- Ajustement de la longueur des titres et des sous-titres.
- Amélioration de la gestion des erreurs.
- Ajout de commentaires et de documentation pour faciliter la maintenance.

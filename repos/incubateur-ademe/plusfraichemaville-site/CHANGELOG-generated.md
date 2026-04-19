## Changelog : plusfraichemaville-site (30 derniers jours, au 17 mai 2026)

### Résumé
Le site plusfraichemaville a connu une période d'amélioration significative ces dernières semaines, avec un accent particulier sur l'expérience utilisateur lors de la création de projets et le suivi des données d'utilisation. Des améliorations ont été apportées à la page d'accueil, au formulaire de création de projet, et à l'intégration de nouvelles métriques de suivi. Une migration vers un nouveau système de gestion des erreurs (Sentry) a également été réalisée pour améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- **Création de projet :** Refonte complète du flux de création de projet avec un formulaire étape par étape [#484](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/484), incluant un bouton d'annulation [#486](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/486) et une alerte pour éviter la perte de données en cas de fermeture intempestive.
- **Page d'accueil :** Nouvelle page d'accueil avec une refonte du design [#487](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/487).
- **Annuaire des projets :** Ajout d'un suivi du nombre de vues des projets dans l'annuaire [#486](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/486).
- **Fiches solutions et diagnostics :** Enregistrement des fiches solutions et diagnostics consultées par chaque utilisateur pour un meilleur suivi de l'utilisation [#482](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/482).
- **Module surchauffe urbaine :** Ajout d'une interface utilisateur pour le module surchauffe urbaine [#478](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/478).
- **Lien vers l'estimation :** Ajout d'un lien vers l'estimation dans les fiches solutions [#477](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/477).
- **Amélioration de l'accessibilité :** Ajout d'attributs `alt` pour l'accessibilité des images dans le carrousel.
- **Gestion des erreurs Cartagène :** Correction de l'affichage des erreurs Cartagène pour éviter les fausses alertes [#481](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/481).

### Évolutions techniques
- **Migration Sentry :** Migration vers un nouveau système de gestion des erreurs (Sentry) pour une meilleure surveillance et résolution des problèmes [#480](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/480).
- **Mise à jour des dépendances :** Mise à jour des dépendances pour améliorer la sécurité et la performance.
- **Utilisation de pnpm :** Passage de npm à pnpm pour la gestion des dépendances.
- **Refactoring et optimisation :** Amélioration du code et suppression de code inutilisé.
- **Mise à jour Tailwind CSS :** Mise à jour de la version de Tailwind CSS.

### Autres changements
- Amélioration des logs pour les erreurs 404 dans Sentry.
- Ajout d'un callback URL et d'une action sur la page de création de projet.
- Amélioration du design de la page "Mes projets" pour une meilleure réactivité.
- Correction de typos.

## Changelog : code-du-travail-numerique (30 derniers jours, au 2026-07-31)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout d'un système de notation des contributions, l'amélioration du suivi des actions des utilisateurs (tracking) et des corrections de bugs pour une meilleure stabilité et fluidité de l'application. Des ajustements ont également été apportés à la gestion des thèmes et des conventions collectives.

### Évolutions fonctionnelles
- Ajout d'un système de notation des contributions pour recueillir les retours des utilisateurs ([#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344)).
- Ajout d'un événement de suivi pour mesurer le taux de complétion des contributions ([#7426](https://github.com/SocialGouv/code-du-travail-numerique/issues/7426)).
- Ajout des tags de thème et de sous-thème en haut des pages de contribution pour une meilleure organisation de l'information ([#7393](https://github.com/SocialGouv/code-du-travail-numerique/issues/7393)).
- Suppression du bloc de partage sur les pages, sauf pour les actualités, simplifiant l'interface utilisateur ([#7392](https://github.com/SocialGouv/code-du-travail-numerique/issues/7392)).
- Ajout d'un score NPS (Net Promoter Score) sur le site pour évaluer la satisfaction des utilisateurs ([#7382](https://github.com/SocialGouv/code-du-travail-numerique/issues/7382)).
- Amélioration de la gestion des retours sur le tracking des contributions ([#7427](https://github.com/SocialGouv/code-du-travail-numerique/issues/7427)).
- Réinitialisation de la modale de convention collective à l'arrivée externe et ajout du nom de la CC en H2 ([#7389](https://github.com/SocialGouv/code-du-travail-numerique/issues/7389)).
- Correction de l'affichage du NPS : ne plus afficher la fenêtre si l'utilisateur ne souhaite pas répondre ([#7406](https://github.com/SocialGouv/code-du-travail-numerique/issues/7406)).

### Évolutions techniques
- Utilisation de Zod pour la validation des entrées des APIs, améliorant la robustesse et la sécurité ([#7407](https://github.com/SocialGouv/code-du-travail-numerique/issues/7407)).
- Migration des builds d'images de buildkit-service vers buildkit-operator ([#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354)).
- Utilisation des accords dans l'ES à la place de l'API Legifrance ([#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381)).
- Nettoyage des URLs trackées par Matomo pour une meilleure précision des données ([#7409](https://github.com/SocialGouv/code-du-travail-numerique/issues/7409)).
- Correction d'un problème de focus lors de la recherche automatique dans l'entreprise ([#7391](https://github.com/SocialGouv/code-du-travail-numerique/issues/7391)).
- Correction de niveaux de headings incorrects dans les actualités.

### Autres changements
- Documentation générée pour le plan de tracking des événements ([#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343)).
- Fin de l'A/B test sur la convention collective, conservation de la version 3 avec boutons radio ([#7379](https://github.com/SocialGouv/code-du-travail-numerique/issues/7379)).
- Suppression de la sélection de convention collective dans l'en-tête ([#7388](https://github.com/SocialGouv/code-du-travail-numerique/issues/7388)).
- Désactivation de Husky lors d'une release pour éviter des erreurs de build.
- Correction d'une ancre d'accordéon dans les tests E2E.
- Correction d'un bug empêchant le tracking de la notation dans Matomo ([#7390](https://github.com/SocialGouv/code-du-travail-numerique/issues/7390)).
- Correction d'un bug sur le bouton de fermeture du mode plein écran pour les tableaux ([#7373](https://github.com/SocialGouv/code-du-travail-numerique/issues/7373)).

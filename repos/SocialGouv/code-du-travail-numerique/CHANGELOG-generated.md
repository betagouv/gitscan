## Changelog : code-du-travail-numerique (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de l'expérience utilisateur, notamment l'ajout d'un système de notation des contributions, l'intégration d'un score NPS pour évaluer la satisfaction des utilisateurs, et des corrections de bugs pour améliorer la stabilité et la fluidité de l'application. Des optimisations techniques ont également été apportées, notamment concernant l'infrastructure de build et l'utilisation des accords.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions, permettant aux utilisateurs de donner leur avis ([#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344)).
- Intégration d'un score NPS (Net Promoter Score) pour mesurer la satisfaction des utilisateurs ([#7382](https://github.com/SocialGouv/code-du-travail-numerique/issues/7382)).
- Suppression du bloc de partage sur toutes les pages sauf les actualités ([#7392](https://github.com/SocialGouv/code-du-travail-numerique/issues/7392)).
- Amélioration de la gestion des conventions collectives : réinitialisation de la modale et affichage du nom de la convention collective ([#7389](https://github.com/SocialGouv/code-du-travail-numerique/issues/7389)).
- Correction d'un bug empêchant la fermeture du mode plein écran sur les tableaux ([#7373](https://github.com/SocialGouv/code-du-travail-numerique/issues/7373)).

### Évolutions techniques
- Migration des builds d'images de buildkit-service vers buildkit-operator ([#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354)).
- Utilisation des accords dans l'ES (Environnement de Simulation) à la place de l'API Legifrance ([#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381)).
- Mise à jour de pnpm vers la version 11 et corrections des problèmes associés.
- Ajout d'un système d'extraction d'événements statiques et de vérification de la dérive des événements pour le suivi analytique ([#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)).
- Ajout de logs pour la recherche DILA.
- Désactivation de Husky lors des releases pour améliorer la stabilité du processus.

### Autres changements
- Correction d'un bug lié à l'affichage du NPS si l'utilisateur refuse de répondre ([#7406](https://github.com/SocialGouv/code-du-travail-numerique/issues/7406)).
- Correction d'un bug empêchant le bon fonctionnement du focus lors de la recherche automatique.
- Correction de niveaux de heading incorrects dans la section actualités.
- Correction d'un problème d'ancrage des accordéons.
- Correction d'un problème de publication npm, ajout d'une tentative de republish.
- Correction d'un bug lié à l'envoi de la notation dans Matomo.

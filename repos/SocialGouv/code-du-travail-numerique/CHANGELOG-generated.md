## Changelog : code-du-travail-numerique (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment l'ajout d'un système de notation des contributions, la gestion du Net Promoter Score (NPS) et des corrections de bugs concernant l'affichage et le fonctionnement de certaines fonctionnalités. Des optimisations techniques ont également été réalisées pour améliorer la robustesse et la qualité du code.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions, permettant aux utilisateurs de donner leur avis. ([#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344))
- Implémentation du Net Promoter Score (NPS) pour mesurer la satisfaction des utilisateurs. ([#7382](https://github.com/SocialGouv/code-du-travail-numerique/issues/7382))
- Amélioration de l'affichage des actualités avec la suppression du bloc de partage, sauf pour les actualités elles-mêmes. ([#7392](https://github.com/SocialGouv/code-du-travail-numerique/issues/7392))
- Correction de l'affichage des titres dans les actualités.
- Amélioration de la gestion de la convention collective lors de l'arrivée depuis une source externe. ([#7389](https://github.com/SocialGouv/code-du-travail-numerique/issues/7389))
- Correction du comportement de la fenêtre NPS pour éviter les sollicitations répétées. ([#7406](https://github.com/SocialGouv/code-du-travail-numerique/issues/7406))
- Correction de l'envoi des données de notation dans Matomo en ajoutant le user-agent. ([#7390](https://github.com/SocialGouv/code-du-travail-numerique/issues/7390))

### Évolutions techniques
- Validation des entrées des APIs avec Zod pour une meilleure robustesse. ([#7407](https://github.com/SocialGouv/code-du-travail-numerique/issues/7407))
- Utilisation des accords dans l'ES à la place de l'API Legifrance. ([#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381))
- Migration des builds d'images de buildkit-service vers buildkit-operator. ([#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354))
- Génération de la documentation du plan de tracking à partir des événements. ([#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343))
- Correction des problèmes liés à la publication npm après une release. ([#7420](https://github.com/SocialGouv/code-du-travail-numerique/issues/7420))
- Mise à jour de pnpm vers la version 11 et corrections des problèmes associés.

### Autres changements
- Ajout d'un événement pour suivre la complétion d'une contribution. ([#7426](https://github.com/SocialGouv/code-du-travail-numerique/issues/7426))
- Désactivation de Husky lors d'une release.
- Correction des ancres des accordéons dans les tests E2E.
- Fin d'un A/B test sur la convention collective, conservation de la version 3 avec boutons radio. ([#7379](https://github.com/SocialGouv/code-du-travail-numerique/issues/7379))
- Suppression de la sélection de convention collective dans l'en-tête. ([#7388](https://github.com/SocialGouv/code-du-travail-numerique/issues/7388))
- Ajout de logs sur la recherche DILA.

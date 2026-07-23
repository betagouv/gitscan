## Changelog : code-du-travail-numerique (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations à l'expérience utilisateur, notamment l'ajout d'un score NPS pour évaluer la satisfaction, la suppression du bloc de partage sur certaines pages, et des corrections de bugs concernant la notation des contributions et le comportement de la recherche. Des améliorations techniques ont également été apportées pour la gestion des builds et l'utilisation des accords.

### Évolutions fonctionnelles
- Ajout d'un score NPS (Net Promoter Score) sur le site pour mesurer la satisfaction des utilisateurs. [#7382](https://github.com/SocialGouv/code-du-travail-numerique/issues/7382)
- Suppression du bloc de partage sur toutes les pages, sauf sur les actualités. [#7392](https://github.com/SocialGouv/code-du-travail-numerique/issues/7392)
- Ajout d'un widget de notation pour les contributions. [#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344)
- Ajout du type "bon à savoir" pour les contributions. [#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)
- Correction pour ne pas déplacer le focus sur les résultats lors de la recherche automatique. [#7391](https://github.com/SocialGouv/code-du-travail-numerique/issues/7391)
- Correction pour la gestion des anciens accords (utilisation des accords dans l'ES au lieu de l'API Legifrance). [#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381)

### Évolutions techniques
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#7354](https://github.com/SocialGouv/code-du-travail-numerique/issues/7354)
- Mise à jour de pnpm vers la version 11 et corrections associées.
- Ajout d'un système d'extraction d'événements statiques et de vérification de la dérive. [#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)
- Génération de la documentation du plan de suivi (tracking plan) à partir des événements. [#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343)
- Désactivation de Husky lors d'une release pour améliorer le processus.

### Autres changements
- Correction de bugs mineurs liés aux en-têtes d'actualités et aux ancres des accordéons.
- Mise à jour des secrets pour l'environnement de pré-production.
- Ajout de logs pour la recherche DILA.
- Correction d'un problème lié au minimum d'ancienneté pour les particuliers employeurs. [#7314](https://github.com/SocialGouv/code-du-travail-numerique/issues/7314)

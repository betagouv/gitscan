# Synthèse d'activité : agora-gouv (du 16/05 au 27/05)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'introduction et l'amélioration de la gestion des thèmes hebdomadaires, tant au niveau de l'interface d'administration ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)) que du backend ([agora-back](/repos/agora-gouv/agora-back)).  Des améliorations ont également été apportées à l'affichage des informations sur les questions/réponses gouvernementales. Enfin, l'application frontale ([agora-app](/repos/agora-gouv/agora-app)) a bénéficié d'une mise à jour de dépendance importante pour la sécurité et la performance.

## Sécurité
L'application frontale [agora-app](/repos/agora-gouv/agora-app) a mis à jour la dépendance `hive` vers `hive_ce` pour bénéficier des dernières corrections de bugs et améliorations de sécurité.

## Autres changements notables
- Implémentation d'un contrôleur dédié pour le traitement hebdomadaire dans [agora-back](/repos/agora-gouv/agora-back), permettant un lancement en mode administration.
- Ajout d'un mécanisme d'anonymisation des noms d'utilisateur dans le traitement hebdomadaire de [agora-back](/repos/agora-gouv/agora-back).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Développement et intégration de la gestion des thèmes hebdomadaires, anonymisation des données et corrections diverses.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Ajout de la collection "theme_hebdo" et enrichissement des informations des QAG.
- [agora-app](/repos/agora-gouv/agora-app) : Ajout d'un mock de tuile pour les thèmes et mise à jour de la dépendance `hive`.

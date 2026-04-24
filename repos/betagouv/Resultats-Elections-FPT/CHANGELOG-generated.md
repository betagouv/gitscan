## Changelog : Resultats-Elections-FPT (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la préparation du lancement de la plateforme, avec des corrections de bugs et des améliorations de l'interface utilisateur. Des travaux ont également été réalisés sur la cartographie des collectivités et le filtrage des données dans le tableau des résultats.

### Évolutions fonctionnelles
- Correction de l'affichage du tag "doublon" sur la cartographie des collectivités, qui est désormais mis en évidence avec un style d'erreur visuel. [#46](https://github.com/betagouv/Resultats-Elections-FPT/pull/46)
- Le filtrage du tableau des résultats ne s'applique désormais qu'après avoir cliqué sur le bouton "Appliquer les filtres", améliorant l'expérience utilisateur. [#45](https://github.com/betagouv/Resultats-Elections-FPT/pull/45)
- Correction du texte exporté pour les colonnes de type badge sur la cartographie. [#43](https://github.com/betagouv/Resultats-Elections-FPT/pull/43)

### Évolutions techniques
- Suppression des anciennes vues HTML remplacées par des vues génériques, simplifiant ainsi le code. [#47](https://github.com/betagouv/Resultats-Elections-FPT/pull/47)
- Création d'une version figée des widgets personnalisés à la version v0.12 pour une meilleure stabilité. [#38](https://github.com/betagouv/Resultats-Elections-FPT/pull/38)
- Ajout d'un build "staging" pour faciliter le recettage et les tests avant la mise en production. [#25](https://github.com/betagouv/Resultats-Elections-FPT/pull/25)

### Autres changements
- Préparation de la version 1.1 (MEP) et déploiement sur l'environnement de staging.
- Plusieurs corrections diverses ont été apportées en préparation du lancement. [#44](https://github.com/betagouv/Resultats-Elections-FPT/pull/44)

## Changelog : agora-back (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion et l'affichage des thèmes hebdomadaires (thèmes "hebdo") ainsi que sur l'intégration avec Strapi. Des corrections et des ajustements ont également été apportés pour améliorer l'anonymisation des données et la présentation des informations sur les questions et réponses.

### Évolutions fonctionnelles
- Ajout d'une nouvelle route API publique pour consulter les thèmes de la semaine : `GET /theme_hebdo` [#22b4642](https://github.com/agora-gouv/agora-back/commit/22b4642)
- Amélioration de la présentation des thèmes hebdomadaires avec un sous-titre dynamique en fonction du type de thème (libre ou non).
- Ajout d'un indicateur "estThemeLibre" pour mieux qualifier les thèmes libres.
- Correction de la sélection pour l'anonymisation des noms d'utilisateurs. [#c601629](https://github.com/agora-gouv/agora-back/commit/c601629)
- Gestion améliorée de la période optionnelle pour les thèmes hebdomadaires côté Strapi.
- Correction du champ "programme_du_mois" pour permettre l'utilisation de texte enrichi.
- Ajout de deux nouveaux champs pour la page de détails QAG gouvernement.

### Évolutions techniques
- Préparation à la migration vers la version 5 de Strapi, incluant l'ajout du header de compatibilité pour les clients V4. [#5bc6b05](https://github.com/agora-gouv/agora-back/commit/5bc6b05)
- Ajout d'un contrôleur dédié au traitement hebdomadaire pour lancement en mode administration. [#3924dab](https://github.com/agora-gouv/agora-back/commit/3924dab)
- Modification du format de la photo des thèmes hebdomadaires pour utiliser le format "media". [#72fb80f](https://github.com/agora-gouv/agora-back/commit/72fb80f)
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette. [#72e8c6c](https://github.com/agora-gouv/agora-back/commit/72e8c6c)
- Amélioration de la gestion des valeurs par défaut et de la génération de la période pour les thèmes hebdomadaires. [#af34990](https://github.com/agora-gouv/agora-back/commit/af34990)
- Correction d'un problème lié à la branche "feat branch issue theme_hebdo". [#68fb407](https://github.com/agora-gouv/agora-back/commit/68fb407)

### Autres changements
- Correction de l'utilisation de la date de début du thème courant pour filtrer les thèmes hebdomadaires suivants. [#b8820b1](https://github.com/agora-gouv/agora-back/commit/b8820b1)
- Mise en majuscule de la "période" du thème hebdomadaire. [#3292b1e](https://github.com/agora-gouv/agora-back/commit/3292b1e)
- Changement de wording pour améliorer la clarté. [#4534de7](https://github.com/agora-gouv/agora-back/commit/4534de7)
- Désactivation de l'anonymisation lors de l'archivage. [#fcd5b70](https://github.com/agora-gouv/agora-back/commit/fcd5b70)
- Filtrage des 3 prochains thèmes pour la tuile du thème hebdomadaire. [#8081d92](https://github.com/agora-gouv/agora-back/commit/8081d92)
- Ajustement des données de test pour la tuile du thème. [#7e13776](https://github.com/agora-gouv/agora-back/commit/7e13776)

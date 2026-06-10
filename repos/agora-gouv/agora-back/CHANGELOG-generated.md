## Changelog : agora-back (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des thèmes hebdomadaires (thème hebdo) et de la page de détails des Questions/Réponses (QAG) gouvernementales. Des corrections et des ajustements ont été apportés pour optimiser l'affichage, le filtrage et l'anonymisation des données. Une préparation à la migration vers Strapi V5 est également en cours.

### Évolutions fonctionnelles
- Ajout d'une nouvelle route API publique pour consulter les thèmes de la semaine : `GET /theme_hebdo` [#22b4642](https://github.com/agora-gouv/agora-back/commit/22b4642).
- Amélioration de la page de détails QAG gouvernementale avec l'ajout de deux nouveaux champs [#6e24fe8](https://github.com/agora-gouv/agora-back/commit/6e24fe8).
- Correction de la sélection pour l'anonymisation des noms d'utilisateurs [#c601629](https://github.com/agora-gouv/agora-back/commit/c601629).
- Gestion améliorée de la période optionnelle pour les thèmes hebdomadaires côté Strapi [#e5d55ca](https://github.com/agora-gouv/agora-back/commit/e5d55ca).
- Correction du champ "programme_du_mois" pour permettre l'utilisation de texte enrichi [#7bb4bd4](https://github.com/agora-gouv/agora-back/commit/7bb4bd4).
- Amélioration de l'affichage du sous-titre dynamique en fonction du type de thème (libre ou non) [#5c83e27](https://github.com/agora-gouv/agora-back/commit/5c83e27).
- Mise en majuscule de la période du thème hebdomadaire [#3292b1e](https://github.com/agora-gouv/agora-back/commit/3292b1e).
- Ajout d'un indicateur booléen `estThemeLibre` pour mieux qualifier les thèmes libres [#bc11d7c](https://github.com/agora-gouv/agora-back/commit/bc11d7c).

### Évolutions techniques
- Préparation à la migration vers la version 5 de Strapi [#631f272](https://github.com/agora-gouv/agora-back/commit/631f272).
- Ajout du header de compatibilité V4 au client Strapi [#5bc6b05](https://github.com/agora-gouv/agora-back/commit/5bc6b05).
- Ajout d'un contrôleur dédié au traitement hebdomadaire pour lancement en mode administrateur [#3924dab](https://github.com/agora-gouv/agora-back/commit/3924dab).
- Modification du format de la photo en "media" pour les thèmes hebdomadaires [#72fb80f](https://github.com/agora-gouv/agora-back/commit/72fb80f).
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette [#72e8c6c](https://github.com/agora-gouv/agora-back/commit/72e8c6c).
- Implémentation de la gestion des valeurs par défaut et du filtrage pour les thèmes hebdomadaires [#af34990](https://github.com/agora-gouv/agora-back/commit/af34990).
- Cablage Strapi pour la récupération des thèmes hebdomadaires [#98d0647](https://github.com/agora-gouv/agora-back/commit/98d0647).

### Autres changements
- L'anonymisation des noms d'utilisateurs est désactivée lors de l'archivage [#fcd5b70](https://github.com/agora-gouv/agora-back/commit/fcd5b70).
- Ajustement des données de test pour la tuile du thème hebdomadaire [#7e13776](https://github.com/agora-gouv/agora-back/commit/7e13776).
- Correction d'un bug lié à la branche "feat branch issue theme_hebdo" [#68fb407](https://github.com/agora-gouv/agora-back/commit/68fb407).
- Changement de wording pour améliorer la clarté [#4534de7](https://github.com/agora-gouv/agora-back/commit/4534de7).
- Filtrage des 3 prochains thèmes pour l'affichage de la tuile du thème hebdomadaire [#8081d92](https://github.com/agora-gouv/agora-back/commit/8081d92).

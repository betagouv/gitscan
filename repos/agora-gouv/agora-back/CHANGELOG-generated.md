## Changelog : agora-back (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion et l'affichage des thèmes hebdomadaires (thèmes "hebdo") ainsi que sur l'intégration avec Strapi (CMS). Des ajustements ont également été apportés à la page de détails des questions/réponses gouvernementales et à l'anonymisation des noms d'utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une nouvelle route API publique pour consulter les thèmes de la semaine : `GET /theme_hebdo` [#22b4642](https://github.com/agora-gouv/agora-back/commit/22b4642)
- Amélioration de l'affichage des thèmes hebdomadaires :
    - Sous-titre dynamique en fonction du type de thème (libre ou non).
    - Filtrage des 3 prochains thèmes pour la tuile "thème hebdo".
    - Gestion de la période optionnelle des thèmes hebdomadaires côté Strapi.
    - Correction de l'affichage de la période des thèmes hebdomadaires (passage en majuscule).
- Ajout de deux nouveaux champs pour la page de détails des questions/réponses gouvernementales [#6e24fe8](https://github.com/agora-gouv/agora-back/commit/6e24fe8)
- Correction de la sélection pour l'anonymisation des noms d'utilisateurs [#c601629](https://github.com/agora-gouv/agora-back/commit/c601629)
- Correction du champ "programme_du_mois" pour permettre l'utilisation de rich text [#7bb4bd4](https://github.com/agora-gouv/agora-back/commit/7bb4bd4)

### Évolutions techniques
- Préparation à la migration vers la version 5 de Strapi [#631f272](https://github.com/agora-gouv/agora-back/commit/631f272)
- Ajout du header de compatibilité avec les clients Strapi V4 [#5bc6b05](https://github.com/agora-gouv/agora-back/commit/5bc6b05)
- Ajout d'un contrôleur dédié au traitement hebdomadaire pour lancement en mode admin [#3924dab](https://github.com/agora-gouv/agora-back/commit/3924dab)
- Modification du format de la photo des thèmes hebdomadaires en "media" [#72fb80f](https://github.com/agora-gouv/agora-back/commit/72fb80f)
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette [#72e8c6c](https://github.com/agora-gouv/agora-back/commit/72e8c6c)
- Ajout d'un boolean 'estThemeLibre' pour qualifier les thèmes libres [#bc11d7c](https://github.com/agora-gouv/agora-back/commit/bc11d7c)

### Autres changements
- L'anonymisation des noms d'utilisateurs est désactivée lors de l'archivage [#fcd5b70](https://github.com/agora-gouv/agora-back/commit/fcd5b70)
- Ajustement des données de test pour la tuile "thème" [#7e13776](https://github.com/agora-gouv/agora-back/commit/7e13776)
- Correction d'un problème lié à la branche "feat branch issue theme_hebdo" [#68fb407](https://github.com/agora-gouv/agora-back/commit/68fb407)
- Changement de wording pour améliorer la clarté [#4534de7](https://github.com/agora-gouv/agora-back/commit/4534de7)

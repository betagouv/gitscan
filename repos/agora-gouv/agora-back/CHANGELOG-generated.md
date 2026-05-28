## Changelog : agora-back (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion et l'affichage des thèmes hebdomadaires, ainsi que sur des ajustements pour l'anonymisation des données et l'enrichissement des informations relatives aux questions/réponses gouvernementales. Plusieurs corrections et ajouts ont été effectués pour améliorer la robustesse et la flexibilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une nouvelle API publique pour consulter les thèmes de la semaine : `GET /theme_hebdo` [#22b4642](https://github.com/agora-gouv/agora-back/commit/22b4642)
- Amélioration de la gestion des périodes optionnelles pour les thèmes hebdomadaires, en intégrant les données depuis Strapi [#e5d55ca](https://github.com/agora-gouv/agora-back/commit/e5d55ca) et [#af34990](https://github.com/agora-gouv/agora-back/commit/af34990)
- Ajout de deux nouveaux champs pour la page de détails des questions/réponses gouvernementales [#6e24fe8](https://github.com/agora-gouv/agora-back/commit/6e24fe8)
- Correction du champ "programme_du_mois" pour permettre l'utilisation de texte enrichi [#7bb4bd4](https://github.com/agora-gouv/agora-back/commit/7bb4bd4)
- Filtrage des 3 prochains thèmes pour l'affichage de la tuile "thème de la semaine" [#8081d92](https://github.com/agora-gouv/agora-back/commit/8081d92)
- Modification du format de la photo des thèmes hebdomadaires pour utiliser le type "media" [#72fb80f](https://github.com/agora-gouv/agora-back/commit/72fb80f)

### Évolutions techniques
- Implémentation d'un contrôleur dédié pour le traitement hebdomadaire, permettant un lancement en mode administration [#3924dab](https://github.com/agora-gouv/agora-back/commit/3924dab)
- Ajout d'un mécanisme d'anonymisation des noms d'utilisateur dans le traitement hebdomadaire [#41b8762](https://github.com/agora-gouv/agora-back/commit/41b8762) et [#c601629](https://github.com/agora-gouv/agora-back/commit/c601629)
- Désactivation de l'anonymisation lors de l'archivage des données [#fcd5b70](https://github.com/agora-gouv/agora-back/commit/fcd5b70)
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette [#72e8c6c](https://github.com/agora-gouv/agora-back/commit/72e8c6c)

### Autres changements
- Correction d'un problème lié à la branche "theme_hebdo" [#68fb407](https://github.com/agora-gouv/agora-back/commit/68fb407)
- Ajustement des données de test pour la tuile "thème" [#7e13776](https://github.com/agora-gouv/agora-back/commit/7e13776)

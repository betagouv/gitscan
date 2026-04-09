## Changelog : Resultats-Elections-FPT (30 derniers jours, au 31 mars 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de la cartographie et des formulaires. Des déploiements en environnement de staging ont également été effectués pour faciliter les tests et le recettage.

### Évolutions fonctionnelles
- Correction de plusieurs bugs avant le lancement, améliorant la stabilité générale de l'application. [#44](https://github.com/betagouv/Resultats-Elections-FPT/pull/44)
- Amélioration de l'export des données cartographiques : le texte des colonnes de type "badge" DSFR est maintenant correctement affiché. [#43](https://github.com/betagouv/Resultats-Elections-FPT/pull/43)
- Correction des problèmes liés aux CAP multiples et au formulaire de modalités de scrutin qui disparaissait après enregistrement. [#42](https://github.com/betagouv/Resultats-Elections-FPT/pull/42)
- Résolution d'un bug empêchant l'affichage du formulaire lors du retour depuis la vue cartographique. [#41](https://github.com/betagouv/Resultats-Elections-FPT/pull/41)

### Évolutions techniques
- Création de versions figées pour les widgets personnalisés (MEP v0.12 et v0.13).
- Ajout d'un type d'affichage "badge" pour les cellules du tableau. [#37](https://github.com/betagouv/Resultats-Elections-FPT/pull/37)
- Mise en place d'un build "staging" pour faciliter le recettage et les tests. [#25](https://github.com/betagouv/Resultats-Elections-FPT/pull/25)
- Amélioration de l'action de build pour mettre à jour le dossier `dist`. [#22](https://github.com/betagouv/Resultats-Elections-FPT/pull/22)
- Création d'une CI pour automatiser le build de l'application. [#20](https://github.com/betagouv/Resultats-Elections-FPT/pull/20)

### Autres changements
- Diverses améliorations UX et UI. [#26](https://github.com/betagouv/Resultats-Elections-FPT/pull/26)
- Amélioration de la recherche : insensible aux accents et affichage automatique de la liste en cas de recherche vide. [#29](https://github.com/betagouv/Resultats-Elections-FPT/pull/29)
- Suppression d'une icône. [#28](https://github.com/betagouv/Resultats-Elections-FPT/pull/28)
- Ajout de la vue pour la cartographie collectivité. [#24](https://github.com/betagouv/Resultats-Elections-FPT/pull/24)
- Diverses améliorations suite au recettage. [#19](https://github.com/betagouv/Resultats-Elections-FPT/pull/19)

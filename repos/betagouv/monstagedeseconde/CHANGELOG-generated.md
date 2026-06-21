## Changelog : monstagedeseconde (30 derniers jours, au 2026-06-19)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la gestion des candidatures, notamment pour éviter les doublons et gérer les périodes de publication. Des corrections ont également été apportées pour améliorer la stabilité et la gestion des erreurs, ainsi que des optimisations techniques pour la sécurité et la performance. Plusieurs mises à jour de l'interface utilisateur ont été réalisées pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création d'utilisateurs après une migration de base de données [#881](https://github.com/betagouv/monstagedeseconde/pulls/881).
- Amélioration de la gestion des doublons de candidatures, notamment en bloquant les candidatures multiples pendant les périodes interdites [#908](https://github.com/betagouv/monstagedeseconde/pulls/908).
- Correction d'un problème de publication multiple d'offres suite à des clics intempestifs [#907](https://github.com/betagouv/monstagedeseconde/pulls/907).
- Possibilité d'associer un personnel pédagogique à un ou plusieurs établissements [#881](https://github.com/betagouv/monstagedeseconde/pulls/881).
- Amélioration de la gestion des conventions, notamment pour éviter les doublons [#892](https://github.com/betagouv/monstagedeseconde/pulls/892).
- Possibilité de modifier l'adresse email des représentants légaux [#906](https://github.com/betagouv/monstagedeseconde/pulls/906).
- Ajout d'un lien vers "letter thief" pour faciliter l'accès à cette fonctionnalité [#873](https://github.com/betagouv/monstagedeseconde/pulls/873).
- Importation des étudiants depuis le tableau de bord administrateur [#883](https://github.com/betagouv/monstagedeseconde/pulls/883).
- Amélioration de la recherche des semaines [#851](https://github.com/betagouv/monstagedeseconde/pulls/851).
- Mise à jour des libellés concernant la récupération des candidatures [#876](https://github.com/betagouv/monstagedeseconde/pulls/876).
- Ajout de la possibilité de renvoyer une candidature [#898](https://github.com/betagouv/monstagedeseconde/pulls/898).
- Gestion des niveaux d'étudiants par établissement [#883](https://github.com/betagouv/monstagedeseconde/pulls/883).

### Évolutions techniques
- Refactorisation de l'architecture des autorisations (Acl) et des capacités (abilities) pour une meilleure organisation et maintenabilité [#889](https://github.com/betagouv/monstagedeseconde/pulls/889).
- Amélioration de la gestion des erreurs Sygne avec la création d'une classe d'erreur spécifique [#888](https://github.com/betagouv/monstagedeseconde/pulls/888).
- Optimisation de la gestion des transactions en base de données pour éviter les blocages [#905](https://github.com/betagouv/monstagedeseconde/pulls/905).
- Amélioration de la sécurité en restreignant les cibles possibles de la reconstruction de l'environnement de revue [#882](https://github.com/betagouv/monstagedeseconde/pulls/882).
- Suppression de code obsolète et nettoyage de la configuration.
- Mise à jour de plusieurs dépendances (qs, @tootallnate/once, shell-quote, net-imap, puma).

### Autres changements
- Amélioration de la documentation et des tests unitaires.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Mise à jour de la configuration de Redis pour l'environnement Heroku.
- Correction de problèmes de configuration liés à la gestion des images.
- Amélioration de l'interface utilisateur pour la recherche d'établissements.
- Ajout de la gestion de la maintenance en mode FlipperCloud.
- Suppression d'un add-on tiers inutile.
- Correction de problèmes de syntaxe dans le code Sass.
- Ajout de la gestion des statistiques pour les statisticiens.
- Correction de la gestion des caractères spéciaux dans la recherche.
- Suppression des descriptions d'extensions commentées dans le fichier structure.sql.
- Amélioration de la gestion des logs et des erreurs.

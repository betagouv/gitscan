## Changelog : code-du-travail-numerique (30 derniers jours, au 23 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de la recherche et de l'affichage des accords d'entreprise, ainsi que par des corrections de bugs concernant l'affichage des tableaux, des redirections et des tests automatisés. Des fonctionnalités liées au SMIC ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des accords d'entreprise dans l'outil "Trouver sa CC" ([#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260)).
- Ajout de méthodes de calcul du SMIC annuel ([#7286](https://github.com/SocialGouv/code-du-travail-numerique/issues/7286)).
- Amélioration de l'affichage des accords, notamment en les ordonnant par date de signature ([#7313](https://github.com/SocialGouv/code-du-travail-numerique/issues/7313)).
- Ajout d'un type de contribution "bon à savoir" ([#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)).
- Ajout de logs pour faciliter le débogage des erreurs d'API liées aux accords.
- Correction de l'affichage des en-têtes de tableaux dans la section contribution ([#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325)).
- Redirection de l'ancienne fiche canicule vers la nouvelle page d'information ([#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318), [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322)).

### Évolutions techniques
- Correction de tests E2E pour le glossaire, la recherche et les conventions collectives ([#7319](https://github.com/SocialGouv/code-du-travail-numerique/issues/7319)).
- Correction de problèmes HTML invalides sur la page d'actualités.
- Correction de tests unitaires suite à des modifications.
- Découplage de l'affichage des accords de la recherche d'entreprise pour une meilleure performance et maintenabilité ([#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324)).
- Correction de bugs liés à l'ouverture de la page de recherche et à l'affichage des résultats.
- Correction de bugs liés à la gestion des attributs du challenger SMIC.
- Amélioration de la gestion des erreurs et ajout de logs.

### Autres changements
- Mise à jour des dépendances ([#7297](https://github.com/SocialGouv/code-du-travail-numerique/issues/7297)).
- Mise à jour des secrets pour l'environnement de pré-production.
- Correction d'un bug bloquant l'affichage des informations sans convention collective sélectionnée ([#7232](https://github.com/SocialGouv/code-du-travail-numerique/issues/7232)).
